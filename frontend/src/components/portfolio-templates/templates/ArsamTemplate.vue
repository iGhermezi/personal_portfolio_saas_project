<template>
  <main class="min-h-screen overflow-hidden bg-[#fff8f5] text-[#4a2630]">
    <!-- Decorative background -->
    <div class="pointer-events-none fixed inset-0 overflow-hidden">
      <div
        class="absolute -left-20 top-20 h-64 w-64 rounded-full bg-pink-200/30 blur-3xl"
      ></div>
      <div
        class="absolute -right-20 top-[40%] h-80 w-80 rounded-full bg-red-200/25 blur-3xl"
      ></div>
      <div
        class="absolute bottom-0 left-[35%] h-72 w-72 rounded-full bg-yellow-100/50 blur-3xl"
      ></div>
    </div>

    <!-- Header -->
    <header class="relative mx-auto max-w-6xl px-5 pt-6 sm:px-8 lg:px-10">
      <nav
        class="flex items-center justify-between rounded-xl border border-[#f6d7d8] bg-white/80 px-5 py-3 shadow-[0_10px_30px_rgba(214,80,100,0.08)] backdrop-blur"
      >
        <div class="flex items-center gap-2">
          <span class="text-2xl">🍓</span>

          <span class="font-black tracking-tight text-[#d83f55]"> arsam </span>
        </div>

        <span
          class="hidden rounded-full bg-[#fff0f2] px-4 py-2 text-xs font-bold text-[#d83f55] sm:block"
        >
          {{ i18nStore.t("portfolioTemplate.creativePortfolio") }} ♡
        </span>
      </nav>
    </header>

    <!-- Hero -->
    <section
      class="relative mx-auto max-w-6xl px-5 pb-20 pt-16 sm:px-8 sm:pt-24 lg:px-10"
    >
      <div class="grid items-center gap-12 lg:grid-cols-[1.15fr_0.85fr]">
        <div>
          <div
            class="inline-flex items-center gap-2 rounded-full border border-[#f4c7ca] bg-white px-4 py-2 text-sm font-bold text-[#d83f55] shadow-sm"
          >
            <span>🍓</span>
            <span>{{ i18nStore.t("portfolioTemplate.hello") }}</span>
            <span>♡</span>
          </div>

          <h1
            class="mt-6 max-w-4xl text-5xl font-black leading-[0.95] tracking-[-0.04em] text-[#542631] sm:text-7xl lg:text-8xl"
          >
            {{ portfolio.title }}
            <span class="text-[#e64b61]">.</span>
          </h1>

          <p
            v-if="portfolio.bio"
            class="mt-7 max-w-2xl text-base leading-8 text-[#805861] sm:text-lg"
          >
            {{ portfolio.bio }}
          </p>

          <div v-if="portfolio.social" class="mt-8 flex flex-wrap gap-3">
            <a
              v-if="portfolio.social.sl_github"
              :href="portfolio.social.sl_github"
              target="_blank"
              rel="noreferrer"
              class="rounded-lg bg-[#e64b61] px-5 py-3 text-sm font-bold text-white shadow-[0_8px_20px_rgba(230,75,97,0.2)] transition hover:-translate-y-1 hover:bg-[#d83f55]"
            >
              GitHub ↗
            </a>

            <a
              v-if="portfolio.social.sl_linkedin"
              :href="portfolio.social.sl_linkedin"
              target="_blank"
              rel="noreferrer"
              class="rounded-lg border border-[#f0c8cb] bg-white px-5 py-3 text-sm font-bold text-[#a94c5b] transition hover:-translate-y-1 hover:bg-[#fff4f4]"
            >
              LinkedIn ♡
            </a>

            <a
              v-if="portfolio.social.sl_personal_web"
              :href="portfolio.social.sl_personal_web"
              target="_blank"
              rel="noreferrer"
              class="rounded-lg border border-[#f0c8cb] bg-white px-5 py-3 text-sm font-bold text-[#a94c5b] transition hover:-translate-y-1 hover:bg-[#fff4f4]"
            >
              {{ i18nStore.t("portfolioTemplate.website") }} ✦
            </a>
          </div>
        </div>

        <!-- Cute strawberry card -->
        <div class="relative mx-auto w-full max-w-sm">
          <div class="absolute -right-3 -top-5 rotate-12 text-4xl">✦</div>

          <div class="absolute -bottom-4 -left-4 -rotate-12 text-3xl">♡</div>

          <div
            class="relative rounded-[2.5rem] border border-[#f4c7ca] bg-[#ffe9eb] p-5 shadow-[0_25px_60px_rgba(216,63,85,0.14)]"
          >
            <div
              class="flex min-h-[340px] items-center justify-center rounded-[2rem] border border-dashed border-[#efafb5] bg-[#fff7f6]"
            >
              <div class="text-center">
                <div
                  class="mx-auto flex h-32 w-32 items-center justify-center rounded-full bg-[#ffd8dc] text-7xl shadow-inner"
                >
                  🍓
                </div>

                <p class="mt-6 text-xl font-black text-[#d83f55]">
                  {{ i18nStore.t("portfolioTemplate.madeWithLove") }}
                </p>

                <p class="mt-2 text-sm text-[#9c6870]">
                  {{ i18nStore.t("portfolioTemplate.codeCreativity") }}
                </p>

                <div class="mt-5 flex justify-center gap-2 text-xl">
                  <span>♡</span>
                  <span>✦</span>
                  <span>♡</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Strawberry divider -->
    <div class="relative mx-auto max-w-6xl px-5 sm:px-8 lg:px-10">
      <div class="flex items-center gap-4">
        <div class="h-px flex-1 bg-[#f2d1d3]"></div>
        <span class="text-xl">🍓</span>
        <div class="h-px flex-1 bg-[#f2d1d3]"></div>
      </div>
    </div>

    <main
      class="relative mx-auto max-w-6xl space-y-20 px-5 py-20 sm:px-8 lg:px-10"
    >
      <!-- Skills -->
      <section v-if="portfolio.skills?.length">
        <div class="mb-8 flex items-end justify-between gap-4">
          <div>
            <p class="text-sm font-bold text-[#e64b61]">
              ✿ {{ i18nStore.t("portfolioTemplate.thingsIKnow") }}
            </p>

            <h2
              class="mt-2 text-3xl font-black tracking-tight text-[#542631] sm:text-4xl"
            >
              {{ i18nStore.t("portfolioTemplate.mySkills") }}
            </h2>
          </div>

          <span class="hidden text-2xl sm:block"> ♡ </span>
        </div>

        <div class="flex flex-wrap gap-3">
          <div
            v-for="skill in portfolio.skills"
            :key="skill.id"
            class="group rounded-full border border-[#f2c7ca] bg-white px-5 py-3 shadow-[0_8px_20px_rgba(216,63,85,0.06)] transition hover:-translate-y-1 hover:border-[#eaa0a7] hover:bg-[#fff1f2]"
          >
            <span class="font-bold text-[#70414b]">
              {{ skill.skill_name }}
            </span>

            <span class="ml-2 text-xs font-black text-[#e64b61]">
              {{ skill.skill_level_in_skill }}/5
            </span>
          </div>
        </div>
      </section>

      <!-- Experience -->
      <section v-if="portfolio.experiences?.length">
        <div class="mb-8">
          <p class="text-sm font-bold text-[#e64b61]">
            🍓 {{ i18nStore.t("portfolioTemplate.whereIHaveBeen") }}
          </p>

          <h2
            class="mt-2 text-3xl font-black tracking-tight text-[#542631] sm:text-4xl"
          >
            {{ i18nStore.t("portfolioTemplate.experience") }}
          </h2>
        </div>

        <div class="space-y-5">
          <article
            v-for="item in portfolio.experiences"
            :key="item.id"
            class="relative rounded-[2rem] border border-[#f2d0d2] bg-white p-6 shadow-[0_12px_30px_rgba(216,63,85,0.06)] transition hover:-translate-y-1 hover:shadow-[0_18px_35px_rgba(216,63,85,0.10)] sm:p-8"
          >
            <div class="absolute -right-2 -top-3 rotate-12 text-xl">✦</div>

            <div class="grid gap-5 sm:grid-cols-[180px_1fr]">
              <div>
                <p class="text-sm font-bold text-[#e64b61]">
                  {{ item.ex_start_date }}
                </p>

                <p class="text-sm text-[#a47a81]">
                  {{
                    item.ex_end_date ||
                    `${i18nStore.t("portfolioTemplate.present")} ♡`
                  }}
                </p>
              </div>

              <div>
                <h3 class="text-xl font-black text-[#542631]">
                  {{ item.ex_position }}
                </h3>

                <p class="mt-1 font-bold text-[#d35465]">
                  {{ item.ex_company }}
                </p>

                <p
                  v-if="item.ex_description"
                  class="mt-4 leading-7 text-[#805861]"
                >
                  {{ item.ex_description }}
                </p>
              </div>
            </div>
          </article>
        </div>
      </section>

      <!-- Projects -->
      <section v-if="portfolio.projects?.length">
        <div class="mb-8 flex items-end justify-between">
          <div>
            <p class="text-sm font-bold text-[#e64b61]">
              ✦ {{ i18nStore.t("portfolioTemplate.thingsMade") }}
            </p>

            <h2
              class="mt-2 text-3xl font-black tracking-tight text-[#542631] sm:text-4xl"
            >
              {{ i18nStore.t("portfolioTemplate.myProjects") }}
            </h2>
          </div>

          <span class="text-2xl"> 🍓 </span>
        </div>

        <div class="grid gap-6 md:grid-cols-2">
          <article
            v-for="project in portfolio.projects"
            :key="project.id"
            class="group overflow-hidden rounded-[2rem] border border-[#f2d0d2] bg-white shadow-[0_12px_30px_rgba(216,63,85,0.06)] transition duration-300 hover:-translate-y-2 hover:shadow-[0_20px_40px_rgba(216,63,85,0.12)]"
          >
            <div
              class="relative flex h-48 items-center justify-center overflow-hidden bg-[#ffecef]"
            >
              <img
                v-if="project.pro_image"
                :src="project.pro_image"
                :alt="project.pro_name"
                class="h-full w-full object-cover transition duration-500 group-hover:scale-105"
              />

              <div
                v-else
                class="text-6xl transition duration-300 group-hover:scale-110"
              >
                🍓
              </div>

              <span
                class="absolute right-4 top-4 rounded-full bg-white/90 px-3 py-1 text-xs font-black text-[#d83f55] shadow-sm"
              >
                {{ i18nStore.t("portfolioTemplate.project") }} ♡
              </span>
            </div>

            <div class="p-7">
              <h3 class="text-xl font-black text-[#542631]">
                {{ project.pro_name }}
              </h3>

              <p
                v-if="project.pro_description"
                class="mt-3 leading-7 text-[#805861]"
              >
                {{ project.pro_description }}
              </p>

              <p
                v-if="project.pro_techs"
                class="mt-4 rounded-2xl bg-[#fff4f4] px-4 py-3 text-sm font-bold text-[#a34d5b]"
              >
                {{ project.pro_techs }}
              </p>

              <div class="mt-6 flex flex-wrap gap-3">
                <a
                  v-if="project.pro_github_url"
                  :href="project.pro_github_url"
                  target="_blank"
                  rel="noreferrer"
                  class="rounded-lg bg-[#542631] px-4 py-2 text-xs font-bold text-white transition hover:bg-[#6d3441]"
                >
                  GitHub ↗
                </a>

                <a
                  v-if="project.pro_live_demo_url"
                  :href="project.pro_live_demo_url"
                  target="_blank"
                  rel="noreferrer"
                  class="rounded-lg border border-[#f0c8cb] px-4 py-2 text-xs font-bold text-[#d83f55] transition hover:bg-[#fff1f2]"
                >
                  {{ i18nStore.t("portfolioTemplate.liveDemo") }} ✦
                </a>
              </div>
            </div>
          </article>
        </div>
      </section>

      <!-- Education -->
      <section v-if="portfolio.educations?.length">
        <div class="mb-8">
          <p class="text-sm font-bold text-[#e64b61]">
            🎀 {{ i18nStore.t("portfolioTemplate.learningJourney") }}
          </p>

          <h2
            class="mt-2 text-3xl font-black tracking-tight text-[#542631] sm:text-4xl"
          >
            {{ i18nStore.t("portfolioTemplate.education") }}
          </h2>
        </div>

        <div class="grid gap-4">
          <div
            v-for="item in portfolio.educations"
            :key="item.id"
            class="rounded-[1.75rem] border border-[#f2d0d2] bg-white px-6 py-5 shadow-sm transition hover:-translate-y-1"
          >
            <div class="flex items-center gap-4">
              <div
                class="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-[#ffe2e5] text-lg"
              >
                🎀
              </div>

              <p class="font-bold text-[#70414b]">
                {{ item.edu }}
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Contact -->
      <section
        class="rounded-[2.5rem] border border-[#f2c5c9] bg-[#ffe9eb] p-8 text-center shadow-[0_18px_45px_rgba(216,63,85,0.08)] sm:p-12"
      >
        <div class="text-4xl">🍓 ♡ ✦</div>

        <h2 class="mt-5 text-3xl font-black text-[#542631]">
          {{ i18nStore.t("portfolioTemplate.letsCreate") }}
        </h2>

        <p class="mx-auto mt-3 max-w-xl leading-7 text-[#805861]">
          {{ i18nStore.t("portfolioTemplate.thanks") }}
        </p>

        <div
          v-if="portfolio.social"
          class="mt-7 flex flex-wrap justify-center gap-3"
        >
          <a
            v-if="portfolio.social.sl_github"
            :href="portfolio.social.sl_github"
            target="_blank"
            rel="noreferrer"
            class="rounded-lg bg-white px-5 py-3 text-sm font-bold text-[#d83f55] shadow-sm transition hover:-translate-y-1"
          >
            GitHub ♡
          </a>

          <a
            v-if="portfolio.social.sl_linkedin"
            :href="portfolio.social.sl_linkedin"
            target="_blank"
            rel="noreferrer"
            class="rounded-lg bg-white px-5 py-3 text-sm font-bold text-[#d83f55] shadow-sm transition hover:-translate-y-1"
          >
            LinkedIn ✦
          </a>

          <a
            v-if="portfolio.social.sl_personal_web"
            :href="portfolio.social.sl_personal_web"
            target="_blank"
            rel="noreferrer"
            class="rounded-lg bg-white px-5 py-3 text-sm font-bold text-[#d83f55] shadow-sm transition hover:-translate-y-1"
          >
            {{ i18nStore.t("portfolioTemplate.website") }} 🍓
          </a>
        </div>
      </section>
    </main>

    <footer class="relative border-t border-[#f2d1d3] bg-white/70">
      <div class="mx-auto max-w-6xl px-5 py-8 text-center sm:px-8 lg:px-10">
        <p class="text-sm font-bold text-[#d35465]">
          🍓 {{ portfolio.title }} ·
          {{ i18nStore.t("portfolioTemplate.madeWithLove") }} ♡
        </p>
      </div>
    </footer>
  </main>
</template>

<script setup>
import { useI18nStore } from "../../../stores/i18n";

const i18nStore = useI18nStore();
defineProps({ portfolio: { type: Object, required: true } });
</script>
