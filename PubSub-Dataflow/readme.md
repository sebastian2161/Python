# 📡 Transmisión en Tiempo Real con Google Cloud: Pub/Sub + Dataflow + Cloud Storage

Este proyecto demuestra cómo implementar una arquitectura de **procesamiento de datos en tiempo real** utilizando los servicios de Google Cloud:

- **Pub/Sub** para la publicación de eventos.
- **Dataflow (Apache Beam)** para el procesamiento en streaming.
- **Cloud Storage** como almacenamiento final de los resultados procesados.

---

## 🚀 Arquitectura General

1. **Productores** envían datos a un **tópico de Pub/Sub**.
2. Un job de **Dataflow en modo streaming** consume los eventos desde el tópico.
3. Los eventos son procesados, agregados por ventanas y almacenados en archivos dentro de un **bucket de Cloud Storage**.

---

## 📦 Componentes del Proyecto

### 1. Servicio Pub/Sub

- **Archivo**: `publicador_mensajes.py`
- **Función**: Publica mensajes simulados (eventos) en el tópico `pubsub_dataflow_demo`.

### 2. Servicio Dataflow

- **Archivo**: `stream_data.py`
- **Función**: Lee eventos desde Pub/Sub, aplica ventanas de tiempo y escribe resultados en Cloud Storage.

### 3. Servicio Cloud Storage

- **Revisar**:El bucket especificado (gs://TU_BUCKET/results/) para ver los archivos generados por Dataflow con los conteos por ventana.






