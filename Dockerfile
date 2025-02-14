# Usa una imagen base de Python
FROM python:3.10

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del servicio
COPY . .

# Exponer el puerto donde correrá el servicio
EXPOSE 8001

# Comando para ejecutar el servicio
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
