<script setup>
import { ref } from 'vue'
import { show_user } from '../api/api.js'

const emit = defineEmits(['logged-in'])

const token = ref('')
const error = ref('')
const loading = ref(false)

async function login() {
  if (!token.value) {
    error.value = 'Введите токен'
    return
  }
  error.value = ''
  loading.value = true
  try {
    await show_user(token.value)
    localStorage.setItem('user_token', token.value)
    emit('logged-in', token.value)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

function onKeydown(e) {
  if (e.key === 'Enter') login()
}
</script>

<template>
  <div class="login">
    <div class="login__box">
      <label class="login__label" for="token-input">введите токен</label>
      <input
        id="token-input"
        class="login__input"
        type="text"
        v-model.trim="token"
        :disabled="loading"
        @keydown="onKeydown"
        placeholder="Ваш токен"
      />
      <button class="login__btn" type="button" :disabled="loading" @click="login">войти</button>
      <div v-if="error" class="login__error">{{ error }}</div>
    </div>
  </div>
  
</template>

<style scoped>
.login {
  display: flex;
  justify-content: center;
  background: #f3f4f6;
  padding: 48px 16px 24px;
}
.login__box {
  width: 100%;
  max-width: 480px;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.06);
}
.login__label {
  display: block;
  margin-bottom: 8px;
  font-size: 16px;
  color: #374151;
}
.login__input {
  width: 100%;
  padding: 16px 18px;
  font-size: 22px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  outline: none;
  background: #fff;
  color: #111827;
}
.login__input:focus { border-color: #a5b4fc; box-shadow: 0 0 0 3px rgba(99,102,241,0.15) }
.login__btn {
  margin-top: 12px;
  width: 100%;
  padding: 14px 16px;
  font-size: 18px;
  border-radius: 8px;
  border: 1px solid #4f46e5;
  background: #4f46e5;
  color: #fff;
  cursor: pointer;
}
.login__btn:disabled { opacity: .7; cursor: default }
.login__error { margin-top: 10px; color: #ef4444; font-size: 14px }
</style>
