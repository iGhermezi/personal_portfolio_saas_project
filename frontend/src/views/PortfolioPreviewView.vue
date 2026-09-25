<template>

  <div class="min-h-screen bg-slate-100">

    <!-- Toolbar -->

    <header
      class="
        sticky
        top-0
        z-50
        border-b
        border-slate-200
        bg-white/95
        backdrop-blur
      "
    >

      <div
        class="
          mx-auto
          flex
          max-w-7xl
          items-center
          justify-between
          gap-4
          px-5
          py-4
        "
      >

        <div>

          <p
            class="
              text-xs
              font-semibold
              uppercase
              tracking-wide
              text-violet-400
            "
          >
            Portfolio Preview
          </p>

          <h1
            class="
              mt-1
              text-lg
              font-bold
              text-slate-800
            "
          >
            {{ portfolio?.title || 'Portfolio' }}
          </h1>

        </div>


        <div class="flex items-center gap-3">

          <button
            type="button"
            class="
              rounded-full
              border
              border-slate-200
              px-4
              py-2
              text-sm
              font-semibold
              text-slate-600
              transition
              hover:bg-slate-50
            "
            @click="router.push('/dashboard')"
          >
            Dashboard
          </button>

          <button
            v-if="portfolio"
            type="button"
            class="
              rounded-full
              bg-violet-500
              px-4
              py-2
              text-sm
              font-semibold
              text-white
              transition
              hover:bg-violet-600
              disabled:cursor-not-allowed
              disabled:opacity-60
            "
            :disabled="publishing"
            @click="togglePublish"
          >
            {{
              publishing
                ? 'Saving...'
                : portfolio.is_published
                  ? 'Unpublish'
                  : 'Publish'
            }}
          </button>

        </div>

      </div>

    </header>


    <!-- Loading -->

    <div
      v-if="loading"
      class="
        flex
        min-h-[70vh]
        items-center
        justify-center
      "
    >
      <p class="text-sm text-slate-400">
        Loading portfolio...
      </p>
    </div>


    <!-- Error -->

    <div
      v-else-if="error"
      class="
        mx-auto
        max-w-xl
        px-6
        py-20
      "
    >

      <div
        class="
          rounded-3xl
          border
          border-red-100
          bg-red-50
          p-8
        "
      >

        <p class="font-semibold text-red-700">
          Failed to load portfolio.
        </p>

        <p class="mt-2 text-sm text-red-500">
          {{ error }}
        </p>

      </div>

    </div>


    <!-- Portfolio -->

    <PortfolioTemplateRenderer
      v-else-if="portfolio"
      :portfolio="portfolio"
    />

  </div>

</template>


<script setup>

import {
  onMounted,
  ref,
} from 'vue'

import { useRoute, useRouter } from 'vue-router'

import api from '../api/axios'

import PortfolioTemplateRenderer
  from '../components/portfolio-templates/PortfolioTemplateRenderer.vue'


const route = useRoute()

const router = useRouter()


const portfolio = ref(null)

const loading = ref(true)

const publishing = ref(false)

const error = ref(null)


const loadPortfolio = async () => {

  loading.value = true
  error.value = null

  try {

    const response = await api.get(
      `/portfolios/${route.params.id}/`
    )

    portfolio.value = response.data

  } catch (err) {

    console.error(
      'Failed to load portfolio:',
      err
    )

    error.value =
      err.response?.data?.detail ||
      'Unable to load this portfolio.'

  } finally {

    loading.value = false

  }

}


const togglePublish = async () => {

  if (!portfolio.value) {
    return
  }

  publishing.value = true

  try {

    const nextPublished =
      !portfolio.value.is_published

    const response = await api.patch(
      `/portfolios/${portfolio.value.id}/`,
      {
        is_published: nextPublished,
      }
    )

    portfolio.value = response.data

  } catch (err) {

    console.error(
      'Failed to update publish status:',
      err
    )

    error.value =
      err.response?.data?.detail ||
      'Unable to update publish status.'

  } finally {

    publishing.value = false

  }

}


onMounted(() => {

  loadPortfolio()

})

</script>