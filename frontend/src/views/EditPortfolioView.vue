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
          Edit your portfolio
        </h1>

        <p class="mt-2 text-sm text-slate-400">
          Update your portfolio information and choose a template.
        </p>
      </div>


      <!-- Loading portfolio -->

      <div
        v-if="loadingPortfolio"
        class="
          rounded-[28px]
          border
          border-violet-100
          bg-white
          p-10
          text-center
          shadow-sm
        "
      >
        <p class="text-sm text-slate-400">
          Loading your portfolio...
        </p>
      </div>


      <!-- Form -->

      <form
        v-else
        class="
          rounded-[28px]
          border
          border-violet-100
          bg-white
          p-7
          shadow-sm
        "
        @submit.prevent="updatePortfolio"
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
            This is used as your public portfolio URL.
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
            v-else-if="templates.length"
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
                group
                relative
                overflow-hidden
                rounded-2xl
                border
                text-left
                transition
              "
              :class="
                template.can_use
                  ? (
                      form.template === template.id
                        ? 'border-violet-400 ring-4 ring-violet-50 hover:-translate-y-0.5 hover:shadow-md'
                        : 'border-slate-200 hover:-translate-y-0.5 hover:shadow-md'
                    )
                  : 'cursor-not-allowed border-slate-200'
              "
              @click="selectTemplate(template)"
            >

              <!-- Template preview -->

              <div
                class="
                  relative
                  flex
                  h-36
                  items-center
                  justify-center
                  overflow-hidden
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


                <!-- Locked overlay -->

                <div
                  v-if="!template.can_use"
                  class="
                    absolute
                    inset-0
                    flex
                    items-center
                    justify-center
                    bg-slate-900/55
                    backdrop-blur-[2px]
                  "
                >
                  <div
                    class="
                      flex
                      flex-col
                      items-center
                      justify-center
                      text-center
                      text-white
                    "
                  >

                    <div
                      class="
                        flex
                        h-12
                        w-12
                        items-center
                        justify-center
                        rounded-full
                        bg-white/15
                        text-xl
                        backdrop-blur
                      "
                    >
                      🔒
                    </div>

                    <p class="mt-2 text-xs font-semibold">
                      Locked
                    </p>

                  </div>
                </div>


                <!-- Selected -->

                <div
                  v-if="
                    template.can_use &&
                    form.template === template.id
                  "
                  class="
                    absolute
                    right-3
                    top-3
                    flex
                    h-8
                    w-8
                    items-center
                    justify-center
                    rounded-full
                    bg-violet-500
                    text-sm
                    font-bold
                    text-white
                    shadow-lg
                  "
                >
                  ✓
                </div>

              </div>


              <!-- Template information -->

              <div class="p-4">

                <div
                  class="
                    flex
                    items-start
                    justify-between
                    gap-2
                  "
                >

                  <h3
                    class="
                      text-sm
                      font-semibold
                      text-slate-800
                    "
                  >
                    {{ template.name }}
                  </h3>


                  <span
                    class="
                      shrink-0
                      rounded-full
                      px-2.5
                      py-1
                      text-[10px]
                      font-semibold
                    "
                    :class="accessBadgeClass(template.access_level)"
                  >
                    {{ accessLabel(template.access_level) }}
                  </span>

                </div>


                <p
                  class="
                    mt-2
                    line-clamp-2
                    text-xs
                    leading-5
                    text-slate-400
                  "
                >
                  {{ template.description }}
                </p>


                <!-- Locked reason -->

                <div
                  v-if="!template.can_use"
                  class="
                    mt-3
                    flex
                    items-center
                    gap-1.5
                    text-[11px]
                    font-medium
                  "
                  :class="
                    template.lock_reason === 'verification'
                      ? 'text-emerald-600'
                      : template.lock_reason === 'subscription'
                        ? 'text-amber-600'
                        : 'text-slate-400'
                  "
                >

                  <span>
                    🔒
                  </span>

                  <span
                    v-if="
                      template.lock_reason === 'verification'
                    "
                  >
                    Verify email to unlock
                  </span>

                  <span
                    v-else-if="
                      template.lock_reason === 'subscription'
                    "
                  >
                    Premium required
                  </span>

                  <span v-else>
                    Currently unavailable
                  </span>

                </div>


                <!-- Available status -->

                <div
                  v-else
                  class="
                    mt-3
                    text-[11px]
                    font-medium
                    text-violet-500
                  "
                >
                  {{
                    form.template === template.id
                      ? 'Currently selected'
                      : 'Available'
                  }}
                </div>

              </div>

            </button>

          </div>


          <!-- No templates -->

          <div
            v-else
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
              No templates are currently available.
            </p>
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
            :disabled="saving"
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
            {{ saving ? 'Saving...' : 'Save Changes' }}
          </button>

        </div>

      </form>

    </main>
  </div>
