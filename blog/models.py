from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "borrador", "Borrador"
        PUBLISHED = "publicado", "Publicado"
        ARCHIVED = "archivado", "Archivado"

    title = models.CharField("título", max_length=200)
    content = models.TextField("contenido")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name="autor",
    )
    tags = models.CharField("etiquetas", max_length=250, blank=True, help_text="Separadas por comas")
    status = models.CharField(
        "estado", max_length=12, choices=Status.choices, default=Status.DRAFT
    )
    image = models.ImageField("imagen", upload_to="posts/", blank=True, null=True)
    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
