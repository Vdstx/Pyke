<template>
  <div class="dashboard-container">
    <div class="dashboard">
      <header class="dashboard-header">
        <img src="../assets/PYKE.png" alt="Pyke Logo" class="logo" />
        <h1>Cyber Dashboard</h1>
      </header>

      <main class="dashboard-content">
        <VPNStatus />
        <IDSStatus />
      </main>
    </div>
  </div>
  
</template>

<script setup>
import VPNStatus from './VPNStatus.vue'
import IDSStatus from './IDSStatus.vue'
</script>

<style scoped>
.dashboard-container {
  max-width: 100%; /* ou 90%, selon ce que tu veux */
  margin: 0 auto; /* centre le container */
  background-color: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
.dashboard {
  font-family: sans-serif;
  padding: 2rem;
  background-color: #fefcfa;
  border-radius: 8px;
}

.dashboard-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 3rem;
  position: flex;
}

.logo {
  position: flex ;
  left: 0;
  margin-left: 2rem;
  width: 20%;
  height: 20%;
}

.dashboard-header h1 {
  font-size: 2.2rem;
  text-align: center;
  width: 100%;
  font-style: bold;
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 2rem;
  padding-left: 2rem;
}
</style>
