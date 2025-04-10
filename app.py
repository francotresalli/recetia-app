# Este archivo requiere los paquetes streamlit y google-generativeai
# Instalación recomendada:
# pip install streamlit google-generativeai

import streamlit as st
import google.generativeai as genai
import os

# Configurar la API key desde secrets o variable de entorno
gemini_api_key = st.secrets["gemini_api_key"] if "gemini_api_key" in st.secrets else os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

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
                model = genai.GenerativeModel(model_name="gemini-pro")
                response = model.generate_content(prompt)
                receta = response.text
                st.success("¡Receta generada!")
                st.markdown(receta)
            except Exception as e:
                st.error("Ocurrió un error generando la receta. Verificá tu conexión o clave de API de Gemini.")
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
