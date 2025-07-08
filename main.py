from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a nossa 1º página = 1º rota
@app.route("/")
def homepage():
    return render_template("index.html")

# roda o nosso aplicativo
if __name__ == "__main__":
    socketio.run(app, host="192.168.0.45", port=5000, debug=True)

#websocket -> tunel