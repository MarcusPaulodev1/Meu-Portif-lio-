# ============================================================
# 💈🎓 BARBER ACADEMY WHATSAPP SCHEDULER
# ============================================================
#
# Sistema de atendimento automático para uma escola de barbeiros
# que também realiza cortes de cabelo.
#
# FUNCIONALIDADES:
# ✅ Chatbot via WhatsApp Business API
# ✅ Menu interativo de atendimento
# ✅ Agendamento de cortes
# ✅ Integração com Google Calendar
# ✅ Lembrete automático antes do horário
# ✅ Captação de alunos interessados em cursos
#
# TECNOLOGIAS:
# - Python
# - Flask
# - Requests
# - WhatsApp Business Cloud API
# - Google Calendar API
# - Threading
#
# ============================================================

from flask import Flask, request
import requests
from datetime import datetime, timedelta
import threading
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ============================================================
# 🚀 INICIALIZAÇÃO DO SERVIDOR FLASK
# ============================================================

app = Flask(__name__)

# ============================================================
# 🔑 CONFIGURAÇÕES DA API DO WHATSAPP
# ============================================================
#
# Substitua os valores abaixo pelos dados reais obtidos no painel
# Meta Developers / WhatsApp Business Platform.
#
# TOKEN_DE_ACESSO: token gerado pela Meta
# ID_NUMERO: Phone Number ID do número WhatsApp
#
# ============================================================

TOKEN_DE_ACESSO = "SEU_TOKEN"
ID_NUMERO = "SEU_PHONE_ID"

URL_API = f"https://graph.facebook.com/v18.0/{ID_NUMERO}/messages"

cabecalhos = {
    "Authorization": f"Bearer {TOKEN_DE_ACESSO}",
    "Content-Type": "application/json"
}

# ============================================================
# 🔑 CONFIGURAÇÕES DO GOOGLE CALENDAR
# ============================================================
#
# O arquivo credenciais.json deve estar na mesma pasta deste código.
# Ele é gerado no Google Cloud Console após criar uma conta de serviço.
#
# ============================================================

ARQUIVO_CREDENCIAIS = "credenciais.json"
SCOPOS = ["https://www.googleapis.com/auth/calendar"]
ID_CALENDARIO = "primary"

credenciais = service_account.Credentials.from_service_account_file(
    ARQUIVO_CREDENCIAIS,
    scopes=SCOPOS
)

servico_calendario = build(
    "calendar",
    "v3",
    credentials=credenciais
)

# ============================================================
# 📲 FUNÇÃO PARA ENVIAR MENSAGEM NO WHATSAPP
# ============================================================

def enviar_mensagem(numero_cliente, mensagem):
    corpo = {
        "messaging_product": "whatsapp",
        "to": numero_cliente,
        "type": "text",
        "text": {
            "body": mensagem
        }
    }

    resposta = requests.post(
        URL_API,
        headers=cabecalhos,
        json=corpo
    )

    print("Status WhatsApp:", resposta.status_code)
    print("Resposta WhatsApp:", resposta.text)

# ============================================================
# 📅 FUNÇÃO PARA CRIAR EVENTO NO GOOGLE CALENDAR
# ============================================================

def criar_agendamento(nome_cliente, servico, data_inicio, data_fim):
    evento = {
        "summary": f"{servico} - {nome_cliente}",
        "description": (
            f"Cliente: {nome_cliente}\n"
            f"Serviço: {servico}\n"
            "Origem: WhatsApp Chatbot"
        ),
        "start": {
            "dateTime": data_inicio,
            "timeZone": "America/Sao_Paulo"
        },
        "end": {
            "dateTime": data_fim,
            "timeZone": "America/Sao_Paulo"
        }
    }

    evento_criado = servico_calendario.events().insert(
        calendarId=ID_CALENDARIO,
        body=evento
    ).execute()

    print("Evento criado no Google Calendar:")
    print(evento_criado.get("htmlLink"))

# ============================================================
# ⏰ FUNÇÃO DE LEMBRETE AUTOMÁTICO
# ============================================================
#
# A função calcula 30 minutos antes do horário agendado e envia
# uma mensagem automática para o cliente no WhatsApp.
#
# ============================================================

def enviar_lembrete(numero_cliente, horario_agendamento, servico):
    horario = datetime.strptime(
        horario_agendamento,
        "%Y-%m-%d %H:%M:%S"
    )

    horario_lembrete = horario - timedelta(minutes=30)
    segundos_espera = (horario_lembrete - datetime.now()).total_seconds()

    if segundos_espera > 0:
        print("Aguardando horário do lembrete...")
        time.sleep(segundos_espera)

    mensagem = (
        "⏰ Lembrete do seu agendamento!\n\n"
        f"💈 Serviço: {servico}\n"
        f"🕒 Horário: {horario.strftime('%d/%m/%Y às %H:%M')}\n\n"
        "📍 Barber Academy - Belo Horizonte/MG\n\n"
        "Aguardamos você ✂️🔥"
    )

    enviar_mensagem(numero_cliente, mensagem)

