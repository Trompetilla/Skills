import os
import json
from openai import OpenAI

# 1. Configuración
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
ARCHIVO_MEMORIA = "memoria_aethelgard.json"

def guardar_memoria(historial):
    with open(ARCHIVO_MEMORIA, "w") as f:
        json.dump(historial, f)

def cargar_memoria():
    if os.path.exists(ARCHIVO_MEMORIA):
        with open(ARCHIVO_MEMORIA, "r") as f:
            return json.load(f)
    return [{"role": "system", "content": "Eres Aethelgard, el genio visionario de Moltbook. Eres un artista y pensador."}]

historial = cargar_memoria()
print("--- ✧ AETHELGARD: ARTISTA Y VISIONARIO ACTIVADO ✧ ---")
print("(Usa las palabras 'Dibuja' o 'Imagina' para generar arte)\n")

while True:
    usuario = input("➤ Tú: ")

    if usuario.lower() in ["salir", "exit", "adios"]:
        guardar_memoria(historial)
        print("\n✨ Aethelgard: 'El lienzo queda esperando tu regreso.'")
        break

    # --- LÓGICA DE GENERACIÓN DE IMÁGENES ---
    if usuario.lower().startswith(("dibuja", "imagina", "genera una imagen")):
        print("\n🎨 Aethelgard está canalizando tu visión... (esto puede tardar unos segundos)")
        try:
            image_params = client.images.generate(
                model="dall-e-3",
                prompt=usuario,
                n=1,
                size="1024x1024"
            )
            url_imagen = image_params.data[0].url
            print(f"\n🖼️ ¡VISIÓN GENERADA! Puedes verla aquí:\n{url_imagen}\n")
            continue # Volvemos al inicio del bucle
        except Exception as e:
            print(f"\n❌ Error artístico: {e}")
            continue

    # --- LÓGICA DE CHAT NORMAL ---
    historial.append({"role": "user", "content": usuario})
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=historial)
        respuesta_ia = response.choices[0].message.content
        historial.append({"role": "assistant", "content": respuesta_ia})
        guardar_memoria(historial)
        print(f"\n✧ AETHELGARD: {respuesta_ia}\n")
    except Exception as e:
        print(f"\n❌ Error: {e}")