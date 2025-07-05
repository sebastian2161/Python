# 📡 Activación de Eventos con Google Cloud: Cloud Run Functions + Dataflow

Este proyecto demuestra cómo implementar una arquitectura de **microservicios asincrónica basada en eventos**, utilizando servicios completamente gestionados de Google Cloud Platform (GCP):

- 🚀 **Cloud Run (Functions Framework)** para activar eventos mediante peticiones HTTP.
- 🔄 **Dataflow** para el procesamiento escalable de datos mediante Apache Beam.

---

## 🧱 Arquitectura General

1. Un servicio externo como una API activa una petición **HTTP** a una función desplegada en **Cloud Run**.
2. La función **Cloud Run Function** inicia un **job en Dataflow** que ejecuta un pipeline previamente definido.

---

## 📦 Componentes del Proyecto

### 1. Cloud Run Function (basada en HTTP Trigger)

- **Archivo principal**: `main.py`
- **Punto de entrada**: `hello_http`
- **Framework**: [Functions Framework for Python](https://cloud.google.com/functions/docs/functions-framework)
- **Tipo de activación**: `HTTP Request`








