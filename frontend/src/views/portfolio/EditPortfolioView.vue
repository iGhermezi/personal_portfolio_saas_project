<template>
  <div class="min-h-screen bg-[#faf9ff] px-4 py-5 sm:px-6">
    <main class="mx-auto max-w-7xl">
      <!-- Header -->
      <div class="mb-5 flex items-center justify-between gap-4">
        <div class="min-w-0">
          <p
            class="text-xs font-semibold uppercase tracking-wider text-violet-500"
          >
            {{ i18nStore.t("portfolio.section") }}
          </p>

          <h1
            class="mt-1 truncate text-2xl font-bold tracking-tight text-slate-900"
          >
            {{ i18nStore.t("portfolio.editTitle") }}
          </h1>

          <p class="mt-1 text-sm text-slate-500">
            {{ i18nStore.t("portfolio.editDescription") }}
          </p>
        </div>

        <button
          type="button"
          class="hidden rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-semibold text-slate-600 transition hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600 sm:block"
          @click="router.back()"
        >
          {{ i18nStore.t("common.cancel") }}
        </button>
      </div>

      <!-- Loading -->
      <div
        v-if="loading"
        class="rounded-2xl border border-slate-200 bg-white p-10 text-center shadow-sm"
      >
        <p class="text-sm text-slate-400">
          {{ i18nStore.t("portfolio.loading") }}
        </p>
      </div>

      <!-- Builder -->
      <div
        v-else
        class="grid gap-5 lg:grid-cols-[220px_minmax(0,1fr)] lg:items-start"
      >
        <!-- SIDEBAR -->
        <aside
          class="rounded-2xl border border-slate-200 bg-white p-3 shadow-sm lg:sticky lg:top-5"
        >
          <div class="px-2 pb-3">
            <p
              class="text-[10px] font-bold uppercase tracking-widest text-slate-400"
            >
              Content
            </p>
          </div>

          <nav class="space-y-1">
            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
              :class="
                activeSection === 'overview'
                  ? 'bg-violet-50 text-violet-700'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
              "
              @click="activeSection = 'overview'"
            >
              <span class="w-5 text-center">⌂</span>
              <span>{{ i18nStore.t("portfolio.basicInformation") }}</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
              :class="
                activeSection === 'experience'
                  ? 'bg-violet-50 text-violet-700'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
              "
              @click="activeSection = 'experience'"
            >
              <span class="w-5 text-center">▣</span>
              <span>{{ i18nStore.t("portfolio.experience") }}</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
              :class="
                activeSection === 'education'
                  ? 'bg-violet-50 text-violet-700'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
              "
              @click="activeSection = 'education'"
            >
              <span class="w-5 text-center">□</span>
              <span>{{ i18nStore.t("portfolio.education") }}</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
              :class="
                activeSection === 'skills'
                  ? 'bg-violet-50 text-violet-700'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
              "
              @click="activeSection = 'skills'"
            >
              <span class="w-5 text-center">◆</span>
              <span>{{ i18nStore.t("portfolio.skills") }}</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
              :class="
                activeSection === 'projects'
                  ? 'bg-violet-50 text-violet-700'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
              "
              @click="activeSection = 'projects'"
            >
              <span class="w-5 text-center">◇</span>
              <span>{{ i18nStore.t("portfolio.projects") }}</span>
            </button>

            <button
              type="button"
              class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
              :class="
                activeSection === 'social'
                  ? 'bg-violet-50 text-violet-700'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
              "
              @click="activeSection = 'social'"
            >
              <span class="w-5 text-center">↗</span>
              <span>{{ i18nStore.t("portfolio.socialLinks") }}</span>
            </button>
          </nav>

          <div class="my-3 border-t border-slate-100"></div>

          <div class="px-2 pb-2">
            <p
              class="text-[10px] font-bold uppercase tracking-widest text-slate-400"
            >
              Design
            </p>
          </div>

          <button
            type="button"
            class="flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-left text-sm font-semibold transition"
            :class="
              activeSection === 'template'
                ? 'bg-violet-50 text-violet-700'
                : 'text-slate-600 hover:bg-slate-50 hover:text-violet-600'
            "
            @click="activeSection = 'template'"
          >
            <span class="w-5 text-center">✦</span>
            <span>{{ i18nStore.t("portfolio.chooseTemplate") }}</span>
          </button>

          <div class="my-3 border-t border-slate-100"></div>

          <div class="px-2 pb-2">
            <p
              class="text-[10px] font-bold uppercase tracking-widest text-slate-400"
            >
              Preview
            </p>
          </div>

          <button
            type="button"
            class="flex w-full items-center gap-2.5 rounded-lg bg-violet-600 px-3 py-2.5 text-left text-sm font-bold text-white transition hover:bg-violet-700"
            @click="router.push(`/portfolio/${route.params.id}/preview`)"
          >
            <span class="w-5 text-center">↗</span>
            <span>{{ i18nStore.t("portfolio.preview") }}</span>
          </button>
        </aside>

        <!-- CONTENT -->
        <section class="min-w-0">
          <!-- GLOBAL ERROR -->
          <div
            v-if="error"
            class="mb-4 rounded-xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
          >
            {{ error }}
          </div>

          <!-- OVERVIEW -->
          <section
            v-show="activeSection === 'overview'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.basicInformation") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.identity") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <div class="grid gap-4 md:grid-cols-2">
                <Field
                  v-model="basic.title"
                  :label="i18nStore.t('portfolio.title')"
                />

                <Field
                  v-model="basic.slug"
                  :label="i18nStore.t('portfolio.url')"
                />
              </div>

              <div class="mt-4">
                <label class="block text-sm font-semibold text-slate-700">
                  {{ i18nStore.t("portfolio.shortBio") }}
                </label>

                <textarea
                  v-model="basic.bio"
                  rows="4"
                  class="mt-1.5 w-full resize-none rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm text-slate-800 outline-none transition placeholder:text-slate-400 focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                />
              </div>

              <div
                v-if="basicError"
                class="mt-4 rounded-lg border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
              >
                {{ basicError }}
              </div>

              <div
                class="mt-5 flex flex-col-reverse gap-3 border-t border-slate-100 pt-5 sm:flex-row sm:justify-end"
              >
                <button
                  type="button"
                  :disabled="savingBasic"
                  class="rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-700 disabled:cursor-not-allowed disabled:opacity-60"
                  @click="saveBasic"
                >
                  {{
                    i18nStore.t(
                      savingBasic
                        ? "portfolio.saving"
                        : "portfolio.saveBasicInformation",
                    )
                  }}
                </button>
              </div>
            </div>
          </section>

          <!-- EXPERIENCE -->
          <section
            v-show="activeSection === 'experience'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.experience") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.manageExperience") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <!-- Add -->
              <div class="rounded-xl bg-slate-50 p-4">
                <div class="grid gap-4 md:grid-cols-2">
                  <Field
                    v-model="experienceForm.ex_company"
                    :label="i18nStore.t('portfolio.company')"
                    :placeholder="i18nStore.t('portfolio.companyPlaceholder')"
                  />

                  <Field
                    v-model="experienceForm.ex_position"
                    :label="i18nStore.t('portfolio.position')"
                    :placeholder="i18nStore.t('portfolio.positionPlaceholder')"
                  />

                  <Field
                    v-model="experienceForm.ex_start_date"
                    :label="i18nStore.t('portfolio.startDate')"
                    type="date"
                  />

                  <Field
                    v-model="experienceForm.ex_end_date"
                    :label="i18nStore.t('portfolio.endDate')"
                    type="date"
                  />
                </div>

                <div class="mt-4">
                  <label class="block text-sm font-semibold text-slate-700">
                    {{ i18nStore.t("portfolio.description") }}
                  </label>

                  <textarea
                    v-model="experienceForm.ex_description"
                    rows="3"
                    class="mt-1.5 w-full resize-none rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                  />
                </div>

                <button
                  type="button"
                  :disabled="actionLoading"
                  class="mt-4 rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-700 disabled:opacity-60"
                  @click="addExperience"
                >
                  + {{ i18nStore.t("portfolio.addExperience") }}
                </button>
              </div>

              <!-- List -->
              <div class="mt-5 space-y-3">
                <div
                  v-for="experience in experiences"
                  :key="experience.id"
                  class="rounded-xl border border-slate-200 p-4"
                >
                  <div v-if="editing.experiences !== experience.id">
                    <div class="flex items-start justify-between gap-4">
                      <div class="min-w-0">
                        <p class="font-semibold text-slate-800">
                          {{ experience.ex_position }}
                        </p>

                        <p class="mt-1 text-sm text-violet-600">
                          {{ experience.ex_company }}
                        </p>

                        <p class="mt-1 text-xs text-slate-400">
                          {{ experience.ex_start_date }} →
                          {{
                            experience.ex_end_date ||
                            i18nStore.t("portfolio.present")
                          }}
                        </p>
                      </div>

                      <div class="flex shrink-0 gap-2">
                        <button
                          type="button"
                          class="rounded-lg border border-slate-200 bg-white px-3 py-2 text-xs font-semibold text-slate-600 transition hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600"
                          @click="startEdit('experiences', experience)"
                        >
                          {{ i18nStore.t("portfolio.edit") }}
                        </button>

                        <button
                          type="button"
                          class="rounded-lg border border-red-100 bg-white px-3 py-2 text-xs font-semibold text-red-500 transition hover:bg-red-50"
                          @click="deleteItem('experiences', experience.id)"
                        >
                          {{ i18nStore.t("portfolio.remove") }}
                        </button>
                      </div>
                    </div>

                    <p
                      v-if="experience.ex_description"
                      class="mt-3 text-sm leading-6 text-slate-500"
                    >
                      {{ experience.ex_description }}
                    </p>
                  </div>

                  <div v-else>
                    <div class="grid gap-4 md:grid-cols-2">
                      <Field
                        v-model="editForms.experiences[experience.id].ex_company"
                        :label="i18nStore.t('portfolio.company')"
                      />

                      <Field
                        v-model="
                          editForms.experiences[experience.id].ex_position
                        "
                        :label="i18nStore.t('portfolio.position')"
                      />

                      <Field
                        v-model="
                          editForms.experiences[experience.id].ex_start_date
                        "
                        :label="i18nStore.t('portfolio.startDate')"
                        type="date"
                      />

                      <Field
                        v-model="
                          editForms.experiences[experience.id].ex_end_date
                        "
                        :label="i18nStore.t('portfolio.endDate')"
                        type="date"
                      />
                    </div>

                    <div class="mt-4">
                      <label
                        class="block text-sm font-semibold text-slate-700"
                      >
                        {{ i18nStore.t("portfolio.description") }}
                      </label>

                      <textarea
                        v-model="
                          editForms.experiences[experience.id].ex_description
                        "
                        rows="3"
                        class="mt-1.5 w-full resize-none rounded-lg border border-slate-200 px-3.5 py-2.5 text-sm outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                      />
                    </div>

                    <div class="mt-4 flex gap-2">
                      <button
                        type="button"
                        class="rounded-lg bg-violet-600 px-4 py-2.5 text-xs font-semibold text-white hover:bg-violet-700"
                        @click="saveEdit('experiences', experience.id)"
                      >
                        {{ i18nStore.t("portfolio.save") }}
                      </button>

                      <button
                        type="button"
                        class="rounded-lg border border-slate-200 bg-white px-4 py-2.5 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                        @click="cancelEdit('experiences')"
                      >
                        {{ i18nStore.t("portfolio.cancel") }}
                      </button>
                    </div>
                  </div>
                </div>

                <EmptyState
                  v-if="!experiences.length"
                  :text="i18nStore.t('portfolio.noExperience')"
                />
              </div>
            </div>
          </section>

          <!-- EDUCATION -->
          <section
            v-show="activeSection === 'education'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.education") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.manageEducation") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <div class="flex gap-3 rounded-xl bg-slate-50 p-4">
                <input
                  v-model="educationForm.edu"
                  type="text"
                  :placeholder="i18nStore.t('portfolio.educationPlaceholder')"
                  class="min-w-0 flex-1 rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                  @keyup.enter="addEducation"
                />

                <button
                  type="button"
                  :disabled="actionLoading"
                  class="shrink-0 rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-violet-700 disabled:opacity-60"
                  @click="addEducation"
                >
                  + {{ i18nStore.t("portfolio.add") }}
                </button>
              </div>

              <div class="mt-5 space-y-3">
                <div
                  v-for="education in educations"
                  :key="education.id"
                  class="rounded-xl border border-slate-200 p-4"
                >
                  <div
                    v-if="editing.educations !== education.id"
                    class="flex items-center justify-between gap-4"
                  >
                    <p class="font-semibold text-slate-800">
                      {{ education.edu }}
                    </p>

                    <div class="flex shrink-0 gap-2">
                      <button
                        type="button"
                        class="rounded-lg border border-slate-200 bg-white px-3 py-2 text-xs font-semibold text-slate-600 hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600"
                        @click="startEdit('educations', education)"
                      >
                        {{ i18nStore.t("portfolio.edit") }}
                      </button>

                      <button
                        type="button"
                        class="rounded-lg border border-red-100 bg-white px-3 py-2 text-xs font-semibold text-red-500 hover:bg-red-50"
                        @click="deleteItem('educations', education.id)"
                      >
                        {{ i18nStore.t("portfolio.remove") }}
                      </button>
                    </div>
                  </div>

                  <div v-else class="flex gap-3">
                    <input
                      v-model="editForms.educations[education.id].edu"
                      type="text"
                      class="min-w-0 flex-1 rounded-lg border border-slate-200 px-3.5 py-2.5 text-sm outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                    />

                    <button
                      type="button"
                      class="rounded-lg bg-violet-600 px-4 py-2.5 text-xs font-semibold text-white hover:bg-violet-700"
                      @click="saveEdit('educations', education.id)"
                    >
                      {{ i18nStore.t("portfolio.save") }}
                    </button>

                    <button
                      type="button"
                      class="rounded-lg border border-slate-200 px-4 py-2.5 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                      @click="cancelEdit('educations')"
                    >
                      {{ i18nStore.t("portfolio.cancel") }}
                    </button>
                  </div>
                </div>

                <EmptyState
                  v-if="!educations.length"
                  :text="i18nStore.t('portfolio.noEducation')"
                />
              </div>
            </div>
          </section>

          <!-- SKILLS -->
          <section
            v-show="activeSection === 'skills'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.skills") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.skillsDescription") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <div class="rounded-xl bg-slate-50 p-4">
                <div
                  class="grid gap-4 md:grid-cols-[minmax(0,1fr)_160px_auto] md:items-end"
                >
                  <Field
                    v-model="skillForm.skill_name"
                    :label="i18nStore.t('portfolio.skill')"
                    :placeholder="i18nStore.t('portfolio.skill')"
                  />

                  <div>
                    <label class="block text-sm font-semibold text-slate-700">
                      {{ i18nStore.t("portfolio.level") }}
                    </label>

                    <select
                      v-model.number="skillForm.skill_level_in_skill"
                      class="mt-1.5 w-full rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm text-slate-900 outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                    >
                      <option :value="1">1 / 5</option>
                      <option :value="2">2 / 5</option>
                      <option :value="3">3 / 5</option>
                      <option :value="4">4 / 5</option>
                      <option :value="5">5 / 5</option>
                    </select>
                  </div>

                  <button
                    type="button"
                    :disabled="actionLoading"
                    class="rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-violet-700 disabled:opacity-60"
                    @click="addSkill"
                  >
                    + {{ i18nStore.t("portfolio.add") }}
                  </button>
                </div>
              </div>

              <div class="mt-5 space-y-3">
                <div
                  v-for="skill in skills"
                  :key="skill.id"
                  class="rounded-xl border border-slate-200 p-4"
                >
                  <div
                    v-if="editing.skills !== skill.id"
                    class="flex items-center justify-between gap-4"
                  >
                    <div>
                      <p class="font-semibold text-slate-800">
                        {{ skill.skill_name }}
                      </p>

                      <p class="mt-1 text-xs text-violet-600">
                        {{ i18nStore.t("portfolio.level") }}
                        {{ skill.skill_level_in_skill }} / 5
                      </p>
                    </div>

                    <div class="flex shrink-0 gap-2">
                      <button
                        type="button"
                        class="rounded-lg border border-slate-200 bg-white px-3 py-2 text-xs font-semibold text-slate-600 hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600"
                        @click="startEdit('skills', skill)"
                      >
                        {{ i18nStore.t("portfolio.edit") }}
                      </button>

                      <button
                        type="button"
                        class="rounded-lg border border-red-100 bg-white px-3 py-2 text-xs font-semibold text-red-500 hover:bg-red-50"
                        @click="deleteItem('skills', skill.id)"
                      >
                        {{ i18nStore.t("portfolio.remove") }}
                      </button>
                    </div>
                  </div>

                  <div
                    v-else
                    class="grid gap-4 md:grid-cols-[minmax(0,1fr)_160px_auto]"
                  >
                    <Field
                      v-model="editForms.skills[skill.id].skill_name"
                      :label="i18nStore.t('portfolio.skill')"
                    />

                    <div>
                      <label
                        class="block text-sm font-semibold text-slate-700"
                      >
                        {{ i18nStore.t("portfolio.level") }}
                      </label>

                      <select
                        v-model.number="
                          editForms.skills[skill.id].skill_level_in_skill
                        "
                        class="mt-1.5 w-full rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm"
                      >
                        <option :value="1">1 / 5</option>
                        <option :value="2">2 / 5</option>
                        <option :value="3">3 / 5</option>
                        <option :value="4">4 / 5</option>
                        <option :value="5">5 / 5</option>
                      </select>
                    </div>

                    <div class="flex gap-2 self-end">
                      <button
                        type="button"
                        class="rounded-lg bg-violet-600 px-4 py-2.5 text-xs font-semibold text-white hover:bg-violet-700"
                        @click="saveEdit('skills', skill.id)"
                      >
                        {{ i18nStore.t("portfolio.save") }}
                      </button>

                      <button
                        type="button"
                        class="rounded-lg border border-slate-200 px-4 py-2.5 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                        @click="cancelEdit('skills')"
                      >
                        {{ i18nStore.t("portfolio.cancel") }}
                      </button>
                    </div>
                  </div>
                </div>

                <EmptyState
                  v-if="!skills.length"
                  :text="i18nStore.t('portfolio.noSkills')"
                />
              </div>
            </div>
          </section>

          <!-- PROJECTS -->
          <section
            v-show="activeSection === 'projects'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.projects") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.manageProjects") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <div class="rounded-xl bg-slate-50 p-4">
                <div class="grid gap-4 md:grid-cols-2">
                  <Field
                    v-model="projectForm.pro_name"
                    :label="i18nStore.t('portfolio.projectName')"
                  />

                  <Field
                    v-model="projectForm.pro_github_url"
                    :label="i18nStore.t('portfolio.githubUrl')"
                  />

                  <Field
                    v-model="projectForm.pro_live_demo_url"
                    :label="i18nStore.t('portfolio.liveDemoUrl')"
                  />

                  <Field
                    v-model="projectForm.pro_techs"
                    :label="i18nStore.t('portfolio.technologies')"
                  />

                  <Field
                    v-model="projectForm.pro_start"
                    :label="i18nStore.t('portfolio.startDate')"
                    type="date"
                  />

                  <Field
                    v-model="projectForm.pro_end"
                    :label="i18nStore.t('portfolio.endDate')"
                    type="date"
                  />
                </div>

                <div class="mt-4">
                  <label class="block text-sm font-semibold text-slate-700">
                    {{ i18nStore.t("portfolio.description") }}
                  </label>

                  <textarea
                    v-model="projectForm.pro_description"
                    rows="3"
                    class="mt-1.5 w-full resize-none rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                  />
                </div>

                <button
                  type="button"
                  :disabled="actionLoading"
                  class="mt-4 rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-violet-700 disabled:opacity-60"
                  @click="addProject"
                >
                  + {{ i18nStore.t("portfolio.addProject") }}
                </button>
              </div>

              <div class="mt-5 grid gap-3 lg:grid-cols-2">
                <div
                  v-for="project in projects"
                  :key="project.id"
                  class="rounded-xl border border-slate-200 p-4"
                >
                  <div v-if="editing.projects !== project.id">
                    <div class="flex items-start justify-between gap-4">
                      <div class="min-w-0">
                        <h3 class="font-semibold text-slate-800">
                          {{ project.pro_name }}
                        </h3>

                        <p class="mt-1 text-xs text-violet-600">
                          {{ project.pro_techs }}
                        </p>

                        <p class="mt-1 text-xs text-slate-400">
                          {{ project.pro_start }} →
                          {{
                            project.pro_end ||
                            i18nStore.t("portfolio.present")
                          }}
                        </p>
                      </div>

                      <div class="flex shrink-0 gap-2">
                        <button
                          type="button"
                          class="rounded-lg border border-slate-200 px-3 py-2 text-xs font-semibold text-slate-600 hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600"
                          @click="startEdit('projects', project)"
                        >
                          {{ i18nStore.t("portfolio.edit") }}
                        </button>

                        <button
                          type="button"
                          class="rounded-lg border border-red-100 px-3 py-2 text-xs font-semibold text-red-500 hover:bg-red-50"
                          @click="deleteItem('projects', project.id)"
                        >
                          {{ i18nStore.t("portfolio.remove") }}
                        </button>
                      </div>
                    </div>

                    <p
                      v-if="project.pro_description"
                      class="mt-3 text-sm leading-6 text-slate-500"
                    >
                      {{ project.pro_description }}
                    </p>
                  </div>

                  <div v-else>
                    <div class="grid gap-4 md:grid-cols-2">
                      <Field
                        v-model="editForms.projects[project.id].pro_name"
                        :label="i18nStore.t('portfolio.projectName')"
                      />

                      <Field
                        v-model="
                          editForms.projects[project.id].pro_github_url
                        "
                        :label="i18nStore.t('portfolio.githubUrl')"
                      />

                      <Field
                        v-model="
                          editForms.projects[project.id].pro_live_demo_url
                        "
                        :label="i18nStore.t('portfolio.liveDemoUrl')"
                      />

                      <Field
                        v-model="editForms.projects[project.id].pro_techs"
                        :label="i18nStore.t('portfolio.technologies')"
                      />

                      <Field
                        v-model="editForms.projects[project.id].pro_start"
                        :label="i18nStore.t('portfolio.startDate')"
                        type="date"
                      />

                      <Field
                        v-model="editForms.projects[project.id].pro_end"
                        :label="i18nStore.t('portfolio.endDate')"
                        type="date"
                      />
                    </div>

                    <div class="mt-4">
                      <label
                        class="block text-sm font-semibold text-slate-700"
                      >
                        {{ i18nStore.t("portfolio.description") }}
                      </label>

                      <textarea
                        v-model="
                          editForms.projects[project.id].pro_description
                        "
                        rows="3"
                        class="mt-1.5 w-full resize-none rounded-lg border border-slate-200 px-3.5 py-2.5 text-sm outline-none focus:border-violet-400 focus:ring-2 focus:ring-violet-100"
                      />
                    </div>

                    <div class="mt-4 flex gap-2">
                      <button
                        type="button"
                        class="rounded-lg bg-violet-600 px-4 py-2.5 text-xs font-semibold text-white hover:bg-violet-700"
                        @click="saveEdit('projects', project.id)"
                      >
                        {{ i18nStore.t("portfolio.save") }}
                      </button>

                      <button
                        type="button"
                        class="rounded-lg border border-slate-200 px-4 py-2.5 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                        @click="cancelEdit('projects')"
                      >
                        {{ i18nStore.t("portfolio.cancel") }}
                      </button>
                    </div>
                  </div>
                </div>

                <EmptyState
                  v-if="!projects.length"
                  :text="i18nStore.t('portfolio.noProjects')"
                />
              </div>
            </div>
          </section>

          <!-- SOCIAL -->
          <section
            v-show="activeSection === 'social'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.socialLinks") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.socialDescriptionFull") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <div class="grid gap-4 md:grid-cols-3">
                <Field
                  v-model="socialForm.sl_github"
                  label="GitHub"
                  placeholder="https://github.com/username"
                />

                <Field
                  v-model="socialForm.sl_linkedin"
                  label="LinkedIn"
                  placeholder="https://linkedin.com/in/username"
                />

                <Field
                  v-model="socialForm.sl_personal_web"
                  :label="i18nStore.t('portfolio.website')"
                  placeholder="https://example.com"
                />
              </div>

              <div
                class="mt-5 flex flex-col gap-3 border-t border-slate-100 pt-5 sm:flex-row sm:items-center sm:justify-between"
              >
                <p class="text-xs text-slate-400">
                  {{
                    i18nStore.t(
                      social
                        ? "portfolio.existingSocialUpdated"
                        : "portfolio.noSocialSaved",
                    )
                  }}
                </p>

                <div class="flex gap-2">
                  <button
                    v-if="social"
                    type="button"
                    class="rounded-lg border border-red-100 bg-white px-4 py-2.5 text-sm font-semibold text-red-500 hover:bg-red-50"
                    :disabled="actionLoading"
                    @click="deleteSocial"
                  >
                    {{ i18nStore.t("portfolio.remove") }}
                  </button>

                  <button
                    type="button"
                    class="rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-violet-700 disabled:opacity-60"
                    :disabled="actionLoading"
                    @click="saveSocial"
                  >
                    {{
                      i18nStore.t(
                        actionLoading
                          ? "portfolio.saving"
                          : social
                            ? "portfolio.updateSocial"
                            : "portfolio.saveSocial",
                      )
                    }}
                  </button>
                </div>
              </div>
            </div>
          </section>

          <!-- TEMPLATE -->
          <section
            v-show="activeSection === 'template'"
            class="rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div class="border-b border-slate-100 px-5 py-4 sm:px-6">
              <h2 class="text-base font-bold text-slate-800">
                {{ i18nStore.t("portfolio.chooseTemplate") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.lockedTemplateDescription") }}
              </p>
            </div>

            <div class="p-5 sm:p-6">
              <div
                v-if="templatesLoading"
                class="rounded-xl bg-slate-50 p-8 text-center text-sm text-slate-400"
              >
                {{ i18nStore.t("portfolio.loadingTemplates") }}
              </div>

              <div
                v-else-if="templates.length"
                class="grid gap-4 sm:grid-cols-2 xl:grid-cols-3"
              >
                <button
                  v-for="template in templates"
                  :key="template.id"
                  type="button"
                  class="group relative overflow-hidden rounded-xl border bg-white text-left transition"
                  :class="
                    template.can_use
                      ? basic.template === template.id
                        ? 'border-violet-400 ring-2 ring-violet-100'
                        : 'border-slate-200 hover:-translate-y-0.5 hover:border-violet-200 hover:shadow-md'
                      : 'cursor-not-allowed border-slate-200'
                  "
                  @click="selectTemplate(template)"
                >
                  <div
                    class="relative flex h-36 items-center justify-center overflow-hidden bg-slate-50"
                  >
                    <img
                      v-if="template.preview_img"
                      :src="template.preview_img"
                      :alt="i18nStore.templateName(template)"
                      class="h-full w-full object-cover transition duration-200 group-hover:scale-[1.02]"
                    />

                    <span
                      v-else
                      class="text-3xl text-violet-300"
                    >
                      ✦
                    </span>

                    <div
                      v-if="!template.can_use"
                      class="absolute inset-0 flex flex-col items-center justify-center bg-slate-900/55 text-white backdrop-blur-[2px]"
                    >
                      <span class="text-2xl">🔒</span>

                      <span class="mt-1 text-xs font-semibold">
                        {{ i18nStore.t("templates.locked") }}
                      </span>
                    </div>

                    <div
                      v-if="
                        template.can_use &&
                        basic.template === template.id
                      "
                      class="absolute right-3 top-3 flex h-7 w-7 items-center justify-center rounded-full bg-violet-600 text-xs font-bold text-white shadow-sm"
                    >
                      ✓
                    </div>
                  </div>

                  <div class="p-4">
                    <div class="flex items-start justify-between gap-2">
                      <h3 class="text-sm font-bold text-slate-800">
                        {{ i18nStore.templateName(template) }}
                      </h3>

                      <span
                        class="shrink-0 rounded-md px-2 py-1 text-[10px] font-semibold"
                        :class="accessBadgeClass(template.access_level)"
                      >
                        {{ accessLabel(template.access_level) }}
                      </span>
                    </div>

                    <p
                      class="mt-2 line-clamp-2 text-xs leading-5 text-slate-400"
                    >
                      {{ i18nStore.templateDescription(template) }}
                    </p>

                    <p
                      v-if="!template.can_use"
                      class="mt-3 text-[11px] font-medium"
                      :class="
                        template.lock_reason === 'email_verification'
                          ? 'text-emerald-600'
                          : 'text-amber-600'
                      "
                    >
                      🔒
                      {{
                        template.lock_reason === "email_verification"
                          ? i18nStore.t("templates.verifyEmailToUnlock")
                          : i18nStore.t("templates.premiumRequired")
                      }}
                    </p>
                  </div>
                </button>
              </div>

              <div
                v-else
                class="rounded-xl border border-dashed border-slate-200 bg-slate-50 p-8 text-center text-sm text-slate-400"
              >
                {{ i18nStore.t("portfolio.noTemplatesNow") }}
              </div>

              <div
                v-if="basicError"
                class="mt-4 rounded-lg border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
              >
                {{ basicError }}
              </div>

              <div class="mt-5 flex justify-end border-t border-slate-100 pt-5">
                <button
                  type="button"
                  :disabled="savingBasic"
                  class="rounded-lg bg-violet-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-violet-700 disabled:cursor-not-allowed disabled:opacity-60"
                  @click="saveBasic"
                >
                  {{
                    i18nStore.t(
                      savingBasic
                        ? "portfolio.saving"
                        : "portfolio.saveBasicInformation",
                    )
                  }}
                </button>
              </div>
            </div>
          </section>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
import { reactive, ref, defineComponent, h, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "../../api/axios";
import { useI18nStore } from "../../stores/i18n";

const route = useRoute();
const router = useRouter();
const i18nStore = useI18nStore();
const portfolioId = route.params.id;

const activeSection = ref("overview");

const Field = defineComponent({
  props: {
    modelValue: { type: [String, Number], default: "" },
    label: { type: String, default: "" },
    placeholder: { type: String, default: "" },
    type: { type: String, default: "text" },
  },
  emits: ["update:modelValue"],
  setup(props, { emit }) {
    return () =>
      h("div", {}, [
        h(
          "label",
          {
            class: "block text-sm font-semibold text-slate-700",
          },
          props.label,
        ),
        h("input", {
          value: props.modelValue,
          type: props.type,
          placeholder: props.placeholder,
          class:
            "mt-1.5 w-full rounded-lg border border-slate-200 bg-white px-3.5 py-2.5 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-400 focus:bg-white focus:ring-2 focus:ring-violet-100",
          onInput: (event) => emit("update:modelValue", event.target.value),
        }),
      ]);
  },
});

const EmptyState = defineComponent({
  props: {
    text: String,
  },
  setup(props) {
    return () =>
      h(
        "div",
        {
          class:
            "rounded-xl border border-dashed border-slate-200 p-6 text-center text-sm text-slate-400",
        },
        props.text,
      );
  },
});

const basic = reactive({
  title: "",
  slug: "",
  bio: "",
  template: null,
});

const templates = ref([]);
const templatesLoading = ref(true);
const loading = ref(true);
const savingBasic = ref(false);
const actionLoading = ref(false);
const error = ref(null);
const basicError = ref(null);

const skills = ref([]);
const educations = ref([]);
const experiences = ref([]);
const projects = ref([]);
const social = ref(null);

const editing = reactive({
  skills: null,
  educations: null,
  experiences: null,
  projects: null,
});

const editForms = reactive({
  skills: {},
  educations: {},
  experiences: {},
  projects: {},
});

const skillForm = reactive({
  skill_name: "",
  skill_level_in_skill: 3,
});

const educationForm = reactive({
  edu: "",
});

const experienceForm = reactive({
  ex_company: "",
  ex_start_date: "",
  ex_end_date: "",
  ex_position: "",
  ex_description: "",
});

const projectForm = reactive({
  pro_name: "",
  pro_description: "",
  pro_image: "",
  pro_github_url: "",
  pro_techs: "",
  pro_live_demo_url: "",
  pro_start: "",
  pro_end: "",
});

const socialForm = reactive({
  sl_github: "",
  sl_linkedin: "",
  sl_personal_web: "",
});

const apiPaths = {
  skills: `/portfolios/${portfolioId}/skills/`,
  educations: `/portfolios/${portfolioId}/educations/`,
  experiences: `/portfolios/${portfolioId}/experiences/`,
  projects: `/portfolios/${portfolioId}/projects/`,
  social: `/portfolios/${portfolioId}/social-links/`,
};

const getList = async (key) => {
  const response = await api.get(apiPaths[key]);
  return Array.isArray(response.data)
    ? response.data
    : response.data.results || [];
};

const handleApiError = (err, fallback) => {
  console.error(err);
  const data = err.response?.data;

  if (data && typeof data === "object") {
    const firstError = Object.values(data).flat().find(Boolean);
    error.value = firstError || fallback;
  } else {
    error.value = fallback;
  }
};

const loadAll = async () => {
  loading.value = true;
  error.value = null;
  basicError.value = null;

  loadTemplates();

  try {
    const portfolioResponse = await api.get(`/portfolios/${portfolioId}/`);

    const portfolio = portfolioResponse.data;

    basic.title = portfolio.title || "";
    basic.slug = portfolio.slug || "";
    basic.bio = portfolio.bio || "";
    basic.template = portfolio.template || null;

    const [skillsData, educationData, experienceData, projectsData] =
      await Promise.all([
        getList("skills"),
        getList("educations"),
        getList("experiences"),
        getList("projects"),
      ]);

    skills.value = skillsData;
    educations.value = educationData;
    experiences.value = experienceData;
    projects.value = projectsData;

    try {
      const response = await api.get(apiPaths.social);

      social.value = response.data;

      socialForm.sl_github = response.data.sl_github || "";
      socialForm.sl_linkedin = response.data.sl_linkedin || "";
      socialForm.sl_personal_web = response.data.sl_personal_web || "";
    } catch (socialError) {
      if (socialError.response?.status === 404) {
        social.value = null;
      } else {
        throw socialError;
      }
    }
  } catch (err) {
    console.error("Failed to load portfolio:", err);

    error.value =
      err.response?.data?.detail || i18nStore.t("portfolio.unableToLoad");
  } finally {
    loading.value = false;
  }
};

const loadTemplates = async () => {
  templatesLoading.value = true;
  basicError.value = null;

  try {
    const response = await api.get("/themes/");

    const data = response.data;

    templates.value = Array.isArray(data)
      ? data
      : Array.isArray(data?.results)
        ? data.results
        : [];

    if (!templates.value.length) {
      basicError.value = i18nStore.t("portfolio.noTemplatesNow");
      return;
    }

    if (basic.template) {
      const current = templates.value.find(
        (item) => item.id === basic.template,
      );

      if (!current) {
        basic.template = null;
      }
    }
  } catch (err) {
    console.error("Failed to load templates:", err);

    templates.value = [];

    basicError.value =
      err.response?.data?.detail ||
      i18nStore.t("portfolio.unableToLoadTemplates");
  } finally {
    templatesLoading.value = false;
  }
};

const accessLabel = (level) => {
  if (level === "premium") return i18nStore.t("templates.premium");
  if (level === "verified") return i18nStore.t("templates.verified");
  return i18nStore.t("templates.free");
};

const accessBadgeClass = (level) => {
  if (level === "premium") return "bg-amber-100 text-amber-700";
  if (level === "verified") return "bg-emerald-100 text-emerald-700";
  return "bg-violet-50 text-violet-500";
};

const selectTemplate = (template) => {
  if (!template.can_use) return;
  basic.template = template.id;
};

const saveBasic = async () => {
  basicError.value = null;

  if (!basic.title.trim()) {
    basicError.value = i18nStore.t("portfolio.enterTitle");
    return;
  }

  if (!basic.slug.trim()) {
    basicError.value = i18nStore.t("portfolio.enterUrl");
    return;
  }

  if (!basic.template) {
    basicError.value = i18nStore.t("portfolio.chooseAvailableTemplate");
    return;
  }

  const selectedTemplate = templates.value.find(
    (template) => template.id === basic.template,
  );

  if (!selectedTemplate?.can_use) {
    basicError.value = i18nStore.t("portfolio.templateUnavailable");
    return;
  }

  savingBasic.value = true;

  try {
    await api.patch(`/portfolios/${portfolioId}/`, {
      title: basic.title.trim(),
      slug: basic.slug.trim(),
      bio: basic.bio.trim(),
      template: basic.template,
    });
  } catch (err) {
    console.error("Failed to save basic information:", err);
    const data = err.response?.data;
    const firstError =
      data && typeof data === "object"
        ? Object.values(data).flat().find(Boolean)
        : null;

    basicError.value = firstError || i18nStore.t("portfolio.unableToSave");
  } finally {
    savingBasic.value = false;
  }
};

const resetSkillForm = () => {
  skillForm.skill_name = "";
  skillForm.skill_level_in_skill = 3;
};

const addSkill = async () => {
  error.value = null;

  if (!skillForm.skill_name.trim()) {
    error.value = i18nStore.t("portfolio.enterSkill");
    return;
  }

  actionLoading.value = true;

  try {
    const response = await api.post(apiPaths.skills, {
      skill_name: skillForm.skill_name.trim(),
      skill_level_in_skill: skillForm.skill_level_in_skill,
    });

    skills.value.push(response.data);
    resetSkillForm();
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableAddSkill"));
  } finally {
    actionLoading.value = false;
  }
};

const addEducation = async () => {
  error.value = null;

  if (!educationForm.edu.trim()) {
    error.value = i18nStore.t("portfolio.enterEducation");
    return;
  }

  actionLoading.value = true;

  try {
    const response = await api.post(apiPaths.educations, {
      edu: educationForm.edu.trim(),
    });

    educations.value.push(response.data);
    educationForm.edu = "";
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableAddEducation"));
  } finally {
    actionLoading.value = false;
  }
};

const addExperience = async () => {
  error.value = null;

  if (!experienceForm.ex_company.trim()) {
    error.value = i18nStore.t("portfolio.enterCompany");
    return;
  }

  if (!experienceForm.ex_position.trim()) {
    error.value = i18nStore.t("portfolio.enterPosition");
    return;
  }

  if (!experienceForm.ex_start_date) {
    error.value = i18nStore.t("portfolio.selectStartDate");
    return;
  }

  actionLoading.value = true;

  try {
    const response = await api.post(apiPaths.experiences, {
      ex_company: experienceForm.ex_company.trim(),
      ex_start_date: experienceForm.ex_start_date,
      ex_end_date: experienceForm.ex_end_date || null,
      ex_position: experienceForm.ex_position.trim(),
      ex_description: experienceForm.ex_description.trim(),
    });

    experiences.value.push(response.data);

    Object.assign(experienceForm, {
      ex_company: "",
      ex_start_date: "",
      ex_end_date: "",
      ex_position: "",
      ex_description: "",
    });
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableAddExperience"));
  } finally {
    actionLoading.value = false;
  }
};

const addProject = async () => {
  error.value = null;

  if (!projectForm.pro_name.trim()) {
    error.value = i18nStore.t("portfolio.enterProject");
    return;
  }

  if (!projectForm.pro_github_url.trim()) {
    error.value = i18nStore.t("portfolio.enterGithub");
    return;
  }

  if (!projectForm.pro_techs.trim()) {
    error.value = i18nStore.t("portfolio.enterTechnologies");
    return;
  }

  if (!projectForm.pro_start) {
    error.value = i18nStore.t("portfolio.selectProjectStart");
    return;
  }

  actionLoading.value = true;

  try {
    const response = await api.post(apiPaths.projects, {
      pro_name: projectForm.pro_name.trim(),
      pro_description: projectForm.pro_description.trim(),
      pro_image: projectForm.pro_image.trim() || null,
      pro_github_url: projectForm.pro_github_url.trim(),
      pro_techs: projectForm.pro_techs.trim(),
      pro_live_demo_url: projectForm.pro_live_demo_url.trim() || null,
      pro_start: projectForm.pro_start,
      pro_end: projectForm.pro_end || null,
    });

    projects.value.push(response.data);

    Object.assign(projectForm, {
      pro_name: "",
      pro_description: "",
      pro_image: "",
      pro_github_url: "",
      pro_techs: "",
      pro_live_demo_url: "",
      pro_start: "",
      pro_end: "",
    });
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableAddProject"));
  } finally {
    actionLoading.value = false;
  }
};

const startEdit = (type, item) => {
  editing[type] = item.id;
  editForms[type][item.id] = JSON.parse(JSON.stringify(item));
  error.value = null;
};

const cancelEdit = (type) => {
  const id = editing[type];

  if (id) {
    delete editForms[type][id];
  }

  editing[type] = null;
};

const replaceItem = (collection, id, data) => {
  const index = collection.value.findIndex((item) => item.id === id);

  if (index !== -1) {
    collection.value[index] = data;
  }
};

const saveEdit = async (type, id) => {
  error.value = null;

  const draft = editForms[type][id];

  if (!draft) return;

  const payloads = {
    skills: {
      skill_name: draft.skill_name?.trim(),
      skill_level_in_skill: Number(draft.skill_level_in_skill),
    },

    educations: {
      edu: draft.edu?.trim(),
    },

    experiences: {
      ex_company: draft.ex_company?.trim(),
      ex_start_date: draft.ex_start_date,
      ex_end_date: draft.ex_end_date || null,
      ex_position: draft.ex_position?.trim(),
      ex_description: draft.ex_description?.trim(),
    },

    projects: {
      pro_name: draft.pro_name?.trim(),
      pro_description: draft.pro_description?.trim(),
      pro_image: draft.pro_image?.trim() || null,
      pro_github_url: draft.pro_github_url?.trim(),
      pro_techs: draft.pro_techs?.trim(),
      pro_live_demo_url: draft.pro_live_demo_url?.trim() || null,
      pro_start: draft.pro_start,
      pro_end: draft.pro_end || null,
    },
  };

  if (type === "skills" && !payloads.skills.skill_name) {
    error.value = i18nStore.t("portfolio.enterSkill");
    return;
  }

  if (type === "educations" && !payloads.educations.edu) {
    error.value = i18nStore.t("portfolio.enterEducation");
    return;
  }

  if (type === "experiences") {
    if (
      !payloads.experiences.ex_company ||
      !payloads.experiences.ex_position ||
      !payloads.experiences.ex_start_date
    ) {
      error.value = i18nStore.t("portfolio.selectStartDate");
      return;
    }
  }

  if (type === "projects") {
    if (
      !payloads.projects.pro_name ||
      !payloads.projects.pro_github_url ||
      !payloads.projects.pro_techs ||
      !payloads.projects.pro_start
    ) {
      error.value = i18nStore.t("portfolio.enterProject");
      return;
    }
  }

  actionLoading.value = true;

  try {
    const response = await api.patch(
      `${apiPaths[type]}${id}/`,
      payloads[type],
    );

    const collections = {
      skills,
      educations,
      experiences,
      projects,
    };

    replaceItem(collections[type], id, response.data);
    cancelEdit(type);
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableToSave"));
  } finally {
    actionLoading.value = false;
  }
};

const deleteItem = async (type, id) => {
  error.value = null;
  actionLoading.value = true;

  try {
    await api.delete(`${apiPaths[type]}${id}/`);

    const collections = {
      skills,
      educations,
      experiences,
      projects,
    };

    const index = collections[type].value.findIndex(
      (item) => item.id === id,
    );

    if (index !== -1) {
      collections[type].value.splice(index, 1);
    }
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableRemove"));
  } finally {
    actionLoading.value = false;
  }
};

const saveSocial = async () => {
  error.value = null;
  actionLoading.value = true;

  const payload = {
    sl_github: socialForm.sl_github.trim() || null,
    sl_linkedin: socialForm.sl_linkedin.trim() || null,
    sl_personal_web: socialForm.sl_personal_web.trim() || null,
  };

  try {
    if (social.value) {
      const response = await api.patch(
        `${apiPaths.social}${social.value.id}/`,
        payload,
      );

      social.value = response.data;
    } else {
      const response = await api.post(apiPaths.social, payload);

      social.value = response.data;
    }
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableToSave"));
  } finally {
    actionLoading.value = false;
  }
};

const deleteSocial = async () => {
  if (!social.value) return;

  error.value = null;
  actionLoading.value = true;

  try {
    await api.delete(`${apiPaths.social}${social.value.id}/`);

    social.value = null;
    socialForm.sl_github = "";
    socialForm.sl_linkedin = "";
    socialForm.sl_personal_web = "";
  } catch (err) {
    handleApiError(err, i18nStore.t("portfolio.unableRemove"));
  } finally {
    actionLoading.value = false;
  }
};

onMounted(loadAll);
</script>