<template>
  <main class="min-h-screen bg-[#090b12] text-[#e8edf5]">
    <section class="mx-auto max-w-6xl px-5 py-6 sm:px-8">
      <header class="flex items-center justify-between border-b border-cyan-400/20 pb-5 font-mono text-xs"><span class="text-cyan-300">~/portfolio</span><span class="text-white/35">ONLINE</span></header>

      <section class="py-20 font-mono">
        <p class="text-cyan-300">$ whoami</p>
        <h1 class="mt-4 text-5xl font-black tracking-tight sm:text-7xl">{{ portfolio.title }}</h1>
        <p class="mt-6 max-w-3xl leading-8 text-white/50">{{ portfolio.bio || 'Developer. Builder. Problem solver.' }}</p>
      </section>

      <div class="grid gap-5 lg:grid-cols-[.7fr_1.3fr]">
        <aside class="space-y-5 font-mono">
          <section v-if="portfolio.skills?.length" class="rounded-xl border border-cyan-400/20 bg-cyan-400/[.03] p-5">
            <p class="text-cyan-300">$ skills</p>
            <div class="mt-5 space-y-3 text-sm">
              <div v-for="skill in portfolio.skills" :key="skill.id" class="flex justify-between gap-3"><span>{{ skill.skill_name }}</span><span class="text-cyan-300">{{ '█'.repeat(skill.skill_level_in_skill) }}{{ '░'.repeat(5-skill.skill_level_in_skill) }}</span></div>
            </div>
          </section>
          <section v-if="portfolio.educations?.length" class="rounded-xl border border-cyan-400/20 bg-cyan-400/[.03] p-5">
            <p class="text-cyan-300">$ education</p>
            <div class="mt-4 space-y-3 text-sm text-white/65"><p v-for="item in portfolio.educations" :key="item.id">> {{ item.edu }}</p></div>
          </section>
        </aside>

        <section v-if="portfolio.projects?.length" class="rounded-xl border border-cyan-400/20 bg-[#0d111b] p-6 font-mono">
          <p class="text-cyan-300">$ ls ./projects</p>
          <div class="mt-6 space-y-5">
            <article v-for="project in portfolio.projects" :key="project.id" class="rounded-lg border border-white/10 p-5">
              <h2 class="font-bold">{{ project.pro_name }}</h2>
              <p v-if="project.pro_description" class="mt-2 text-sm leading-6 text-white/45">{{ project.pro_description }}</p>
              <p v-if="project.pro_techs" class="mt-3 text-xs text-cyan-300">{{ project.pro_techs }}</p>
              <div class="mt-4 flex gap-4 text-xs"><a v-if="project.pro_github_url" :href="project.pro_github_url" target="_blank" class="text-white/70 hover:text-cyan-300">[github]</a><a v-if="project.pro_live_demo_url" :href="project.pro_live_demo_url" target="_blank" class="text-white/70 hover:text-cyan-300">[live]</a></div>
            </article>
          </div>
        </section>
      </div>

      <section v-if="portfolio.experiences?.length" class="mt-5 rounded-xl border border-cyan-400/20 bg-cyan-400/[.03] p-6 font-mono">
        <p class="text-cyan-300">$ cat experience.log</p>
        <div class="mt-6 space-y-6"><article v-for="item in portfolio.experiences" :key="item.id"><p class="text-sm text-white/35">[{{ item.ex_start_date }} — {{ item.ex_end_date || 'present' }}]</p><p class="mt-1 font-bold">{{ item.ex_position }} @ {{ item.ex_company }}</p><p v-if="item.ex_description" class="mt-2 text-sm leading-6 text-white/45">{{ item.ex_description }}</p></article></div>
      </section>

      <footer class="mt-10 border-t border-cyan-400/20 py-8 font-mono text-xs text-white/40">
        <div class="flex flex-wrap gap-5"><a v-if="portfolio.social?.sl_github" :href="portfolio.social.sl_github" target="_blank">github</a><a v-if="portfolio.social?.sl_linkedin" :href="portfolio.social.sl_linkedin" target="_blank">linkedin</a><a v-if="portfolio.social?.sl_personal_web" :href="portfolio.social.sl_personal_web" target="_blank">website</a></div>
      </footer>
    </section>
  </main>
</template>
<script setup>
defineProps({ portfolio: { type: Object, required: true } })
</script>
