# 📱 Despliegue de Aplicación Django/FastApi/Flask como SaaS en Google Cloud Platform (GCP)

Este proyecto demuestra cómo desplegar una **aplicación web Django/FastApi/Flask** bajo el modelo **SaaS (Software como Servicio)** utilizando **Cloud Run**,  
**Cloud Build** y **Artifact Registry** en GCP.

---

## 🚀 Arquitectura General

1. Crea el proyecto app.py y/o my_django_project.
2. Crea el archivo de requirements.txt
3. Crea el archivo Dockerfile.
4. Compila la imagen Docker en Cloud Build.
5. Despliega la imagen Docker en Cloud Run.

---

## 🧱️ Componentes del Proyecto

### ⚙️ Cloud Build

- Compila el archivo Dockerfile, para crear una imagen y almacenarla en el servicio Artifact Registry.


### ⚙️ Artifact Registry

- Almacena la imagen docker, para utilizarla en el servicio Cloud Run.


### ⚙️ Cloud Run

- Despliega la imagen docker, creando un servicio y una url de activación: https://[Nombre-Servicio]-cloudrun-390075199183.us-central1.run.app/




## ⚙️ Pasos para Desplegar la Aplicación Web Django:

    - `Estructura del Proyecto`:
        my_django_project/
        ├── Dockerfile
        ├── requirements.txt
        ├── manage.py
        ├── myapp/
        │   ├── __init__.py
        │   ├── views.py
        │   ├── urls.py
        │   └── apps.py
        └── my_django_project/
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py

     - Crear carpeta local en Cloud Shell `mkdir django-cloudrun && cd django-cloudrun`

     - Crear el proyecto my_djando_proyecto.

     - Crear el archivo requirements, con las librerias que utiliza Django.     

     - Crear el archivo Dockerfile, subirlo en la ruta django-cloudrun/my_django_project
    
     - Compilar el archivo Dockerfile con el servicio Cloud Build: `gcloud builds submit --tag gcr.io/sesion04-461702/django-cloudrun`
 
     - Desplegar la imagen Docker con Cloud Run: gcloud run deploy django-cloudrun \
                                                    --image gcr.io/sesion04-461702/django-cloudrun \
                                                    --platform managed \
                                                    --region us-central1 \
                                                    --allow-unauthenticated

     - Debes ir a Cloud Run/Servicios, encontraras el servicio django-cloudrun activado, tipo de implementación contenedor.  



## ⚙️ Pasos para Desplegar la Aplicación Web FastApi:

    - `Estructura del Proyecto`:
       -app.y 
       -Dockerfile
       -requirements.txt

     - Crear carpeta local en Cloud Shell `mkdir flastapi-cloudrun && cd flastapi-cloudrun`

     - Crear la app.py.

     - Crear el archivo requirements, con las librerias que utiliza FastApi.     

     - Crear el archivo Dockerfile, subirlo en la ruta flastapi-cloudrun
    
     - Compilar el archivo Dockerfile con el servicio Cloud Build: `gcloud builds submit --tag gcr.io/sesion04-461702/flastapi-cloudrun`
 
     - Desplegar la imagen Docker con Cloud Run:   gcloud run deploy flastapi-cloudrun \
                                                      --image gcr.io/sesion04-461702/flastapi-cloudrun \
                                                      --platform managed \
                                                      --region us-central1 \
                                                      --allow-unauthenticated

     - Debes ir a Cloud Run/Servicios, encontraras el servicio flastapi-cloudrun activado, tipo de implementacion contenedor.  


## ⚙️ Pasos para Desplegar la Aplicación Web Flask:

    - `Estructura del Proyecto`:
       -app.y 
       -Dockerfile
       -requirements.txt

     - Crear carpeta local en Cloud Shell `mkdir flask-cloudrun && cd flask-cloudrun`

     - Crear la app.py.

     - Crear el archivo requirements, con las librerias que utiliza Flask.     

     - Crear el archivo Dockerfile, subirlo en la ruta flask-cloudrun
    
     - Compilar el archivo Dockerfile con el servicio Cloud Build: `gcloud builds submit --tag gcr.io/sesion04-461702/flask-cloudrun`
 
     - Desplegar la imagen Docker con Cloud Run:   gcloud run deploy flask-cloudrun \
                                                      --image gcr.io/sesion04-461702/flask-cloudrun \
                                                      --platform managed \
                                                      --region us-central1 \
                                                      --allow-unauthenticated

     - Debes ir a Cloud Run/Servicios, encontraras el servicio flask-cloudrun activado, tipo de implementacion contenedor.  


## 📚 Recursos Adicionales

- [Flask Oficial](https://flask.palletsprojects.com/)
- [GCP CLI - gcloud](https://cloud.google.com/sdk/gcloud)


