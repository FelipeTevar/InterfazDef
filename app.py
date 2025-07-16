import streamlit as st

# Título de la aplicación
st.title("Gestión de Documentos")

# 1. Desplegable para seleccionar tipo de documento
tipo_documento = st.selectbox("Selecciona el tipo de documento:", ["Factura", "Albarán"])

# 2. Carga de archivos
st.markdown("### Cargar archivo")
archivo = st.file_uploader("Arrastra o examina un archivo", type=["pdf"])

# Feedback visual: mostrar nombre del archivo y cambiar color
if archivo:
    st.success(f"Archivo cargado: {archivo.name}")
    archivo_cargado = True
else:
    archivo_cargado = False
    st.info("No se ha cargado ningún archivo.")

# 3. Botón para procesar archivo
if archivo_cargado:
    if st.button("Procesar archivo"):
        # Simulación de validación
        if "error" in archivo.name.lower():
            st.warning("Advertencia: El archivo contiene inconsistencias.")
            accion = st.radio("¿Qué deseas hacer?", ["Aceptar", "Cancelar"])

            # 4. Si es Albarán y se cancela, mostrar opciones adicionales
            if tipo_documento == "Albarán" and accion == "Cancelar":
                st.markdown("### ¿Qué deseas hacer con el albarán?")
                opcion_albaran = st.selectbox("Selecciona una opción:", ["Modificar", "Volcar datos"])
                st.info(f"Opción seleccionada: {opcion_albaran}")
        else:
            st.success("✅ El archivo ha sido validado correctamente.")
