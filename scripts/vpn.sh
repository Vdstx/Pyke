#!/usr/bin/env bash
# scripts/vpn.sh
set -euo pipefail

EASYRSA_DIR="/opt/pyke/pki"          # CA hors code source
SERVER_CN="pyke-vpn"
OVPN_DIR="/etc/openvpn/server"
OVPN_CONF="$OVPN_DIR/server.conf"
PKI_BIN="/usr/share/easy-rsa/3/easyrsa"

case "$1" in
  init-pki)
    sudo mkdir -p "$EASYRSA_DIR"
    cd "$EASYRSA_DIR"
    $PKI_BIN init-pki
    EASYRSA_BATCH=1 $PKI_BIN build-ca nopass <<<"$SERVER_CN"
    ;;
  build-server)
    cd "$EASYRSA_DIR"
    EASYRSA_BATCH=1 $PKI_BIN build-server-full "$SERVER_CN" nopass
    sudo install -Dm600 "pki/issued/$SERVER_CN.crt"   "$OVPN_DIR/server.crt"
    sudo install -Dm600 "pki/private/$SERVER_CN.key" "$OVPN_DIR/server.key"
    sudo install -Dm644 "pki/ca.crt"                 "$OVPN_DIR/ca.crt"
    ;;
  build-client)
    NAME="$2"
    [[ -z "$NAME" ]] && { echo "Usage: $0 build-client <name>"; exit 1; }
    cd "$EASYRSA_DIR"
    EASYRSA_BATCH=1 $PKI_BIN build-client-full "$NAME" nopass
    # crée un .ovpn prêt à exporter
    cat > "${NAME}.ovpn" <<EOF
client
dev tun
proto udp
remote $(curl -s ifconfig.me) 1194
<ca>
$(cat pki/ca.crt)
</ca>
<cert>
$(cat pki/issued/$NAME.crt)
</cert>
<key>
$(cat pki/private/$NAME.key)
</key>
EOF
    echo "Fichier client généré : $(pwd)/${NAME}.ovpn"
    ;;
  start)
    sudo systemctl start openvpn-server@server
    ;;
  stop)
    sudo systemctl stop openvpn-server@server
    ;;
  status)
    sudo systemctl is-active openvpn-server@server
    ;;
  *)
    echo "Usage: $0 {init-pki|build-server|build-client <name>|start|stop|status}"
    exit 1
esac
