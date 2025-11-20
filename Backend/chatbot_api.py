'''
TODO Conexion con Ollama
- [ ] Conectarse al modelo de Ollama
- [ ] Crear Parametodos de consulta
- [ ] Manejar respuestas y errores
- [ ] Agregar Informacion del hotel

TODO Conexion con Frontend
- [ ] Configurar API
- [ ] Probar integracion

TODO Mejoras futuras
- [ ] Conexion con base de datos
'''
# Para conectarse a Ollama y hacer preguntas al modelo
import requests

# Función para hacer una pregunta al chatbot y obtener la respuesta
''' 
Se le pasa una pregunta como string y devuelve la respuesta en string
'''
def preguntar_chatbot(pregunta):
    # URL del servidor de Ollama
    url = "http://localhost:11434/api/generate"

    # Payload con los parámetros para la solicitud
    '''
    model: Nombre del modelo a usar
    prompt: Pregunta o mensaje del usuario
    stream: Si se quiere la respuesta letra por letra (True) o completa (False)
    temperature: Nivel de creatividad en la respuesta (0.0 a 1.0)
    '''
    payload = {
        "model": "llama3.2:1b",
        "prompt": pregunta,
        "stream":False,
        "temperature":0.7
    }

    # Hacer la solicitud POST al servidor de Ollama, con url, parametros y tiempo de espera
    response = requests.post(url, json=payload, timeout=30)
    # Verificar que la solicitud fue exitosa
    response.raise_for_status()
    # Obtener la respuesta en formato JSON
    resultado = response.json()
    # Devolver la respuesta del chatbot
    return resultado.get("response")

# Ejemplo de uso
pregunta = input("Pregunta al chatbot: ").strip()
respuesta = preguntar_chatbot(pregunta)
print(respuesta)