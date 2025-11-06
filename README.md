# 🐝 Abejitas Flask App

Aplicación web Flask con temática de abejitas que incluye sistema de login y página de inicio, con base de datos MongoDB.

## 📋 Requisitos

- Docker
- Docker Compose

## ⚙️ Configuración Inicial

### 1. Configurar variables de entorno

Copia el archivo de ejemplo y configura tus credenciales:

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus valores:

```env
# Configuración de la aplicación Flask
FLASK_ENV=development
FLASK_DEBUG=1

# Configuración de MongoDB
MONGODB_URI=mongodb://mongodb:27017/abejitas_db
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=tu_password_seguro
MONGO_INITDB_DATABASE=abejitas_db

# Configuración de Mongo Express
ME_CONFIG_MONGODB_ADMINUSERNAME=admin
ME_CONFIG_MONGODB_ADMINPASSWORD=tu_password_seguro
ME_CONFIG_MONGODB_SERVER=mongodb
ME_CONFIG_MONGODB_PORT=27017
```

## 🚀 Ejecución con Docker Compose

### Iniciar todos los servicios

```bash
# Construir y ejecutar la aplicación
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d --build

# Solo ejecutar (sin rebuild)
docker-compose up

# Detener la aplicación
docker-compose down
```

## 🌐 Acceso a la Aplicación

Una vez que la aplicación esté ejecutándose:

- **Aplicación Flask**: http://localhost:8080/
- **Login**: http://localhost:8080/
- **Home**: http://localhost:8080/home
- **Database**: http://localhost:8080/database
- **Mongo Express** (UI MongoDB): http://localhost:8081/
  - Usuario: `admin`
  - Contraseña: (la que configuraste en `.env`)

## 📡 API Endpoints

### POST `/api/registros`

Crear un nuevo registro de sensor.

**Body (JSON):**

```json
{
  "valor_sensor": 23.5
}
```

**Respuesta:**

```json
{
  "message": "Registro creado exitosamente",
  "registro": {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "valor_sensor": 23.5,
    "created_at": "2025-10-21T20:01:27.879Z"
  }
}
```

### GET `/api/test-db`

Verificar la conexión a la base de datos.

**Respuesta:**

```json
{
  "status": "success",
  "message": "Conexión exitosa a MongoDB",
  "database": "abejitas_db",
  "collections": {
    "usuarios": 0,
    "productos": 0
  }
}
```

## 📁 Estructura del Proyecto

```
proyecto/
├── .env                    # Variables de entorno (NO incluir en Git)
├── .env.example            # Ejemplo de variables de entorno
├── .gitignore              # Archivos ignorados por Git
├── Dockerfile              # Configuración de Docker
├── docker-compose.yml      # Configuración de servicios Docker
├── README.md               # Este archivo
├── requirements.txt        # Dependencias Python del proyecto
├── mongo-init/             # Scripts de inicialización de MongoDB
│   └── init-mongo.js
└── src/
    ├── app.py              # Aplicación Flask principal
    ├── templates/
    │   ├── login.html      # Template de login
    │   ├── home.html       # Template de home
    │   └── database.html   # Template de base de datos
    └── static/             # Archivos estáticos (CSS, JS, imágenes)
```

## 🐳 Servicios Docker

El proyecto incluye 3 servicios en Docker:

1. **abejitas-flask** (Puerto 8080)
   - Aplicación Flask principal
   - Recarga automática en desarrollo
2. **mongodb** (Puerto 27017)
   - Base de datos MongoDB 7.0
   - Volumen persistente para datos
3. **mongo-express** (Puerto 8081)
   - Interfaz web para administrar MongoDB
   - Autenticación requerida

## � Dependencias

### Python

- Flask 3.1.2
- PyMongo 4.6.0
- Jinja2 3.1.6
- Werkzeug 3.1.3

### Docker

- Python 3.12-slim (imagen base)
- MongoDB 7.0
- Mongo Express (última versión)

Todas las dependencias están listadas en `requirements.txt`

## 🤝 Contribuir

1. Clona el repositorio
2. Copia `.env.example` a `.env` y configura tus variables
3. Ejecuta `docker-compose up --build`
4. Haz tus cambios
5. Prueba que todo funcione
6. Crea un Pull Request

## � Notas

- El proyecto usa MongoDB sin autenticación por defecto en desarrollo
- Para producción, configura autenticación en MongoDB
- Los datos de MongoDB persisten en el volumen `mongodb_data`

## 👥 Autores

- Semillero Abejitas Flask

## � Licencia

Este proyecto es de código abierto.
