import streamlit as st
import math
import time

st.set_page_config(page_title="Super Calculadora", layout="centered")

# 🎨 ESTILO MÓVIL
st.markdown("""
<style>
.stApp {
    background-color: black;
    max-width: 400px;
    margin: auto;
}

/* Pantalla */
.display {
    background-color: black;
    color: #22c55e;
    font-size: 45px;
    text-align: right;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 10px;
}

/* Botones */
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

/* Historial */
.historial {
    background-color: #020617;
    padding: 10px;
    border-radius: 10px;
    max-height: 150px;
    overflow-y: auto;
}
</style>
""", unsafe_allow_html=True)

# 🔊 SONIDO (click)
st.markdown("""
<audio id="clickSound" src="https://www.soundjay.com/buttons/sounds/button-16.mp3"></audio>
<script>
function playSound(){
    var audio = document.getElementById("clickSound");
    audio.currentTime = 0;
    audio.play();
}
</script>
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
        resultado = str(eval(st.session_state.expresion))
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

# 🖥️ pantalla
st.markdown(f'<div class="display">{st.session_state.expresion}</div>', unsafe_allow_html=True)

# 🔢 botones
botones = [
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

# ➗ fila final
c1, c2 = st.columns(2)

with c1:
    st.button("=", on_click=calcular, use_container_width=True)

with c2:
    st.button("RESET", on_click=reset_total, use_container_width=True)

# 📜 historial
st.subheader("📜 Historial")

st.markdown('<div class="historial">', unsafe_allow_html=True)

for item in reversed(st.session_state.historial):
    st.write(item)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🗑️ Borrar historial"):
    st.session_state.historial = []
