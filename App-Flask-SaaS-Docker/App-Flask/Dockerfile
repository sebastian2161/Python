# Dockerfile
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Puerto usado por Cloud Run
ENV PORT=8080

# Comando para ejecutar la app
CMD ["python", "app.py"]
