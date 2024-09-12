import credenciais
import telebot
import temp


bot = telebot.TeleBot(credenciais.token_bot)

@bot.message_handler(commands = ['tempo'])
def cidade(mensagem):
    cidade = mensagem.text
    cidade = cidade[7:]
    bot.send_message(mensagem.chat.id, f"Procurando informações sobre: {cidade}")
    texto = temp.gerarTexto(cidade)
    bot.send_message(mensagem.chat.id, texto)



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def inicio(mensagem):
    texto = """
    Este é um bot criado para fornecer informações sobre o tempo.
    Para saber como está o clima em uma cidade, siga o modelo abaixo:

    /tempo <nome da cidade>

    ex:
    /tempo belém
    /tempo rio de janeiro


    Não adianta ficar mandando qualquer coisa. Siga o modelo!
    """
    bot.send_message(mensagem.chat.id, texto)



bot.infinity_polling()