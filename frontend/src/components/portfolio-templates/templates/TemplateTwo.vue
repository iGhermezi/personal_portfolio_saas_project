<template>
  <main class="min-h-screen bg-[#101010] text-white">
    <section class="mx-auto max-w-6xl px-6 py-8 sm:px-10">
      <nav class="flex justify-between border-b border-white/10 pb-6 text-xs uppercase tracking-[.25em] text-white/45">
        <span>Portfolio / 02</span><span>{{ portfolio.title }}</span>
      </nav>

      <header class="grid gap-12 py-24 lg:grid-cols-[1.3fr_.7fr] lg:items-end">
        <div>
          <p class="text-sm font-bold uppercase tracking-[.3em] text-violet-300">Minimal / Digital</p>
          <h1 class="mt-5 text-6xl font-black leading-[.9] tracking-[-.06em] sm:text-8xl">{{ portfolio.title }}</h1>
          <p v-if="portfolio.bio" class="mt-8 max-w-2xl text-lg leading-8 text-white/50">{{ portfolio.bio }}</p>
        </div>
        <div class="rounded-3xl border border-white/10 bg-white/[.04] p-7">
          <p class="text-xs uppercase tracking-[.25em] text-white/35">Current focus</p>
          <p class="mt-3 text-xl font-bold">{{ portfolio.skills?.[0]?.skill_name || 'Building things' }}</p>
        </div>
      </header>

      <section v-if="portfolio.skills?.length" class="border-t border-white/10 py-16">
        <h2 class="text-3xl font-black">Skills</h2>
        <div class="mt-8 flex flex-wrap gap-3">
          <span v-for="skill in portfolio.skills" :key="skill.id" class="rounded-full border border-white/10 bg-white/[.04] px-4 py-2 text-sm text-white/65">{{ skill.skill_name }} · {{ skill.skill_level_in_skill }}/5</span>
        </div>
      </section>

      <section v-if="portfolio.projects?.length" class="border-t border-white/10 py-16">
        <h2 class="text-3xl font-black">Selected work</h2>
        <div class="mt-8 grid gap-5 md:grid-cols-2">
          <article v-for="project in portfolio.projects" :key="project.id" class="rounded-3xl border border-white/10 bg-white/[.03] p-7 transition hover:-translate-y-1 hover:bg-white/[.06]">
            <h3 class="text-xl font-bold">{{ project.pro_name }}</h3>
            <p v-if="project.pro_description" class="mt-4 leading-7 text-white/45">{{ project.pro_description }}</p>
            <p v-if="project.pro_techs" class="mt-5 text-xs uppercase tracking-widest text-white/30">{{ project.pro_techs }}</p>
            <div class="mt-6 flex gap-4 text-sm font-bold"><a v-if="project.pro_github_url" :href="project.pro_github_url" target="_blank" class="text-violet-300">GitHub ↗</a><a v-if="project.pro_live_demo_url" :href="project.pro_live_demo_url" target="_blank" class="text-white/55">Live ↗</a></div>
          </article>
        </div>
      </section>

      <section v-if="portfolio.experiences?.length" class="border-t border-white/10 py-16">
        <h2 class="text-3xl font-black">Experience</h2>
        <div class="mt-8 space-y-7">
          <article v-for="item in portfolio.experiences" :key="item.id" class="grid gap-3 border-l border-violet-300/40 pl-6 sm:grid-cols-[180px_1fr]">
            <div class="text-sm text-white/30">{{ item.ex_start_date }} — {{ item.ex_end_date || 'Present' }}</div>
            <div><h3 class="font-bold">{{ item.ex_position }}</h3><p class="text-violet-300">{{ item.ex_company }}</p><p v-if="item.ex_description" class="mt-2 text-sm leading-6 text-white/45">{{ item.ex_description }}</p></div>
          </article>
        </div>
      </section>

      <footer class="border-t border-white/10 py-10 text-sm text-white/35">
        <div class="flex gap-5"><a v-if="portfolio.social?.sl_github" :href="portfolio.social.sl_github" target="_blank">GitHub</a><a v-if="portfolio.social?.sl_linkedin" :href="portfolio.social.sl_linkedin" target="_blank">LinkedIn</a><a v-if="portfolio.social?.sl_personal_web" :href="portfolio.social.sl_personal_web" target="_blank">Website</a></div>
      </footer>
    </section>
  </main>
</template>
<script setup>
defineProps({ portfolio: { type: Object, required: true } })
</script>
