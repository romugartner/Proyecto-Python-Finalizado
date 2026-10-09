import json
import os
from blog.modelos import Autor, Post

ARCHIVO_JSON = "posts.json"


def cargar_posts():
    if not os.path.exists(ARCHIVO_JSON):
        # Datos iniciales si el archivo aún no existe
        autor_default = Autor("Romulo Gartner", "Desarrollador web junior.")
        posts_iniciales = [
            Post(
                1,
                "Primeros pasos con Python",
                "Inicio en Python",
                autor_default,
                ["Python", "Principiantes"],
                "publicado",
            ),
            Post(
                2,
                "Qué es Django",
                "Intro a Django",
                autor_default,
                ["Python", "Django", "Web"],
                "borrador",
            ),
            Post(
                3,
                "Organizando datos con diccionarios",
                "Diccionarios en Python",
                autor_default,
                ["Python", "Diccionarios"],
                "archivado",
            ),
        ]
        guardar_posts(posts_iniciales)
        return posts_iniciales

    with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
        try:
            lista_dict = json.load(f)
            return [Post.from_dict(item) for item in lista_dict]
        except json.JSONDecodeError:
            return []


def guardar_posts(posts):
    lista_dict = [p.to_dict() for p in posts]
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_dict, f, indent=4, ensure_ascii=False)

