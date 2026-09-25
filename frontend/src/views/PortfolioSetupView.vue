<template>

  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">

    <main class="mx-auto max-w-6xl px-6 py-8">

      <!-- Header -->

      <div class="mb-8">

        <button
          type="button"
          class="mb-5 text-sm font-medium text-slate-400 transition hover:text-violet-500"
          @click="goBack"
        >
          ← Back
        </button>

        <p class="text-sm font-medium text-violet-400">
          Portfolio setup
        </p>

        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          Complete your portfolio
        </h1>

        <p class="mt-2 text-sm text-slate-400">
          Add your skills, education, experience, projects and social links.
        </p>

      </div>


      <!-- Progress -->

      <div class="mb-8 overflow-x-auto">

        <div class="flex min-w-max gap-2">

          <button
            v-for="item in steps"
            :key="item.number"
            type="button"
            class="rounded-full px-4 py-2 text-xs font-semibold transition"
            :class="
              currentStep === item.number
                ? 'bg-violet-400 text-white'
                : currentStep > item.number
                  ? 'bg-violet-100 text-violet-600'
                  : 'bg-white text-slate-400'
            "
            @click="goToStep(item.number)"
          >
            {{ item.number }}. {{ item.title }}
          </button>

        </div>

      </div>


      <!-- Loading -->

      <div
        v-if="pageLoading"
        class="rounded-[28px] border border-violet-100 bg-white p-10 text-center shadow-sm"
      >

        <p class="text-sm text-slate-400">
          Loading your portfolio...
        </p>

      </div>


      <!-- Main -->

      <div
        v-else
        class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm"
      >

        <!-- ========================= -->
        <!-- SKILLS -->
        <!-- ========================= -->

        <section v-if="currentStep === 2">

          <StepHeader
            title="Your skills"
            description="Add the technologies and skills you want to showcase."
          />


          <div class="grid gap-6 lg:grid-cols-[1fr_1.2fr]">

            <!-- Form -->

            <form
              class="rounded-2xl bg-slate-50 p-5"
              @submit.prevent="addSkill"
            >

              <label class="block text-sm font-semibold text-slate-700">
                Skill name
              </label>

              <input
                v-model="skillForm.skill_name"
                type="text"
                placeholder="e.g. Django"
                class="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
              />


              <label class="mt-5 block text-sm font-semibold text-slate-700">
                Skill level
              </label>

              <select
                v-model.number="skillForm.skill_level_in_skill"
                class="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
              >

                <option :value="1">1 / 5</option>
                <option :value="2">2 / 5</option>
                <option :value="3">3 / 5</option>
                <option :value="4">4 / 5</option>
                <option :value="5">5 / 5</option>

              </select>


              <button
                type="submit"
                :disabled="actionLoading"
                class="mt-5 w-full rounded-full bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500 disabled:opacity-60"
              >
                + Add Skill
              </button>

            </form>


            <!-- Existing -->

            <div>

              <div
                v-if="skills.length === 0"
                class="rounded-2xl border border-dashed border-slate-200 p-8 text-center"
              >
                <p class="text-sm text-slate-400">
                  No skills added yet.
                </p>
              </div>


              <div
                v-else
                class="space-y-3"
              >

                <div
                  v-for="skill in skills"
                  :key="skill.id"
                  class="flex items-center justify-between rounded-2xl border border-slate-100 p-4"
                >

                  <div>

                    <p class="font-semibold text-slate-800">
                      {{ skill.skill_name }}
                    </p>

                    <p class="mt-1 text-xs text-slate-400">
                      Level {{ skill.skill_level_in_skill }} / 5
                    </p>

                  </div>

                  <button
                    type="button"
                    class="text-xs font-semibold text-red-400 hover:text-red-500"
                    @click="deleteItem('skills', skill.id)"
                  >
                    Remove
                  </button>

                </div>

              </div>

            </div>

          </div>

        </section>


        <!-- ========================= -->
        <!-- EDUCATION -->
        <!-- ========================= -->

        <section v-else-if="currentStep === 3">

          <StepHeader
            title="Education"
            description="Add your education history."
          />


          <form
            class="mb-6 rounded-2xl bg-slate-50 p-5"
            @submit.prevent="addEducation"
          >

            <label class="block text-sm font-semibold text-slate-700">
              Education
            </label>

            <input
              v-model="educationForm.edu"
              type="text"
              placeholder="e.g. B.Sc. Computer Engineering — University of Tehran"
              class="mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
            />

            <button
              type="submit"
              :disabled="actionLoading"
              class="mt-5 rounded-full bg-violet-400 px-6 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60"
            >
              + Add Education
            </button>

          </form>


          <div
            v-if="educations.length === 0"
            class="rounded-2xl border border-dashed border-slate-200 p-8 text-center"
          >
            <p class="text-sm text-slate-400">
              No education added yet.
            </p>
          </div>


          <div v-else class="space-y-3">

            <div
              v-for="education in educations"
              :key="education.id"
              class="flex items-center justify-between rounded-2xl border border-slate-100 p-4"
            >

              <p class="font-semibold text-slate-800">
                {{ education.edu }}
              </p>

              <button
                type="button"
                class="text-xs font-semibold text-red-400 hover:text-red-500"
                @click="deleteItem('educations', education.id)"
              >
                Remove
              </button>

            </div>

          </div>

        </section>


        <!-- ========================= -->
        <!-- EXPERIENCE -->
        <!-- ========================= -->

        <section v-else-if="currentStep === 4">

          <StepHeader
            title="Experience"
            description="Tell visitors about your professional experience."
          />


          <form
            class="rounded-2xl bg-slate-50 p-5"
            @submit.prevent="addExperience"
          >

            <div class="grid gap-5 md:grid-cols-2">

              <Field
                v-model="experienceForm.ex_company"
                label="Company"
                placeholder="e.g. Acme Inc."
              />

              <Field
                v-model="experienceForm.ex_position"
                label="Position"
                placeholder="e.g. Backend Developer"
              />

              <Field
                v-model="experienceForm.ex_start_date"
                label="Start date"
                type="date"
              />

              <Field
                v-model="experienceForm.ex_end_date"
                label="End date"
                type="date"
              />

            </div>


            <label class="mt-5 block text-sm font-semibold text-slate-700">
              Description
            </label>

            <textarea
              v-model="experienceForm.ex_description"
              rows="4"
              placeholder="Describe your responsibilities..."
              class="mt-2 w-full resize-none rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
            />


            <button
              type="submit"
              :disabled="actionLoading"
              class="mt-5 rounded-full bg-violet-400 px-6 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60"
            >
              + Add Experience
            </button>

          </form>


          <div class="mt-6 space-y-3">

            <div
              v-for="experience in experiences"
              :key="experience.id"
              class="rounded-2xl border border-slate-100 p-5"
            >

              <div class="flex items-start justify-between gap-4">

                <div>

                  <p class="font-semibold text-slate-800">
                    {{ experience.ex_position }}
                  </p>

                  <p class="mt-1 text-sm text-violet-500">
                    {{ experience.ex_company }}
                  </p>

                  <p class="mt-1 text-xs text-slate-400">
                    {{ experience.ex_start_date }}
                    →
                    {{ experience.ex_end_date || 'Present' }}
                  </p>

                </div>

                <button
                  type="button"
                  class="text-xs font-semibold text-red-400"
                  @click="deleteItem('experiences', experience.id)"
                >
                  Remove
                </button>

              </div>

              <p
                v-if="experience.ex_description"
                class="mt-4 text-sm leading-6 text-slate-500"
              >
                {{ experience.ex_description }}
              </p>

            </div>

          </div>

        </section>


        <!-- ========================= -->
        <!-- PROJECTS -->
        <!-- ========================= -->

        <section v-else-if="currentStep === 5">

          <StepHeader
            title="Projects"
            description="Showcase the projects you are proud of."
          />


          <form
            class="rounded-2xl bg-slate-50 p-5"
            @submit.prevent="addProject"
          >

            <div class="grid gap-5 md:grid-cols-2">

              <Field
                v-model="projectForm.pro_name"
                label="Project name"
                placeholder="e.g. Portfolio SaaS"
              />

              <Field
                v-model="projectForm.pro_github_url"
                label="GitHub URL"
                placeholder="https://github.com/..."
              />

              <Field
                v-model="projectForm.pro_live_demo_url"
                label="Live demo URL"
                placeholder="https://..."
              />

              <Field
                v-model="projectForm.pro_techs"
                label="Technologies"
                placeholder="Django, Vue, PostgreSQL"
              />

              <Field
                v-model="projectForm.pro_start"
                label="Start date"
                type="date"
              />

              <Field
                v-model="projectForm.pro_end"
                label="End date"
                type="date"
              />

            </div>


            <label class="mt-5 block text-sm font-semibold text-slate-700">
              Description
            </label>

            <textarea
              v-model="projectForm.pro_description"
              rows="4"
              placeholder="Describe the project..."
              class="mt-2 w-full resize-none rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
            />


            <button
              type="submit"
              :disabled="actionLoading"
              class="mt-5 rounded-full bg-violet-400 px-6 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60"
            >
              + Add Project
            </button>

          </form>


          <div class="mt-6 grid gap-4 lg:grid-cols-2">

            <div
              v-for="project in projects"
              :key="project.id"
              class="rounded-2xl border border-slate-100 p-5"
            >

              <div class="flex items-start justify-between gap-4">

                <div>

                  <h3 class="font-semibold text-slate-800">
                    {{ project.pro_name }}
                  </h3>

                  <p class="mt-1 text-xs text-violet-500">
                    {{ project.pro_techs }}
                  </p>

                </div>

                <button
                  type="button"
                  class="text-xs font-semibold text-red-400"
                  @click="deleteItem('projects', project.id)"
                >
                  Remove
                </button>

              </div>

              <p
                v-if="project.pro_description"
                class="mt-4 text-sm leading-6 text-slate-500"
              >
                {{ project.pro_description }}
              </p>

            </div>

          </div>

        </section>


        <!-- ========================= -->
        <!-- SOCIAL -->
        <!-- ========================= -->

        <section v-else-if="currentStep === 6">

          <StepHeader
            title="Social links"
            description="Connect your professional profiles."
          />


          <form
            class="rounded-2xl bg-slate-50 p-5"
            @submit.prevent="saveSocial"
          >

            <Field
              v-model="socialForm.sl_github"
              label="GitHub"
              placeholder="https://github.com/username"
            />

            <Field
              v-model="socialForm.sl_linkedin"
              label="LinkedIn"
              placeholder="https://linkedin.com/in/username"
              class="mt-5"
            />

            <Field
              v-model="socialForm.sl_personal_web"
              label="Personal website"
              placeholder="https://example.com"
              class="mt-5"
            />


            <button
              type="submit"
              :disabled="actionLoading"
              class="mt-5 rounded-full bg-violet-400 px-6 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60"
            >
              {{ socialExists ? 'Update Social Links' : 'Save Social Links' }}
            </button>

          </form>

        </section>


        <!-- Error -->

        <div
          v-if="error"
          class="mt-6 rounded-2xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
        >
          {{ error }}
        </div>


        <!-- Navigation -->

        <div class="mt-8 flex flex-col gap-3 border-t border-slate-100 pt-6 sm:flex-row sm:justify-between">

          <button
            type="button"
            class="rounded-full px-6 py-3 text-sm font-semibold text-slate-500 hover:bg-slate-50"
            @click="previousStep"
          >
            ← Previous
          </button>


          <button
            v-if="currentStep < 6"
            type="button"
            class="rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 hover:bg-violet-500"
            @click="nextStep"
          >
            Continue →
          </button>


          <button
            v-else
            type="button"
            class="rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 hover:bg-violet-500"
            @click="finishSetup"
          >
            Finish Portfolio ✓
          </button>

        </div>

      </div>

    </main>

  </div>