</template>


<script setup>

import {
  onMounted,
  reactive,
  ref,
} from 'vue'

import {
  useRoute,
  useRouter,
} from 'vue-router'

import api from '../api/axios'


const route = useRoute()

const router = useRouter()


/*
 * Form
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
 * Page state
 */

const loadingPortfolio = ref(true)

const saving = ref(false)

const error = ref(null)


/*
 * Template helpers
 */

const accessLabel = (level) => {
  if (level === 'premium') {
    return 'Premium'
  }

  if (level === 'verified') {
    return 'Verified'
  }

  return 'Free'
}


const accessBadgeClass = (level) => {
  if (level === 'premium') {
    return 'bg-amber-100 text-amber-700'
  }

  if (level === 'verified') {
    return 'bg-emerald-100 text-emerald-700'
  }

  return 'bg-violet-50 text-violet-500'
}


/*
 * Select template
 */

const selectTemplate = (template) => {

  /*
   * Important:
   * Locked templates must NEVER modify
   * form.template.
   *
   * Backend also validates this again.
   */

  if (!template.can_use) {
    return
  }

  form.template = template.id

}


/*
 * Load portfolio
 */

const loadPortfolio = async () => {

  loadingPortfolio.value = true

  error.value = null

  try {

    const response = await api.get(
      `/portfolios/${route.params.id}/`
    )

    const portfolio = response.data

    form.title =
      portfolio.title || ''

    form.slug =
      portfolio.slug || ''

    form.bio =
      portfolio.bio || ''

    form.template =
      portfolio.template || null

  } catch (err) {

    console.error(
      'Failed to load portfolio:',
      err
    )

    error.value =
      err.response?.data?.detail ||
      'Unable to load your portfolio.'

  } finally {

    loadingPortfolio.value = false

  }

}


/*
 * Load templates
 */

const loadTemplates = async () => {

  templatesLoading.value = true

  try {

    const response = await api.get('/themes/')

    templates.value =
      Array.isArray(response.data)
        ? response.data
        : response.data.results || []


    /*
     * If the currently selected template is
     * no longer available to the user,
     * force the user to choose an available
     * template before saving.
     */

    if (form.template) {

      const currentTemplate =
        templates.value.find(
          (template) =>
            template.id === form.template
        )

      if (
        currentTemplate &&
        !currentTemplate.can_use
      ) {
        form.template = null
      }

    }

  } catch (err) {

    console.error(
      'Failed to load templates:',
      err
    )

    error.value =
      err.response?.data?.detail ||
      'Unable to load templates.'

  } finally {

    templatesLoading.value = false

  }

}


/*
 * Update portfolio
 */

const updatePortfolio = async () => {

  error.value = null


  /*
   * Basic validation
   */

  if (!form.title.trim()) {

    error.value =
      'Please enter a portfolio title.'

    return

  }


  if (!form.slug.trim()) {

    error.value =
      'Please enter a portfolio URL.'

    return

  }


  if (!form.template) {

    error.value =
      'Please choose an available template.'

    return

  }


  /*
   * Extra frontend safety check
   *
   * Never send a locked template.
   */

  const selectedTemplate =
    templates.value.find(
      (template) =>
        template.id === form.template
    )


  if (
    !selectedTemplate ||
    !selectedTemplate.can_use
  ) {

    error.value =
      'The selected template is not available for your account.'

    return

  }


  saving.value = true


  try {

    await api.patch(
      `/portfolios/${route.params.id}/`,
      {
        title:
          form.title.trim(),

        slug:
          form.slug.trim(),

        bio:
          form.bio.trim(),

        template:
          form.template,
      }
    )


    await router.push('/dashboard')

  } catch (err) {

    console.error(
      'Failed to update portfolio:',
      err
    )

    const data =
      err.response?.data


    if (
      data &&
      typeof data === 'object'
    ) {

      const firstError =
        Object.values(data)
          .flat()
          .find(Boolean)

      error.value =
        firstError ||
        'Unable to update your portfolio.'

    } else {

      error.value =
        'Unable to update your portfolio.'

    }

  } finally {

    saving.value = false

  }

}


/*
 * Initial load
 */

onMounted(async () => {

  /*
   * Portfolio must load first because
   * we need its current template before
   * checking template access.
   */

  await loadPortfolio()

  await loadTemplates()

})

</script>