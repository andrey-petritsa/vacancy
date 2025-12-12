<script setup>
// Presentational component: receives a single vacancy and emits actions.
const props = defineProps({
  vacancy: { type: Object, required: true }
});

const emit = defineEmits(["like", "dislike", "more"]);

function onButtonClick(button) {
  if (button.type === "like-button") emit("like");
  else if (button.type === "dislike-button") emit("dislike");
  else emit("more");
}

</script>

<template>
  <div class="vacancy-card" v-if="vacancy">
    <div class="vacancy-card__header">
      <div class="vacancy-card__company_labels">
        <span v-for="(label, index) in vacancy['header']['company_labels']" :key="index">
          {{ label.text }}
        </span>
      </div>
      <div class="vacancy-card__header-title">{{ vacancy['header']['title_label']['text'] }}</div>
      <div class="vacancy-card__header-salary_label">{{ vacancy['header']['salary_label']['text'] }}</div>
    </div>

    <div class="vacancy-card__body">
      <div
        v-if="vacancy['body'] && vacancy['body']['skills']"
        class="vacancy-card__skills"
      >
        <div
          class="vacancy-card__skill"
          v-for="(s, idx) in vacancy['body']['skills']"
          :key="s.text + String(s.type) + idx"
          :class="`skill-color_type_${s.type}`"
        >
          {{ s.text }}
        </div>
      </div>
    </div>

    <div class="vacancy-card__footer">
      <div class="vacancy-card__description-labels">
        <span class="vacancy-card__description-label"
            v-for="(description_label, index) in vacancy['footer']['description_labels']" :key="index">
              {{ description_label.text }}
        </span>
      </div>

      <div class="vacancy-card__footer_buttons">
        <button
          :class="`${button.type}`"
          v-for="(button, index) in vacancy['footer']['buttons']"
          :key="index"
          @click="onButtonClick(button)"
        >
          {{ button.text }}
        </button>
      </div>

    </div>
  </div>
</template>

<style scoped>

.vacancy-card {
  background-color: #ffffff;
  border-radius: 16px;
  padding: 20px;
  color: #000000;
}

.vacancy-card__header {
  margin-bottom: 14px;
}

.vacancy-card__body {
  margin-bottom: 14px;
}

.vacancy-card__header-title {
  font-weight: 700;
  font-size: 20px;
  line-height: 1.2;
  color: #000000;
}

.vacancy-card__company_labels {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 14px;
}

.vacancy_card__description_labels {
  display: flex;
  flex-direction: column;
}

.vacancy_card__description_label {
  margin-bottom: 5px;
}

.vacancy-card__header-salary_label {
  font-weight: 700;
  font-size: 20px;
  line-height: 1.2;
  color: #000000;
}

.vacancy_card__footer_buttons {
  margin-top: 14px
}

.like-button {
  background-color: #4d7319;
}

.more-button {
  background-color: #1d4b78;
}

.dislike-button {
  background-color: #ae3b33;
}

.vacancy-card__skills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.vacancy-card__skill {
  font-size: 12px;
  border: 1px solid transparent;
  border-radius: 9999px;
  padding: 2px 8px;
}
</style>

<style src="../assets/skill-colors.css"></style>