<template>
  <main class="min-h-screen bg-slate-950 text-white">

    <!-- Hero -->

    <section
      class="
        mx-auto
        max-w-6xl
        px-6
        py-24
        sm:px-8
        lg:px-10
      "
    >

      <div class="max-w-3xl">

        <p
          class="
            text-sm
            font-semibold
            uppercase
            tracking-[0.25em]
            text-violet-400
          "
        >
          Portfolio
        </p>

        <h1
          class="
            mt-5
            text-5xl
            font-bold
            tracking-tight
            sm:text-6xl
          "
        >
          {{ portfolio.title }}
        </h1>

        <p
          v-if="portfolio.bio"
          class="
            mt-6
            max-w-2xl
            text-lg
            leading-8
            text-slate-300
          "
        >
          {{ portfolio.bio }}
        </p>

      </div>

    </section>


    <!-- Skills -->

    <section
      v-if="portfolio.skills?.length"
      class="
        border-t
        border-slate-800
      "
    >

      <div
        class="
          mx-auto
          max-w-6xl
          px-6
          py-16
          sm:px-8
          lg:px-10
        "
      >

        <h2 class="text-2xl font-bold">
          Skills
        </h2>

        <div
          class="
            mt-8
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
              border-slate-700
              bg-slate-900
              px-4
              py-2
              text-sm
              text-slate-200
            "
          >
            {{ skill.skill_name }}
          </div>

        </div>

      </div>

    </section>


    <!-- Experience -->

    <section
      v-if="portfolio.experiences?.length"
      class="
        border-t
        border-slate-800
      "
    >

      <div
        class="
          mx-auto
          max-w-6xl
          px-6
          py-16
          sm:px-8
          lg:px-10
        "
      >

        <h2 class="text-2xl font-bold">
          Experience
        </h2>

        <div class="mt-8 space-y-6">

          <article
            v-for="experience in portfolio.experiences"
            :key="experience.id"
            class="
              rounded-2xl
              border
              border-slate-800
              bg-slate-900
              p-6
            "
          >

            <div
              class="
                flex
                flex-col
                gap-2
                sm:flex-row
                sm:items-start
                sm:justify-between
              "
            >

              <div>

                <h3 class="text-lg font-semibold">
                  {{ experience.ex_position }}
                </h3>

                <p class="mt-1 text-sm text-violet-400">
                  {{ experience.ex_company }}
                </p>

              </div>

              <p class="text-sm text-slate-400">
                {{ experience.ex_start_date }}
                <span v-if="experience.ex_end_date">
                  — {{ experience.ex_end_date }}
                </span>
                <span v-else>
                  — Present
                </span>
              </p>

            </div>

            <p
              v-if="experience.ex_description"
              class="
                mt-4
                text-sm
                leading-7
                text-slate-300
              "
            >
              {{ experience.ex_description }}
            </p>

          </article>

        </div>

      </div>

    </section>


    <!-- Projects -->

    <section
      v-if="portfolio.projects?.length"
      class="
        border-t
        border-slate-800
      "
    >

      <div
        class="
          mx-auto
          max-w-6xl
          px-6
          py-16
          sm:px-8
          lg:px-10
        "
      >

        <h2 class="text-2xl font-bold">
          Projects
        </h2>

        <div
          class="
            mt-8
            grid
            gap-6
            md:grid-cols-2
          "
        >

          <article
            v-for="project in portfolio.projects"
            :key="project.id"
            class="
              overflow-hidden
              rounded-2xl
              border
              border-slate-800
              bg-slate-900
            "
          >

            <img
              v-if="project.pro_image"
              :src="project.pro_image"
              :alt="project.pro_name"
              class="
                h-52
                w-full
                object-cover
              "
            />

            <div class="p-6">

              <h3 class="text-xl font-semibold">
                {{ project.pro_name }}
              </h3>

              <p
                v-if="project.pro_description"
                class="
                  mt-3
                  text-sm
                  leading-7
                  text-slate-300
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
                  uppercase
                  tracking-wide
                  text-violet-400
                "
              >
                {{ project.pro_techs }}
              </p>

              <div
                class="
                  mt-6
                  flex
                  flex-wrap
                  gap-3
                "
              >

                <a
                  v-if="project.pro_github_url"
                  :href="project.pro_github_url"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="
                    rounded-full
                    bg-white
                    px-4
                    py-2
                    text-sm
                    font-semibold
                    text-slate-900
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
                    bg-violet-500
                    px-4
                    py-2
                    text-sm
                    font-semibold
                    text-white
                  "
                >
                  Live Demo
                </a>

              </div>

            </div>

          </article>

        </div>

      </div>

    </section>


    <!-- Education -->

    <section
      v-if="portfolio.educations?.length"
      class="
        border-t
        border-slate-800
      "
    >

      <div
        class="
          mx-auto
          max-w-6xl
          px-6
          py-16
          sm:px-8
          lg:px-10
        "
      >

        <h2 class="text-2xl font-bold">
          Education
        </h2>

        <div class="mt-8 space-y-3">

          <div
            v-for="education in portfolio.educations"
            :key="education.id"
            class="
              rounded-2xl
              border
              border-slate-800
              bg-slate-900
              px-6
              py-5
            "
          >
            {{ education.edu }}
          </div>

        </div>

      </div>

    </section>


    <!-- Social -->

    <footer
      v-if="portfolio.social"
      class="
        border-t
        border-slate-800
      "
    >

      <div
        class="
          mx-auto
          flex
          max-w-6xl
          flex-wrap
          gap-4
          px-6
          py-12
          sm:px-8
          lg:px-10
        "
      >

        <a
          v-if="portfolio.social.sl_github"
          :href="portfolio.social.sl_github"
          target="_blank"
          rel="noopener noreferrer"
          class="text-sm text-slate-300 hover:text-white"
        >
          GitHub
        </a>

        <a
          v-if="portfolio.social.sl_linkedin"
          :href="portfolio.social.sl_linkedin"
          target="_blank"
          rel="noopener noreferrer"
          class="text-sm text-slate-300 hover:text-white"
        >
          LinkedIn
        </a>

        <a
          v-if="portfolio.social.sl_personal_web"
          :href="portfolio.social.sl_personal_web"
          target="_blank"
          rel="noopener noreferrer"
          class="text-sm text-slate-300 hover:text-white"
        >
          Website
        </a>

      </div>

    </footer>

  </main>
</template>

<script setup>

defineProps({
  portfolio: {
    type: Object,
    required: true,
  },
})

</script>