</template>


<script setup>

import {
  computed,
  defineComponent,
  h,
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


const portfolioId = route.params.id


const steps = [
  { number: 2, title: 'Skills' },
  { number: 3, title: 'Education' },
  { number: 4, title: 'Experience' },
  { number: 5, title: 'Projects' },
  { number: 6, title: 'Social' },
]


const currentStep = ref(2)

const pageLoading = ref(true)
const actionLoading = ref(false)
const error = ref(null)


const skills = ref([])
const educations = ref([])
const experiences = ref([])
const projects = ref([])
const social = ref(null)


const skillForm = reactive({
  skill_name: '',
  skill_level_in_skill: 3,
})


const educationForm = reactive({
  edu: '',
})


const experienceForm = reactive({
  ex_company: '',
  ex_start_date: '',
  ex_end_date: '',
  ex_position: '',
  ex_description: '',
})


const projectForm = reactive({
  pro_name: '',
  pro_description: '',
  pro_image: '',
  pro_github_url: '',
  pro_techs: '',
  pro_live_demo_url: '',
  pro_start: '',
  pro_end: '',
})


const socialForm = reactive({
  sl_github: '',
  sl_linkedin: '',
  sl_personal_web: '',
})


const socialExists = computed(() => {
  return !!social.value
})


const apiPaths = {
  skills: `/portfolios/${portfolioId}/skills/`,
  educations: `/portfolios/${portfolioId}/educations/`,
  experiences: `/portfolios/${portfolioId}/experiences/`,
  projects: `/portfolios/${portfolioId}/projects/`,
  social: `/portfolios/${portfolioId}/social-links/`,
}


const getList = async (key) => {

  const response = await api.get(apiPaths[key])

  return Array.isArray(response.data)
    ? response.data
    : response.data.results || []

}


const loadData = async () => {

  pageLoading.value = true
  error.value = null

  try {

    skills.value = await getList('skills')
    educations.value = await getList('educations')
    experiences.value = await getList('experiences')
    projects.value = await getList('projects')


    try {

      const response = await api.get(
        apiPaths.social
      )

      social.value = response.data

      socialForm.sl_github =
        response.data.sl_github || ''

      socialForm.sl_linkedin =
        response.data.sl_linkedin || ''

      socialForm.sl_personal_web =
        response.data.sl_personal_web || ''

    } catch (socialError) {

      if (socialError.response?.status === 404) {
        social.value = null
      } else {
        throw socialError
      }

    }

  } catch (err) {

    console.error(
      'Failed to load portfolio setup:',
      err
    )

    error.value =
      err.response?.data?.detail ||
      'Unable to load portfolio setup.'

  } finally {

    pageLoading.value = false

  }

}


const resetSkillForm = () => {

  skillForm.skill_name = ''
  skillForm.skill_level_in_skill = 3

}


const resetEducationForm = () => {

  educationForm.edu = ''

}


const resetExperienceForm = () => {

  experienceForm.ex_company = ''
  experienceForm.ex_start_date = ''
  experienceForm.ex_end_date = ''
  experienceForm.ex_position = ''
  experienceForm.ex_description = ''

}


const resetProjectForm = () => {

  projectForm.pro_name = ''
  projectForm.pro_description = ''
  projectForm.pro_image = ''
  projectForm.pro_github_url = ''
  projectForm.pro_techs = ''
  projectForm.pro_live_demo_url = ''
  projectForm.pro_start = ''
  projectForm.pro_end = ''

}


const handleApiError = (err, fallback) => {

  console.error(err)

  const data = err.response?.data

  if (data && typeof data === 'object') {

    const firstError = Object.values(data)
      .flat()
      .find(Boolean)

    error.value = firstError || fallback

  } else {

    error.value = fallback

  }

}


const addSkill = async () => {

  error.value = null

  if (!skillForm.skill_name.trim()) {
    error.value = 'Please enter a skill name.'
    return
  }

  actionLoading.value = true

  try {

    const response = await api.post(
      apiPaths.skills,
      {
        skill_name: skillForm.skill_name.trim(),
        skill_level_in_skill:
          skillForm.skill_level_in_skill,
      }
    )

    skills.value.push(response.data)

    resetSkillForm()

  } catch (err) {

    handleApiError(
      err,
      'Unable to add this skill.'
    )

  } finally {

    actionLoading.value = false

  }

}


const addEducation = async () => {

  error.value = null

  if (!educationForm.edu.trim()) {
    error.value = 'Please enter your education.'
    return
  }

  actionLoading.value = true

  try {

    const response = await api.post(
      apiPaths.educations,
      {
        edu: educationForm.edu.trim(),
      }
    )

    educations.value.push(response.data)

    resetEducationForm()

  } catch (err) {

    handleApiError(
      err,
      'Unable to add this education.'
    )

  } finally {

    actionLoading.value = false

  }

}


const addExperience = async () => {

  error.value = null

  if (!experienceForm.ex_company.trim()) {
    error.value = 'Please enter the company name.'
    return
  }

  if (!experienceForm.ex_position.trim()) {
    error.value = 'Please enter your position.'
    return
  }

  if (!experienceForm.ex_start_date) {
    error.value = 'Please select a start date.'
    return
  }

  actionLoading.value = true

  try {

    const response = await api.post(
      apiPaths.experiences,
      {
        ex_company:
          experienceForm.ex_company.trim(),

        ex_start_date:
          experienceForm.ex_start_date,

        ex_end_date:
          experienceForm.ex_end_date || null,

        ex_position:
          experienceForm.ex_position.trim(),

        ex_description:
          experienceForm.ex_description.trim(),
      }
    )

    experiences.value.push(response.data)

    resetExperienceForm()

  } catch (err) {

    handleApiError(
      err,
      'Unable to add this experience.'
    )

  } finally {

    actionLoading.value = false

  }

}


const addProject = async () => {

  error.value = null

  if (!projectForm.pro_name.trim()) {
    error.value = 'Please enter the project name.'
    return
  }

  if (!projectForm.pro_github_url.trim()) {
    error.value = 'Please enter the GitHub URL.'
    return
  }

  if (!projectForm.pro_techs.trim()) {
    error.value = 'Please enter the technologies.'
    return
  }

  if (!projectForm.pro_start) {
    error.value = 'Please select the project start date.'
    return
  }

  actionLoading.value = true

  try {

    const response = await api.post(
      apiPaths.projects,
      {
        pro_name:
          projectForm.pro_name.trim(),

        pro_description:
          projectForm.pro_description.trim(),

        pro_image:
          projectForm.pro_image.trim() || null,

        pro_github_url:
          projectForm.pro_github_url.trim(),

        pro_techs:
          projectForm.pro_techs.trim(),

        pro_live_demo_url:
          projectForm.pro_live_demo_url.trim() || null,

        pro_start:
          projectForm.pro_start,

        pro_end:
          projectForm.pro_end || null,
      }
    )

    projects.value.push(response.data)

    resetProjectForm()

  } catch (err) {

    handleApiError(
      err,
      'Unable to add this project.'
    )

  } finally {

    actionLoading.value = false

  }

}


const saveSocial = async () => {

  error.value = null

  actionLoading.value = true

  try {

    const payload = {
      sl_github:
        socialForm.sl_github.trim() || null,

      sl_linkedin:
        socialForm.sl_linkedin.trim() || null,

      sl_personal_web:
        socialForm.sl_personal_web.trim() || null,
    }


    if (social.value) {

      const response = await api.patch(
        `${apiPaths.social}${social.value.id}/`,
        payload
      )

      social.value = response.data

    } else {

      const response = await api.post(
        apiPaths.social,
        payload
      )

      social.value = response.data

    }

  } catch (err) {

    handleApiError(
      err,
      'Unable to save social links.'
    )

  } finally {

    actionLoading.value = false

  }

}


const deleteItem = async (type, id) => {

  error.value = null
  actionLoading.value = true

  try {

    await api.delete(
      `${apiPaths[type]}${id}/`
    )

    if (type === 'skills') {
      skills.value =
        skills.value.filter(item => item.id !== id)
    }

    if (type === 'educations') {
      educations.value =
        educations.value.filter(item => item.id !== id)
    }

    if (type === 'experiences') {
      experiences.value =
        experiences.value.filter(item => item.id !== id)
    }

    if (type === 'projects') {
      projects.value =
        projects.value.filter(item => item.id !== id)
    }

  } catch (err) {

    handleApiError(
      err,
      'Unable to remove this item.'
    )

  } finally {

    actionLoading.value = false

  }

}


const goToStep = (step) => {

  if (step < 2 || step > 6) {
    return
  }

  currentStep.value = step
  error.value = null

}


const nextStep = () => {

  if (currentStep.value < 6) {
    currentStep.value += 1
    error.value = null
  }

}


const previousStep = () => {

  if (currentStep.value > 2) {
    currentStep.value -= 1
    error.value = null
    return
  }

  goBack()

}


const goBack = () => {

  router.push('/dashboard')

}


const finishSetup = async () => {

  error.value = null

  await router.push('/dashboard')

}


onMounted(() => {

  if (!portfolioId) {

    router.replace('/dashboard')
    return

  }

  loadData()

})


/*
 * کوچک‌ترین کامپوننت‌های موردنیاز فرم
 */

const StepHeader = defineComponent({
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  },

  setup(props) {

    return () =>
      h(
        'div',
        { class: 'mb-8' },
        [
          h(
            'h2',
            {
              class:
                'text-2xl font-bold text-slate-900',
            },
            props.title
          ),

          h(
            'p',
            {
              class:
                'mt-2 text-sm text-slate-400',
            },
            props.description
          ),
        ]
      )

  },
})


const Field = defineComponent({
  props: {
    modelValue: {
      type: String,
      default: '',
    },

    label: {
      type: String,
      required: true,
    },

    placeholder: {
      type: String,
      default: '',
    },

    type: {
      type: String,
      default: 'text',
    },

    class: {
      type: String,
      default: '',
    },
  },

  emits: ['update:modelValue'],

  setup(props, { emit }) {

    return () =>
      h(
        'div',
        { class: props.class },
        [
          h(
            'label',
            {
              class:
                'block text-sm font-semibold text-slate-700',
            },
            props.label
          ),

          h(
            'input',
            {
              type: props.type,
              value: props.modelValue,
              placeholder: props.placeholder,

              class:
                'mt-2 w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-50',

              onInput: event =>
                emit(
                  'update:modelValue',
                  event.target.value
                ),
            }
          ),
        ]
      )

  },
})

</script>