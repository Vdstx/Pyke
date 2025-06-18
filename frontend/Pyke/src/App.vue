<template>
  <div>
    <h1>Pyke - Dashboard</h1>
    <p>VPN status: {{ vpnStatus }}</p>
    <button @click="startVPN">Start VPN</button>
    <button @click="stopVPN">Stop VPN</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const vpnStatus = ref('Unknown')

async function getVPNStatus() {
  const res = await fetch('http://localhost:5000/api/vpn/status')
  const data = await res.json()
  vpnStatus.value = data.vpn
}

async function startVPN() {
  await fetch('http://localhost:5000/api/vpn/start', { method: 'POST' })
  getVPNStatus()
}

async function stopVPN() {
  await fetch('http://localhost:5000/api/vpn/stop', { method: 'POST' })
  getVPNStatus()
}

onMounted(getVPNStatus)
</script>
