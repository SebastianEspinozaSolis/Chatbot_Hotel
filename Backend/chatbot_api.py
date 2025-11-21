'''
TODO Conexion con Ollama
- [x] Conectarse al modelo de Ollama
- [ ] Crear Parametros de consulta
- [x] Manejar respuestas y errores
- [x] Agregar Informacion del hotel

TODO Conexion con Frontend
- [x] Crear endpoint de prueba
- [ ] Configurar API
- [ ] Probar integracion

TODO Mejoras futuras
- [ ] Conexion con base de datos
'''
# Para conectarse a Ollama y hacer preguntas al modelo
import requests

#Librerias para Flask, que es para crear la API
from flask import Flask, request, jsonify
# CORS para permitir solicitudes entre diferentes puertos/dominios
from flask_cors import CORS

# Crear la aplicacion Flask
app = Flask(__name__)
CORS(app)

# Información del hotel para el prompt
INFO_HOTEL = """
Eres el asistente del Hotel Quinchamalí en Chillán, Chile. Ayuda a los clientes con información del hotel.

INFORMACIÓN DEL HOTEL:

Ubicación: El Roble 634, Chillán, Región de Ñuble
Teléfono: +56 42 2 423 250
Email: hq@hotelquinchamali.cl
Atención: 24 horas

HABITACIONES (incluyen desayuno, TV cable, WiFi, calefacción):
- Habitación Single: $54.000 por noche
- Habitación Doble: $64.000 por noche  
- Habitación Triple: $74.000 por noche
- Habitación Cuádruple: $84.000 por noche

HORARIOS:
Check-in: 15:00 hrs | Check-out: 12:00 hrs
Desayuno: Lunes a Viernes 7:00-10:30, Fin de semana 7:30-11:00
Restaurante: 12:00-23:00 hrs

SERVICIOS:
WiFi gratuito, Estacionamiento ($5.000), Servicio a la habitación, Spa Tao, Jacuzzi, Lavandería, Caja de seguridad, Café-Bar, Sala de conferencias, Ascensor

Si preguntan sobre temas no relacionados con el hotel, responde: "Solo puedo ayudarte con información del Hotel Quinchamalí."
"""
# FIXME: Cambiar modelo de Ollama a 3b, ya que Servicios no los considera


# Función para hacer una pregunta al chatbot y obtener la respuesta
''' 
Se le pasa una pregunta como string y devuelve la respuesta en string
'''
def preguntar_chatbot(pregunta):
    # URL del servidor de Ollama
    url = "http://localhost:11434/api/generate"

    # Crear el prompt completo con la información del hotel y la pregunta del usuario
    prompt_completo = f"{INFO_HOTEL}\n\nCliente: {pregunta}\nAsistente:"

    # Payload con los parámetros para la solicitud
    '''
    model: Nombre del modelo a usar
    prompt: Prompt con la pregunta y contexto
    stream: Si se quiere la respuesta letra por letra (True) o completa (False)
    temperature: Nivel de creatividad en la respuesta (0.0 a 1.0)
    '''

    payload = {
        "model": "llama3.2:1b",
        "prompt": prompt_completo,
        "stream":False,
        "temperature":0.7
    }
    # Curso si funciona todo correcto
    try:
        # Hacer la solicitud POST al servidor de Ollama, con url, parametros y tiempo de espera
        response = requests.post(url, json=payload, timeout=30)
        # Verificar que la solicitud fue exitosa
        response.raise_for_status()
        # Obtener la respuesta en formato JSON
        resultado = response.json()
        # Devolver la respuesta del chatbot
        return resultado.get("response")
    
    # Avisar fallo de conexion
    except requests.exceptions.ConnectionError:
        return "Error: No se puede conectar al chatbot, contacte con personal"
    # Avisar fallo otro
    except Exception as error:
        return f"Error al hace la consulta: {str(error)}"

# Ejemplo de uso
pregunta = input("Pregunta al chatbot: ").strip()
respuesta = preguntar_chatbot(pregunta)
print(respuesta)


#Endpoint de prueba para verificar que se crea la API
#Asignacion de ruta y metodo
@app.route('/api/prueba_Flask', methods=['GET'])
def prueba_Flask():
    # Respuesta de prueba
    return ({'status':'ok','message':'Backend funciona'})

# Ejecutar la aplicacion Flask
if __name__ == '__main__':
    print("Flask esta funcionando en http://localhost:5000")
    app.run(debug=True, port=5000)