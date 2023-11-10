import requests

def obter_clima(cidade, chave_api):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric'
    resposta = requests.get(url)
    dados = resposta.json()

    if dados['cod'] == 200:
        clima = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        return f'Clima: {clima.capitalize()}\nTemperatura: {temperatura}°C'
    else:
        return 'Cidade não encontrada. Verifique o nome da cidade e tente novamente.'

def main():
    cidade = input('Digite o nome da cidade: ')
    chave_api = 'f28af5234a48492f60017b90ef745f74'
    resultado = obter_clima(cidade, chave_api)
    print(resultado)

if __name__ == "__main__":
    main()
