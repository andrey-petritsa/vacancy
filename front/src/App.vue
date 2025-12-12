<script setup>
import { ref, onMounted } from 'vue'
import MainPage from './components/MainPage.vue'
import LoginPage from './components/LoginPage.vue'
import { show_user } from './api/api.js'

const isAuthorized = ref(false)
const checking = ref(true)

async function initAuth() {
  const token = localStorage.getItem('user_token')
  if (!token) {
    isAuthorized.value = false
    checking.value = false
    return
  }
  try {
    await show_user(token)
    isAuthorized.value = true
  } catch (_) {
    localStorage.removeItem('user_token')
    isAuthorized.value = false
  } finally {
    checking.value = false
  }
}

function onLoggedIn() {
  isAuthorized.value = true
}

onMounted(initAuth)
</script>

<template>
  <div>
    <div v-if="checking"></div>
    <LoginPage v-else-if="!isAuthorized" @logged-in="onLoggedIn" />
    <MainPage v-else />
  </div>
</template>
