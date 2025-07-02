# 📡 Activación de Eventos con Google Cloud: Cloud Run Functions + Cloud Storage

Este proyecto demuestra cómo implementar una arquitectura **asíncrona basada en eventos** utilizando servicios de Google Cloud:

- **Cloud Run (usando Functions Framework)** para procesar eventos automáticamente.
- **Cloud Storage** como sistema de almacenamiento de archivos (origen y destino).

---

## 🚀 Arquitectura General

1. Un archivo es cargado al bucket de origen en **Cloud Storage**.
2. La subida del archivo genera un evento tipo `finalize`, el cual activa una función desplegada en **Cloud Run**.
3. La función valida el tamaño del archivo:
   - Si el archivo **pesa menos de 2 MB**, se copia al bucket de **destino**.
   - Si el archivo **supera los 2 MB**, **no se copia** y puede ser descartado.

---

## 📦 Componentes del Proyecto

### 1. Cloud Run Function (basada en CloudEvents)

- **Archivo** principal: `main.py`
- **Punto de entrada**: `hello_gcs`
- **Framework** utilizado: [Functions Framework for Python](https://cloud.google.com/functions/docs/functions-framework)
- **Tipo de evento**: `google.storage.object.finalize` (cuando un archivo es creado o actualizado en el bucket)








