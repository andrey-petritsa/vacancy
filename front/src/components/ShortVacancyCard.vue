<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { generate_cover_latter } from '../api/api.js'

const {
  vacancy
} = defineProps({
  vacancy: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['processed', 'cancel'])

const expanded = ref(false)
function toggleExpand() {
  expanded.value = !expanded.value
}

function onYes(id) { emit('processed', id) }
function onNo(id) { emit('cancel', id) }

const cover_latter = ref('')
const is_generation = ref(false)
const gen_error = ref('')
const is_conver_open = ref(false)

function openCoverModal() {
  is_conver_open.value = true
}
function close_cover_modal() {
  is_conver_open.value = false
}

function on_key_down(e) {
  if (e.key === 'Escape' && is_conver_open.value) {
    close_cover_modal()
  }
}

onMounted(() => {
  window.addEventListener('keydown', on_key_down)
})
onBeforeUnmount(() => {
  window.removeEventListener('keydown', on_key_down)
})

async function on_brain_click() {
  if (!vacancy?.text) return
  is_generation.value = true
  gen_error.value = ''
  cover_latter.value = ''
  openCoverModal()
  try {
    const result = await generate_cover_latter(vacancy.text)
    cover_latter.value = result
  } catch (e) {
    gen_error.value = 'Не удалось сгенерировать сопроводительное письмо'
  } finally {
    is_generation.value = false
  }
}

</script>

<template>
  <div class="short-vacancy-card">
    <div class="short-vacancy-card__main">
      <div class="short-vacancy-card__header">
        <div class="short-vacancy-card__date">{{ vacancy.date }}</div>
        <div class="short-vacancy-card__title">{{ vacancy.title }}</div>
        <div v-if="vacancy.salary" class="short-vacancy-card__salary">{{ vacancy.salary }}</div>
        <div class="short-vacancy-card__company">{{ vacancy.company }}</div>
        <div v-if="vacancy.contact" class="short-vacancy-card__contact">{{ vacancy.contact }}</div>
      </div>

      <div class="short-vacancy-card__skills" v-if="vacancy.skills">
        <div
          class="short-vacancy-card__skill"
          :class="`skill-color_type_${s.type}`"
          v-for="s in vacancy.skills"
          :key="s.text + String(s.type)"
        >
          {{ s.text }}
        </div>
        <button
          v-if="vacancy.text"
          class="short-vacancy-card__expand-chip"
          type="button"
          :aria-expanded="expanded ? 'true' : 'false'"
          :aria-label="expanded ? 'Скрыть описание' : 'Показать описание'"
          @click="toggleExpand"
        >
          <span class="short-vacancy-card__expand-icon">{{ expanded ? '▴' : '▾' }}</span>
        </button>
      </div>

      <transition name="short-vacancy-card__text-fx">
        <div v-if="expanded" class="short-vacancy-card__text">{{ vacancy.text }}</div>
      </transition>
    </div>

    <div class="short-vacancy-card__actions">
      <button class="short-vacancy-card__btn short-vacancy-card__btn_type_yes"
              type="button"
              aria-label="like"
              @click="onYes(vacancy.id)">
        ✓
      </button>
      <button class="short-vacancy-card__btn short-vacancy-card__btn_type_no"
              type="button"
              aria-label="dislike"
              @click="onNo(vacancy.id)">
        ✗
      </button>
      <button class="short-vacancy-card__btn short-vacancy-card__btn_type_brain"
              type="button"
              aria-label="brain"
              :disabled="is_generation"
              @click="on_brain_click">
        🧠
      </button>
    </div>

    <teleport to="body">
      <div v-if="is_conver_open" class="cover-modal__overlay" @click.self="close_cover_modal">
        <div class="cover-modal" role="dialog" aria-modal="true" aria-labelledby="cover-modal-title">
          <div class="cover-modal__header">
            <h3 id="cover-modal-title" class="cover-modal__title">Сопроводительное письмо</h3>
            <button class="cover-modal__close" type="button" aria-label="Закрыть" @click="close_cover_modal">✕</button>
          </div>
          <div class="cover-modal__body">
            <div v-if="is_generation" class="short-vacancy-card__cover-loading">Генерация...</div>
            <div v-else-if="gen_error" class="short-vacancy-card__cover-error">{{ gen_error }}</div>
            <div v-else class="short-vacancy-card__cover-text">{{ cover_latter }}</div>
          </div>
        </div>
      </div>
    </teleport>
  </div>
</template>

<style scoped>
.short-vacancy-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: #fff;
}

