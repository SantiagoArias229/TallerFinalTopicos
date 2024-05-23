# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el resto de los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
