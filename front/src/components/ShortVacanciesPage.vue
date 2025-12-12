<script setup>
import { onMounted, ref } from 'vue'
import ShortVacancyCard from './ShortVacancyCard.vue'
import { show_short_vacancies_cards, change_vacancy_status } from '../api/api.js'

const vacancies = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const urlParams = new URLSearchParams(window.location.search)
    const search_query = Object.fromEntries(urlParams)
    vacancies.value = await show_short_vacancies_cards(search_query)
  } catch (e) {
    error.value = 'Не удалось загрузить вакансии'
  } finally {
    loading.value = false
  }
})

async function onProcessed(id) {
  await change_vacancy_status(id, 'processed')
  vacancies.value = vacancies.value.filter(v => v.id !== id)
}

async function onCancel(id) {
  await change_vacancy_status(id, 'cancelled')
  vacancies.value = vacancies.value.filter(v => v.id !== id)
}
</script>

<template>
  <div class="short-vacancies-page">
    <div class="short-vacancies-page__container">
      <div v-if="loading" class="short-vacancies-page__state">Загрузка…</div>
      <div v-else-if="error" class="short-vacancies-page__state">{{ error }}</div>

      <div v-else-if="vacancies.length" class="short-vacancies-page__list">
        <ShortVacancyCard
          v-for="v in vacancies"
          :key="v.id"
          class="short-vacancies-page__item"
          :vacancy="v"
          @processed="onProcessed"
          @cancel="onCancel"
        />
      </div>

      <div v-else class="short-vacancies-page__state">Ничего не найдено</div>
    </div>
  </div>
</template>

<style scoped>
.short-vacancies-page {
  display: flex;
  justify-content: center;
  padding: 16px;
}

.short-vacancies-page__container {
  width: 100%;
  max-width: 720px;
}

.short-vacancies-page__list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.short-vacancies-page__item {
  width: 100%;
}

.short-vacancies-page__state {
  color: #6b7280;
}
</style>
