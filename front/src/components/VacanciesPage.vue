<script setup>
import { onMounted, ref, computed } from 'vue'
import VacancyCard from './VacancyCard.vue'
import {change_vacancy_status, show_vacancies_cards} from '../api/api.js'

const vacancies = ref([])
const index = ref(0)
const loading = ref(true)
const error = ref(null)

const currentVacancy = computed(() => vacancies.value[index.value] || null)

onMounted(async () => {
  const urlParams = new URLSearchParams(window.location.search)
  const search_query = Object.fromEntries(urlParams)
  vacancies.value = await show_vacancies_cards(search_query)
  loading.value = false
})

async function nextCard() {
  if (index.value < vacancies.value.length - 1) index.value += 1
  else index.value = vacancies.value.length
}

async function onLike() {
  const v = currentVacancy.value
  await change_vacancy_status(v.id, 'like')
  await nextCard()
}

async function onDislike() {
  const v = currentVacancy.value
  await change_vacancy_status(v.id, 'dislike')
  await nextCard()
}

function onMore() {}
</script>

<template>
  <div class="vacancies-page">
    <div class="vacancies-page__container">
      <div v-if="loading" class="vacancies-page__state">Загрузка…</div>
      <div v-else-if="error" class="vacancies-page__state">{{ error }}</div>

      <VacancyCard
        v-else-if="currentVacancy"
        class="vacancies-page__vacancy-card"
        :vacancy="currentVacancy"
        @like="onLike"
        @dislike="onDislike"
        @more="onMore"
      />

      <div v-else class="vacancies-page__state">Вакансий больше нет</div>
    </div>
  </div>
</template>

<style scoped>
.vacancies-page {
  display: flex;
  justify-content: center;
  padding: 24px;
}

.vacancies-page__container {
  width: 100%;
  max-width: 720px;
}

.vacancies-page__vacancy-card {
  width: 100%;
}

.vacancies-page__state {
  color: #666;
}
</style>
