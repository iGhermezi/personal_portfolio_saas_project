<template>

  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">

    <main class="mx-auto max-w-5xl px-6 py-8">

      <!-- Header -->

      <div class="mb-8">

        <button
          type="button"
          class="
            mb-5
            text-sm
            font-medium
            text-slate-400
            transition
            hover:text-violet-500
          "
          @click="router.back()"
        >
          ← Back
        </button>

        <p class="text-sm font-medium text-violet-400">
          Portfolio
        </p>

        <h1
          class="
            mt-1
            text-3xl
            font-bold
            tracking-tight
            text-slate-900
          "
        >
          Create your portfolio
        </h1>

        <p class="mt-2 text-sm text-slate-400">
          Set up your portfolio and choose how it will look.
        </p>

      </div>


      <!-- Form -->

      <form
        class="
          rounded-[28px]
          border
          border-violet-100
          bg-white
          p-7
          shadow-sm
        "
        @submit.prevent="createPortfolio"
      >

        <!-- Title -->

        <div>

          <label
            for="title"
            class="
              block
              text-sm
              font-semibold
              text-slate-700
            "
          >
            Portfolio title
          </label>

          <input
            id="title"
            v-model="form.title"
            type="text"
            placeholder="e.g. John Doe — Full Stack Developer"
            class="
              mt-2
              w-full
              rounded-2xl
              border
              border-slate-200
              px-4
              py-3
              text-sm
              text-slate-800
              outline-none
              transition
              focus:border-violet-300
              focus:ring-4
              focus:ring-violet-50
            "
          />

        </div>


        <!-- Slug -->

        <div class="mt-6">

          <label
            for="slug"
            class="
              block
              text-sm
              font-semibold
              text-slate-700
            "
          >
            Portfolio URL
          </label>

          <input
            id="slug"
            v-model="form.slug"
            type="text"
            placeholder="john-doe"
            class="
              mt-2
              w-full
              rounded-2xl
              border
              border-slate-200
              px-4
              py-3
              text-sm
              text-slate-800
              outline-none
              transition
              focus:border-violet-300
              focus:ring-4
              focus:ring-violet-50
            "
          />

          <p class="mt-2 text-xs text-slate-400">
            This will be used as your public portfolio URL.
          </p>

        </div>


        <!-- Bio -->

        <div class="mt-6">

          <label
            for="bio"
            class="
              block
              text-sm
              font-semibold
              text-slate-700
            "
          >
            Short bio
          </label>

          <textarea
            id="bio"
            v-model="form.bio"
            rows="5"
            placeholder="Tell visitors a little about yourself..."
            class="
              mt-2
              w-full
              resize-none
              rounded-2xl
              border
              border-slate-200
              px-4
              py-3
              text-sm
              text-slate-800
              outline-none
              transition
              focus:border-violet-300
              focus:ring-4
              focus:ring-violet-50
            "
          />

        </div>


        <!-- Templates -->

        <div class="mt-8">

          <div>

            <h2
              class="
                text-sm
                font-semibold
                text-slate-700
              "
            >
              Choose a template
            </h2>

            <p class="mt-1 text-xs text-slate-400">
              Available templates depend on your account access.
            </p>

          </div>


          <!-- Loading templates -->

          <div
            v-if="templatesLoading"
            class="
              mt-4
              rounded-2xl
              border
              border-slate-100
              bg-slate-50
              p-6
              text-center
            "
          >

            <p class="text-sm text-slate-400">
              Loading templates...
            </p>

          </div>


          <!-- Templates -->

          <div
            v-else
            class="
              mt-4
              grid
              gap-4
              sm:grid-cols-2
              lg:grid-cols-3
            "
          >

            <button
              v-for="template in templates"
              :key="template.id"
              type="button"
              class="
                overflow-hidden
                rounded-2xl
                border
                text-left
                transition
                hover:-translate-y-0.5
                hover:shadow-md
              "
              :class="
                form.template === template.id
                  ? 'border-violet-400 ring-4 ring-violet-50'
                  : 'border-slate-200'
              "
              @click="form.template = template.id"
            >

              <div
                class="
                  flex
                  h-36
                  items-center
                  justify-center
                  bg-slate-50
                "
              >

                <img
                  v-if="template.preview_img"
                  :src="template.preview_img"
                  :alt="template.name"
                  class="h-full w-full object-cover"
                />

                <span
                  v-else
                  class="text-3xl text-violet-300"
                >
                  ✦
                </span>

              </div>


              <div class="p-4">

                <h3
                  class="
                    text-sm
                    font-semibold
                    text-slate-800
                  "
                >
                  {{ template.name }}
                </h3>

                <p
                  class="
                    mt-1
                    line-clamp-2
                    text-xs
                    leading-5
                    text-slate-400
                  "
                >
                  {{ template.description }}
                </p>

                <span
                  class="
                    mt-3
                    inline-block
                    rounded-full
                    bg-violet-50
                    px-3
                    py-1
                    text-[11px]
                    font-medium
                    text-violet-500
                  "
                >
                  {{ template.access_level }}
                </span>

              </div>

            </button>

          </div>

        </div>


        <!-- Error -->

        <div
          v-if="error"
          class="
            mt-6
            rounded-2xl
            border
            border-red-100
            bg-red-50
            px-4
            py-3
            text-sm
            text-red-500
          "
        >
          {{ error }}
        </div>


        <!-- Actions -->

        <div
          class="
            mt-8
            flex
            flex-col-reverse
            gap-3
            sm:flex-row
            sm:justify-end
          "
        >

          <button
            type="button"
            class="
              rounded-full
              px-6
              py-3
              text-sm
              font-semibold
              text-slate-500
              transition
              hover:bg-slate-50
            "
            @click="router.back()"
          >
            Cancel
          </button>


          <button
            type="submit"
            :disabled="loading"
            class="
              rounded-full
              bg-violet-400
              px-7
              py-3
              text-sm
              font-semibold
              text-white
              shadow-lg
              shadow-violet-100
              transition
              hover:-translate-y-0.5
              hover:bg-violet-500
              disabled:cursor-not-allowed
              disabled:opacity-60
            "
          >
            {{ loading ? 'Creating...' : 'Create Portfolio' }}
          </button>

        </div>

      </form>

    </main>

  </div>

