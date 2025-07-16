import streamlit as st
import random

st.set_page_config(page_title="Subida de Archivos", layout="centered")
st.markdown("<h2 style='font-size: 32px;'>Selecciona el tipo de archivo</h2>", unsafe_allow_html=True)

# Paso 1: Selección de tipo
tipo = st.selectbox("Tipo de archivo", ["Factura", "Albarán"])

st.markdown("### ")
st.markdown("<h3>📁 Arrastra un archivo</h3>", unsafe_allow_html=True)

# Paso 2: Carga de archivo
uploaded_file = st.file_uploader("", type=["pdf", "jpg", "png", "docx"])

if uploaded_file:
    st.markdown(f"""
        <div style='background-color: #e6ffe6; padding: 20px; border-radius: 10px; text-align: center; font-size: 18px;'>
            Archivo cargado: <b>{uploaded_file.name}</b>
        </div>
    """, unsafe_allow_html=True)

    # Paso 3: Simular procesamiento
    st.markdown("---")
    st.markdown("### Resultado del procesamiento")

    resultado = random.choice(["ok", "warning"])  # Simulación

    if resultado == "warning":
        st.markdown("""
        <div style="background-color: #f4edfa; padding: 20px; border-radius: 15px;">
            <h4 style="color: #5a189a;">⚠️ Los documentos no coinciden</h4>
            <p><i>"Variables que no coinciden"</i></p>
            <p>¿Quieres ver los documentos en su totalidad?</p>
            <div style="display: flex; gap: 20px;">
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            aceptar = st.button("Aceptar")
        with col2:
            cancelar = st.button("Cancelar")

        if cancelar and tipo == "Albarán":
            st.markdown("### ¿Qué deseas hacer con los datos del albarán?")
            accion = st.selectbox("Selecciona una opción", ["", "Modificar datos", "Volcar datos"])
            if accion:
                st.success(f"Has seleccionado: {accion}")

    else:
        st.success("✅ Todo correcto. Los documentos coinciden.")

else:
    st.markdown("""
        <div style='background-color: #f2f2f2; padding: 20px; border-radius: 10px; text-align: center; font-size: 16px;'>
            Arrastra el archivo aquí o examina tu equipo.
        </div>
    """, unsafe_allow_html=True)
