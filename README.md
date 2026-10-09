Qué entregar


La URL directa de un repositorio público de GitHub con el código completo y funcional del blog. El repo debe contener: código del proyecto Django, apps, templates, archivos estáticos, migraciones, requirements.txt, README.md, .gitignore y .env.example (solo si usaste variables de entorno).

Criterios de aceptación
Publicaciones (desde la interfaz web, no solo el admin)

Listar posts, ver detalle, crear, editar y eliminar.
Cargar y mostrar imagen del post; el template no se rompe si falta la imagen.
Usuarios

Registro, login y logout funcionando.
Perfil accesible (editar perfil e imagen de perfil solo si los implementaste).
El sistema distingue usuario anónimo de autenticado.
Rutas protegidas

Crear/editar/eliminar posts y editar perfil requieren sesión iniciada.
La protección está en la view con @login_required o LoginRequiredMixin (ocultar el botón en el template no alcanza).
Media

MEDIA_URL y MEDIA_ROOT configurados; las imágenes se ven en desarrollo.
Búsqueda (solo si la implementaste)

Busca por título o contenido, muestra resultados y avisa cuando no hay coincidencias.
Repositorio

Es público y abre correctamente en el navegador.
Existen requirements.txt (con Django, Pillow y python-decouple si corresponde, actualizado), README.md y .gitignore.
El historial de commits muestra progreso (no todo en un único commit final).
No hay rutas absolutas; la config se apoya en BASE_DIR.
README — debe incluir como mínimo:

Título, descripción breve, tecnologías, funcionalidades principales.
Instrucciones de instalación, migraciones y arranque del servidor.
Información del autor.
Sin contraseñas ni claves reales.
Pasos
Antes de entregar, verificá localmente y contra GitHub que: el servidor inicia sin errores, las migraciones aplican, el CRUD funciona, las imágenes cargan (y el template resiste sin imagen), registro/login/logout funcionan, las rutas protegidas redirigen, y los cambios están sincronizados con GitHub (no basta con guardar en local).

Cómo entregar
Enviá el enlace directo al repositorio del proyecto. No entregues un .zip, ni una captura, ni el link a tu perfil general de GitHub.

Qué evitar
Repositorio privado (los evaluadores no lo verían).
Subir venv/, .env, __pycache__/, .pyc, archivos temporales o config local del editor → usá .gitignore.
Subir claves o contraseñas reales (ni en el código ni en el README).
Dejar rutas absolutas de tu computadora.
Faltar requirements.txt o las migraciones.
Probar todo con sesión iniciada y olvidar al visitante anónimo.
README que solo tenga el nombre del proyecto.

- La aplicación usa SQLite para desarrollo.
- Las etiquetas se almacenan como texto separado por comas, para mantener simple la migración desde el proyecto original.
- La carga de imágenes requiere Pillow.
- No se incluye despliegue automático ni configuración de un proveedor de hosting.
