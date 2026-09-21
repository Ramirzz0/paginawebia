import streamlit as st
import base64

# Configuración de la página
st.set_page_config(page_title="Inteligencia Artificial", layout="wide")

# Estilos personalizados con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        color: #ecf0f1;
    }
    </style>
""", unsafe_allow_html=True)

# Barra de navegación lateral
menu = st.sidebar.radio("📌 Navegación", 
                        ["Inicio", "Línea del Tiempo IA", "Problemática de Línea del Tiempo", "Infografías IA's", "Glosario IA", "Disciplinas básicas de la IA"])

# ---------------- Pantalla de Inicio ----------------
if menu == "Inicio":
    st.title("🤖 Bienvenido a la aplicación de Inteligencia Artificial")
    st.markdown("""
    La **Inteligencia Artificial (IA)** hoy en día está presente en casi todos los ámbitos: 
    desde motores de recomendación como Netflix, asistentes virtuales, hasta sistemas generativos 
    como ChatGPT y modelos multimodales que trabajan con texto, imágenes, audio y video.  

    ### Características actuales:
    - Aprendizaje automático y profundo  
    - Procesamiento de lenguaje natural  
    - Visión artificial  
    - IA generativa y multimodal  
    - Automatización de procesos  
    """)

# ---------------- Línea del Tiempo IA ----------------
elif menu == "Línea del Tiempo IA":
    st.title("🕒 Línea del Tiempo de la IA")
    st.image("imagenes/linea_tiempo.png", caption="Principales hitos de la IA")

# ---------------- Infografías IA's ----------------
elif menu == "Infografías IA's":
    st.title("📊 Infografías sobre IA")
    st.image("imagenes/netflix.png", caption="Motor de recomendación de Netflix")
    st.image("imagenes/alice.png", caption="Robot doméstico Alice")
    st.image("imagenes/ultron.png", caption="IA superinteligente Ultron")


# ---------------- Problemática ----------------
elif menu == "Problemática de Línea del Tiempo":

    st.title("📝 Problemática de la Línea del Tiempo")
    st.image("imagenes/1.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/2.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/3.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/4.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/5.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/6.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/7.png", caption="Problemática de la Línea del Tiempo")
    st.image("imagenes/8.png", caption="Problemática de la Línea del Tiempo")



# ---------------- Glosario IA ----------------
elif menu == "Glosario IA":
    st.title("📘 Glosario de Inteligencia Artificial")
    st.markdown("Selecciona un término para ver su definición.")

    glosario = {
        "Inteligencia Artificial (IA)": "Tecnología que permite a las máquinas realizar tareas que normalmente requieren inteligencia humana.",
        "Machine Learning": "Método mediante el cual una computadora aprende a partir de datos para hacer predicciones o tomar decisiones.",
        "Aprendizaje profundo": "Tipo de aprendizaje automático que utiliza varias capas de redes neuronales para analizar información.",
        "Red neuronal": "Sistema inspirado en el cerebro humano que utiliza conexiones entre diferentes nodos para procesar información.",
        "Algoritmo": "Conjunto de instrucciones que una computadora sigue para resolver un problema o realizar una tarea.",
        "Datos": "Información que se utiliza para entrenar sistemas de inteligencia artificial.",
        "Modelo de IA": "Sistema entrenado con datos que puede realizar una tarea, como reconocer imágenes o generar texto.",
        "Entrenamiento": "Proceso mediante el cual un modelo aprende utilizando grandes cantidades de datos.",
        "Aprendizaje supervisado": "Método donde la IA aprende utilizando datos que ya tienen respuestas o etiquetas conocidas.",
        "Aprendizaje no supervisado": "Método donde la IA analiza datos sin etiquetas para encontrar patrones o relaciones.",
        "Aprendizaje por refuerzo": "Método en el que una IA aprende mediante prueba y error, recibiendo recompensas por realizar acciones correctas.",
        "Aprendizaje semisupervisado": "Combina datos etiquetados y no etiquetados para entrenar un modelo.",
        "Aprendizaje autosupervisado": "Método en el que el sistema obtiene información de los propios datos para aprender sin depender completamente de etiquetas humanas.",
        "IA generativa": "Tipo de IA capaz de crear contenido nuevo, como textos, imágenes, videos o audio.",
        "Modelo fundacional": "Modelo de IA entrenado con grandes cantidades de información que puede servir como base para diferentes aplicaciones.",
        "Modelo de lenguaje grande (LLM)": "Modelo de IA entrenado con grandes cantidades de texto para comprender y generar lenguaje.",
        "Procesamiento de Lenguaje Natural (PLN)": "Tecnología que permite a las computadoras comprender y trabajar con el lenguaje humano.",
        "Visión artificial": "Tecnología que permite a las computadoras analizar e interpretar imágenes y videos.",
        "Transformador": "Tipo de modelo de IA utilizado para procesar y generar información, especialmente texto.",
        "Chatbot": "Programa que utiliza IA para mantener conversaciones y responder preguntas de los usuarios.",
        "Agente de IA": "Programa capaz de realizar tareas y alcanzar objetivos utilizando herramientas y tomando ciertas decisiones de manera autónoma.",
        "Automatización": "Uso de tecnología para realizar tareas automáticamente sin que una persona tenga que hacerlas constantemente."
    }

    for termino, definicion in sorted(glosario.items()):
        with st.expander(f"📖 {termino}"):
            st.write(definicion)

# ---------------- Disciplinas básicas de la IA ----------------
elif menu == "Disciplinas básicas de la IA":
    st.title("📚 Disciplinas básicas de la IA")
    st.markdown("""
    1. **Aprendizaje automático (Machine Learning)**  
    2. **Procesamiento de lenguaje natural (PLN)**  
    3. **Visión artificial**  
    4. **Robótica**  
    5. **Sistemas expertos**  
    """)

