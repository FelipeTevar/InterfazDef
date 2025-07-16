import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestión de Documentos", layout="centered")

# Título principal
st.title("📄 Gestión de Documentos")

# Instrucciones iniciales
st.markdown("Por favor, siga los pasos para cargar y validar su documento. Esta aplicación está diseñada para ser fácil de usar.")

# 1. Selección del tipo de documento
tipo_documento = st.selectbox("1️⃣ Seleccione el tipo de documento:", ["Factura", "Albarán"])

# 2. Carga del archivo
st.markdown("2️⃣ Cargue su archivo (puede arrastrarlo o hacer clic en el botón para buscar en su equipo):")
archivo = st.file_uploader("Seleccione un archivo desde su equipo", type=["pdf", "docx", "xlsx", "csv", "txt"], label_visibility="collapsed")

# Mostrar nombre del archivo y retroalimentación visual
if archivo:
    st.success(f"✅ Archivo cargado correctamente: {archivo.name}")
    archivo_cargado = True
else:
    archivo_cargado = False
    st.info("📂 Aún no ha cargado ningún archivo.")

# 3. Botón para procesar el archivo
if archivo_cargado:
    if st.button("🔍 Procesar archivo"):
        # Simulación de validación
        if "error" in archivo.name.lower():
            st.warning("⚠️ El archivo contiene datos que no coinciden o presentan errores.")
            accion = st.radio("¿Qué desea hacer?", ["Aceptar", "Cancelar"], index=0)

            # 4. Si es Albarán y se cancela, mostrar opciones adicionales
            if tipo_documento == "Albarán" and accion == "Cancelar":
                st.markdown("🛠️ ¿Qué desea hacer con el albarán?")
                opcion_albaran = st.selectbox("Seleccione una opción:", ["Modificar albarán", "Volcar datos del albarán"])
                st.info(f"Ha seleccionado: **{opcion_albaran}**")
        else:
            st.success("✅ El archivo ha sido validado correctamente. No se encontraron errores.")

# Pie de página
st.markdown("---")
st.markdown("🧓 Esta aplicación ha sido diseñada para ser clara y sencilla. Si necesita ayuda, por favor pida asistencia.")
