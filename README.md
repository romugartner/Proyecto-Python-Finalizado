# Blog en Django

Aplicación web de blog basada en el proyecto original de consola. Se conservaron los conceptos de publicaciones, autor, etiquetas y estados, trasladándolos a Django y SQLite.

## Funcionalidades

- Listado público de publicaciones publicadas.
- Vista de detalle de una publicación.
- Alta, edición y eliminación de publicaciones para usuarios autenticados.
- Solo el autor de una publicación puede editarla o eliminarla.
- Registro, inicio y cierre de sesión.
- Carga y visualización opcional de imágenes.
- Búsqueda por título y filtrado por etiqueta.
- Estados de publicación: borrador, publicada y archivada.
- Pruebas automatizadas de permisos y flujos principales.

## Requisitos

- Python 3.10 o superior.
- pip.

## Instalación local

```bash
python -m venv .venv
```

Activar el entorno virtual:

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Instalar dependencias y preparar la base de datos:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/`.

## Pruebas

```bash
python manage.py test
```

## Seguridad antes de publicar/desplegar

- `DEBUG` se configura según la variable de entorno `DJANGO_DEBUG` (por defecto, activado solo para desarrollo local).
- En producción, definir `DJANGO_SECRET_KEY` con un valor secreto y único.
- Configurar `DJANGO_ALLOWED_HOSTS` con los dominios permitidos.
- No subir `.env`, `db.sqlite3`, `media/`, credenciales ni el entorno virtual.
- En producción, servir archivos multimedia mediante un almacenamiento adecuado y configurar HTTPS.
- Ejecutar `python manage.py check --deploy` con los ajustes de producción.

## Publicar el proyecto en GitHub

1. Crear un repositorio **público** vacío en GitHub.
2. Desde esta carpeta, ejecutar:

```bash
git init
git add .
git commit -m "Crear blog web con Django"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

3. Sustituir `USUARIO/REPOSITORIO` por la URL real del repositorio.
4. Revisar la pestaña **Actions** (si se añade CI), el README y los archivos antes de confirmar que la publicación está terminada.

> No se ha publicado automáticamente en GitHub: para hacerlo se necesita que el usuario cree o autorice el repositorio remoto. Este paquete queda preparado para subirlo.

## Modelo de datos

Cada publicación contiene título, contenido, autor, etiquetas, estado, fecha de creación/actualización e imagen opcional. Las cuentas y contraseñas son gestionadas por el sistema de autenticación de Django; las contraseñas no se guardan en texto plano en el modelo del blog.

## Limitaciones conocidas

- La aplicación usa SQLite para desarrollo.
- Las etiquetas se almacenan como texto separado por comas, para mantener simple la migración desde el proyecto original.
- La carga de imágenes requiere Pillow.
- No se incluye despliegue automático ni configuración de un proveedor de hosting.
