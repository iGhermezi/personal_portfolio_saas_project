<template>
  <main class="min-h-screen bg-[#f2eee6] text-[#28241f]">
    <section class="mx-auto max-w-6xl px-6 py-8 sm:px-10">
      <header
        class="grid gap-12 border-b border-[#bcb3a5] pb-16 lg:grid-cols-[.8fr_1.2fr]"
      >
        <div class="flex flex-col justify-end">
          <p class="font-serif text-sm italic text-[#877e71]">
            {{ i18nStore.t("portfolioTemplate.personalEditorial") }}
          </p>
          <h1
            class="mt-5 font-serif text-6xl leading-[.9] tracking-[-.05em] sm:text-8xl"
          >
            {{ portfolio.title }}
          </h1>
        </div>
        <div>
          <p class="max-w-2xl font-serif text-2xl leading-10 text-[#625b52]">
            {{
              portfolio.bio || i18nStore.t("portfolioTemplate.thoughtfulBio")
            }}
          </p>
          <div
            class="mt-8 flex flex-wrap gap-4 text-xs font-bold uppercase tracking-widest"
          >
            <a
              v-if="portfolio.social?.sl_github"
              :href="portfolio.social.sl_github"
              target="_blank"
              >GitHub</a
            ><a
              v-if="portfolio.social?.sl_linkedin"
              :href="portfolio.social.sl_linkedin"
              target="_blank"
              >LinkedIn</a
            ><a
              v-if="portfolio.social?.sl_personal_web"
              :href="portfolio.social.sl_personal_web"
              target="_blank"
              >{{ i18nStore.t("portfolioTemplate.website") }}</a
            >
          </div>
        </div>
      </header>

      <section v-if="portfolio.projects?.length" class="py-16">
        <div
          class="mb-10 flex items-baseline justify-between border-b border-[#bcb3a5] pb-4"
        >
          <h2 class="font-serif text-4xl">
            {{ i18nStore.t("portfolioTemplate.selectedWorkTitle") }}
          </h2>
          <span class="text-xs uppercase tracking-widest text-[#877e71]">{{
            i18nStore.t("portfolioTemplate.projects")
          }}</span>
        </div>
        <div>
          <article
            v-for="project in portfolio.projects"
            :key="project.id"
            class="grid gap-8 border-b border-[#bcb3a5] py-9 md:grid-cols-[180px_1fr_160px]"
          >
            <div class="text-xs uppercase tracking-widest text-[#877e71]">
              {{ i18nStore.t("portfolioTemplate.project") }}
            </div>
            <div>
              <h3 class="font-serif text-3xl">{{ project.pro_name }}</h3>
              <p
                v-if="project.pro_description"
                class="mt-3 max-w-2xl leading-7 text-[#625b52]"
              >
                {{ project.pro_description }}
              </p>
              <p
                v-if="project.pro_techs"
                class="mt-4 text-xs uppercase tracking-widest"
              >
                {{ project.pro_techs }}
              </p>
            </div>
            <div class="flex gap-4 text-sm font-bold md:justify-end">
              <a
                v-if="project.pro_github_url"
                :href="project.pro_github_url"
                target="_blank"
                >GitHub ↗</a
              ><a
                v-if="project.pro_live_demo_url"
                :href="project.pro_live_demo_url"
                target="_blank"
                >{{ i18nStore.t("portfolioTemplate.live") }} ↗</a
              >
            </div>
          </article>
        </div>
      </section>

      <div class="grid gap-16 border-t border-[#bcb3a5] py-16 md:grid-cols-2">
        <section v-if="portfolio.experiences?.length">
          <h2 class="font-serif text-3xl">
            {{ i18nStore.t("portfolioTemplate.experience") }}
          </h2>
          <div class="mt-8 space-y-8">
            <article v-for="item in portfolio.experiences" :key="item.id">
              <p class="text-xs uppercase tracking-widest text-[#877e71]">
                {{ item.ex_start_date }} —
                {{
                  item.ex_end_date || i18nStore.t("portfolioTemplate.present")
                }}
              </p>
              <h3 class="mt-2 font-serif text-xl">{{ item.ex_position }}</h3>
              <p class="text-[#877e71]">{{ item.ex_company }}</p>
              <p
                v-if="item.ex_description"
                class="mt-2 text-sm leading-6 text-[#625b52]"
              >
                {{ item.ex_description }}
              </p>
            </article>
          </div>
        </section>
        <section v-if="portfolio.skills?.length">
          <h2 class="font-serif text-3xl">
            {{ i18nStore.t("portfolioTemplate.expertise") }}
          </h2>
          <div class="mt-8 grid grid-cols-2 gap-y-3">
            <span
              v-for="skill in portfolio.skills"
              :key="skill.id"
              class="text-sm"
              >{{ skill.skill_name }}</span
            >
          </div>
        </section>
      </div>

      <section
        v-if="portfolio.educations?.length"
        class="border-t border-[#bcb3a5] py-12"
      >
        <h2 class="font-serif text-3xl">
          {{ i18nStore.t("portfolioTemplate.education") }}
        </h2>
        <div class="mt-6 space-y-3 text-sm">
          <p v-for="item in portfolio.educations" :key="item.id">
            {{ item.edu }}
          </p>
        </div>
      </section>
      <footer
        class="border-t border-[#bcb3a5] py-8 text-xs uppercase tracking-widest text-[#877e71]"
      >
        {{ portfolio.title }} — {{ i18nStore.t("portfolioTemplate.portfolio") }}
      </footer>
    </section>
  </main>
</template>
<script setup>
import { useI18nStore } from "../../../stores/i18n";

const i18nStore = useI18nStore();

defineProps({ portfolio: { type: Object, required: true } });
</script>
