import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IA en la Salud Mental",
    page_icon="🧠",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stQuote {
        font-style: italic;
        color: #555;
        border-left: 5px solid #4a90e2;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (Navegación y Bibliografía) ---
with st.sidebar:
    st.title("Recursos")
    st.info("**Frase del día:**\n\n *'Que la innovación no sea un conflicto'*")
    
    st.header("Bibliografía")
    with st.expander("Ver referencias académicas"):
        st.caption("Agudelo-Londoño, S. M. (2025). Revista AMC, 50(1).")
        st.caption("Beg, M. J., et al. (2024). Artificial Intelligence for Psychotherapy.")
        st.caption("Cruz-Gonzalez, P., et al. (2025). Psychological Medicine, 55.")
        st.caption("Gkintoni, E., et al. (2025). Journal of Clinical Medicine, 14.")
        st.caption("Luxton, D. D. (2013). Professional Psychology: Research and Practice.")

# --- TÍTULO PRINCIPAL ---
st.title("¿Un psicólogo en mi bolsillo?")
st.subheader("Cómo la Inteligencia Artificial está transformando la salud mental")
st.markdown("---")

# --- INTRODUCCIÓN ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    En los últimos años, la tecnología ha dejado de ser solo una herramienta de comunicación para convertirse en una 
    **aliada inesperada de nuestra salud emocional**.
    
    Hoy en día, la Inteligencia Artificial (IA) no solo recomienda canciones o rutas de tráfico; también está aprendiendo a 
    **identificar señales de ansiedad, depresión e insomnio**, colaborando estrechamente con los profesionales de la psicología clínica.
    """)

with col2:
    st.image("https://img.icons8.com/illustrations/external-pablo-dot-design/512/external-online-therapy-medical-pablo-dot-design.png", caption="IA y Bienestar")

# --- SECCIÓN 1: CONCEPTOS ---
st.header("¿Qué es realmente la IA en psicología?")
col_a, col_b = st.columns(2)

with col_a:
    st.info("### Machine Learning")
    st.write("Mediante el aprendizaje automático, las máquinas pueden analizar miles de datos para predecir si una persona está en riesgo de tener una recaída emocional.")
    st.caption("*Fuente: Luxton (2013)*")

with col_b:
    st.success("### Procesamiento de Lenguaje Natural")
    st.write("Es la capacidad de la IA para 'entender' no solo las palabras que escribimos, sino el sentimiento detrás de ellas, detectando patrones de estrés.")
    st.caption("*Fuente: Luxton (2013)*")

# --- SECCIÓN 2: APLICACIONES PRÁCTICAS ---
st.header("De la teoría a la práctica: Chatbots y Terapias Digitales")

tab1, tab2 = st.tabs(["Chatbots Terapéuticos", "Terapia Digital (dCBT)"])

with tab1:
    st.write("""
    Estos asistentes virtuales no buscan reemplazar al psicólogo, sino ofrecer **apoyo inmediato las 24 horas**. 
    Han demostrado ser efectivos para ayudar a personas con depresión y ansiedad.
    """)
    st.metric(label="Disponibilidad", value="24/7", delta="Acceso Inmediato")

with tab2:
    st.write("""
    La Terapia Cognitivo-Conductual Digital (dCBT) ayuda a combatir el insomnio ajustando el tratamiento según cómo duerme 
    el paciente cada noche, logrando cambios reales en el cerebro.
    """)
    st.caption("*Estudio: Gkintoni et al. (2025)*")

# --- SECCIÓN 3: ÉTICA Y SEGURIDAD ---
st.header("¿Es seguro confiar en una máquina?")
st.warning("Aunque la IA es excelente para el monitoreo, el factor humano sigue siendo irreemplazable (Cruz-Gonzalez et al., 2025).")

col_e1, col_e2, col_e3 = st.columns(3)
with col_e1:
    st.markdown("**Privacidad**")
    st.write("¿Quién ve mis datos? La información debe estar protegida bajo leyes estrictas.")
with col_e2:
    st.markdown("**Veracidad**")
    st.write("Debemos asegurar que el contenido sea validado por expertos (Agudelo-Londoño, 2025).")
with col_e3:
    st.markdown("**Alianza Terapéutica**")
    st.write("La calidez humana es algo que la tecnología aún no logra igualar.")

# --- CONCLUSIÓN ---
st.markdown("---")
st.subheader("Conclusión")
st.write("""
La Inteligencia Artificial no ha llegado para quitarle el trabajo a los psicólogos, sino para darles **'superpoderes'**. 
El futuro de la salud mental parece ser una combinación de la **precisión del algoritmo** y la **empatía del ser humano**.
""")

# Pie de página
st.markdown("<div style='text-align: center; color: grey;'>© 2026 Dashboard de Salud Mental e IA</div>", unsafe_allow_html=True)
