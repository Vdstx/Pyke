from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

vpn_running = False
ids_running = False

@app.route('/api/vpn/status')
def vpn_status():
    return jsonify({"vpn": "running" if vpn_running else "stopped"})

@app.route('/api/vpn/start', methods=['POST'])
def vpn_start():
    global vpn_running
    vpn_running = True
    return jsonify({"message": "VPN démarré"})

@app.route('/api/vpn/stop', methods=['POST'])
def vpn_stop():
    global vpn_running
    vpn_running = False
    return jsonify({"message": "VPN arrêté"})

@app.route('/api/ids/status')
def ids_status():
    return jsonify({"ids": "running" if ids_running else "stopped"})

@app.route('/api/ids/start', methods=['POST'])
def ids_start():
    global ids_running
    ids_running = True
    return jsonify({"message": "IDS démarré"})

@app.route('/api/ids/stop', methods=['POST'])
def ids_stop():
    global ids_running
    ids_running = False
    return jsonify({"message": "IDS arrêté"})

if __name__ == '__main__':
    app.run(debug=True)
