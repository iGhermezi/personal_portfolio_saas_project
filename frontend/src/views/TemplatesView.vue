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
          Your portfolio content stays the same.
        </p>


        <!-- Error -->

        <div
          v-if="error"
          class="mt-6 rounded-2xl border border-red-100 bg-red-50 px-5 py-4 text-sm text-red-600"
        >
          {{ error }}
        </div>


        <!-- Loading -->

        <div
          v-if="loading"
          class="mt-8 rounded-3xl border border-slate-100 bg-white p-10 text-center shadow-sm"
        >
          <p class="text-sm text-slate-400">
            Loading templates...
          </p>
        </div>


        <!-- Templates -->

        <div
          v-else
          class="mt-8 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3"
        >

          <article
            v-for="template in templates"
            :key="template.id"
            class="overflow-hidden rounded-3xl border bg-white shadow-sm transition"
            :class="
              selectedTemplateId === template.id
                ? 'border-violet-400 ring-2 ring-violet-100'
                : 'border-violet-100'
            "
          >

            <!-- Preview -->

            <div class="relative h-48 overflow-hidden bg-slate-100">

              <img
                v-if="template.preview_img"
                :src="template.preview_img"
                :alt="template.name"
                class="h-full w-full object-cover"
              />

              <div
                v-else
                class="flex h-full items-center justify-center"
                :class="
                  template.template_key === 'template_2'
                    ? 'bg-stone-100'
                    : 'bg-slate-950'
                "
              >

                <div
                  v-if="template.template_key === 'template_2'"
                  class="w-3/4 rounded-xl bg-white p-5 shadow-lg"
                >
                  <div class="h-2 w-20 rounded bg-slate-200"></div>
                  <div class="mt-4 h-5 w-40 rounded bg-slate-800"></div>
                  <div class="mt-3 h-2 w-48 rounded bg-slate-200"></div>

                  <div class="mt-6 grid grid-cols-3 gap-2">
                    <div class="h-10 rounded bg-slate-100"></div>
                    <div class="h-10 rounded bg-slate-100"></div>
                    <div class="h-10 rounded bg-slate-100"></div>
                  </div>
                </div>

                <div
                  v-else
                  class="w-3/4 rounded-xl bg-slate-900 p-5"
                >
                  <div class="h-2 w-20 rounded bg-violet-300"></div>
                  <div class="mt-4 h-5 w-40 rounded bg-white/80"></div>
                  <div class="mt-3 h-2 w-48 rounded bg-white/20"></div>
                </div>

              </div>


              <!-- Current -->

              <span
                v-if="selectedTemplateId === template.id"
                class="absolute right-4 top-4 rounded-full bg-violet-500 px-3 py-1 text-xs font-bold text-white"
              >
                Current
              </span>

            </div>


            <!-- Info -->

            <div class="p-6">

              <div class="flex items-start justify-between gap-3">

                <h2 class="text-lg font-bold text-slate-800">
                  {{ template.name }}
                </h2>

                <span
                  class="rounded-full px-3 py-1 text-xs font-semibold"
                  :class="badgeClass(template.access_level)"
                >
                  {{ accessLabel(template.access_level) }}
                </span>

              </div>


              <p class="mt-2 text-sm leading-6 text-slate-500">
                {{ template.description }}
              </p>


              <button
                type="button"
                :disabled="
                  selecting ||
                  selectedTemplateId === template.id
                "
                @click="selectTemplate(template)"
                class="mt-5 w-full rounded-full px-5 py-3 text-sm font-semibold transition disabled:cursor-not-allowed disabled:opacity-60"
                :class="
                  selectedTemplateId === template.id
                    ? 'bg-slate-100 text-slate-400'
                    : 'bg-violet-400 text-white hover:bg-violet-500'
                "
              >
                {{
                  selectedTemplateId === template.id
                    ? 'Currently selected'
                    : selecting
                      ? 'Saving...'
                      : 'Use this template'
                }}
              </button>

            </div>

          </article>

        </div>

      </div>

    </main>

  </div>
</template>


<script setup>

import { onMounted, ref } from 'vue'

import api from '../api/axios'

import DashboardSidebar
  from '../components/Dashboard/DashboardSidebar.vue'


const sidebarCollapsed = ref(false)

const templates = ref([])

const portfolio = ref(null)

const loading = ref(true)

const selecting = ref(false)

const selectedTemplateId = ref(null)

const error = ref(null)


const accessLabel = (level) => {

  if (level === 'premium') {
    return 'Premium'
  }

  if (level === 'verified') {
    return 'Verified'
  }

  return 'Free'
}


const badgeClass = (level) => {

  if (level === 'premium') {
    return 'bg-amber-100 text-amber-700'
  }

  if (level === 'verified') {
    return 'bg-emerald-100 text-emerald-700'
  }

  return 'bg-violet-100 text-violet-600'
}


const loadData = async () => {

  loading.value = true
  error.value = null

  try {

    const [templatesResponse, portfolioResponse] =
      await Promise.all([
        api.get('themes/'),
        api.get('/portfolios/'),
      ])


    templates.value =
      Array.isArray(templatesResponse.data)
        ? templatesResponse.data
        : templatesResponse.data.results || []


    const portfolios = portfolioResponse.data

    portfolio.value =
      Array.isArray(portfolios) && portfolios.length
        ? portfolios[0]
        : null


    selectedTemplateId.value =
      portfolio.value?.template || null

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

  if (!portfolio.value) {

    error.value =
      'Create a portfolio before selecting a template.'

    return

  }


  selecting.value = true
  error.value = null


  try {

    const response = await api.patch(
      `/portfolios/${portfolio.value.id}/`,
      {
        template: template.id,
      }
    )


    portfolio.value = response.data

    selectedTemplateId.value = template.id

  } catch (err) {

    console.error('Failed to select template:', err)

    error.value =
      err.response?.data?.template?.[0] ||
      err.response?.data?.detail ||
      'Unable to select this template.'

  } finally {

    selecting.value = false

  }

}


onMounted(() => {
  loadData()
})

</script>