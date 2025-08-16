from flask import Flask, request, jsonify, render_template_string
import string
import random
 
app = Flask(__name__)
 
# Función para generar la contraseña
def generar_password(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))
 
# Pantalla de bienvenida con formulario
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>Generador de Contraseñas - Grupo 8</title>
<style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; text-align: center; padding-top: 50px; }
        .container { background-color: #fff; padding: 30px; border-radius: 10px; display: inline-block; }
        input[type=number] { padding: 5px; font-size: 16px; width: 60px; }
        button { padding: 5px 10px; font-size: 16px; cursor: pointer; }
        h2 { color: #333; }
        p { color: #555; }
</style>
</head>
<body>
<div class="container">
<h2>BIENVENIDO AL MEJOR GENERADOR DE CONTRASEÑAS</h2>
<p>GRUPO 8 - MAESTRIA EN CIBERSEGURIDAD</p>
<p>INTEGRANTES:<br>- Omar Larrea<br>- Rommel Arevalo<br>- Henry Barreno</p>
<form method="get" action="/generar_password">
<label for="longitud">Cantidad de caracteres:</label>
<input type="number" id="longitud" name="longitud" min="4" max="64" required>
<button type="submit">Generar contraseña</button>
</form>
</div>
</body>
</html>
"""
 
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)
 
@app.route('/generar_password', methods=['GET'])
def api_generar_password():
    longitud = request.args.get('longitud')
    if not longitud:
        return jsonify({"error": "Se requiere indicar la cantidad de caracteres"}), 400
    try:
        longitud = int(longitud)
    except ValueError:
        return jsonify({"error": "Longitud inválida"}), 400
    if longitud < 4 or longitud > 64:
        return jsonify({"error": "Longitud debe estar entre 4 y 64"}), 400
 
    password = generar_password(longitud)
    return jsonify({"password": password})
 
if __name__ == '__main__':
    app.run(debug=True)