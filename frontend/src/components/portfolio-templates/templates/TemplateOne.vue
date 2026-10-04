<template>
  <main class="min-h-screen overflow-hidden bg-[#fff8f5] text-[#4a2630]">
    <div class="pointer-events-none fixed inset-0">
      <div
        class="absolute -left-24 top-24 h-72 w-72 rounded-full bg-pink-200/30 blur-3xl"
      />
      <div
        class="absolute -right-24 top-[40%] h-80 w-80 rounded-full bg-red-200/25 blur-3xl"
      />
    </div>

    <section class="relative mx-auto max-w-6xl px-5 pt-6 sm:px-8">
      <nav
        class="flex items-center justify-between rounded-xl border border-[#f6d7d8] bg-white/85 px-5 py-3 shadow-sm backdrop-blur"
      >
        <div class="flex items-center gap-2">
          <span class="text-2xl">🍓</span
          ><span class="font-black text-[#d83f55]">arsam</span>
        </div>
        <span
          class="hidden rounded-full bg-[#fff0f2] px-4 py-2 text-xs font-bold text-[#d83f55] sm:block"
          >{{ i18nStore.t("portfolioTemplate.creativePortfolio") }} ♡</span
        >
      </nav>
    </section>

    <section class="relative mx-auto max-w-6xl px-5 py-20 sm:px-8 lg:py-28">
      <div class="grid items-center gap-12 lg:grid-cols-[1.15fr_.85fr]">
        <div>
          <div
            class="inline-flex rounded-full border border-[#f4c7ca] bg-white px-4 py-2 text-sm font-bold text-[#d83f55]"
          >
            🍓 {{ i18nStore.t("portfolioTemplate.hello") }} ♡
          </div>
          <h1
            class="mt-6 text-6xl font-black leading-[.92] tracking-[-.05em] text-[#542631] sm:text-8xl"
          >
            {{ portfolio.title }}<span class="text-[#e64b61]">.</span>
          </h1>
          <p
            v-if="portfolio.bio"
            class="mt-7 max-w-2xl text-lg leading-8 text-[#805861]"
          >
            {{ portfolio.bio }}
          </p>
          <div v-if="portfolio.social" class="mt-8 flex flex-wrap gap-3">
            <a
              v-if="portfolio.social.sl_github"
              :href="portfolio.social.sl_github"
              target="_blank"
              class="rounded-lg bg-[#e64b61] px-5 py-3 text-sm font-bold text-white"
              >GitHub ↗</a
            >
            <a
              v-if="portfolio.social.sl_linkedin"
              :href="portfolio.social.sl_linkedin"
              target="_blank"
              class="rounded-lg border border-[#f0c8cb] bg-white px-5 py-3 text-sm font-bold text-[#a94c5b]"
              >LinkedIn ♡</a
            >
            <a
              v-if="portfolio.social.sl_personal_web"
              :href="portfolio.social.sl_personal_web"
              target="_blank"
              class="rounded-lg border border-[#f0c8cb] bg-white px-5 py-3 text-sm font-bold text-[#a94c5b]"
              >{{ i18nStore.t("portfolioTemplate.website") }} ✦</a
            >
          </div>
        </div>

        <div
          class="rounded-[2.5rem] border border-[#f4c7ca] bg-[#ffe9eb] p-5 shadow-[0_25px_60px_rgba(216,63,85,.14)]"
        >
          <div
            class="grid min-h-[340px] place-items-center rounded-[2rem] border border-dashed border-[#efafb5] bg-[#fff7f6]"
          >
            <div class="text-center">
              <div
                class="mx-auto grid h-32 w-32 place-items-center rounded-full bg-[#ffd8dc] text-7xl"
              >
                🍓
              </div>
              <p class="mt-6 text-xl font-black text-[#d83f55]">
                {{ i18nStore.t("portfolioTemplate.madeWithLove") }}
              </p>
              <p class="mt-2 text-sm text-[#9c6870]">
                {{ i18nStore.t("portfolioTemplate.codeCreativity") }}
              </p>
              <div class="mt-5 text-xl">♡ ✦ ♡</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <main class="relative mx-auto max-w-6xl space-y-16 px-5 pb-20 sm:px-8">
      <section v-if="portfolio.skills?.length">
        <p class="text-sm font-bold text-[#e64b61]">
          ✿ {{ i18nStore.t("portfolioTemplate.thingsIKnow") }}
        </p>
        <h2 class="mt-2 text-4xl font-black text-[#542631]">
          {{ i18nStore.t("portfolioTemplate.mySkills") }}
        </h2>
        <div class="mt-7 flex flex-wrap gap-3">
          <span
            v-for="skill in portfolio.skills"
            :key="skill.id"
            class="rounded-full border border-[#f2c7ca] bg-white px-5 py-3 font-bold shadow-sm"
            >{{ skill.skill_name }}
            <small class="text-[#e64b61]"
              >{{ skill.skill_level_in_skill }}/5</small
            ></span
          >
        </div>
      </section>

      <section v-if="portfolio.projects?.length">
        <div class="mb-7">
          <p class="text-sm font-bold text-[#e64b61]">
            ✦ {{ i18nStore.t("portfolioTemplate.thingsMade") }}
          </p>
          <h2 class="mt-2 text-4xl font-black text-[#542631]">
            {{ i18nStore.t("portfolioTemplate.myProjects") }}
          </h2>
        </div>
        <div class="grid gap-6 md:grid-cols-2">
          <article
            v-for="project in portfolio.projects"
            :key="project.id"
            class="overflow-hidden rounded-[2rem] border border-[#f2d0d2] bg-white shadow-sm transition hover:-translate-y-2"
          >
            <div
              class="flex h-44 items-center justify-center bg-[#ffecef] text-6xl"
            >
              🍓
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
              <div class="mt-5 flex gap-3 text-sm font-bold">
                <a
                  v-if="project.pro_github_url"
                  :href="project.pro_github_url"
                  target="_blank"
                  >GitHub ↗</a
                ><a
                  v-if="project.pro_live_demo_url"
                  :href="project.pro_live_demo_url"
                  target="_blank"
                  >{{ i18nStore.t("portfolioTemplate.liveDemo") }} ✦</a
                >
              </div>
            </div>
          </article>
        </div>
      </section>

      <section v-if="portfolio.experiences?.length">
        <p class="text-sm font-bold text-[#e64b61]">
          🍓 {{ i18nStore.t("portfolioTemplate.whereIHaveBeen") }}
        </p>
        <h2 class="mt-2 text-4xl font-black text-[#542631]">
          {{ i18nStore.t("portfolioTemplate.experience") }}
        </h2>
        <div class="mt-7 space-y-5">
          <article
            v-for="item in portfolio.experiences"
            :key="item.id"
            class="rounded-[2rem] border border-[#f2d0d2] bg-white p-7 shadow-sm"
          >
            <p class="text-sm font-bold text-[#e64b61]">
              {{ item.ex_start_date }} —
              {{
                item.ex_end_date ||
                `${i18nStore.t("portfolioTemplate.present")} ♡`
              }}
            </p>
            <h3 class="mt-2 text-xl font-black">{{ item.ex_position }}</h3>
            <p class="font-bold text-[#d35465]">{{ item.ex_company }}</p>
            <p v-if="item.ex_description" class="mt-3 leading-7 text-[#805861]">
              {{ item.ex_description }}
            </p>
          </article>
        </div>
      </section>

      <section v-if="portfolio.educations?.length">
        <p class="text-sm font-bold text-[#e64b61]">
          🎀 {{ i18nStore.t("portfolioTemplate.learningJourney") }}
        </p>
        <h2 class="mt-2 text-4xl font-black text-[#542631]">
          {{ i18nStore.t("portfolioTemplate.education") }}
        </h2>
        <div class="mt-7 grid gap-4">
          <div
            v-for="item in portfolio.educations"
            :key="item.id"
            class="rounded-[1.75rem] border border-[#f2d0d2] bg-white px-6 py-5 font-bold shadow-sm"
          >
            🎀 {{ item.edu }}
          </div>
        </div>
      </section>

      <section
        class="rounded-[2.5rem] border border-[#f2c5c9] bg-[#ffe9eb] p-10 text-center"
      >
        <div class="text-4xl">🍓 ♡ ✦</div>
        <h2 class="mt-4 text-3xl font-black text-[#542631]">
          {{ i18nStore.t("portfolioTemplate.letsCreate") }}
        </h2>
        <p class="mt-3 text-[#805861]">
          {{ i18nStore.t("portfolioTemplate.thanks") }}
        </p>
      </section>
    </main>

    <footer
      class="border-t border-[#f2d1d3] bg-white/70 py-8 text-center text-sm font-bold text-[#d35465]"
    >
      🍓 {{ portfolio.title }} ·
      {{ i18nStore.t("portfolioTemplate.madeWithLove") }} ♡
    </footer>
  </main>
</template>
<script setup>
import { useI18nStore } from "../../../stores/i18n";

const i18nStore = useI18nStore();

defineProps({ portfolio: { type: Object, required: true } });
</script>
