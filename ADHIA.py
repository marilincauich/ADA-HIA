import streamlit as st

# 1. IMPORTANTE: Esto debe ir al principio para que no de NameError
# Configuración de la página
st.set_page_config(
    page_title="IA en la Salud Mental",
    page_icon="🧠",
    layout="wide"
)

# --- BARRA LATERAL CON RESÚMENES DETALLADOS ---
with st.sidebar:
    st.title("Recursos y Referencias")
    st.info("**Frase del día:**\n\n *'Que la innovación no sea un conflicto'*") [cite: 2]
    
    st.header("Bibliografía Completa")
    st.write("Haz clic para expandir los resúmenes científicos:")

    # Referencia 1: Agudelo-Londoño
    with st.expander("Agudelo-Londoño (2025)"):
        st.write("**Título:** En la era de la IA: ¿conocimiento original y veraz? ")
        st.write("**Resumen:** Analiza cómo la IA optimiza la edición en salud (revisión de errores), pero advierte sobre la pérdida de originalidad y la generación de referencias falsas. ")

    # Referencia 2: Beg et al.
    with st.expander("Beg et al. (2024)"):
        st.write("**Título:** Artificial Intelligence for Psychotherapy ")
        st.write("**Resumen:** Describe el uso de chatbots y análisis de lenguaje para apoyo continuo. Resalta que, aunque mejora el acceso, no puede reemplazar la empatía humana. ")

    # Referencia 3: Cruz-Gonzalez et al.
    with st.expander("Cruz-González et al. (2025)"):
        st.write("**Título:** AI in mental health care: systematic review ")
        st.write("**Resumen:** Revisa el uso de algoritmos para detectar depresión y ansiedad mediante redes sociales y apps. Subraya la necesidad de supervisión profesional. ")

    # Referencia 4: Gkintoni et al.
    with st.expander("Gkintoni et al. (2025)"):
        st.write("**Título:** Digital and AI-Enhanced CBT for Insomnia ")
        st.write("**Resumen:** Explica cómo la IA personaliza el tratamiento del insomnio analizando patrones de sueño nocturnos para ajustar la terapia en tiempo real. ")

    # Referencia 5: Luxton
    with st.expander("Luxton (2013)"):
        st.write("**Título:** AI in Psychological Practice ")
        st.write("**Resumen:** Pionero en analizar agentes conversacionales para evaluar riesgo de suicidio. Concluye que la IA es una herramienta de apoyo, no un sustituto. ")

# --- CUERPO DEL ARTÍCULO ---
st.title("¿Un psicólogo en mi bolsillo?") [cite: 1]
st.subheader("Cómo la Inteligencia Artificial está transformando la salud mental")

st.markdown("""
En los últimos años, la tecnología se ha convertido en una aliada inesperada de nuestra salud emocional[cite: 3]. 
Hoy, la IA ayuda a identificar señales de ansiedad, depresión e insomnio[cite: 5].
""")

# Sección de Conceptos
col1, col2 = st.columns(2)
with col1:
    st.info("### Machine Learning")
    st.write("Permite predecir riesgos de recaída emocional analizando miles de datos[cite: 8].")
with col2:
    st.success("### Procesamiento de Lenguaje Natural")
    st.write("Capacidad de 'entender' el sentimiento detrás de las palabras y detectar patrones de tristeza[cite: 9, 10].")

# Sección de Aplicaciones
st.header("Aplicaciones Prácticas")
tab1, tab2 = st.tabs(["Chatbots", "Terapia Digital (dCBT)"])
with tab1:
    st.write("Asistentes disponibles 24/7 para ofrecer apoyo inmediato en casos de ansiedad[cite: 13, 14].")
with tab2:
    st.write("Tratamientos para el insomnio que logran cambios reales en el funcionamiento del cerebro[cite: 16, 17].")

# Retos Éticos
st.warning("### Retos Éticos Irreemplazables")
st.write("* **Privacidad:** Protección estricta de datos personales[cite: 22].")
st.write("* **Veracidad:** La información debe ser validada por expertos para evitar datos falsos[cite: 23].")
st.write("* **Empatía:** La calidez humana de la alianza terapéutica sigue siendo inalcanzable para las máquinas[cite: 24].")

st.divider()
st.write("**Conclusión:** El futuro es una combinación entre la precisión del algoritmo y la empatía humana[cite: 28].")
