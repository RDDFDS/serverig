from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Rota para a página principal onde o usuário escolhe o nome de usuário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para enviar e receber mensagens
@socketio.on('message')
def handle_message(data):
    # Enviar a mensagem para todos os usuários conectados
    emit('broadcast', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
