<template>
  <main class="min-h-screen bg-[#171717] px-4 py-8 text-white sm:px-6 lg:px-10">
    <div
      class="mx-auto max-w-5xl overflow-hidden border-y-4 border-[#10b981] bg-[#1d1d1d] shadow-[0_0_45px_rgba(16,185,129,0.10)]"
    >
      <!-- Hero / CV header -->
      <section
        class="grid gap-8 p-6 sm:p-8 md:grid-cols-[230px_1fr] md:gap-10 md:p-10"
      >
        <!-- Temporary photo placeholder -->
        <div
          class="mx-auto flex h-[330px] w-[210px] items-center justify-center rounded-[2rem] border-4 border-[#10b981] bg-[#111111] shadow-[0_0_25px_rgba(16,185,129,0.16)] md:mx-0 md:h-[360px] md:w-[220px]"
        >
          <div class="text-center">
            <div class="text-7xl font-light leading-none text-[#10b981]">★</div>
            <p
              class="mt-4 text-xs font-bold uppercase tracking-[0.28em] text-[#6ee7b7]"
            >
              {{ i18nStore.t("portfolioTemplate.photo") }}
            </p>
          </div>
        </div>

        <div class="flex flex-col justify-center">
          <p
            class="font-['Brush_Script_MT','Segoe_Script',cursive] text-5xl italic leading-none text-[#10b981] sm:text-6xl"
          >
            {{ i18nStore.t("portfolioTemplate.hello") }}
          </p>

          <h1
            class="mt-2 text-4xl font-black tracking-tight text-white sm:text-5xl"
          >
            {{ i18nStore.t("portfolioTemplate.introPrefix") }}
            {{ portfolio.title || i18nStore.t("portfolioTemplate.yourName") }}
          </h1>

          <div class="mt-4 h-px w-full bg-[#10b981]" />

          <p
            v-if="portfolio.bio"
            class="mt-5 max-w-2xl text-sm leading-6 text-[#c7d1cc] sm:text-[15px]"
          >
            {{ portfolio.bio }}
          </p>
          <p
            v-else
            class="mt-5 max-w-2xl text-sm leading-6 text-[#8fa39a] sm:text-[15px]"
          >
            {{ i18nStore.t("portfolioTemplate.intro") }}
          </p>

          <div
            class="mt-6 flex flex-wrap gap-2 text-xs font-bold uppercase tracking-wider text-[#6ee7b7]"
          >
            <span
              class="rounded-full border border-[#065f46] bg-[#10251d] px-3 py-1"
              >{{ i18nStore.t("portfolioTemplate.portfolio") }}</span
            >
            <span
              v-if="portfolio.job_title"
              class="rounded-full border border-[#065f46] bg-[#10251d] px-3 py-1"
            >
              {{ portfolio.job_title }}
            </span>
            <span
              v-if="portfolio.location"
              class="rounded-full border border-[#065f46] bg-[#10251d] px-3 py-1"
            >
              {{ portfolio.location }}
            </span>
          </div>
        </div>
      </section>

      <!-- Education / Tools -->
      <section class="grid border-t border-[#24443a] md:grid-cols-2">
        <div
          class="border-b border-[#24443a] p-6 sm:p-8 md:border-b-0 md:border-r"
        >
          <h2 class="text-2xl font-bold text-[#10b981]">
            {{ i18nStore.t("portfolioTemplate.education") }}
          </h2>
          <div class="mt-4 space-y-3">
            <div
              v-for="item in portfolio.educations || []"
              :key="item.id"
              class="border-l-2 border-[#10b981] pl-4"
            >
              <p class="text-sm leading-6 text-[#d1d5d3]">{{ item.edu }}</p>
            </div>

            <p
              v-if="!portfolio.educations?.length"
              class="text-sm text-[#7f9189]"
            >
              {{ i18nStore.t("portfolioTemplate.educationPlaceholder") }}
            </p>
          </div>
        </div>

        <div class="p-6 sm:p-8">
          <h2 class="text-2xl font-bold text-[#10b981]">
            {{ i18nStore.t("portfolioTemplate.tools") }}
          </h2>
          <div
            class="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-2 lg:grid-cols-3"
          >
            <div
              v-for="skill in portfolio.skills || []"
              :key="skill.id"
              class="rounded-lg border border-[#285244] bg-[#151c19] px-3 py-3"
            >
              <div class="flex items-center justify-between gap-2">
                <span class="text-sm font-semibold text-white">{{
                  skill.skill_name
                }}</span>
                <span class="text-xs font-bold text-[#34d399]">
                  {{ skill.skill_level_in_skill }}/5
                </span>
              </div>
            </div>

            <p
              v-if="!portfolio.skills?.length"
              class="col-span-full text-sm text-[#7f9189]"
            >
              {{ i18nStore.t("portfolioTemplate.skillsPlaceholder") }}
            </p>
          </div>
        </div>
      </section>

      <!-- Contact -->
      <section class="border-t border-[#24443a] p-6 sm:p-8">
        <h2 class="text-2xl font-bold text-[#10b981]">
          {{ i18nStore.t("portfolioTemplate.contact") }}
        </h2>

        <div class="mt-5 grid gap-3 text-sm sm:grid-cols-2">
          <a
            v-if="portfolio.email"
            :href="`mailto:${portfolio.email}`"
            class="break-all text-[#d1d5d3] transition hover:text-[#34d399]"
          >
            <span class="mr-2 text-[#10b981]">●</span>{{ portfolio.email }}
          </a>

          <a
            v-if="portfolio.social?.sl_github"
            :href="portfolio.social.sl_github"
            target="_blank"
            rel="noopener noreferrer"
            class="break-all text-[#d1d5d3] transition hover:text-[#34d399]"
          >
            <span class="mr-2 text-[#10b981]">●</span>GitHub
          </a>

          <a
            v-if="portfolio.social?.sl_linkedin"
            :href="portfolio.social.sl_linkedin"
            target="_blank"
            rel="noopener noreferrer"
            class="break-all text-[#d1d5d3] transition hover:text-[#34d399]"
          >
            <span class="mr-2 text-[#10b981]">●</span>LinkedIn
          </a>

          <a
            v-if="portfolio.social?.sl_personal_web"
            :href="portfolio.social.sl_personal_web"
            target="_blank"
            rel="noopener noreferrer"
            class="break-all text-[#d1d5d3] transition hover:text-[#34d399]"
          >
            <span class="mr-2 text-[#10b981]">●</span
            >{{ i18nStore.t("portfolioTemplate.personalWebsite") }}
          </a>

          <p v-if="portfolio.phone" class="text-[#d1d5d3]">
            <span class="mr-2 text-[#10b981]">●</span>{{ portfolio.phone }}
          </p>

          <p
            v-if="!portfolio.email && !portfolio.phone && !portfolio.social"
            class="text-sm text-[#7f9189]"
          >
            {{ i18nStore.t("portfolioTemplate.contactPlaceholder") }}
          </p>
        </div>
      </section>

      <!-- Projects -->
      <section
        v-if="portfolio.projects?.length"
        class="border-t border-[#24443a] p-6 sm:p-8"
      >
        <h2 class="text-2xl font-bold text-[#10b981]">
          {{ i18nStore.t("portfolioTemplate.projects") }}
        </h2>
        <div class="mt-5 grid gap-4 md:grid-cols-2">
          <article
            v-for="project in portfolio.projects"
            :key="project.id"
            class="rounded-xl border border-[#285244] bg-[#151c19] p-5"
          >
            <h3 class="font-bold text-white">{{ project.pro_name }}</h3>
            <p
              v-if="project.pro_description"
              class="mt-2 text-sm leading-6 text-[#aab8b2]"
            >
              {{ project.pro_description }}
            </p>
            <p
              v-if="project.pro_techs"
              class="mt-3 text-xs font-semibold text-[#34d399]"
            >
              {{ project.pro_techs }}
            </p>
            <div class="mt-4 flex flex-wrap gap-4 text-xs font-bold">
              <a
                v-if="project.pro_github_url"
                :href="project.pro_github_url"
                target="_blank"
                rel="noopener noreferrer"
                class="text-[#6ee7b7] hover:text-white"
              >
                GitHub ↗
              </a>
              <a
                v-if="project.pro_live_demo_url"
                :href="project.pro_live_demo_url"
                target="_blank"
                rel="noopener noreferrer"
                class="text-[#6ee7b7] hover:text-white"
              >
                {{ i18nStore.t("portfolioTemplate.liveDemo") }} ↗
              </a>
            </div>
          </article>
        </div>
      </section>

      <footer
        class="border-t border-[#24443a] px-6 py-5 text-center text-xs font-semibold uppercase tracking-[0.25em] text-[#4fa987]"
      >
        {{ portfolio.title || i18nStore.t("portfolioTemplate.portfolio") }} ·
        {{ i18nStore.t("portfolioTemplate.greenCV") }}
      </footer>
    </div>
  </main>
</template>

<script setup>
import { useI18nStore } from "../../../stores/i18n";

const i18nStore = useI18nStore();

defineProps({
  portfolio: {
    type: Object,
    required: true,
  },
});
</script>
