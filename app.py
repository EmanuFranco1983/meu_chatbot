import gradio as gr
import requests

def chat_with_mistral(message, history):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": message,
            "stream": False
        }
    )
    answer = response.json()["response"]
    return answer

custom_css = """
body {
    background-color: #1e3a8a;
}
.gradio-container {
    background-color: #1e3a8a !important;
}
.message-textbox textarea {
    background-color: #ffffff !important;
    color: #000000;
}
button {
    background-color: #f97316 !important;
    color: white !important;
}
"""

chatbot = gr.ChatInterface(
    fn=chat_with_mistral,
    title="Manu Chat",
    textbox=gr.Textbox(placeholder="Digite sua pergunta...", lines=1),
    theme="default",
    css=custom_css
)

chatbot.launch()
