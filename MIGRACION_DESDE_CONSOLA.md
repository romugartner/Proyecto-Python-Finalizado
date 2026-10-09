# Migración del proyecto original

El ZIP recibido contenía una aplicación de consola que usaba clases `Autor`, `Post`, `Blog` y persistencia JSON; no contenía una aplicación Django. Por eso se creó una aplicación web Django en la raíz y se conservó una copia reducida del ejercicio de consola en `legacy_console/`.

La aplicación web reemplaza la persistencia JSON por un modelo relacional Django/SQLite, utiliza el sistema de autenticación de Django y añade permisos por autor, formularios, plantillas, carga de imágenes y pruebas automatizadas.
