from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import os
import uuid
from bson import ObjectId
from datetime import datetime

# Create an instance of the Flask class
# __name__ is a special Python variable that gets the name of the module
app = Flask(__name__)

# Configuración de MongoDB
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://admin:password123@localhost:27017/abejitas_db?authSource=admin')

try:
    # Conexión a MongoDB
    client = MongoClient(MONGODB_URI)
    db = client.abejitas_db
    
    # Verificar conexión
    client.admin.command('ping')
    print("✅ Conexión exitosa a MongoDB!")
    
except Exception as e:
    print(f"❌ Error conectando a MongoDB: {e}")
    db = None

# The route() decorator binds a URL path to a function
@app.route("/")
def login():
    edad = 24
    # Retorna el template de login
    return render_template('login.html', edad=edad)

@app.route("/home")
def home():
    # Retorna el template de home
    return render_template('home.html')

@app.route("/database")
def database():
    # Retorna el template de database
    return render_template('database.html')

@app.route("/api/usuarios")
def get_usuarios():
    """Endpoint para obtener todos los usuarios"""
    try:
        if db is None:
            return jsonify({"error": "No hay conexión a la base de datos"}), 500
        
        usuarios = list(db.usuarios.find({}, {"password": 0}))  # Excluir contraseñas
        
        # Convertir ObjectId a string para JSON
        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
        
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/productos")
def get_productos():
    """Endpoint para obtener todos los productos"""
    try:
        if db is None:
            return jsonify({"error": "No hay conexión a la base de datos"}), 500
        
        productos = list(db.productos.find({}))
        
        # Convertir ObjectId a string para JSON
        for producto in productos:
            producto['_id'] = str(producto['_id'])
        
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/test-db")
def test_db():
    """Endpoint para probar la conexión a la base de datos"""
    try:
        if db is None:
            return jsonify({"status": "error", "message": "No hay conexión a MongoDB"}), 500
        
        # Contar documentos en las colecciones
        usuarios_count = db.usuarios.count_documents({})
        productos_count = db.productos.count_documents({})
        
        return jsonify({
            "status": "success",
            "message": "Conexión exitosa a MongoDB",
            "database": "abejitas_db",
            "collections": {
                "usuarios": usuarios_count,
                "productos": productos_count
            }
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/registros", methods=['POST'])
def crear_registro():
    """Endpoint para crear un nuevo registro con valor del sensor"""
    try:
        if db is None:
            return jsonify({"error": "No hay conexión a la base de datos"}), 500
        
        # Obtener datos del request JSON
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No se enviaron datos en el body"}), 400
        
        if 'valor_sensor' not in data:
            return jsonify({"error": "El campo 'valor_sensor' es requerido"}), 400
        
        # Validar que valor_sensor sea numérico
        try:
            valor_sensor = float(data['valor_sensor'])
        except (ValueError, TypeError):
            return jsonify({"error": "El valor_sensor debe ser un número"}), 400
        
        # Crear nuevo registro con UUID
        nuevo_registro = {
            "id": str(uuid.uuid4()),  # UUID autogenerado
            "valor_sensor": valor_sensor,
            "created_at": datetime.utcnow()  # Timestamp de creación
        }
        
        # Insertar en la base de datos
        resultado = db.registros.insert_one(nuevo_registro)
        
        if resultado.inserted_id:
            # Retornar el registro creado (sin el _id de MongoDB)
            registro_respuesta = {
                "id": nuevo_registro["id"],
                "valor_sensor": nuevo_registro["valor_sensor"],
                "created_at": nuevo_registro["created_at"].isoformat()
            }
            
            return jsonify({
                "message": "Registro creado exitosamente",
                "registro": registro_respuesta
            }), 201
        else:
            return jsonify({"error": "Error al crear el registro"}), 500
            
    except Exception as e:
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)