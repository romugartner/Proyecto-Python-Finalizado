# Checklist de aceptación

## Instalación y arranque
- [ ] Crear y activar un entorno virtual limpio.
- [ ] Instalar dependencias con `python -m pip install -r requirements.txt`.
- [ ] Ejecutar `python manage.py migrate`.
- [ ] Ejecutar `python manage.py check`.
- [ ] Ejecutar `python manage.py test`.
- [ ] Arrancar `python manage.py runserver` y abrir `http://127.0.0.1:8000/`.

## Funcionalidad
- [ ] Un visitante ve publicaciones publicadas.
- [ ] Un visitante no ve borradores ni publicaciones archivadas.
- [ ] Un visitante que intenta crear una publicación es enviado al inicio de sesión.
- [ ] Un usuario puede registrarse, iniciar sesión y cerrar sesión.
- [ ] Un usuario autenticado puede crear una publicación.
- [ ] El autor puede editar y eliminar su publicación.
- [ ] Otro usuario recibe HTTP 403 al intentar editar o eliminar una publicación ajena.
- [ ] Una imagen válida se puede subir y visualizar.
- [ ] La búsqueda por texto y el filtro por etiqueta funcionan.
- [ ] Formularios inválidos muestran errores y no guardan datos.

## Repositorio público
- [ ] Confirmar que `venv/`, `.env`, `db.sqlite3`, `media/` y `__pycache__/` no se suben.
- [ ] Confirmar que README explica instalación, ejecución y pruebas.
- [ ] Crear repositorio público y hacer `git push`.
- [ ] Abrir el enlace público en una ventana privada para verificar acceso.
