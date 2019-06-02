  ![alt text][rasa]![alt text][slack]
# bot-weather_slack
Um projeto que envolve a criação de um bot com a [Stack Rasa](http://rasa.com/) (NLU e Core), integrado ao Slack.



[rasa]: https://i.stack.imgur.com/aSSBC.png "Rasa Stack"
[slack]: https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/slack/icon.png "Slack"

## Clonando o repositório localmente
    git clone https://github.com/tarcisiobruni/bot-weather_slack

## Instalação

É necessário a criação de um ambiente virtual
- sudo apt-get update
- sudo apt install python3-pip
- sudo pip3 install virtualenv
- virtualenv venv --python=python3
- source venv/bin/activate

Agora é preciso instalar as versões mais recentes do Rasa NLU e Rasa Core
- pip3 install -r requirements.txt

Por último, a instalação do modelo de linguagem em Inglês. No caso o bot está planejado para a lingua inglesa.
- python -m spacy download en

## Execução
Há um arquivo MakeFile no diretório com as intruções de execução. Mas uma breve explicação:
1) **Treinando o modelo Rasa NLU**

    make train-nlu
    
    Esse comando traina o modelo NLU do Rasa e armazena isso dentro do diretório */models/current/nlu* do projeto

2) **Treinando o modelo Rasa Core**

    make train-core
    
    Esse comando traina o modelo NLU do Rasa e armazena isso dentro do diretório */models/current/dialogue* do projeto

3) **Iniciando servidor para as *ações* customizadas**

    make action-server
    
    Esse comando inicia o servidor para emular as ações customizadas

4) **Testanto o bot**

    make cmdline
    
    Esse comando inicia uma conversa com o bot via linha de comando

5) **Treinando Online**

    python train_online.py
    
    Esse comando permite conversar com o modelo mas também interferir nas decisões que ele toma e assim ajustar seu aprendizado

6) **Verificando a confiança**

    cd tests/
    python test_interpreter.py
    
    Esse comando permite identificar o quanto de confiança o modelo tem para cada umas das nossas intenções

### Colaboração
Esses material foi produzido a partir de uma série de outros repositórios, materiais, artigos e videos:

- [Rasa HQ](https://github.com/RasaHQ/rasa) 
- [Weather Tutorial](https://github.com/JustinaPetr/Weatherbot_Tutorial)
- [Building-a-Conversational-Chatbot-for-Slack-using-Rasa-and-Python](https://github.com/parulnith/Building-a-Conversational-Chatbot-for-Slack-using-Rasa-and-Python)
- [Building a Conversational Chatbot for Slack using Rasa and Python Artigo](https://towardsdatascience.com/building-a-conversational-chatbot-for-slack-using-rasa-and-python-part-1-bca5cc75d32f)
- [Building a chatbot With Rasa NLU and Rasa Core](https://www.youtube.com/watch?v=xu6D_vLP5vY)
 