# ============================================================
# 🔥 WEBHOOK PRINCIPAL
# ============================================================
#
# Esse endpoint recebe as mensagens enviadas pelos clientes no
# WhatsApp e responde automaticamente de acordo com o texto.
#
# ============================================================

@app.route("/webhook", methods=["POST"])
def webhook():
    dados = request.json

    try:
        mensagem = dados["entry"][0]["changes"][0]["value"]["messages"][0]
        numero_cliente = mensagem["from"]
        texto = mensagem["text"]["body"].lower()

        if texto in ["oi", "olá", "ola", "menu"]:
            resposta = (
                "👋 Bem-vindo à Barber Academy ✂️\n\n"
                "Escolha uma opção:\n\n"
                "1️⃣ Agendar corte\n"
                "2️⃣ Conhecer cursos\n"
                "3️⃣ Ver preços\n"
                "4️⃣ Falar com atendente\n"
                "5️⃣ Endereço e horário"
            )

        elif texto == "1":
            resposta = (
                "💈 Escolha o serviço:\n\n"
                "1️⃣ Corte masculino\n"
                "2️⃣ Barba\n"
                "3️⃣ Corte + Barba\n"
                "4️⃣ Corte premium\n\n"
                "Digite o número do serviço desejado."
            )

        elif texto == "3":
            resposta = (
                "💲 Tabela de preços:\n\n"
                "✂️ Corte masculino: R$35\n"
                "🧔 Barba: R$25\n"
                "🔥 Corte + Barba: R$50\n"
                "⭐ Corte premium: R$70"
            )

        elif texto == "2":
            resposta = (
                "🎓 Cursos disponíveis:\n\n"
                "1️⃣ Barbeiro iniciante\n"
                "2️⃣ Fade avançado\n"
                "3️⃣ Pigmentação\n"
                "4️⃣ Design de barba\n\n"
                "Um consultor pode te enviar a grade completa do curso."
            )

        elif texto == "4":
            resposta = "📞 Um atendente falará com você em breve."

        elif texto == "5":
            resposta = (
                "📍 Barber Academy\n"
                "Belo Horizonte - MG\n\n"
                "🕒 Segunda a sábado\n"
                "09h às 20h"
            )

        elif texto in ["1️⃣", "corte", "corte masculino"]:
            inicio = "2026-05-10T14:00:00"
            fim = "2026-05-10T15:00:00"
            horario_lembrete = "2026-05-10 14:00:00"

            criar_agendamento(
                nome_cliente="Cliente WhatsApp",
                servico="Corte Masculino",
                data_inicio=inicio,
                data_fim=fim
            )

            thread_lembrete = threading.Thread(
                target=enviar_lembrete,
                args=(numero_cliente, horario_lembrete, "Corte Masculino")
            )
            thread_lembrete.start()

            resposta = (
                "✅ Agendamento realizado com sucesso!\n\n"
                "💈 Serviço: Corte Masculino\n"
                "🕒 Horário: 10/05/2026 às 14h\n\n"
                "⏰ Você receberá um lembrete automático 30 minutos antes."
            )

        else:
            resposta = (
                "❌ Não entendi sua mensagem.\n\n"
                "Digite 'oi' para abrir o menu principal."
            )

        enviar_mensagem(numero_cliente, resposta)

    except Exception as erro:
        print("Erro encontrado:", erro)

    return "ok", 200

# ============================================================
# 🚀 EXECUTAR A APLICAÇÃO
# ============================================================

if __name__ == "__main__":
    app.run(port=5000)

# ============================================================
# 🧠 PASSO A PASSO DE USO
# ============================================================
#
# 1. Instale as dependências:
#
#    pip install flask requests google-api-python-client google-auth-httplib2 google-auth-oauthlib
#
# 2. Configure suas credenciais da Meta:
#
#    TOKEN_DE_ACESSO = "SEU_TOKEN"
#    ID_NUMERO = "SEU_PHONE_ID"
#
# 3. Configure o Google Calendar:
#
#    - Crie um projeto no Google Cloud
#    - Ative a Google Calendar API
#    - Crie uma conta de serviço
#    - Baixe o arquivo JSON
#    - Renomeie para credenciais.json
#
# 4. Rode o projeto:
#
#    python barber_academy_whatsapp_scheduler.py
#
# 5. Exponha o servidor:
#
#    ngrok http 5000
#
# 6. Configure o webhook na Meta:
#
#    https://SEU_NGROK/webhook
#
# ============================================================
