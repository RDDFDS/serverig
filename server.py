from flask import Flask, render_template, request
import platform, psutil, socket

app = Flask(__name__)

def get_system_info():
    return {
        "Server machine name": platform.node(),
        "OS": platform.system(),
        "OS version": platform.version(),
        "Arq.": platform.architecture()[0],
        "Processor": "Intel® Core™ i9 14900KS -- 6.20 GHz -- Limited by Host"
        "CPU Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True),
        "Total Mem.": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "RAM Usage": f"{psutil.virtual_memory().percent}%",
        "Server IP": socket.gethostbyname(socket.gethostname())
    }

def get_client_info(request):
    return {
        "IP": request.remote_addr,
        "Machine": socket.getfqdn(request.remote_addr),
        "OS": platform.system(),
        "SO version": platform.version(),
        "Arq.": platform.architecture()[0],
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True),
        "Total Mem.": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "RAM Usage": f"{psutil.virtual_memory().percent}%",
        "User-Agent": request.headers.get('User-Agent'),
        "Accept Lang.": request.headers.get('Accept-Language'),
        "Accept Encoding": request.headers.get('Accept-Encoding')
    }

@app.route('/')
def index():
    client_info = get_client_info(request)
    server_info = get_system_info()
    return render_template('index.html', client_info=client_info, server_info=server_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
