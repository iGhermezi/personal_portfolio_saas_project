<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <div class="mx-auto max-w-6xl px-6 py-8">
        <p class="text-sm font-medium text-violet-400">
          Templates
        </p>

        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          Choose your design
        </h1>

        <p class="mt-2 text-sm text-slate-400">
          Choose a template for your portfolio.
          Premium templates require an active subscription.
        </p>

        <div
          v-if="loading"
          class="mt-8 rounded-3xl border border-slate-100 bg-white p-10 text-center shadow-sm"
        >
          <p class="text-sm text-slate-400">
            Loading templates...
          </p>
        </div>

        <div
          v-else-if="error"
          class="mt-8 rounded-3xl border border-red-100 bg-red-50 p-6"
        >
          <p class="text-sm font-medium text-red-600">
            {{ error }}
          </p>
        </div>

        <div
          v-else
          class="mt-8 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3"
        >
          <div
            v-for="template in templates"
            :key="template.id"
            class="group relative overflow-hidden rounded-3xl border border-violet-100 bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-lg"
          >
            <!-- Preview -->
            <div
              class="relative flex h-44 items-center justify-center overflow-hidden bg-violet-50"
            >
              <img
                v-if="template.preview_img"
                :src="template.preview_img"
                :alt="template.name"
                class="h-full w-full object-cover"
              />

              <span
                v-else
                class="text-5xl text-violet-200"
              >
                ◈
              </span>

              <!-- Lock overlay -->
              <div
                v-if="!template.can_use"
                class="absolute inset-0 flex items-center justify-center bg-slate-900/55 backdrop-blur-[2px]"
              >
                <div
                  class="flex flex-col items-center text-center text-white"
                >
                  <div
                    class="flex h-14 w-14 items-center justify-center rounded-full bg-white/15 text-2xl backdrop-blur"
                  >
                    🔒
                  </div>

                  <p class="mt-2 text-sm font-semibold">
                    Locked
                  </p>
                </div>
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-start justify-between gap-3">
                <h2 class="text-lg font-bold text-slate-800">
                  {{ template.name }}
                </h2>

                <span
                  class="shrink-0 rounded-full px-3 py-1 text-xs font-semibold"
                  :class="badgeClass(template.access_level)"
                >
                  {{ accessLabel(template.access_level) }}
                </span>
              </div>

              <p class="mt-2 text-sm leading-6 text-slate-500">
                {{ template.description }}
              </p>

              <!-- Available -->
              <button
                v-if="template.can_use"
                type="button"
                class="mt-5 w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
                :disabled="selectingId === template.id"
                @click="selectTemplate(template)"
              >
                {{
                  selectingId === template.id
                    ? 'Selecting...'
                    : 'Use this template'
                }}
              </button>

              <button
                v-else
                type="button"
                disabled
                class="mt-5 w-full cursor-not-allowed rounded-2xl bg-slate-100 px-5 py-3 text-sm font-semibold text-slate-400"
              >
                Unavailable
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

import api from '../api/axios'

import DashboardSidebar
  from '../components/Dashboard/DashboardSidebar.vue'

const router = useRouter()

const sidebarCollapsed = ref(false)

const templates = ref([])
const loading = ref(true)
const error = ref(null)
const selectingId = ref(null)

const badgeClass = (level) => {
  if (level === 'premium') {
    return 'bg-amber-100 text-amber-700'
  }

  return 'bg-violet-100 text-violet-600'
}

const accessLabel = (level) => {
  if (level === 'premium') {
    return 'Premium'
  }

  return 'Free'
}

const loadTemplates = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await api.get('themes/')

    templates.value = Array.isArray(response.data)
      ? response.data
      : response.data.results || []
  } catch (err) {
    console.error('Failed to load templates:', err)

    error.value =
      err.response?.data?.detail ||
      'Unable to load templates.'
  } finally {
    loading.value = false
  }
}

const selectTemplate = async (template) => {
  if (!template.can_use) {
    return
  }

  selectingId.value = template.id

  try {
    /*
     * We get the portfolio list first because the current
     * Templates page is responsible only for template selection.
     */
    const response = await api.get('portfolios/')

    const portfolios = Array.isArray(response.data)
      ? response.data
      : response.data.results || []

    if (!portfolios.length) {
      router.push('/portfolio/create')
      return
    }

    const portfolio = portfolios[0]

    await api.patch(
      `portfolios/${portfolio.id}/`,
      {
        template: template.id,
      }
    )

    router.push(
      `/portfolio/${portfolio.id}/preview`
    )
  } catch (err) {
    console.error('Failed to select template:', err)

    error.value =
      err.response?.data?.template?.[0] ||
      err.response?.data?.detail ||
      'Unable to select this template.'
  } finally {
    selectingId.value = null
  }
}

const goToUpgrade = () => {
  router.push('/upgrade')
}


onMounted(() => {
  loadTemplates()
})
</script>