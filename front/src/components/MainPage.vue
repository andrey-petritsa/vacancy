<script setup>
import { ref } from 'vue'
import ShortVacanciesPage from './ShortVacanciesPage.vue'
import VacanciesPage from './VacanciesPage.vue'

const tab = ref('short')
function updateUrlStatus(t) {
  const params = new URLSearchParams(window.location.search)
  params.set('status', t === 'new' ? 'unseen' : 'like')
  const url = `${window.location.pathname}?${params.toString()}`
  window.history.replaceState({}, '', url)
}

function select(t) {
  updateUrlStatus(t)
  tab.value = t
}
</script>

<template>
  <div class="main-page">
    <div class="main-page__container">
      <div class="main-page__nav">
        <button
          class="main-page__nav-item"
          :class="{ 'main-page__nav-item_active': tab === 'short' }"
          type="button"
          @click="select('short')"
        >
          Просмотр лайк вакансий
        </button>
        <button
          class="main-page__nav-item"
          :class="{ 'main-page__nav-item_active': tab === 'new' }"
          type="button"
          @click="select('new')"
        >
          Просмотр новых вакансий
        </button>
      </div>

      <div class="main-page__content">
        <ShortVacanciesPage v-if="tab === 'short'" />
        <VacanciesPage v-else />
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-page {
  display: flex;
  justify-content: center;
  padding: 16px;
}

.main-page__container {
  width: 100%;
  max-width: 820px;
}

.main-page__nav {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.main-page__nav-item {
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  background: #f9fafb;
  color: #374151;
}

.main-page__nav-item_active {
  background: #eef2ff;
  border-color: #c7d2fe;
  color: #3730a3;
}

.main-page__content {
}
</style>
