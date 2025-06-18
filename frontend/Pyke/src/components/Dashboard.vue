<template>
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
</template>

<script setup>
import VPNStatus from './VPNStatus.vue'
import IDSStatus from './IDSStatus.vue'
</script>

<style scoped>
.dashboard {
  font-family: sans-serif;
  padding: 2rem;
  background-color: #fefcfa;
  width: 100%; 
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
  width: 90%;
  height: 90%;
}

.dashboard-header h1 {
  font-size: 2rem;
  text-align: center;
  width: 100%;
}

.dashboard-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 2rem;
  padding-left: 2rem;
}
</style>