.short-vacancy-card__main {
  flex: 1 1 auto;
  min-width: 0;
}

.short-vacancy-card__header {
  display: grid;
  grid-template-columns: auto;
  row-gap: 4px;
}

.short-vacancy-card__date {
  font-size: 12px;
  color: #6b7280;
}

.short-vacancy-card__title {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
}

.short-vacancy-card__salary {
  font-size: 14px;
  color: #111827;
}

.short-vacancy-card__company {
  font-size: 14px;
  color: #374151;
}

.short-vacancy-card__contact {
  font-size: 12px;
  color: #6b7280;
}

.short-vacancy-card__skills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 8px;
}

.short-vacancy-card__skill {
  font-size: 12px;
  border: 1px solid transparent;
  border-radius: 9999px;
  padding: 2px 8px;
}

.short-vacancy-card__actions {
  display: flex;
  gap: 8px;
}

.short-vacancy-card__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 32px;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
  background: #fff;
  cursor: default;
  transition: transform 120ms ease, box-shadow 120ms ease, background-color 120ms ease, border-color 120ms ease, color 120ms ease;
}

.short-vacancy-card__btn_type_yes {
  color: #10b981;
}

.short-vacancy-card__btn_type_no {
  color: #ef4444;
}

.short-vacancy-card__btn_type_brain {
  color: #8b5cf6;
}

.short-vacancy-card__btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.short-vacancy-card__btn:active {
  transform: translateY(0);
  box-shadow: none;
}

.short-vacancy-card__btn:focus-visible {
  outline: 2px solid #93c5fd;
  outline-offset: 2px;
}

.short-vacancy-card__btn_type_yes:hover {
  background: #ecfdf5;
  border-color: #a7f3d0;
}
.short-vacancy-card__btn_type_yes:active {
  background: #d1fae5;
  border-color: #6ee7b7;
}

.short-vacancy-card__btn_type_no:hover {
  background: #fef2f2;
  border-color: #fecaca;
}
.short-vacancy-card__btn_type_no:active {
  background: #fee2e2;
  border-color: #fca5a5;
}

.short-vacancy-card__btn_type_brain:hover {
  background: #f5f3ff;
  border-color: #ddd6fe;
}
.short-vacancy-card__btn_type_brain:active {
  background: #ede9fe;
  border-color: #c4b5fd;
}


.short-vacancy-card__cover-loading {
  font-size: 13px;
  color: #6b7280;
}

.short-vacancy-card__cover-error {
  font-size: 13px;
  color: #ef4444;
}

.short-vacancy-card__cover-text {
  white-space: pre-wrap;
  font-size: 13px;
  line-height: 1.4;
  color: #111827;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  border-radius: 6px;
  padding: 10px;
}

/* Cover letter modal */
.cover-modal__overlay {
  position: fixed;
  inset: 0;
  background: rgba(17, 24, 39, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  z-index: 1000;
}

.cover-modal {
  width: 100%;
  max-width: 720px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  border: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  max-height: 85vh;
}

.cover-modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 14px;
  border-bottom: 1px solid #e5e7eb;
}

.cover-modal__title {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: #111827;
}

.cover-modal__close {
  width: 32px;
  height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
  background: #fff;
  cursor: pointer;
}

.cover-modal__close:hover {
  background: #f3f4f6;
}

.cover-modal__body {
  padding: 12px 14px;
  overflow: auto;
}

.short-vacancy-card__expand-chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 2px 8px;
  border-radius: 9999px;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  color: #6b7280;
  font-size: 12px;
  cursor: pointer;
  transition: background-color 120ms ease, border-color 120ms ease, color 120ms ease, transform 120ms ease;
}

.short-vacancy-card__expand-chip:hover {
  background: #f3f4f6;
  transform: translateY(-1px);
}

.short-vacancy-card__expand-chip:active {
  transform: translateY(0);
}

.short-vacancy-card__expand-chip:focus-visible {
  outline: 2px solid #93c5fd;
  outline-offset: 2px;
}

.short-vacancy-card__expand-icon {
  line-height: 1;
  font-size: 14px;
}

.short-vacancy-card__text {
  margin-top: 8px;
  font-size: 13px;
  line-height: 1.4;
  color: #374151;
}

.short-vacancy-card__text-fx-enter-active,
.short-vacancy-card__text-fx-leave-active {
  transition: opacity 150ms ease, transform 150ms ease;
}
.short-vacancy-card__text-fx-enter-from,
.short-vacancy-card__text-fx-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>

<style src="../assets/skill-colors.css"></style>
