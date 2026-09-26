<template>
  <main class="min-h-screen bg-[#fff9eb] text-[#252525]">
    <section class="mx-auto max-w-6xl px-5 py-7 sm:px-10">
      <header class="grid gap-10 border-b-4 border-[#252525] pb-12 lg:grid-cols-[1fr_220px]">
        <div>
          <p class="inline-block bg-[#ffd43b] px-3 py-1 text-xs font-black uppercase tracking-widest">Creative Portfolio</p>
          <h1 class="mt-7 text-6xl font-black uppercase leading-[.86] tracking-[-.07em] sm:text-8xl">{{ portfolio.title }}</h1>
          <p v-if="portfolio.bio" class="mt-7 max-w-2xl text-xl font-medium leading-8">{{ portfolio.bio }}</p>
        </div>
        <div class="flex items-end justify-end"><div class="grid h-40 w-40 place-items-center rounded-full border-4 border-[#252525] bg-[#ff6b6b] text-6xl shadow-[10px_10px_0_#252525]">✦</div></div>
      </header>

      <section v-if="portfolio.skills?.length" class="grid gap-8 border-b-4 border-[#252525] py-14 md:grid-cols-[220px_1fr]">
        <h2 class="text-2xl font-black uppercase">Skills →</h2>
        <div class="flex flex-wrap gap-4"><span v-for="skill in portfolio.skills" :key="skill.id" class="border-2 border-[#252525] bg-[#b8f2e6] px-5 py-3 font-black shadow-[5px_5px_0_#252525]">{{ skill.skill_name }} / {{ skill.skill_level_in_skill }}</span></div>
      </section>

      <section v-if="portfolio.projects?.length" class="border-b-4 border-[#252525] py-14">
        <h2 class="text-4xl font-black uppercase">Selected work ↘</h2>
        <div class="mt-10 grid gap-8 md:grid-cols-2">
          <article v-for="(project,index) in portfolio.projects" :key="project.id" class="border-4 border-[#252525] bg-white p-7 shadow-[10px_10px_0_#252525]" :class="index % 2 ? 'rotate-1' : '-rotate-1'">
            <div class="flex h-36 items-center justify-center bg-[#ffd6a5] text-6xl">✹</div>
            <h3 class="mt-6 text-2xl font-black uppercase">{{ project.pro_name }}</h3>
            <p v-if="project.pro_description" class="mt-3 leading-7">{{ project.pro_description }}</p>
            <p v-if="project.pro_techs" class="mt-4 font-black text-[#e85d04]">{{ project.pro_techs }}</p>
            <div class="mt-6 flex gap-4 font-black"><a v-if="project.pro_github_url" :href="project.pro_github_url" target="_blank">GITHUB ↗</a><a v-if="project.pro_live_demo_url" :href="project.pro_live_demo_url" target="_blank">LIVE ↗</a></div>
          </article>
        </div>
      </section>

      <section v-if="portfolio.experiences?.length" class="border-b-4 border-[#252525] py-14">
        <h2 class="text-4xl font-black uppercase">Experience</h2>
        <div class="mt-8 grid gap-6"><article v-for="item in portfolio.experiences" :key="item.id" class="grid gap-4 border-2 border-[#252525] p-6 md:grid-cols-[190px_1fr]"><p class="font-black">{{ item.ex_start_date }} — {{ item.ex_end_date || 'NOW' }}</p><div><h3 class="text-xl font-black uppercase">{{ item.ex_position }}</h3><p class="font-bold text-[#e85d04]">{{ item.ex_company }}</p><p v-if="item.ex_description" class="mt-2 leading-7">{{ item.ex_description }}</p></div></article></div>
      </section>

      <footer class="py-10"><div class="flex flex-wrap gap-6 font-black uppercase"><a v-if="portfolio.social?.sl_github" :href="portfolio.social.sl_github" target="_blank">GitHub ↗</a><a v-if="portfolio.social?.sl_linkedin" :href="portfolio.social.sl_linkedin" target="_blank">LinkedIn ↗</a><a v-if="portfolio.social?.sl_personal_web" :href="portfolio.social.sl_personal_web" target="_blank">Website ↗</a></div></footer>
    </section>
  </main>
</template>
<script setup>
defineProps({ portfolio: { type: Object, required: true } })
</script>
