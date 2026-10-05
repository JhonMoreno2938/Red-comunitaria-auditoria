# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos e instalamos las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de archivos (main.py, models.py, database.py)
COPY . .

# Exponemos el puerto interno donde correrá Uvicorn
EXPOSE 8000

# Comando para iniciar la API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]