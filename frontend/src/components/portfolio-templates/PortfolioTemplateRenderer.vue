<template>
  <component :is="templateComponent" :portfolio="portfolio" />
</template>

<script setup>
import { computed } from 'vue'

import TemplateOne from './templates/TemplateOne.vue'
import TemplateTwo from './templates/TemplateTwo.vue'
import TemplateThree from './templates/TemplateThree.vue'
import TemplateFour from './templates/TemplateFour.vue'
import TemplateFive from './templates/TemplateFive.vue'

const props = defineProps({
  portfolio: {
    type: Object,
    required: true,
  },
})

const templateMap = {
  arsam: TemplateOne,
  template_1: TemplateOne,
  template_2: TemplateTwo,
  template_3: TemplateThree,
  template_4: TemplateFour,
  template_5: TemplateFive,
}

const templateComponent = computed(() => {
  return templateMap[props.portfolio.template_key] || TemplateOne
})
</script>
