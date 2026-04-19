# MailCraft AI — Generador de Correos Profesionales con IA

Aplicación web desarrollada con Streamlit e integrada con OpenAI para generar correos profesionales de forma automática a partir de una descripción simple del usuario.

Proyecto Final del curso Prompt Engineering.

---

## Problema que resuelve

Muchas personas no saben cómo redactar correos profesionales efectivos para situaciones como postularse a un empleo, hacer un reclamo, negociar condiciones o hacer seguimiento de una entrevista. El resultado son mensajes confusos, poco efectivos o con tono inadecuado.

## Solución

MailCraft AI permite al usuario describir su situación en lenguaje natural y, a través de un prompt estructurado enviado a GPT-4o-mini, genera un correo completo (asunto + cuerpo + despedida) listo para enviar, con el tono y el idioma deseados.

---

## Cómo usar la app

1. Accedé al [link de la app en Streamlit]()
2. Ingresá tu API Key de OpenAI en el panel lateral (⚙️)
3. Completá el formulario: tipo de correo, destinatario, tono e idioma
4. Describí tu situación con tus propias palabras
5. Hacé clic en **"Generar correo profesional"**
6. Copiá o descargá el resultado

---

## Prompt utilizado

System prompt:
"Eres un experto redactor de comunicaciones profesionales con más de 15 años de experiencia. Tu tarea es redactar correos electrónicos profesionales, claros, efectivos y adaptados al contexto del usuario..."

User prompt dinámico: incluye tipo de correo, destinatario, tono, idioma y descripción libre del usuario.

---

## Tecnologías

- [Streamlit](https://streamlit.io/) — interfaz web
- [OpenAI API](https://platform.openai.com/) — modelo `gpt-4o-mini`
- Python 3.10+

---

## Instalación local

```bash
git clone https://github.com/Alejandro7Patino/mailcraft-ai.git
cd mailcraft-ai
pip install -r requirements.txt
streamlit run app.py
```

Necesitás una API Key de OpenAI. Podés obtener una en [platform.openai.com](https://platform.openai.com).

---

## Estructura del proyecto

```
mailcraft-ai/
│
├── app.py               # Código principal de la app
├── requirements.txt     # Dependencias
└── README.md            # Este archivo
```

---

## Factibilidad económica

El modelo `gpt-4o-mini` es extremadamente económico:
- Costo aproximado: **$0.00015 por cada 1.000 tokens** de entrada
- Un correo típico usa ~400 tokens de entrada y ~400 de salida
- Costo por correo generado: **~$0.0002 (menos de 1 centavo de dólar)**
- OpenAI otorga créditos gratuitos al registrarse
