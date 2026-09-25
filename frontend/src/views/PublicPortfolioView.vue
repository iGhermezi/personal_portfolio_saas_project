<template>

  <div class="min-h-screen bg-[#faf9ff]">

    <!-- Loading -->

    <div
      v-if="loading"
      class="
        flex
        min-h-screen
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
        flex
        min-h-screen
        items-center
        justify-center
        px-6
        text-center
      "
    >

      <div>

        <div
          class="
            mx-auto
            flex
            h-16
            w-16
            items-center
            justify-center
            rounded-2xl
            bg-red-50
            text-2xl
          "
        >
          !
        </div>

        <h1
          class="
            mt-5
            text-2xl
            font-bold
            text-slate-800
          "
        >
          Portfolio not available
        </h1>

        <p class="mt-2 text-sm text-slate-400">
          {{ error }}
        </p>

      </div>

    </div>


    <!-- Portfolio -->

    <main
      v-else-if="portfolio"
      class="mx-auto max-w-6xl px-6 py-10 sm:py-16"
    >

      <!-- Hero -->

      <section
        class="
          overflow-hidden
          rounded-[32px]
          border
          border-violet-100
          bg-white
          shadow-sm
        "
      >

        <div
          class="
            bg-gradient-to-br
            from-violet-50
            via-white
            to-indigo-50
            px-7
            py-20
            text-center
            sm:px-12
          "
        >

          <div
            class="
              mx-auto
              flex
              h-20
              w-20
              items-center
              justify-center
              rounded-3xl
              bg-violet-100
              text-3xl
              text-violet-500
            "
          >
            ✦
          </div>

          <h1
            class="
              mx-auto
              mt-7
              max-w-4xl
              text-4xl
              font-bold
              tracking-tight
              text-slate-900
              sm:text-5xl
            "
          >
            {{ portfolio.title }}
          </h1>

          <p
            v-if="portfolio.bio"
            class="
              mx-auto
              mt-6
              max-w-2xl
              text-base
              leading-7
              text-slate-500
            "
          >
            {{ portfolio.bio }}
          </p>

        </div>


        <!-- Content -->

        <div class="space-y-14 px-7 py-12 sm:px-12">


          <!-- Skills -->

          <section v-if="portfolio.skills?.length">

            <h2 class="text-2xl font-bold text-slate-800">
              Skills
            </h2>

            <div
              class="
                mt-6
                flex
                flex-wrap
                gap-3
              "
            >

              <div
                v-for="skill in portfolio.skills"
                :key="skill.id"
                class="
                  rounded-full
                  border
                  border-violet-100
                  bg-violet-50
                  px-5
                  py-2.5
                  text-sm
                  font-medium
                  text-violet-600
                "
              >
                {{ skill.skill_name }}
                ·
                {{ skill.skill_level_in_skill }}/5
              </div>

            </div>

          </section>


          <!-- Education -->

          <section v-if="portfolio.educations?.length">

            <h2 class="text-2xl font-bold text-slate-800">
              Education
            </h2>

            <div class="mt-6 space-y-3">

              <div
                v-for="education in portfolio.educations"
                :key="education.id"
                class="
                  rounded-2xl
                  border
                  border-slate-100
                  bg-slate-50
                  p-5
                "
              >
                <p class="text-sm font-semibold text-slate-700">
                  {{ education.edu }}
                </p>
              </div>

            </div>

          </section>


          <!-- Experience -->

          <section v-if="portfolio.experiences?.length">

            <h2 class="text-2xl font-bold text-slate-800">
              Experience
            </h2>

            <div class="mt-6 space-y-5">

              <article
                v-for="experience in portfolio.experiences"
                :key="experience.id"
                class="
                  rounded-2xl
                  border
                  border-slate-100
                  bg-slate-50
                  p-6
                "
              >

                <h3 class="text-lg font-bold text-slate-800">
                  {{ experience.ex_position }}
                </h3>

                <p class="mt-1 text-sm font-medium text-violet-500">
                  {{ experience.ex_company }}
                </p>

                <p class="mt-3 text-xs text-slate-400">
                  {{ experience.ex_start_date }}
                  →
                  {{ experience.ex_end_date || 'Present' }}
                </p>

                <p
                  v-if="experience.ex_description"
                  class="
                    mt-4
                    text-sm
                    leading-6
                    text-slate-500
                  "
                >
                  {{ experience.ex_description }}
                </p>

              </article>

            </div>

          </section>


          <!-- Projects -->

          <section v-if="portfolio.projects?.length">

            <h2 class="text-2xl font-bold text-slate-800">
              Projects
            </h2>

            <div
              class="
                mt-6
                grid
                gap-5
                md:grid-cols-2
              "
            >

              <article
                v-for="project in portfolio.projects"
                :key="project.id"
                class="
                  rounded-2xl
                  border
                  border-slate-100
                  bg-slate-50
                  p-6
                "
              >

                <h3 class="text-lg font-bold text-slate-800">
                  {{ project.pro_name }}
                </h3>

                <p
                  v-if="project.pro_description"
                  class="
                    mt-3
                    text-sm
                    leading-6
                    text-slate-500
                  "
                >
                  {{ project.pro_description }}
                </p>

                <p
                  v-if="project.pro_techs"
                  class="
                    mt-4
                    text-xs
                    font-medium
                    text-slate-400
                  "
                >
                  {{ project.pro_techs }}
                </p>

                <div class="mt-5 flex gap-3">

                  <a
                    :href="project.pro_github_url"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="
                      rounded-full
                      bg-slate-900
                      px-4
                      py-2
                      text-xs
                      font-semibold
                      text-white
                    "
                  >
                    GitHub
                  </a>

                  <a
                    v-if="project.pro_live_demo_url"
                    :href="project.pro_live_demo_url"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="
                      rounded-full
                      bg-violet-100
                      px-4
                      py-2
                      text-xs
                      font-semibold
                      text-violet-600
                    "
                  >
                    Live Demo
                  </a>

                </div>

              </article>

            </div>

          </section>


          <!-- Social -->

          <section v-if="portfolio.social">

            <h2 class="text-2xl font-bold text-slate-800">
              Connect
            </h2>

            <div class="mt-6 flex flex-wrap gap-3">

              <a
                v-if="portfolio.social.sl_github"
                :href="portfolio.social.sl_github"
                target="_blank"
                rel="noopener noreferrer"
                class="
                  rounded-full
                  border
                  border-slate-200
                  bg-white
                  px-5
                  py-2.5
                  text-sm
                  font-medium
                  text-slate-600
                "
              >
                GitHub
              </a>

              <a
                v-if="portfolio.social.sl_linkedin"
                :href="portfolio.social.sl_linkedin"
                target="_blank
                "
                rel="noopener noreferrer"
                class="
                  rounded-full
                  border
                  border-slate-200
                  bg-white
                  px-5
                  py-2.5
                  text-sm
                  font-medium
                  text-slate-600
                "
              >
                LinkedIn
              </a>

              <a
                v-if="portfolio.social.sl_personal_web"
                :href="portfolio.social.sl_personal_web"
                target="_blank"
                rel="noopener noreferrer"
                class="
                  rounded-full
                  border
                  border-slate-200
                  bg-white
                  px-5
                  py-2.5
                  text-sm
                  font-medium
                  text-slate-600
                "
              >
                Website
              </a>

            </div>

          </section>

        </div>

      </section>


      <footer class="py-8 text-center">

        <p class="text-xs text-slate-400">
          Built with Personal Portfolio SaaS
        </p>

      </footer>

    </main>

  </div>

</template>


<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import api from '../api/axios'


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

    console.error(
      'Failed to load public portfolio:',
      err
    )

    error.value =
      err.response?.data?.detail ||
      'This portfolio is not available.'

  } finally {

    loading.value = false

  }

}


onMounted(() => {

  loadPortfolio()

})

</script>