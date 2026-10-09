# Generated for the initial blog schema.
import django.conf
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(django.conf.settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="título")),
                ("content", models.TextField(verbose_name="contenido")),
                ("tags", models.CharField(blank=True, help_text="Separadas por comas", max_length=250, verbose_name="etiquetas")),
                ("status", models.CharField(choices=[("borrador", "Borrador"), ("publicado", "Publicado"), ("archivado", "Archivado")], default="borrador", max_length=12, verbose_name="estado")),
                ("image", models.ImageField(blank=True, null=True, upload_to="posts/", verbose_name="imagen")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="creado")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="actualizado")),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="blog_posts", to=django.conf.settings.AUTH_USER_MODEL, verbose_name="autor")),
            ],
            options={
                "verbose_name": "publicación",
                "verbose_name_plural": "publicaciones",
                "ordering": ["-created_at"],
            },
        ),
    ]
