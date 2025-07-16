import streamlit as st

st.set_page_config(page_title="Subida de Archivos", layout="centered")

st.markdown("<h2 style='font-size: 32px;'>Selecciona el tipo de archivo</h2>", unsafe_allow_html=True)

# Paso 1: Selección de tipo de archivo
tipo = st.selectbox("Tipo de archivo", ["Factura", "Albarán"])

st.markdown("### ")
st.markdown("<h3>📁 Arrastra un archivo</h3>", unsafe_allow_html=True)

# Paso 2: Subida del archivo
uploaded_file = st.file_uploader("", type=["pdf", "jpg", "png", "docx"])

# Simulador de análisis para la demo
modo_demo = st.checkbox("Modo demo (activar simulación manual)")
if modo_demo:
    resultado_simulado = st.radio("Forzar resultado de análisis", ["Correcto", "Advertencia"])
else:
    resultado_simulado = None

# Mostrar información del archivo cargado
if uploaded_file:
    st.markdown(f"""
        <div style='background-color: #e6ffe6; padding: 20px; border-radius: 10px; text-align: center; font-size: 18px;'>
            Archivo cargado: <b>{uploaded_file.name}</b>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Resultado del procesamiento")

    # Definir el resultado según demo o aleatorio
    if modo_demo:
        resultado = "ok" if resultado_simulado == "Correcto" else "warning"
    else:
        import random
        resultado = random.choice(["ok", "warning"])

    # Resultado: Advertencia
    if resultado == "warning":
        st.markdown("""
        <div style="background-color: #f4edfa; padding: 20px; border-radius: 15px;">
            <h4 style="color: #5a189a;">⚠️ Los documentos no coinciden</h4>
            <p><i>"Variables que no coinciden"</i></p>
            <p>¿Quieres ver los documentos en su totalidad?</p>
                    
            col1, col2 = st.columns(2)
            aceptar = col1.button("Aceptar")
            cancelar = col2.button("Cancelar")
        </div>
        """, unsafe_allow_html=True)

       

        # Mostrar opciones adicionales si es albarán y se cancela
        if cancelar and tipo == "Albarán":
            st.markdown("### ¿Qué deseas hacer con los datos del albarán?")
            accion = st.selectbox("Selecciona una opción", ["", "Modificar datos", "Volcar datos"])
            if accion:
                st.success(f"Has seleccionado: {accion}")

    # Resultado: Correcto
    else:
        st.markdown("""
        <div style="background-color: #e6f9f0; padding: 20px; border-radius: 15px;">
            <h4 style="color: #007f5f;">✅ Todo correcto. Los documentos coinciden.</h4>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
        <div style='background-color: #f2f2f2; padding: 20px; border-radius: 10px; text-align: center; font-size: 16px;'>
            Arrastra el archivo aquí o examina tu equipo.
        </div>
    """, unsafe_allow_html=True)
