# 📱 Despliegue de Aplicación Flask como SaaS en Google Cloud Platform (GCP)

Este proyecto demuestra cómo desplegar una **aplicación web Flask** bajo el modelo **SaaS (Software como Servicio)** utilizando **Compute Engine** en GCP.

---

## 🚀 Arquitectura General

1. Se crea una instancia de máquina virtual en **Compute Engine**.
2. Se instala Python y Flask en la instancia.
3. Se despliega la aplicación Flask como servicio web.
4. Se accede a la aplicación desde Internet utilizando la **IP externa** de la VM.

---

## 🧱️ Componentes del Proyecto

### 👤 Compute Engine (VM)

- Hospeda y ejecuta la aplicación Flask.
- Configurada para permitir tráfico HTTP/HTTPS (puerto 8080).

### 🐍 Flask App (archivo: `app.py`)

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Bienvenido a la App Flask en Google Cloud - GCP!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

---

## ✅ Pre-requisitos

### 🔌 Servicios habilitados en GCP

-

---

## ⚙️ Pasos para Desplegar la App

### 1. Crear VM en Compute Engine

- Habilita tráfico HTTP y HTTPS.
- Nombre sugerido: `flask-vm`
- Zona sugerida: `us-central1-c`

### 2. Agregar Regla de Firewall para el puerto 8080

```bash
gcloud compute firewall-rules create allow-flask-8080 \
  --allow tcp:8080 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=http-server \
  --description="Permitir tráfico al puerto 8080 para Flask"
```

### 3. Asignar el Tag `http-server` a la VM

```bash
gcloud compute instances add-tags flask-vm \
  --tags=http-server \
  --zone=us-central1-c
```

### 4. Conectarse vía SSH a la VM

```bash
gcloud compute ssh flask-vm --zone=us-central1-c
```

### 5. Instalar Python y Flask en la VM

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install flask --break-system-packages
```

### 6. Subir archivo `app.py` a la VM

Desde tu máquina local:

```bash
gcloud compute scp ./app.py capacitacioncloud303@flask-vm:~/ --zone=us-central1-c
```

### 7. Ejecutar la aplicación Flask

```bash
python3 app.py
```

---

## 🌐 Acceder a la Aplicación

1. Obtén la **IP externa** de la VM:

```bash
gcloud compute instances describe flask-vm --zone=us-central1-c --format="get(networkInterfaces[0].accessConfigs[0].natIP)"
```

2. Abre en tu navegador:

```
http://[IP-EXTERNA]:8080
```

🔵 Verás: `¡Bienvenido a la App Flask en Google Cloud - GCP!`

---

## 🛠️ Tips de Solución de Problemas

| Problema                           | Posible Causa                     | Solución                                                          |
| ---------------------------------- | --------------------------------- | ----------------------------------------------------------------- |
| No carga la app en el navegador    | Puerto bloqueado                  | Verifica regla de firewall y que la app escuche en `0.0.0.0:8080` |
| Error `ModuleNotFoundError: flask` | Flask no instalado                | Ejecuta `pip3 install flask`                                      |
| Error HTTPS                        | La app no sirve HTTPS por defecto | Usa HTTP o configura proxy inverso con HTTPS                      |

---

## 📚 Recursos Adicionales

- [Documentación Compute Engine](https://cloud.google.com/compute/docs)
- [Flask Oficial](https://flask.palletsprojects.com/)
- [GCP CLI - gcloud](https://cloud.google.com/sdk/gcloud)


