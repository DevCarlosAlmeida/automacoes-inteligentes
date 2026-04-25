"""
bot_motivacional.py — Seu robô pessoal de frases motivacionais no Telegram.
Agenda mensagens diárias pra você ou seu time. De graça, sem frescura.
"""

import os
import asyncio
import random
from datetime import datetime, time
from telegram import Bot
from telegram.error import TelegramError


# 🎯 FRASES MOTIVACIONAIS (adicione quantas quiser)
FRASES = [
    "💪 A única pessoa que você precisa superar é você mesmo de ontem.",
    "🚀 Grandes coisas nunca vieram da zona de conforto.",
    "⚡ Você está a uma decisão de distância de uma vida completamente diferente.",
    "🔥 O sucesso é a soma de pequenos esforços repetidos dia após dia.",
    "🌟 Acredite em você. O resto virá naturalmente.",
    "🎯 Foco não é dizer sim para o que importa. É dizer não para o que distrai.",
    "🧠 Invista em conhecimento. É o único ativo que ninguém pode tirar de você.",
    "⏰ Não espere o momento perfeito. Faça o momento ser perfeito.",
    "🏆 Quem quer faz. Quem não quer arruma desculpa.",
    "💡 Hoje é o melhor dia para começar algo novo.",
]


async def enviar_mensagem(bot_token, chat_id):
    """Envia uma frase motivacional aleatória."""
    frase = random.choice(FRASES)
    mensagem = f"{frase}\n\n_📅 {datetime.now().strftime('%d/%m/%Y')} — Seu bot motivacional_"

    bot = Bot(token=bot_token)

    try:
        await bot.send_message(chat_id=chat_id, text=mensagem, parse_mode="Markdown")
        print(f"✅ Mensagem enviada: {frase[:50]}...")
    except TelegramError as e:
        print(f"❌ Erro ao enviar: {e}")


def main():
    """Executa o envio imediato (para teste) ou orienta sobre agendamento."""
    print("🤖 Bot Motivacional do Telegram\n")

    # Verifica se o token está no ambiente
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not bot_token:
        print("⚠️  Token do bot não encontrado!")
        print("\n📋 Como configurar:")
        print("1. Crie um bot no Telegram: @BotFather")
        print("2. Pegue o token que ele te der")
        print("3. Descubra seu chat_id: @userinfobot")
        print("4. Execute:")
        print('   export TELEGRAM_BOT_TOKEN="seu_token_aqui"')
        print('   export TELEGRAM_CHAT_ID="seu_chat_id_aqui"')
        print("5. Rode: python scripts/bot_motivacional.py")
        return

    if not chat_id:
        print("⚠️  Chat ID não encontrado! Siga as instruções acima.")
        return

    mensagem = random.choice(FRASES)
    print(f"📨 Enviando: {mensagem}\n")
    asyncio.run(enviar_mensagem(bot_token, chat_id))

    print("\n⏱️  Quer agendar envios diários? Adicione ao crontab:")
    print("   crontab -e")
    print("   8 0 * * * python3 /caminho/do/scripts/bot_motivacional.py")


if __name__ == "__main__":
    main()
