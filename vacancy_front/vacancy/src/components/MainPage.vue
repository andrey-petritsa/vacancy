<script setup>
import { ref } from "vue"

const clicks = ref(0)
const wow = () => (clicks.value += 1)
const features = [
  "⚡ Молниеносная скорость",
  "🧠 Умнее, чем кажется",
  "🧩 Плагинов больше, чем нужно",
  "🚀 Запускается быстрее, чем ты читаешь это",
]
</script>

<template>
  <div class="hero">
    <div class="card">
      <h1>Очень Крутой Проект</h1>
      <p class="tagline">Настолько крутой, что у него есть свой собственный файл README 😎</p>

      <div class="cta">
        <button @click="wow">Хочу демо!</button>
        <span class="clicks" v-if="clicks">Вау x{{ clicks }}</span>
      </div>

      <ul class="features">
        <li v-for="f in features" :key="f">{{ f }}</li>
      </ul>

      <div class="stats">
        <div><strong>99.99%</strong><span>аптайм</span></div>
        <div><strong>∞</strong><span>масштабируемость</span></div>
        <div><strong>0</strong><span>багов (в теории)</span></div>
      </div>

      <p class="footnote">* Все цифры подтверждены независимой комиссией из одного разработчика.</p>
    </div>
  </div>
</template>

<style scoped>
:root { --bg1:#111827; --bg2:#0b1220; --accent:#7c3aed; --accent-2:#22d3ee; }

.hero {
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(1200px 600px at 100% 0, rgba(34,211,238,.15), transparent),
  radial-gradient(1200px 600px at 0 100%, rgba(124,58,237,.18), transparent),
  linear-gradient(180deg, var(--bg1), var(--bg2));
  color: #e5e7eb;
  padding: 24px;
}

.card {
  width: min(920px, 100%);
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  backdrop-filter: blur(8px);
  border-radius: 24px;
  padding: 32px;
  box-shadow: 0 20px 60px rgba(0,0,0,.35);
  animation: pop .5s ease-out;
}

@keyframes pop {
  from { transform: translateY(8px) scale(.98); opacity: 0; }
  to   { transform: translateY(0)   scale(1);    opacity: 1; }
}

h1 {
  font-size: clamp(32px, 5vw, 56px);
  line-height: 1.1;
  margin: 0 0 8px;
  background: linear-gradient(90deg, #fff, var(--accent-2), var(--accent));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.tagline {
  margin: 0 0 20px;
  color: #cbd5e1;
  font-size: clamp(16px, 2.4vw, 20px);
}

.cta {
  display: flex;
  align-items: center;
  gap: 14px;
  margin: 18px 0 26px;
}

button {
  border: none;
  padding: 12px 18px;
  font-size: 16px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--accent), #4f46e5);
  color: white;
  cursor: pointer;
  box-shadow: 0 10px 30px rgba(124,58,237,.4);
  transition: transform .08s ease, filter .2s ease;
}
button:hover { filter: brightness(1.08); }
button:active { transform: translateY(1px) scale(.98); }

.clicks {
  color: #a5b4fc;
  font-weight: 600;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 10px 14px;
  margin: 10px 0 24px;
  padding-left: 18px;
}
.features li { color: #d1d5db; }

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 14px;
  margin: 6px 0 8px;
}
.stats > div {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  padding: 16px;
  border-radius: 14px;
  text-align: center;
}
.stats strong {
  display: block;
  font-size: 28px;
  color: #ffffff;
}
.stats span {
  color: #cbd5e1;
  font-size: 13px;
}

.footnote {
  margin-top: 16px;
  color: #93c5fd;
  font-size: 12px;
  text-align: center;
}
</style>