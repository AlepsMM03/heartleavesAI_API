import streamlit as st
import json

st.set_page_config(page_title="API – HeartLeaves AI", page_icon="🧠", layout="wide")

# Título principal con estilo y emoji
st.markdown(
    "<h1 style='text-align:center; color:#4B8BBE;'>🧠 HeartLeaves AI – API de Predicción de Infarto</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#555;'>Documentación oficial y guía rápida</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Endpoints disponibles con tarjetas estilo acordeón
st.header("📘 Endpoints disponibles")

with st.expander("✅ GET / – Verificar estado de la API", expanded=True):
    st.markdown(
        "Este endpoint devuelve un mensaje de confirmación de que la API está activa."
    )
    st.code("GET https://flask-api-model.onrender.com/", language="bash")
    st.subheader("Respuesta esperada:")
    st.code(
        json.dumps({"message": "✅ API de predicción de infarto activa"}, indent=2),
        language="json",
    )

with st.expander("🧠 POST /predict – Realizar predicción de riesgo"):
    st.markdown(
        "Envía valores clínicos al modelo Random Forest para evaluar el riesgo de infarto."
    )
    st.code("POST https://flask-api-model.onrender.com/predict", language="bash")

    st.subheader("📥 Cuerpo de la solicitud (JSON):")
    request_json = {
        "Troponin": 0.03,
        "CK-MB": 4.7,
        "Age": 60,
    }
    st.code(json.dumps(request_json, indent=2), language="json")

    st.subheader("📤 Respuesta esperada:")
    response_json = {
        "prediction": 1,
        "diagnosis": "Positivo para infarto",
        "input": {
            "Troponin": 0.03,
            "CK-MB": 4.7,
            "Age": 60,
        },
    }
    st.code(json.dumps(response_json, indent=2), language="json")

    st.subheader("🧾 Parámetros esperados:")
    st.markdown(
        """
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr style="background-color:#4B8BBE; color:white;">
                <th style="padding: 8px; border: 1px solid #ddd;">Campo</th>
                <th style="padding: 8px; border: 1px solid #ddd;">Tipo</th>
                <th style="padding: 8px; border: 1px solid #ddd;">Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr><td style="padding: 8px; border: 1px solid #ddd;">Troponin</td><td style="padding: 8px; border: 1px solid #ddd;">float</td><td style="padding: 8px; border: 1px solid #ddd;">Nivel de troponina (ng/mL)</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;">CK-MB</td><td style="padding: 8px; border: 1px solid #ddd;">float</td><td style="padding: 8px; border: 1px solid #ddd;">Nivel de creatina quinasa-MB (U/L)</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;">Age</td><td style="padding: 8px; border: 1px solid #ddd;">int</td><td style="padding: 8px; border: 1px solid #ddd;">Edad del paciente</td></tr>
        </tbody>
    </table>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# Modelo
st.header("🧠 Modelo Random Forest")
st.markdown(
    """
Entrenado con datos clínicos reales y validado rigurosamente con aprendizaje automático.

- Algoritmo: **Random Forest Classifier**
- Precisión: **99%**
- Análisis de importancia de variables con `feature_importances_`
""")

st.code(
    """
importances = model.feature_importances_
features = X.columns
importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
importance_df.sort_values(by='Importance', ascending=False)
""",
    language="python",
)

st.markdown(
    """
#### Principales factores identificados:
- **Troponina** – marcador cardíaco clave
- **CK-MB** – enzima específica de daño miocárdico
- **Edad** – factor de riesgo importante

> La combinación de estos parámetros permite una predicción altamente confiable.
"""
)

st.markdown("---")

# Demo
st.header("🚀 Accede a la demostración")
st.markdown(
    """
Para probar la predicción en vivo, accede a la aplicación web interactiva:

[👉 HeartLeaves AI](https://heartleavesai.streamlit.app/)  
"""
)

st.markdown("---")

# Contacto con estilo
st.header("📨 Contacto")
st.markdown(
    """
- **Desarrollador:** Jesús Alejandro Montes Medina  
- **Proyecto:** HeartLeaves AI  
- **Email:** [amontesdev21@gmail.com](mailto:amontesdev21@gmail.com)  
- **Institución:** Universidad Autónoma del Estado de Zacatecas  
"""
)

st.caption("© 2025 HeartLeaves AI – Todos los derechos reservados.")
