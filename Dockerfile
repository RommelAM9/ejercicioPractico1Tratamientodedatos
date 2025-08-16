# Usamos una imagen base ligera de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente de la app
COPY ./app.py /app/app.py

# Establecemos la variable de entorno para Flask
ENV FLASK_APP=app

# Indicamos el comando para ejecutar la app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]


