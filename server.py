from flask import Flask, render_template, request
import platform, psutil, socket

app = Flask(__name__)

def get_system_info():
    return {
        "Sistema Operativo": platform.system(),
        "Versão do SO": platform.version(),
        "Arquitetura": platform.architecture()[0],
        "Processador": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True),
        "Memória Total": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Uso de CPU": f"{psutil.cpu_percent()}%",
        "Uso de RAM": f"{psutil.virtual_memory().percent}%",
        "IP do Servidor": socket.gethostbyname(socket.gethostname())
    }

@app.route('/')
def index():
    client_ip = request.remote_addr
    server_info = get_system_info()
    return render_template('index.html', client_ip=client_ip, server_info=server_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
