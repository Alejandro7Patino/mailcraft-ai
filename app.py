import streamlit as st
from openai import OpenAI

# ─── Configuración de la página ───────────────────────────────────────────────
st.set_page_config(
    page_title="MailCraft AI",
    page_icon="✉️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Estilos CSS personalizados ───────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .main {
        background-color: #0f0f0f;
        color: #f5f5f0;
    }

    .stApp {
        background-color: #0f0f0f;
    }

    h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem !important;
        color: #f5f5f0 !important;
        letter-spacing: -1px;
    }

    .subtitle {
        color: #a0a09a;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .badge {
        background-color: #d4af37;
        color: #0f0f0f;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        color: #d4af37;
        font-size: 1.3rem;
        margin-top: 2rem;
        border-bottom: 1px solid #2a2a2a;
        padding-bottom: 0.5rem;
    }

    .how-it-works {
        background-color: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
    }

    .step {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1rem;
    }

    .step-number {
        background-color: #d4af37;
        color: #0f0f0f;
        border-radius: 50%;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.85rem;
        flex-shrink: 0;
        margin-right: 12px;
        margin-top: 2px;
    }

    .result-box {
        background-color: #1a1a1a;
        border-left: 3px solid #d4af37;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.97rem;
        line-height: 1.7;
        color: #f0f0ea;
        white-space: pre-wrap;
    }

    .stTextArea textarea {
        background-color: #1a1a1a !important;
        border: 1px solid #333 !important;
        color: #f5f5f0 !important;
        border-radius: 10px !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    .stSelectbox > div > div {
        background-color: #1a1a1a !important;
        border: 1px solid #333 !important;
        color: #f5f5f0 !important;
        border-radius: 10px !important;
    }

    .stTextInput input {
        background-color: #1a1a1a !important;
        border: 1px solid #333 !important;
        color: #f5f5f0 !important;
        border-radius: 10px !important;
    }

    .stButton > button {
        background-color: #d4af37 !important;
        color: #0f0f0f !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-size: 1rem !important;
        width: 100% !important;
        transition: opacity 0.2s ease !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    .stButton > button:hover {
        opacity: 0.85 !important;
    }

    label, .stSelectbox label, .stTextArea label {
        color: #a0a09a !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
    }

    hr {
        border-color: #2a2a2a !important;
    }

    footer {
        color: #555 !important;
        font-size: 0.8rem;
        text-align: center;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown('<div class="badge">✉ Powered by GPT-4o-mini</div>', unsafe_allow_html=True)
st.markdown("# MailCraft AI")
st.markdown('<p class="subtitle">Generá correos profesionales perfectos en segundos. Describí tu situación y la IA hace el resto.</p>', unsafe_allow_html=True)

st.markdown("---")


# ─── Sidebar: API Key ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Configuración")
    api_key = st.text_input(
        "Tu API Key de OpenAI",
        type="password",
        placeholder="sk-...",
        help="Conseguí tu clave en platform.openai.com"
    )
    st.caption("🔒 Tu clave no se almacena. Solo se usa durante esta sesión.")
    st.markdown("---")
    st.markdown("**¿Cómo conseguir una API Key?**")
    st.markdown("1. Entrá a [platform.openai.com](https://platform.openai.com)")
    st.markdown("2. Creá una cuenta gratuita")
    st.markdown("3. Andá a *API Keys* y generá una nueva")


# ─── Formulario principal ──────────────────────────────────────────────────────
st.markdown('<p class="section-title">📝 Contanos tu situación</p>', unsafe_allow_html=True)

tonos = [
    "Formal y profesional",
    "Cordial y cercano",
    "Firme y directo",
    "Persuasivo",
    "Empático y comprensivo",
]

situaciones = [
    "Postulación a un empleo",
    "Seguimiento de entrevista / aplicación",
    "Reclamo o queja formal",
    "Negociación de salario o condiciones",
    "Solicitud de reunión o colaboración",
    "Agradecimiento profesional",
    "Pedido de información o presupuesto",
    "Otro (describir en el campo)",
]

col1, col2 = st.columns(2)
with col1:
    situacion = st.selectbox("Tipo de correo", situaciones)
with col2:
    tono = st.selectbox("Tono deseado", tonos)

destinatario = st.text_input(
    "¿A quién va dirigido?",
    placeholder="Ej: Gerente de RRHH de una empresa de tecnología"
)

descripcion = st.text_area(
    "Describí tu situación con tus propias palabras",
    placeholder="Ej: Me postulé hace 2 semanas para el puesto de diseñador UX y no recibí respuesta. Quiero hacer un seguimiento sin sonar insistente...",
    height=150,
)

idioma = st.selectbox("Idioma del correo", ["Español", "Inglés", "Portugués"])

generar = st.button("✨ Generar correo profesional")


# ─── Lógica de generación ──────────────────────────────────────────────────────
if generar:
    # Validaciones
    if not api_key:
        st.error("⚠️ Ingresá tu API Key de OpenAI en el panel lateral (⚙️).")
        st.stop()
    if not descripcion.strip():
        st.error("⚠️ Por favor describí tu situación antes de continuar.")
        st.stop()
    if not destinatario.strip():
        st.error("⚠️ Indicá a quién va dirigido el correo.")
        st.stop()

    # Construcción del prompt
    system_prompt = """Eres un experto redactor de comunicaciones profesionales con más de 15 años de experiencia.
Tu tarea es redactar correos electrónicos profesionales, claros, efectivos y adaptados al contexto del usuario.
El correo debe incluir: asunto, saludo, cuerpo del mensaje y despedida.
No incluyas placeholders genéricos como [Nombre]. Redactá el correo completo y listo para enviar.
Si falta el nombre del remitente, usá una firma genérica apropiada.
Respondé ÚNICAMENTE con el correo, sin explicaciones adicionales."""

    user_prompt = f"""Tipo de correo: {situacion}
Destinatario: {destinatario}
Tono deseado: {tono}
Idioma: {idioma}

Situación del usuario:
{descripcion}

Redactá un correo profesional completo, incluyendo el asunto en la primera línea con el formato:
Asunto: [asunto aquí]

Luego el cuerpo del correo."""

    # Llamada a la API
    with st.spinner("Redactando tu correo..."):
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=800,
                temperature=0.7,
            )
            correo_generado = response.choices[0].message.content

            st.markdown('<p class="section-title">📬 Tu correo generado</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-box">{correo_generado}</div>', unsafe_allow_html=True)

            # Botón de copia
            st.download_button(
                label="⬇️ Descargar correo como .txt",
                data=correo_generado,
                file_name="correo_profesional.txt",
                mime="text/plain",
            )

        except Exception as e:
            st.error(f"❌ Error al conectar con OpenAI: {str(e)}")
            st.info("Verificá que tu API Key sea válida y que tengas créditos disponibles.")


# ─── Sección Cómo Funciona ─────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<p class="section-title">🔍 ¿Cómo funciona MailCraft AI?</p>', unsafe_allow_html=True)

st.markdown("""
<div class="how-it-works">

<div class="step">
  <div class="step-number">1</div>
  <div><strong>Describís tu situación</strong><br>
  Completás el formulario con el tipo de correo, a quién va dirigido, el tono que querés y una descripción libre de tu situación en pocas palabras.</div>
</div>

<div class="step">
  <div class="step-number">2</div>
  <div><strong>La IA analiza el contexto</strong><br>
  El modelo GPT-4o-mini de OpenAI recibe un prompt estructurado con toda tu información y genera un correo adaptado a tu caso específico.</div>
</div>

<div class="step">
  <div class="step-number">3</div>
  <div><strong>Obtenés un correo listo para enviar</strong><br>
  El resultado incluye asunto, saludo, cuerpo y despedida. Podés copiarlo directamente o descargarlo como archivo de texto.</div>
</div>

<div class="step">
  <div class="step-number">4</div>
  <div><strong>Casos de uso</strong><br>
  Postulaciones laborales, seguimiento de entrevistas, reclamos, negociaciones, agradecimientos y mucho más. Ideal para estudiantes, freelancers y profesionales.</div>
</div>

</div>
""", unsafe_allow_html=True)


# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<footer>
    <br>MailCraft AI · Proyecto Final - Prompt Engineering para Programadores · CoderHouse<br>
    Desarrollado con Streamlit + OpenAI GPT-4o-mini
</footer>
""", unsafe_allow_html=True)
