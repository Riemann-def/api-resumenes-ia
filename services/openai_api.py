import json
from app.extensions import openAi_client

def crear_prompt(url):
    prompt = [
        {
            "role": "system", 
            "content": """Actúa como un asistente inteligente y genera un resumen conciso de la noticia contenida en el siguiente artículo, 
                            incluyendo los siguientes atributos: título, autor, fecha de publicación, 
                            categoría (opciones: Cultura, Deportes, Economía, Política, Salud, Tecnología), 
                            tono (opciones: Informativo, Neutro, Optimista, Pesimista, Sarcástico) 
                            y nivel de fake news (opciones: Alto, Bajo, Medio, Ninguno)."""
        },
        {
            "role": "user", 
            "content": f"Artículo: {url}"
        }
    ]
    print("Prompt generado:", prompt)  # Imprimir el prompt
    return prompt

def crear_response_format():
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "resumen_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "resumen": {
                        "description": "El resumen del artículo",
                        "type": "string"
                    },
                    "categoria": {
                        "description": "La categoría de la noticia",
                        "type": "string"
                    },
                    "tono": {
                        "description": "El tono de la noticia",
                        "type": "string"
                    },
                    "fake_news_level": {
                        "description": "El nivel de fake news",
                        "type": "string"
                    },
                    "additionalProperties": False
                }
            }
        }
    }

def procesar_respuesta(response):
    try:
        contenido = response.choices[0].message.content
        contenido = json.loads(contenido)
        return {
            'resumen': contenido.get('resumen', "Resumen no encontrado"),
            'category': contenido.get('categoria', "Categoría no encontrada"),
            'tone': contenido.get('tono', "Tono no encontrado"),
            'fake_news_level': contenido.get('fake_news_level', "Nivel de fake news no encontrado")
        }
    except Exception as e:
        return {"error": f"Error al procesar la respuesta: {str(e)}"}

def realizar_peticion_openai(url):
    prompt = crear_prompt(url)
    response_format = crear_response_format()
    
    try:
        response = openAi_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=prompt,
            response_format=response_format
        )
        return procesar_respuesta(response)
    except Exception as e:
        return {"error": f"Error al realizar la petición a OpenAI: {str(e)}"}

def generate_summary(url):
    respuesta = realizar_peticion_openai(url)
    print("Respuesta de OpenAI:", respuesta)  # Imprimir la salida
    return respuesta
