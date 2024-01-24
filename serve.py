from flask import Flask, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    # init stress_cpu.py in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify(message="CPU stress test initialized!"), 200

@app.route('/', methods=['GET'])
def handle_get():
    # Get the private IP address of current EC2 instance
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return jsonify(private_ip=private_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
