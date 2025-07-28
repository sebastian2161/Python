# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia archivos de tu app al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto 8080 (requerido por Cloud Run)
EXPOSE 8080

# Comando de inicio para uvicorn (servidor FastAPI)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
