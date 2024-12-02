# API Resúmenes IA

API que ofrece rutas para crear y obtener resúmenes de noticias a partir de una URL. Utiliza la tecnología de OpenAI para generar resúmenes y permite enviar estos resúmenes por correo electrónico.

## Descripción

Esta API permite a los usuarios enviar una URL de un artículo de noticias y recibir un resumen generado automáticamente. Los resúmenes se pueden guardar en una base de datos y opcionalmente enviar por correo electrónico al usuario.

## Instalación

1. **Clonar el repositorio:**   ```bash
   git clone https://github.com/tu-usuario/api-resumenes-ia.git
   cd api-resumenes-ia   ```

2. **Instalar dependencias:**
   Asegúrate de tener `pip` y `virtualenv` instalados.   ```bash
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt   ```

3. **Configurar variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto y añade las configuraciones necesarias, como las credenciales de la API de OpenAI y la configuración del correo electrónico.

4. **Ejecutar la aplicación:**   ```bash
   flask run   ```

## Uso

### Crear un resumen

- **Endpoint:** `/api/summary/`
- **Método:** `POST`
- **Cuerpo de la solicitud:**  ```json
  {
    "url": "https://example.com/article",
    "email": "usuario@example.com"
  }  ```
- **Respuesta exitosa:**  ```json
  {
    "id": "123",
    "summary": "Este es el resumen del artículo..."
  }  ```

### Obtener resúmenes

- **Endpoint:** `/api/summary/`
- **Método:** `GET`
- **Parámetros de consulta opcionales:**
  - `id`: Obtener un resumen específico por ID.
- **Respuesta exitosa:**  ```json
  [
    {
      "id": "123",
      "original_url": "https://example.com/article",
      "summary_text": "Este es el resumen del artículo...",
      "category": "Noticias",
      "fake_news_level": "Bajo",
      "tone": "Neutral",
      "created_at": "2023-10-01T12:00:00Z",
      "email": "usuario@example.com"
    }
  ]  ```

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Contacto

Para preguntas o soporte, por favor contacta a [hola@markelramiro.com](mailto:hola@markelramiro.com).
