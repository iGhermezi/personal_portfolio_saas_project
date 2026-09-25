<template>
  <component
    :is="templateComponent"
    :portfolio="portfolio"
  />
</template>

<script setup>
import { computed } from 'vue'

import TemplateOne from './templates/TemplateOne.vue'
import TemplateTwo from './templates/TemplateTwo.vue'

const props = defineProps({
  portfolio: {
    type: Object,
    required: true,
  },
})

const templateMap = {
  template_1: TemplateOne,
  template_2: TemplateTwo,
}

const templateComponent = computed(() => {
  return templateMap[props.portfolio.template_key] || TemplateOne
})
</script>