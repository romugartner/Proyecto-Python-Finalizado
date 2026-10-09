from blog.datos import cargar_posts, guardar_posts
from blog.menu import obtener_opcion
from blog.modelos import Autor, Blog, Post


def mostrar_lista(posts):
    if not posts:
        print("\nNo se encontraron posts.")
        return

    print("\n" + "-" * 50)
    for p in posts:
        print(f"ID: {p.id} | Título: {p.titulo} | Estado: {p.estado}")
        print(f"Autor: {p.autor.nombre} ({p.autor.bio})")
        print(f"Tags: {', '.join(p.tags)}")
        print(f"Contenido: {p.contenido}")
        print("-" * 50)


if __name__ == "__main__":
    blog = Blog()
    blog.posts = cargar_posts()

    while True:
        opcion = obtener_opcion()
        if opcion is None:
            continue

        if opcion == 1:
            mostrar_lista(blog.listar_posts())

        elif opcion == 2:
            termino = input("\nIngresá el texto a buscar en el título: ").strip()
            resultados = blog.buscar_por_titulo(termino)
            mostrar_lista(resultados)

        elif opcion == 3:
            tag = input("\nIngresá el tag a filtrar: ").strip()
            resultados = blog.filtrar_por_tag(tag)
            mostrar_lista(resultados)

        elif opcion == 4:
            print("\n--- NUEVO POST ---")
            titulo = input("Título: ").strip()
            contenido = input("Contenido: ").strip()
            nombre_autor = input("Nombre del autor: ").strip()
            bio_autor = input("Bio del autor: ").strip()
            tags_input = input("Tags (separados por coma): ").strip()
            tags = [t.strip() for t in tags_input.split(",") if t.strip()]

            nuevo_id = len(blog.posts) + 1
            nuevo_autor = Autor(nombre_autor, bio_autor)
            nuevo_post = Post(
                nuevo_id, titulo, contenido, nuevo_autor, tags, estado="publicado"
            )

            blog.agregar_post(nuevo_post)
            guardar_posts(blog.posts)
            print(" Post guardado y persistido en posts.json.")

        elif opcion == 5:
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Elegí un número del 1 al 5.")
