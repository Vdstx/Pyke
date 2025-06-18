from flask import Flask, jsonify
import subprocess
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/api/vpn/status')
def vpn_status():
    return jsonify({"vpn": "running"})

@app.route('/api/vpn/start', methods=['POST'])
def vpn_start():
    return jsonify({"message": "VPN démarré"})

@app.route('/api/vpn/stop', methods=['POST'])
def vpn_stop():
    return jsonify({"message": "VPN arrêté"})

if __name__ == '__main__':
    app.run(debug=True)
