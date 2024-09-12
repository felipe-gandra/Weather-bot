import credenciais
import telebot
import weather


bot = telebot.TeleBot(credenciais.token_bot)

@bot.message_handler(commands = ['tempo'])  # Função que le a cidade para verificar o tempo
def cidade(mensagem):
    cidade = mensagem.text

    if (len(mensagem.text) < 7):
        bot.send_message(mensagem.chat.id, "Digite um nome de cidade válido")
        return
    
    cidade = cidade[7:] #corta o '/tempo'

    bot.send_message(mensagem.chat.id, f"Procurando informações sobre: {cidade}")
    texto = weather.gerarTexto(cidade)  #gera o texto de resposta com base nos dados climaticos
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):  #retorna true se houver mensagem no chat
    return True

@bot.message_handler(func=verificar) #mensagem padrão
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