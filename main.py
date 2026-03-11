import eventlet

# O monkey_patch deve ser chamado antes de qualquer outro import
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    # reenvia a mensagem para todos os clientes conectados
    send(mensagem, broadcast=True)

# criar a nossa 1º página = 1º rota
@app.route("/")
def homepage():
    # garante que estamos renderizando o template correto
    return render_template("homepage.html")

# roda o nosso aplicativo
if __name__ == "__main__":
    # usa o mesmo host/porta que o front espera (mesma origem)
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)

#websocket -> tunelC