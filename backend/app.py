from flask import Flask, jsonify, request
from flask_cors import CORS
import vpn

app = Flask(__name__)
CORS(app)

vpn_running = False
ids_running = False

# Routes VPN
@app.get("/api/vpn/status")
def vpn_status():
    result = vpn.status()
    # systemctl renvoie "active" ou "inactive"
    return jsonify({"vpn": "running" if "active" in result["stdout"] else "stopped"})

@app.post("/api/vpn/start")
def vpn_start():
    vpn.start()
    return jsonify({"message": "VPN démarré"})

@app.post("/api/vpn/stop")
def vpn_stop():
    vpn.stop()
    return jsonify({"message": "VPN arrêté"})

@app.route('/api/ids/status')
def ids_status():
    return jsonify({"ids": "running" if ids_running else "stopped"})

@app.route('/api/ids/start', methods=['POST'])
def ids_start():
    global ids_running
    #ids_running = True
    return jsonify({"message": "IDS démarré"})

@app.route('/api/ids/stop', methods=['POST'])
def ids_stop():
    global ids_running
    #ids_running = False
    return jsonify({"message": "IDS arrêté"})

# PKI / Clients
@app.post("/api/vpn/init")
def init_pki():
    return jsonify(vpn.init_pki())

@app.post("/api/vpn/server")
def build_server():
    return jsonify(vpn.build_server())

@app.post("/api/vpn/client")
def build_client():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "champ 'name' manquant"}), 400
    return jsonify(vpn.build_client(name))


if __name__ == '__main__':
    app.run(debug=True)
