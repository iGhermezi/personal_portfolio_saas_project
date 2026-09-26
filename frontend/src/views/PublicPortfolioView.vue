<template>
  <div class="min-h-screen bg-slate-100">
    <div
      v-if="loading"
      class="flex min-h-screen items-center justify-center"
    >
      <p class="text-sm text-slate-400">Loading portfolio...</p>
    </div>

    <div
      v-else-if="error"
      class="flex min-h-screen items-center justify-center px-6 text-center"
    >
      <div>
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-red-50 text-2xl text-red-500">
          !
        </div>
        <h1 class="mt-5 text-2xl font-bold text-slate-800">
          Portfolio not available
        </h1>
        <p class="mt-2 text-sm text-slate-400">{{ error }}</p>
      </div>
    </div>

    <template v-else-if="portfolio">
      <PortfolioTemplateRenderer :portfolio="portfolio" />
    </template>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import api from '../api/axios'
import PortfolioTemplateRenderer from '../components/portfolio-templates/PortfolioTemplateRenderer.vue'

const route = useRoute()

const portfolio = ref(null)
const loading = ref(true)
const error = ref(null)

const loadPortfolio = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await api.get(
      `/portfolios/public/${route.params.slug}/`
    )

    portfolio.value = response.data
  } catch (err) {
    console.error('Failed to load public portfolio:', err)

    error.value =
      err.response?.data?.detail ||
      'This portfolio is not available.'
  } finally {
    loading.value = false
  }
}

onMounted(loadPortfolio)
</script>
