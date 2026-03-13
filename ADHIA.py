# --- BARRA LATERAL (Navegación y Bibliografía con Resúmenes) ---
with st.sidebar:
    st.title("Recursos")
    st.info(f"**Frase del día:**\n\n *'{'[cite: 2]'}'*")
    
    st.header("Bibliografía Detallada")
    st.write("Haz clic en cada autor para leer el resumen del estudio:")

    # Referencia 1: Agudelo-Londoño
    with st.expander("Agudelo-Londoño (2025)"):
        st.write("**Resumen:**")
        st.write("Analiza el impacto de la IA en la edición académica de salud. Destaca que optimiza la revisión de manuscritos y detección de errores.")
        st.write("Advierte sobre riesgos éticos como la pérdida de originalidad, referencias falsas y la necesidad de supervisión humana para garantizar la veracidad.")

    # Referencia 2: Beg et al.
    with st.expander("Beg et al. (2024)"):
        st.write("**Resumen:**")
        st.write("Revisa el uso de chatbots y análisis de lenguaje en psicoterapia para mejorar el acceso y ofrecer apoyo continuo entre sesiones.")
        st.write("Identifica limitaciones como la falta de regulación y la incapacidad de la IA para reemplazar la empatía humana.")

    # Referencia 3: Cruz-Gonzalez et al.
    with st.expander("Cruz-González et al. (2025)"):
        st.write("**Resumen:**")
        st.write("Revisión sistemática sobre diagnóstico y monitoreo. La IA ayuda en la detección temprana de depresión y ansiedad mediante datos de redes sociales y apps.")
        st.write("Subraya desafíos en validez clínica, sesgos algorítmicos y la necesidad de marcos éticos sólidos.")

    # Referencia 4: Gkintoni et al.
    with st.expander("Gkintoni et al. (2025)"):
        st.write("**Resumen:**")
        st.write("Estudia la dCBT (Terapia Cognitivo-Conductual Digital) para el insomnio. La IA ajusta el tratamiento analizando patrones de sueño en tiempo real.")
        st.write("Muestra que mejora la calidad del sueño al reducir la hiperactivación cognitiva y regular las emociones.")

    # Referencia 5: Luxton
    with st.expander("Luxton (2013)"):
        st.write("**Resumen:**")
        st.write("Analiza sistemas expertos y agentes conversacionales para la evaluación del riesgo suicida y seguimiento terapéutico.")
        st.write("Concluye que la IA debe ser una herramienta complementaria al juicio clínico y nunca sustituir la relación terapéutica.")
