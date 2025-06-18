<template>
    <div>
      <h2>IDS / IPS</h2>
      <p>Status: {{ idsStatus }}</p>
      <button @click="startIDS">Start IDS</button>
      <button @click="stopIDS">Stop IDS</button>
    </div>
  </template>
  <style scoped>
  h2 {
    margin-bottom: 0.5rem;
  }
  
  p {
    font-weight: bold;
    margin-bottom: 1rem;
  }
  
  button {
    padding: 0.6rem 1.4rem;
    margin-right: 1rem;
    margin-top: 0.5rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button:first-of-type {
    background-color: #4CAF50; /* vert */
    color: white;
  }
  
  button:first-of-type:hover {
    background-color: #45a049;
  }
  
  button:last-of-type {
    background-color: #f44336; /* rouge */
    color: white;
  }
  
  button:last-of-type:hover {
    background-color: #d32f2f;
  }
  </style>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const idsStatus = ref('Unknown')
  
  async function getIDSStatus() {
    const res = await fetch('http://localhost:5000/api/ids/status')
    const data = await res.json()
    idsStatus.value = data.ids
  }
  
  async function startIDS() {
    await fetch('http://localhost:5000/api/ids/start', { method: 'POST' })
    getIDSStatus()
  }
  
  async function stopIDS() {
    await fetch('http://localhost:5000/api/ids/stop', { method: 'POST' })
    getIDSStatus()
  }
  
  onMounted(getIDSStatus)
  </script>
  