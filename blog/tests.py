from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import Post

User = get_user_model()


class BlogAcceptanceTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="autora", password="StrongPass123!")
        self.other = User.objects.create_user(username="lector", password="StrongPass123!")
        self.published = Post.objects.create(
            title="Post publicado", content="Contenido público",
            author=self.author, status=Post.Status.PUBLISHED, tags="Python, Django"
        )
        self.draft = Post.objects.create(
            title="Borrador privado", content="Contenido en borrador",
            author=self.author, status=Post.Status.DRAFT
        )

    def test_public_list_only_shows_published_posts(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post publicado")
        self.assertNotContains(response, "Borrador privado")

    def test_anonymous_user_is_redirected_from_create(self):
        response = self.client.get(reverse("post_create"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    def test_authenticated_user_can_create_post(self):
        self.client.force_login(self.author)
        response = self.client.post(reverse("post_create"), {
            "title": "Nuevo artículo",
            "content": "Contenido nuevo",
            "tags": "Testing, Python",
            "status": Post.Status.PUBLISHED,
        })
        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(title="Nuevo artículo")
        self.assertEqual(post.author, self.author)

    def test_non_owner_cannot_edit_or_delete_post(self):
        self.client.force_login(self.other)
        edit_response = self.client.get(reverse("post_update", args=[self.published.pk]))
        delete_response = self.client.post(reverse("post_delete", args=[self.published.pk]))
        self.assertEqual(edit_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
        self.assertTrue(Post.objects.filter(pk=self.published.pk).exists())

    def test_owner_can_edit_post(self):
        self.client.force_login(self.author)
        response = self.client.post(reverse("post_update", args=[self.published.pk]), {
            "title": "Título actualizado",
            "content": "Contenido actualizado",
            "tags": "Django",
            "status": Post.Status.PUBLISHED,
        })
        self.assertEqual(response.status_code, 302)
        self.published.refresh_from_db()
        self.assertEqual(self.published.title, "Título actualizado")

    def test_anonymous_user_cannot_view_draft(self):
        response = self.client.get(reverse("post_detail", args=[self.draft.pk]))
        self.assertEqual(response.status_code, 404)

    def test_registration_creates_account_and_logs_user_in(self):
        response = self.client.post(reverse("register"), {
            "username": "nueva",
            "email": "nueva@example.com",
            "password1": "OtraClaveFuerte123!",
            "password2": "OtraClaveFuerte123!",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="nueva").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_image_upload_is_accepted(self):
        self.client.force_login(self.author)
        # GIF de 1x1 píxel válido para Pillow.
        image = SimpleUploadedFile(
            "pixel.gif",
            b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;",
            content_type="image/gif",
        )
        response = self.client.post(reverse("post_create"), {
            "title": "Post con imagen",
            "content": "Contenido con imagen",
            "tags": "Imagen",
            "status": Post.Status.PUBLISHED,
            "image": image,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Post con imagen", image__isnull=False).exists())
