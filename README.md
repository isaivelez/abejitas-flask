# 🐝 Abejitas Flask App

Aplicación web Flask con temática de abejitas que incluye sistema de login y página de inicio.

## 📋 Requisitos

- Docker
- Docker Compose (opcional, pero recomendado)

## 🚀 Ejecución con Docker

### Opción 1: Usando Docker Compose (Recomendado)

```bash
# Construir y ejecutar la aplicación
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d --build

# Detener la aplicación
docker-compose down
```

### Opción 2: Usando Docker directamente

```bash
# Construir la imagen
docker build -t abejitas-flask .

# Ejecutar el contenedor
docker run -p 8080:8080 abejitas-flask

# Ejecutar en segundo plano
docker run -d -p 8080:8080 --name abejitas-app abejitas-flask
```

## 🌐 Acceso a la Aplicación

Una vez que la aplicación esté ejecutándose:

- **Login**: http://localhost:8080/
- **Home**: http://localhost:8080/home

## 📁 Estructura del Proyecto

```
proyecto/
├── Dockerfile              # Configuración de Docker
├── docker-compose.yml      # Configuración de Docker Compose
├── .dockerignore           # Archivos ignorados por Docker
├── README.md               # Este archivo
└── src/
    ├── app.py              # Aplicación Flask principal
    ├── requirements.txt    # Dependencias de Python
    ├── templates/
    │   ├── login.html      # Template de login
    │   └── home.html       # Template de home
    └── static/             # Archivos estáticos (CSS, JS, imágenes)
```

## 🛠️ Desarrollo Local

Para desarrollo con recarga automática, usar Docker Compose que ya incluye el montaje de volúmenes:

```bash
docker-compose up --build
```

Los cambios en el código se reflejarán automáticamente sin necesidad de reconstruir la imagen.

## 🐳 Comandos Útiles de Docker

```bash
# Ver contenedores en ejecución
docker ps

# Ver logs de la aplicación
docker logs abejitas-app

# Acceder al contenedor
docker exec -it abejitas-app /bin/bash

# Eliminar contenedor
docker rm abejitas-app

# Eliminar imagen
docker rmi abejitas-flask
```

## 📦 Dependencias

- Flask 3.1.2
- Jinja2 3.1.6
- Werkzeug 3.1.3
- Y otras dependencias listadas en `requirements.txt`
