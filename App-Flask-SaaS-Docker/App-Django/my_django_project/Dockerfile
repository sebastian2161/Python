FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "my_django_project.wsgi:application", "--bind", "0.0.0.0:8080"]