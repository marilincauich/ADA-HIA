import streamlit as st

# ---------------- CONFIGURACIÓN DE PÁGINA ----------------
st.set_page_config(
    page_title="IA en la Salud Mental",
    page_icon="🧠",
    layout="wide"
)

# ---------------- BARRA LATERAL ----------------
with st.sidebar:
    st.title("Recursos y Referencias")

    st.info(
        "**Frase del día:**\n\n"
        "*Que la innovación no sea un conflicto*"
    )

    st.header("Bibliografía Completa")

    with st.expander("Agudelo-Londoño (2025)"):
        st.write("""
Este artículo analiza el impacto de la inteligencia artificial en los procesos de edición académica de revistas científicas en el área de la salud. 
La autora explica que el crecimiento del volumen de publicaciones científicas ha generado nuevos retos para mantener la calidad editorial, 
lo que ha motivado la incorporación de herramientas de IA en procesos como la revisión de manuscritos, la detección de errores y la gestión 
editorial.

El texto también advierte sobre riesgos éticos y epistemológicos importantes. Entre ellos se encuentran la posible pérdida de originalidad 
del conocimiento, la generación automática de referencias falsas, el uso indebido de herramientas generativas y la presión institucional 
por incorporar inteligencia artificial sin una reflexión crítica.

Finalmente, se propone un enfoque equilibrado en el que la IA funcione como una herramienta de apoyo que mejore la eficiencia de los procesos 
editoriales, pero manteniendo siempre la supervisión humana para garantizar la transparencia, la integridad científica y la veracidad del conocimiento.
""")

    with st.expander("Beg et al. (2024)"):
        st.write("""
Este artículo revisa el estado actual del uso de la inteligencia artificial en la psicoterapia y describe diversas herramientas que ya 
están siendo utilizadas en el ámbito clínico. Entre ellas destacan los chatbots terapéuticos, los sistemas de análisis del lenguaje y las 
plataformas de terapia digital diseñadas para apoyar procesos de evaluación psicológica, intervención y seguimiento de pacientes.

Los autores señalan que estas tecnologías pueden mejorar significativamente el acceso a servicios de salud mental, especialmente en 
contextos donde los recursos clínicos son limitados. Además, permiten ofrecer intervenciones personalizadas y proporcionar apoyo continuo 
entre sesiones terapéuticas, lo que puede fortalecer el proceso de tratamiento.

No obstante, el estudio también identifica limitaciones importantes, como problemas relacionados con la privacidad de los datos, la falta 
de regulación clara en el uso de estas tecnologías y el riesgo de dependencia tecnológica. Asimismo, se destaca que los sistemas de IA 
no pueden reemplazar la empatía humana que caracteriza a la relación terapéutica.
""")

    with st.expander("Cruz-González et al. (2025)"):
        st.write("""
Este estudio presenta una revisión sistemática sobre la aplicación de la inteligencia artificial en la atención de la salud mental, 
centrándose en tres áreas principales: diagnóstico, monitoreo e intervención.

Los autores analizan investigaciones que utilizan algoritmos de aprendizaje automático, procesamiento de lenguaje natural y análisis 
de datos conductuales para identificar trastornos mentales, evaluar síntomas y ofrecer tratamientos digitales.

Los resultados muestran que la IA tiene un gran potencial para mejorar la detección temprana de trastornos como depresión, ansiedad o 
psicosis. También puede monitorear el estado emocional de los pacientes a través de datos obtenidos de redes sociales, aplicaciones 
móviles o dispositivos digitales.

Sin embargo, el artículo advierte sobre desafíos importantes como la validez clínica de los algoritmos, los sesgos en los sistemas 
automatizados, la privacidad de los datos personales y la necesidad de supervisión profesional en el uso de estas herramientas.
""")

    with st.expander("Gkintoni et al. (2025)"):
        st.write("""
Este artículo examina el uso de terapias cognitivo-conductuales digitales potenciadas con inteligencia artificial para el tratamiento 
del insomnio.

Los autores explican que las plataformas digitales pueden adaptar las intervenciones terapéuticas a las características individuales 
de cada paciente mediante el análisis de patrones de sueño, comportamientos y respuestas cognitivas.

El estudio también explora los mecanismos neurocognitivos del insomnio, incluyendo la hiperactivación cognitiva, la ansiedad asociada 
al sueño y las dificultades en la regulación emocional. Gracias a la inteligencia artificial, estas plataformas pueden monitorear 
estos factores y ajustar el tratamiento en tiempo real mediante recomendaciones personalizadas y retroalimentación continua.

Los resultados sugieren que estas intervenciones digitales pueden mejorar significativamente la calidad del sueño cuando se utilizan 
como complemento de la terapia psicológica tradicional.
""")

    with st.expander("Luxton (2013)"):
        st.write("""
Este artículo analiza las aplicaciones actuales y futuras de la inteligencia artificial en la práctica psicológica.

El autor describe diversas tecnologías emergentes como sistemas expertos, agentes conversacionales, análisis automatizado del 
lenguaje y herramientas de evaluación psicológica basadas en algoritmos. Estas tecnologías pueden apoyar a los profesionales 
de la salud mental en tareas como el diagnóstico clínico, la evaluación del riesgo suicida, el seguimiento del progreso terapéutico 
y la recopilación de datos clínicos.

Asimismo, la inteligencia artificial puede ampliar el acceso a servicios psicológicos mediante plataformas de telepsicología 
e intervenciones digitales.

Sin embargo, el autor también advierte sobre desafíos éticos importantes relacionados con la protección de datos, la responsabilidad 
clínica, la fiabilidad de los sistemas automatizados y el riesgo de depender excesivamente de la tecnología en la práctica profesional.
""")

