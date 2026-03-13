import streamlit as st

# 1. Configuración de la página (Debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="IA en la Salud Mental",
    page_icon="🧠",
    layout="wide"
)

# --- BARRA LATERAL CON RESÚMENES ---
with st.sidebar:
    st.title("Recursos y Referencias")
    # Nota: Se eliminó el [cite: 2] que causaba el error
    st.info("**Frase del día:**\n\n *'Que la innovación no sea un conflicto'*")
    
    st.header("Bibliografía Completa")
    
    with st.expander("Agudelo-Londoño (2025)"):
        st.write("**Resumen:** Analiza el impacto de la IA en la edición académica de salud. Destaca que optimiza la revisión de manuscritos, pero advierte sobre riesgos éticos como la pérdida de originalidad.")

    with st.expander("Beg et al. (2024)"):
        st.write("**Resumen:** Revisa el uso de chatbots y análisis del lenguaje para apoyo continuo. Resalta que mejora el acceso pero no reemplaza la empatía humana.")

    with st.expander("Cruz-González et al. (2025)"):
        st.write("**Resumen:** Revisión sistemática sobre diagnóstico y monitoreo. La IA ayuda en la detección temprana de depresión y ansiedad mediante datos de redes sociales.")

    with st.expander("Gkintoni et al. (2025)"):
        st.write("**Resumen:** Examina el uso de dCBT potenciada con IA para tratar el insomnio, ajustando el tratamiento según patrones de sueño en tiempo real.")

    with st.expander("Luxton (2013)"):
        st.write("**Resumen:** Analiza aplicaciones de IA como agentes conversacionales para la evaluación del riesgo suicida y seguimiento terapéutico.")

# --- CUERPO DEL DASHBOARD ---
st.title("¿Un psicólogo en mi bolsillo?")
st.subheader("Cómo la Inteligencia Artificial está transformando la salud mental")

st.markdown("""
En los últimos años, la tecnología ha dejado de ser solo una herramienta de comunicación para convertirse en una aliada inesperada de nuestra salud emocional.
""")

# Secciones de Conceptos
col1, col2 = st.columns(2)
with col1:
    st.info("### Machine Learning")
    st.write("Las máquinas pueden analizar miles de datos para predecir si una persona está en riesgo de tener una recaída emocional.")

with col2:
    st.success("### Procesamiento de Lenguaje Natural")
    st.write("Capacidad de la IA para 'entender' el sentimiento detrás de las palabras y detectar patrones de tristeza.")

# Aplicaciones
st.header("De la teoría a la práctica")
tab1, tab2 = st.tabs(["Chatbots", "Terapia Digital (dCBT)"])

with tab1:
    st.write("Sistemas disponibles las 24 horas que han demostrado efectividad para ayudar a personas con depresión y ansiedad.")

with tab2:
    st.write("Tecnología que ayuda a combatir el insomnio logrando cambios reales en el funcionamiento del cerebro.")

# Ética
st.warning("### Retos Éticos")
st.write("- **Privacidad:** La información debe estar protegida bajo leyes estrictas.")
st.write("- **Veracidad:** Cuidado con la información generada; debe ser validada por expertos.")
st.write("- **Alianza Terapéutica:** La calidez humana aún no ha sido igualada por la tecnología.")

st.divider()
st.markdown("<div style='text-align: center;'>El futuro es una combinación de la precisión del algoritmo y la empatía humana.</div>", unsafe_allow_html=True)
