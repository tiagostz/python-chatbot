# ChatBot em Flask com Socket.IO

Este projeto é um chatbot em tempo real desenvolvido com Python, Flask e Flask-SocketIO. Ele permite que múltiplos usuários conversem em um chat moderno, responsivo e com suporte a WebSockets.

## Funcionalidades
- Envio e recebimento de mensagens em tempo real
- Interface moderna e responsiva
- Diferenciação visual entre mensagens do usuário e de outros participantes
- Avatares automáticos (inicial do nome)
- Suporte a modo escuro

## Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

## Instalação
1. Clone este repositório ou baixe os arquivos.
2. No terminal, navegue até a pasta do projeto:
   ```
   cd C:\Projetos\python-chatbot
   ```
3. Instale as dependências necessárias:
   ```
   pip install flask flask-socketio eventlet
   ```

## Como executar
1. No terminal, execute o arquivo principal:
   ```
   python main.py
   ```
2. O servidor será iniciado e exibirá o endereço de acesso, por exemplo:
   ```
   * Running on http://192.168.0.45:5000/
   ```
3. Abra o navegador e acesse o endereço informado.
4. Digite seu nome de usuário, escreva uma mensagem e clique em enviar!

## Estrutura dos arquivos
- `main.py`: Backend Flask e SocketIO
- `templates/index.html`: Interface web do chat
- `templates/homepage.html`: (Opcional) Exemplo de outra página

## Observações
- O endereço IP e porta podem ser alterados em `main.py` conforme sua rede.
- Para acessar de outros dispositivos na mesma rede, use o IP local do seu computador.
- O chat suporta múltiplos usuários simultâneos.

## Licença
Este projeto é livre para uso educacional e pessoal. 