</template>


<script setup>

import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

import api from '../api/axios'


const router = useRouter()


/*
 * Form state
 */

const form = reactive({
  title: '',
  slug: '',
  bio: '',
  template: null,
})


/*
 * Templates
 */

const templates = ref([])

const templatesLoading = ref(true)


/*
 * Form state
 */

const loading = ref(false)

const error = ref(null)


/*
 * Load available templates
 */

const loadTemplates = async () => {

  templatesLoading.value = true
  error.value = null

  try {

    const response = await api.get('/templates/')

    templates.value = Array.isArray(response.data)
      ? response.data
      : response.data.results || []

  } catch (err) {

    console.error('Failed to load templates:', err)

    error.value =
      err.response?.data?.detail ||
      'Unable to load templates.'

  } finally {

    templatesLoading.value = false

  }

}


/*
 * Create portfolio
 */

const createPortfolio = async () => {

  error.value = null

  if (!form.title.trim()) {
    error.value = 'Please enter a portfolio title.'
    return
  }

  if (!form.slug.trim()) {
    error.value = 'Please enter a portfolio URL.'
    return
  }

  if (!form.template) {
    error.value = 'Please choose a template.'
    return
  }

  loading.value = true

  try {

    await api.post('/portfolios/', {
      title: form.title.trim(),
      slug: form.slug.trim(),
      bio: form.bio.trim(),
      template: form.template,
    })

    await router.push('/dashboard')

  } catch (err) {

    console.error('Failed to create portfolio:', err)

    const data = err.response?.data

    if (data && typeof data === 'object') {

      const firstError = Object.values(data)
        .flat()
        .find(Boolean)

      error.value =
        firstError ||
        'Unable to create your portfolio.'

    } else {

      error.value =
        'Unable to create your portfolio.'

    }

  } finally {

    loading.value = false

  }

}


/*
 * Load templates when page opens
 */

onMounted(() => {

  loadTemplates()

})

</script>