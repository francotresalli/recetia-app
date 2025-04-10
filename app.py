# Este archivo requiere los paquetes streamlit y openai >= 1.0.0
# Instalación recomendada:
# pip install streamlit openai

import streamlit as st
import openai
import os

# Configurar la API key desde secrets o variable de entorno
api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # Método compatible con openai>=1.0.0 si no usás el cliente nuevo

st.set_page_config(page_title="RecetIA - Cociná con lo que tenés", page_icon="🥘")

# Título y descripción
st.title("RecetIA 🥘")
st.write("Descubrí recetas fáciles y sabrosas según lo que tengas en tu heladera. Solo ingresá los ingredientes y dejá que la IA cocine por vos.")

# Input del usuario
ingredientes = st.text_area("¿Qué ingredientes tenés?", placeholder="Ejemplo: arroz, zanahoria, huevo, cebolla")

# Botón para generar receta
if st.button("¡Generar receta!"):
    if ingredientes:
        with st.spinner("Pensando una receta deliciosa..."):
            prompt = f"Tengo los siguientes ingredientes: {ingredientes}. Sugerime una receta fácil, rápida y sabrosa que pueda hacer solo con eso. Indicá los pasos y la cantidad aproximada de ingredientes."

            try:
                respuesta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                receta = respuesta.choices[0].message.content
                st.success("¡Receta generada!")
                st.markdown(receta)
            except Exception as e:
                st.error("Ocurrió un error generando la receta. Verificá tu conexión o clave de API.")
                st.exception(e)
    else:
        st.warning("Por favor ingresá al menos un ingrediente.")

# Sección "Cómo funciona"
st.markdown("---")
st.header("¿Cómo funciona?")
st.markdown("""
1. Ingresás los ingredientes que tenés disponibles.
2. Presionás el botón y la IA analiza tus ingredientes.
3. RecetIA te sugiere una receta simple, rápida y sabrosa que podés hacer en casa.

🔍 *Recomendamos usar entre 3 y 10 ingredientes para mejores resultados.*

💡 *RecetIA no reemplaza a un chef profesional, pero te saca de apuros.*
""")
