<template>
  <div class="min-h-screen bg-stone-50 text-slate-800">

    <!-- Hero -->
    <header class="border-b border-slate-200 bg-white">
      <div class="mx-auto max-w-5xl px-6 py-16 sm:px-10">

        <p class="text-sm font-semibold uppercase tracking-[0.25em] text-slate-400">
          {{ portfolio.template_name || 'Professional Portfolio' }}
        </p>

        <h1 class="mt-5 max-w-4xl text-5xl font-black tracking-tight sm:text-7xl">
          {{ portfolio.title }}
        </h1>

        <p
          v-if="portfolio.bio"
          class="mt-6 max-w-3xl text-lg leading-8 text-slate-500"
        >
          {{ portfolio.bio }}
        </p>

        <div
          v-if="portfolio.social"
          class="mt-8 flex flex-wrap gap-3"
        >
          <a
            v-if="portfolio.social.sl_github"
            :href="portfolio.social.sl_github"
            target="_blank"
            rel="noreferrer"
            class="rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-semibold hover:bg-slate-50"
          >
            GitHub
          </a>

          <a
            v-if="portfolio.social.sl_linkedin"
            :href="portfolio.social.sl_linkedin"
            target="_blank"
            rel="noreferrer"
            class="rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-semibold hover:bg-slate-50"
          >
            LinkedIn
          </a>

          <a
            v-if="portfolio.social.sl_personal_web"
            :href="portfolio.social.sl_personal_web"
            target="_blank"
            rel="noreferrer"
            class="rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-semibold hover:bg-slate-50"
          >
            Website
          </a>
        </div>

      </div>
    </header>


    <main class="mx-auto max-w-5xl space-y-16 px-6 py-14 sm:px-10">


      <!-- Skills -->
      <section v-if="portfolio.skills?.length">

        <SectionHeading>
          Skills
        </SectionHeading>

        <div class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">

          <div
            v-for="skill in portfolio.skills"
            :key="skill.id"
            class="rounded-xl border border-slate-200 bg-white p-5"
          >

            <div class="flex items-center justify-between gap-4">

              <span class="font-semibold">
                {{ skill.skill_name }}
              </span>

              <span class="text-sm text-slate-400">
                {{ skill.skill_level_in_skill }}/5
              </span>

            </div>

            <div class="mt-4 h-2 overflow-hidden rounded-full bg-slate-100">

              <div
                class="h-full rounded-full bg-slate-800"
                :style="{
                  width: `${skill.skill_level_in_skill * 20}%`
                }"
              ></div>

            </div>

          </div>

        </div>

      </section>


      <!-- Experience -->
      <section v-if="portfolio.experiences?.length">

        <SectionHeading>
          Experience
        </SectionHeading>

        <div class="mt-6 space-y-8">

          <article
            v-for="item in portfolio.experiences"
            :key="item.id"
            class="grid gap-3 border-t border-slate-200 pt-6 sm:grid-cols-[180px_1fr]"
          >

            <div class="text-sm text-slate-400">
              {{ item.ex_start_date }}
              —
              {{ item.ex_end_date || 'Present' }}
            </div>

            <div>

              <h3 class="text-xl font-bold">
                {{ item.ex_position }}
              </h3>

              <p class="mt-1 font-medium text-slate-500">
                {{ item.ex_company }}
              </p>

              <p
                v-if="item.ex_description"
                class="mt-3 leading-7 text-slate-500"
              >
                {{ item.ex_description }}
              </p>

            </div>

          </article>

        </div>

      </section>


      <!-- Projects -->
      <section v-if="portfolio.projects?.length">

        <SectionHeading>
          Projects
        </SectionHeading>

        <div class="mt-6 grid gap-5 md:grid-cols-2">

          <article
            v-for="project in portfolio.projects"
            :key="project.id"
            class="rounded-2xl border border-slate-200 bg-white p-6"
          >

            <div class="flex items-start justify-between gap-4">

              <h3 class="text-xl font-bold">
                {{ project.pro_name }}
              </h3>

              <span
                v-if="project.pro_start"
                class="text-xs text-slate-400"
              >
                {{ project.pro_start }}
              </span>

            </div>

            <p
              v-if="project.pro_description"
              class="mt-4 leading-7 text-slate-500"
            >
              {{ project.pro_description }}
            </p>

            <p
              v-if="project.pro_techs"
              class="mt-4 text-sm font-semibold text-slate-700"
            >
              {{ project.pro_techs }}
            </p>

            <div class="mt-6 flex flex-wrap gap-4 text-sm font-semibold">

              <a
                v-if="project.pro_github_url"
                :href="project.pro_github_url"
                target="_blank"
                rel="noreferrer"
                class="hover:underline"
              >
                GitHub ↗
              </a>

              <a
                v-if="project.pro_live_demo_url"
                :href="project.pro_live_demo_url"
                target="_blank"
                rel="noreferrer"
                class="hover:underline"
              >
                Live Demo ↗
              </a>

            </div>

          </article>

        </div>

      </section>


      <!-- Education -->
      <section v-if="portfolio.educations?.length">

        <SectionHeading>
          Education
        </SectionHeading>

        <div class="mt-6 space-y-3">

          <div
            v-for="item in portfolio.educations"
            :key="item.id"
            class="border-l-2 border-slate-800 bg-white px-5 py-4"
          >
            <p class="font-semibold">
              {{ item.edu }}
            </p>
          </div>

        </div>

      </section>

    </main>


    <footer class="border-t border-slate-200 bg-white">
      <div class="mx-auto max-w-5xl px-6 py-8 text-center text-xs text-slate-400">
        {{ portfolio.title }}
      </div>
    </footer>

  </div>
</template>


<script setup>

import SectionHeading from './SectionHeading.vue'

defineProps({
  portfolio: {
    type: Object,
    required: true,
  },
})

</script>