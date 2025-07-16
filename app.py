import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestión de Documentos", layout="centered")

# Título principal
st.title("📄 Gestión de Documentos")

# Instrucciones iniciales
st.markdown("Por favor, siga los pasos para cargar y validar su documento.")

# 1. Selección del tipo de documento
tipo_documento = st.selectbox("1️⃣ Seleccione el tipo de archivo:", ["Factura", "Albarán"])

# 2. Carga del archivo
st.markdown("2️⃣ Cargue su archivo (puede arrastrarlo o hacer clic en el botón para buscar en su equipo):")
archivo = st.file_uploader("Seleccione un archivo desde su equipo", type=["pdf", "docx", "xlsx", "csv", "txt"], label_visibility="collapsed")

# Mostrar nombre del archivo y retroalimentación visual
if archivo:
    st.success(f"✅ Archivo cargado correctamente: {archivo.name}")
    archivo_cargado = False
else:
    archivo_cargado = False
    st.info("📂 Aún no ha cargado ningún archivo.")

# 3. Botón para procesar el archivo
if archivo_cargado:
    st.markdown("3️⃣ ¿El archivo contiene errores?")
    tiene_error = st.radio("Seleccione una opción:", ["No", "Sí"], index=0)

    if st.button("🔍 Procesar archivo"):
        if tiene_error == "Sí":
            st.warning("⚠️ Los documentos no coinciden\nVariables que no coinciden\n")
            accion = st.radio("¿Quieres ver los documentos en su totalidad?", ["Aceptar", "Cancelar"], index=0)

            # 4. Si es Albarán y se cancela, mostrar opciones adicionales
            if tipo_documento == "Albarán" and accion == "Cancelar":
                st.markdown("🛠️ ¿Quieres modificar la línea de pedido?")
                opcion_albaran = st.selectbox("Seleccione una opción:", ["Aceptar", "Cancelar"])
                st.info(f"Ha seleccionado: **{opcion_albaran}**")
        else:
            st.success("✅ El archivo ha sido validado correctamente. No se encontraron errores.")