# ---------------- CONTENIDO PRINCIPAL ----------------

st.title("¿Un psicólogo en mi bolsillo?")
st.subheader("Cómo la Inteligencia Artificial está transformando la salud mental")

st.markdown("""
En los últimos años, la tecnología ha dejado de ser únicamente una herramienta de comunicación para convertirse en una aliada 
inesperada de nuestra salud emocional. Actualmente, la Inteligencia Artificial no solo recomienda música, películas o rutas de 
tráfico, sino que también está comenzando a identificar señales de ansiedad, depresión e insomnio.

A través del análisis de grandes cantidades de datos, estas tecnologías pueden detectar patrones emocionales y conductuales que 
resultan difíciles de identificar únicamente mediante la observación humana. De esta manera, la IA está comenzando a colaborar 
estrechamente con profesionales de la psicología clínica, apoyando procesos de diagnóstico, monitoreo y tratamiento psicológico.
""")

# ---------------- CONCEPTOS ----------------

col1, col2 = st.columns(2)

with col1:
    st.info("### Machine Learning")
    st.write("""
El Machine Learning, o aprendizaje automático, es una de las tecnologías más importantes dentro de la inteligencia artificial.

En el contexto de la salud mental, permite que los sistemas informáticos analicen grandes cantidades de información clínica, 
conductual y emocional para identificar patrones que podrían indicar riesgo psicológico.

Por ejemplo, mediante el análisis de historiales clínicos, registros de comportamiento o datos digitales, los algoritmos 
pueden predecir si una persona podría experimentar una recaída emocional o desarrollar síntomas de ansiedad o depresión.
""")

with col2:
    st.success("### Procesamiento de Lenguaje Natural")
    st.write("""
El Procesamiento de Lenguaje Natural (PLN) es la capacidad de las máquinas para interpretar y analizar el lenguaje humano.

En psicología, esta tecnología permite que los sistemas de inteligencia artificial analicen no solo las palabras que una 
persona escribe o dice, sino también el tono emocional, los patrones lingüísticos y los indicadores de estrés o tristeza 
presentes en el discurso.

Gracias a esta capacidad, algunas herramientas digitales pueden detectar cambios emocionales en pacientes y ofrecer apoyo 
o alertas tempranas cuando identifican señales de riesgo psicológico.
""")

# ---------------- APLICACIONES ----------------

st.header("De la teoría a la práctica")

tab1, tab2 = st.tabs(["Chatbots terapéuticos", "Terapia Cognitivo-Conductual Digital"])

with tab1:
    st.write("""
Los chatbots terapéuticos son asistentes virtuales diseñados para interactuar con los usuarios mediante conversaciones 
automatizadas.

Estos sistemas utilizan inteligencia artificial para responder preguntas, ofrecer estrategias de afrontamiento y brindar 
apoyo emocional inmediato. Una de sus principales ventajas es que están disponibles las 24 horas del día, lo que permite que 
las personas puedan recibir orientación en momentos en los que no tienen acceso inmediato a un profesional.

Diversos estudios han demostrado que estos sistemas pueden ser útiles para apoyar a personas con síntomas de depresión 
o ansiedad, especialmente como complemento a la terapia psicológica tradicional.
""")

with tab2:
    st.write("""
La Terapia Cognitivo-Conductual Digital (dCBT) es una adaptación tecnológica de uno de los enfoques terapéuticos más utilizados 
en psicología.

En este tipo de intervención, las plataformas digitales utilizan inteligencia artificial para analizar el comportamiento del 
paciente y adaptar las estrategias terapéuticas de manera personalizada.

Por ejemplo, en el tratamiento del insomnio, estos sistemas pueden monitorear los patrones de sueño de una persona, identificar 
factores que afectan su descanso y ofrecer recomendaciones personalizadas para mejorar la calidad del sueño.

Estas intervenciones han mostrado resultados prometedores, especialmente cuando se utilizan como complemento del tratamiento 
clínico tradicional.
""")

# ---------------- ÉTICA ----------------

st.warning("### Retos Éticos en el uso de la IA")

st.write("""
A pesar de los beneficios potenciales de la inteligencia artificial en la salud mental, su uso también plantea importantes 
desafíos éticos y profesionales.

**Privacidad:** Los sistemas de IA suelen trabajar con grandes volúmenes de información personal y datos sensibles. Por ello, 
es fundamental garantizar que esta información esté protegida mediante normas estrictas de confidencialidad y seguridad.

**Veracidad y calidad del conocimiento:** Algunos autores advierten que las herramientas generativas pueden producir 
información incorrecta o referencias falsas, por lo que es necesario validar siempre los resultados mediante supervisión 
humana y criterios científicos.

**Alianza terapéutica:** La relación entre terapeuta y paciente sigue siendo uno de los elementos centrales de la psicoterapia. 
Aunque la tecnología puede ofrecer apoyo, la empatía, la comprensión emocional y la interacción humana siguen siendo elementos 
difíciles de replicar por los sistemas automatizados.
""")

st.markdown("---")

st.markdown(
    "<div style='text-align: center;'>"
    "La inteligencia artificial no reemplaza a los psicólogos: les proporciona herramientas "
    "para ampliar el alcance de la atención en salud mental y mejorar la precisión de las intervenciones."
    "</div>",
    unsafe_allow_html=True
)
