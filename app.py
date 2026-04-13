import streamlit as st
import math
import time
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="LaCalcu", layout="centered")

# 🎨 ESTILO
st.markdown("""
<style>
.stApp {
    background-color: black;
    max-width: 400px;
    margin: auto;
}

.display {
    background-color: black;
    color: #22c55e;
    font-size: 45px;
    text-align: right;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 10px;
}

button {
    height: 65px;
    font-size: 20px !important;
    border-radius: 15px !important;
    margin: 3px;
    background-color: #1e293b !important;
    color: white !important;
    transition: 0.15s;
}

button:active {
    transform: scale(0.95);
    background-color: #22c55e !important;
    color: black !important;
}

.historial {
    background-color: #020617;
    padding: 10px;
    border-radius: 10px;
    max-height: 150px;
    overflow-y: auto;
}
</style>
""", unsafe_allow_html=True)

# 🔊 SONIDO
st.markdown("""
<audio id="clickSound" src="https://www.soundjay.com/buttons/sounds/button-16.mp3"></audio>
""", unsafe_allow_html=True)

# 🧠 memoria
if "expresion" not in st.session_state:
    st.session_state.expresion = ""

if "historial" not in st.session_state:
    st.session_state.historial = []

# 🔘 funciones
def agregar(valor):
    st.session_state.expresion += str(valor)

def calcular():
    try:
        exp = st.session_state.expresion

        # funciones científicas
        exp = exp.replace("√", "math.sqrt")
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("tan", "math.tan")

        resultado = str(eval(exp))
        st.session_state.historial.append(f"{st.session_state.expresion} = {resultado}")

        with st.spinner("Calculando..."):
            time.sleep(0.3)

        st.session_state.expresion = resultado
    except:
        st.session_state.expresion = "Error"

def limpiar():
    st.session_state.expresion = ""

def reset_total():
    st.session_state.clear()

# 🏷️ título
st.title("🧮 LaCalcu")
st.caption("Calculadora inteligente 🚀")

# 🖥️ pantalla
st.markdown(f'<div class="display">{st.session_state.expresion}</div>', unsafe_allow_html=True)

# 🔢 botones (con modo científico)
botones = [
    ["sin(", "cos(", "tan(", "√("],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
]

for fila in botones:
    cols = st.columns(4)
    for i, val in enumerate(fila):
        with cols[i]:
            if val == "C":
                st.button(val, on_click=limpiar, use_container_width=True)
            else:
                st.button(val, on_click=agregar, args=(val,), use_container_width=True)

# ➗ botones finales
c1, c2 = st.columns(2)

with c1:
    st.button("=", on_click=calcular, use_container_width=True)

with c2:
    st.button("RESET", on_click=reset_total, use_container_width=True)

# 📜 HISTORIAL
st.subheader("📜 Historial")

st.markdown('<div class="historial">', unsafe_allow_html=True)

for item in reversed(st.session_state.historial):
    st.write(f"🧮 {item}")

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🗑️ Borrar historial"):
    st.session_state.historial = []

# 📊 GRÁFICAS
st.subheader("📊 Graficar función")

funcion = st.text_input("Ejemplo: sin(x), x**2, cos(x)+x")

if st.button("Graficar"):
    try:
        x = np.linspace(-10, 10, 100)

        # adaptar funciones
        func = funcion.replace("sin", "np.sin")
        func = func.replace("cos", "np.cos")
        func = func.replace("tan", "np.tan")

        y = eval(func)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Gráfica")

        st.pyplot(fig)

    except:
        st.error("Función no válida")
