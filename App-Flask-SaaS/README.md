# 📡 Desplegar la App Flask en modo Software como Servicio(SaaS) utilizando Google Cloud Platform (GCP): Compute Engine + App Flask

Este proyecto demuestra cómo implementar una arquitectura de **Software como Servicio(SaaS)** utilizando el 
servicio nativo **Compute Engine** en Google Cloud.

---

## 🚀 Arquitectura General

La solución tiene la siguiente arquitectura:

1. Crear un instancia en **Compute Engine**, permitiendo el trafico HTTP y HTTPS.
2. Conectarse a SSH de la instancia (maquina virtual).
3. En la terminal remota debe instalar `python sudo apt install python3-pip -y`, la libreria flask `pip3 install flask --break-system-packages`.
4. Subir la App Flask a la maquina virtual remota SSH y ejecutarla `python3 app.py`.
5. Acceder a la App Flask desde el navegador copiar la IP externa de la VM (Compute Engine > IP externa) y abrir en tu navegador `http://[IP-EXTERNA]:8080`.
6. Verás: ¡Bienvenido a la App Flask en Google Cloud-GCP!


---

## 🧪 Componentes del Proyecto

### 1. Compute Engine - `app.py`

- Maquina virtual que ejecuta el codigo app.py, para desplegar la App Flask en el navegador web.

---

## ✅ Pre-requisitos

Asegúrate de cumplir con los siguientes pasos antes de ejecutar la App Flask:

### 🔌 Servicios habilitados en GCP

- [x] **Compute Engine**
- [x] **Permiso Firewall habilidado con el puerto 8080**
                        gcloud compute firewall-rules create allow-flask-8080 \
                                    --allow tcp:8080 \
                                    --source-ranges=0.0.0.0/0 \
                                    --target-tags=http-server \
                                    --description="Permitir tráfico al puerto 8080 para Flask"

- [x] ** Tags agregado a la maquina virtual, en este caso flask-vm**
                        gcloud compute instances add-tags flask-vm \
                                    --tags=http-server \
                                    --zone=us-central1-c
          
 - [x] ** Revisar los tags asignados a la maquina virtual flask-vm**
                        gcloud compute instances describe flask-vm --zone=us-central1-c --format="get(tags.items)"



