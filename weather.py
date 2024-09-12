import requests
import credenciais

# link do open_weather: https://openweathermap.org/



def gerarTexto(cidade):
    API_KEY = credenciais.token_weather
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    info = requisicao.json()

    if 'main' not in info:
        texto = "Essa cidade não foi encontrada"
        return texto

    #le as informações e separa as que serao mostradas
    temperatura = info['main']['temp'] - 273
    sensacao = info['main']['feels_like'] - 273
    umidade = info['main']['humidity']
    geral = info['weather'][0]['main']

    #traduz as codições para o português
    if geral == 'Clouds': geral = 'Nublado'
    if geral == 'Clear': geral = 'Tempo aberto'
    if geral == 'Snow': geral = 'Nevando'
    if  geral == 'Rain': geral = 'Chovendo'
    if geral == 'Drizzle': geral = 'Chuviscando'
    if geral == 'Thunderstorm': geral = 'Trovoadas'


    if (umidade < 30):
        condicao_umidade = "Umidade extremamente baixa"
    elif umidade < 50:
        condicao_umidade = "Umidade baixa"
    elif umidade < 70:
        condicao_umidade = "Umidade ideal"
    else:
        condicao_umidade = "Umidade elevada"
    

    texto = f"""
    Boletim do clima em {cidade}:
    Situação: {geral}
    Temperatura: {int(temperatura)} C
    Sensação térmica: {int(sensacao)} C
    Umidade: {umidade}%
    Obs: {condicao_umidade}

    """

    return texto


