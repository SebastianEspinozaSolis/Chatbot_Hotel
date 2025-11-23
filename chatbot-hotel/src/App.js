/*
TODO Tareas de front

- [x] Crear componente principal del Chatbot Hotel
  - [x] Crear Estados iniciales del Chatbot
  - [x] Crear Formulario de entrada de usuario
  - [x] Crear Chat con mensajes de usuario y bot
  - [x] Validadores basicos
  - [x] Vaciar input al enviar mensaje
  - [x] Manejar input vacio y estado de loading
  - [x] Manejar lados del chat (izquierda para bot, derecha para usuario)
  - [x] Hacer scroll automático al final del chat
  - [x] Agregar iconos y estilos con Tailwind CSS
- [x] Conectar con backend (pendiente de implementar en backend)
*/

// funciones especificas de React
import React, { useState, useRef, useEffect } from 'react';
// Iconos de lucide-react, https://lucide.dev/icons/
import { Send, Bot, User } from 'lucide-react';

// Componente principal del Chatbot Hotel
export default function ChatbotHotel() {

  /*Estados del Chatbot
  messages: array de mensajes del chat
  setMessages: función para actualizar los mensajes
  Estructura de messages: { role: 'user' | 'bot', content: 'texto del mensaje' }
  useState: maneja el estado inicial del chat con un mensaje de bienvenida del bot
  input: estado para el texto del input del usuario
  setInput: función para actualizar el estado del input
  loading: estado para indicar si se está esperando una respuesta del bot
  setLoading: función para actualizar el estado de loading
  messagesEndRef: referencia para hacer scroll automático al final del chat
  */
  const [messages, setMessages] = useState([
    { role: 'bot', content: '¡Hola! Soy el chatbot del Hotel Quinchamalí. ¿En qué puedo ayudarte?' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Función para hacer scroll automático al final del chat
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // useEffect para hacer scroll automático cuando cambian los mensajes
  useEffect(() => {
    scrollToBottom();
  }, [messages]);
  
  // Función para manejar el envío de mensajes
  const enviarMensaje = async (e) => {
    e.preventDefault();
    
    // Evitar enviar mensajes vacíos o mientras se carga una respuesta
    if (!input.trim() || loading) return;

    // Guardar el mensaje del usuario y luego limpiar el input
    const mensajeUsuario = input.trim();
    setInput('');
    
    // Agregar mensaje del usuario y mostrar loading
    setMessages(prev => [...prev, { role: 'user', content: mensajeUsuario }]);
    setLoading(true);

    // espacio para llamar al backend
    try {
      /* TODO: Conectar con backend
      - [x] Enviar el mensaje del usuario al backend
      - [x] Recibir la respuesta del bot
      - [x] Agregar la respuesta del bot a los mensajes
    
      */

      const response = await fetch('http://localhost:8000/api/chatbot', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: mensajeUsuario }),
      });

      const data = await response.json();

      setMessages(prev => [...prev,{
        role:'bot',
        content: data.response || 'Lo siento, no pude obtener una respuesta en este momento.'
      }]);
    } 
    // Manejo de errores en la conexión con el backend
    catch (error) {
      setMessages(prev => [...prev, { 
        role: 'bot', 
        content: '❌ Error de conexión. ¿Está el backend corriendo?' 
      }]);
    } 
    // Finalmente, desactivar el estado de loading
    finally {
      setLoading(false);
    }
  };

  return (
    // Contenedor principal del Chatbot
    // Para los estilos se esta usando Tailwind CSS, https://tailwindcss.com/plus/ui-blocks?ref=sidebar
    <div className="flex flex-col h-screen bg-gradient-to-br from-blue-50 to-blue-100">
      
      {/* Header */}
      <div className="bg-blue-600 text-white p-4 shadow-lg">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <Bot size={32} />
          <div>
            <h1 className="text-2xl font-bold">Hotel Quinchamalí</h1>
            <p className="text-sm text-blue-100">Chatbot</p>
          </div>
        </div>
      </div>

      {/* Chat Container */}
      <div className="flex-1 overflow-y-auto p-4">
        <div className="max-w-4xl mx-auto space-y-4">
          {/* Se recorre el array de mensajes para mostrarlos, se le da el indice como key y segun el rol se alinea a la derecha o izquierda */}
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              {/* Si es Bot se muestra el icono del bot */}
              {msg.role === 'bot' && (
                <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center flex-shrink-0">
                  <Bot size={20} className="text-white" />
                </div>
              )}
              
              {/* Si es usuario se le dara un color a sus mensajes, de lo contrario se mostrará el asignado a bot */}
              <div
                className={`max-w-xl p-4 rounded-2xl shadow-md ${
                  msg.role === 'user'
                    ? 'bg-blue-600 text-white rounded-br-none'
                    : 'bg-white text-gray-800 rounded-bl-none'
                }`}
              >
                {/* Mostrar el contenido del mensaje */}
                <p className="whitespace-pre-wrap">{msg.content}</p>
              </div>

              {/* Si es Usuario se muestra el icono del usuario */}
              {msg.role === 'user' && (
                <div className="w-8 h-8 rounded-full bg-gray-600 flex items-center justify-center flex-shrink-0">
                  <User size={20} className="text-white" />
                </div>
              )}
            </div>
          ))}

          {/* Indicador de carga mientras se espera la respuesta del bot */}
          {loading && (
            <div className="flex gap-3 justify-start">
              <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center">
                <Bot size={20} className="text-white" />
              </div>
              <div className="bg-white p-4 rounded-2xl rounded-bl-none shadow-md">
                <div className="flex gap-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                </div>
              </div>
            </div>
          )}
          
          {/* Referencia para hacer scroll automático al final de los mensajes */}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input Form */}
      <div className="border-t bg-white p-4 shadow-lg">
        {/* Formulario para enviar mensajes, activa loading mientras se espera respuesta y el boton de enviar */}
        <form onSubmit={enviarMensaje} className="max-w-4xl mx-auto flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Escribe tu pregunta..."
            disabled={loading}
            className="flex-1 p-3 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="bg-blue-600 text-white p-3 rounded-full hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
          >
            <Send size={20} />
          </button>
        </form>
      </div>
    </div>
  );
}