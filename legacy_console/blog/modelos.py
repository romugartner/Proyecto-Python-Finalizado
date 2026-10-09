class Autor:
    def __init__(self, nombre, bio=""):
        self.nombre = nombre
        self.bio = bio

    def to_dict(self):
        return {"nombre": self.nombre, "bio": self.bio}

    @classmethod
    def from_dict(cls, data):
        return cls(nombre=data.get("nombre", "Anónimo"), bio=data.get("bio", ""))


class Post:
    def __init__(self, id_post, titulo, contenido, autor, tags, estado="borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Instancia de Autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, data):
        autor = Autor.from_dict(data.get("autor", {}))
        return cls(
            id_post=data.get("id"),
            titulo=data.get("titulo", ""),
            contenido=data.get("contenido", ""),
            autor=autor,
            tags=data.get("tags", []),
            estado=data.get("estado", "borrador"),
        )


class Blog:
    def __init__(self):
        self.posts = []  # Lista de objetos Post

    def agregar_post(self, post):
        self.posts.append(post)

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, termino):
        termino = termino.lower().strip()
        return [p for p in self.posts if termino in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        tag = tag.lower().strip()
        return [p for p in self.posts if tag in [t.lower() for t in p.tags]]
