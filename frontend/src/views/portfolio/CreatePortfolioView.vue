<template>
  <div class="min-h-screen bg-[#faf9ff]">
    <!-- Main Site Sidebar -->
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <!-- Page Content -->
    <div
      class="min-h-screen transition-all duration-300"
      :class="sidebarCollapsed ? 'pl-[78px]' : 'pl-64'"
    >
      <main class="mx-auto max-w-5xl px-6 py-8 lg:px-10">
        <!-- Header -->
        <div class="mb-8">
          <p class="text-sm font-medium text-violet-400">
            {{ i18nStore.t("portfolio.createStep") }}
          </p>

          <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
            {{ i18nStore.t("portfolio.createTitle") }}
          </h1>

          <p class="mt-2 text-sm text-slate-400">
            {{ i18nStore.t("portfolio.createDescription") }}
          </p>
        </div>

        <!-- Form -->
        <form
          class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm"
          @submit.prevent="createPortfolio"
        >
          <!-- Title -->
          <div>
            <label
              for="title"
              class="block text-sm font-semibold text-slate-700"
            >
              {{ i18nStore.t("portfolio.title") }}
            </label>

            <input
              id="title"
              v-model="form.title"
              type="text"
              :placeholder="i18nStore.t('portfolio.titlePlaceholder')"
              class="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm text-slate-800 outline-none transition focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
            />
          </div>

          <!-- Slug -->
          <div class="mt-6">
            <label
              for="slug"
              class="block text-sm font-semibold text-slate-700"
            >
              {{ i18nStore.t("portfolio.url") }}
            </label>

            <input
              id="slug"
              v-model="form.slug"
              type="text"
              :placeholder="i18nStore.t('portfolio.slugPlaceholder')"
              class="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm text-slate-800 outline-none transition focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
            />

            <p class="mt-2 text-xs text-slate-400">
              {{ i18nStore.t("portfolio.urlDescription") }}
            </p>
          </div>

          <!-- Bio -->
          <div class="mt-6">
            <label
              for="bio"
              class="block text-sm font-semibold text-slate-700"
            >
              {{ i18nStore.t("portfolio.shortBio") }}
            </label>

            <textarea
              id="bio"
              v-model="form.bio"
              rows="5"
              :placeholder="i18nStore.t('portfolio.bioPlaceholder')"
              class="mt-2 w-full resize-none rounded-2xl border border-slate-200 px-4 py-3 text-sm text-slate-800 outline-none transition focus:border-violet-300 focus:ring-4 focus:ring-violet-50"
            />
          </div>

          <!-- Templates -->
          <div class="mt-8">
            <div>
              <h2 class="text-sm font-semibold text-slate-700">
                {{ i18nStore.t("portfolio.chooseTemplate") }}
              </h2>

              <p class="mt-1 text-xs text-slate-400">
                {{ i18nStore.t("portfolio.templateAccessDescription") }}
              </p>
            </div>

            <!-- Loading -->
            <div
              v-if="templatesLoading"
              class="mt-4 rounded-2xl border border-slate-100 bg-slate-50 p-6 text-center"
            >
              <p class="text-sm text-slate-400">
                {{ i18nStore.t("portfolio.loadingTemplates") }}
              </p>
            </div>

            <!-- Templates -->
            <div
              v-else-if="templates.length"
              class="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3"
            >
              <button
                v-for="template in templates"
                :key="template.id"
                type="button"
                class="overflow-hidden rounded-2xl border text-left transition hover:-translate-y-0.5 hover:shadow-md"
                :class="
                  form.template === template.id
                    ? 'border-violet-400 ring-4 ring-violet-50'
                    : 'border-slate-200'
                "
                @click="form.template = template.id"
              >
                <div
                  class="flex h-36 items-center justify-center bg-slate-50"
                >
                  <img
                    v-if="template.preview_img"
                    :src="template.preview_img"
                    :alt="i18nStore.templateName(template)"
                    class="h-full w-full object-cover"
                  />

                  <span
                    v-else
                    class="text-3xl text-violet-300"
                  >
                    ✦
                  </span>
                </div>

                <div class="p-4">
                  <h3 class="text-sm font-semibold text-slate-800">
                    {{ i18nStore.templateName(template) }}
                  </h3>

                  <p
                    class="mt-1 line-clamp-2 text-xs leading-5 text-slate-400"
                  >
                    {{ i18nStore.templateDescription(template) }}
                  </p>

                  <span
                    class="mt-3 inline-block rounded-full bg-violet-50 px-3 py-1 text-[11px] font-medium text-violet-500"
                  >
                    {{
                      i18nStore.t(
                        template.access_level === "premium"
                          ? "templates.premium"
                          : template.access_level === "verified"
                            ? "templates.verified"
                            : "templates.free",
                      )
                    }}
                  </span>
                </div>
              </button>
            </div>

            <!-- No templates -->
            <div
              v-else
              class="mt-4 rounded-2xl border border-slate-100 bg-slate-50 p-6 text-center"
            >
              <p class="text-sm text-slate-400">
                {{ i18nStore.t("portfolio.noTemplatesForAccount") }}
              </p>
            </div>
          </div>

          <!-- Error -->
          <div
            v-if="error"
            class="mt-6 rounded-2xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
          >
            {{ error }}
          </div>

          <!-- Actions -->
          <div
            class="mt-8 flex flex-col-reverse gap-3 sm:flex-row sm:justify-end"
          >
            <button
              type="button"
              class="rounded-lg px-6 py-3 text-sm font-semibold text-slate-500 transition hover:bg-slate-50"
              @click="router.back()"
            >
              {{ i18nStore.t("common.cancel") }}
            </button>

            <button
              type="submit"
              :disabled="loading || templatesLoading"
              class="rounded-lg bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:-translate-y-0.5 hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {{
                loading
                  ? i18nStore.t("portfolio.creatingPortfolio")
                  : `${i18nStore.t("portfolio.continue")} →`
              }}
            </button>
          </div>
        </form>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";

import api from "../../api/axios";
import { useI18nStore } from "../../stores/i18n";
import DashboardSidebar from "../../components/Dashboard/DashboardSidebar.vue";

const router = useRouter();
const i18nStore = useI18nStore();

const sidebarCollapsed = ref(true);

const form = reactive({
  title: "",
  slug: "",
  bio: "",
  template: null,
});

const templates = ref([]);
const templatesLoading = ref(true);

const loading = ref(false);
const error = ref(null);

const loadTemplates = async () => {
  templatesLoading.value = true;
  error.value = null;

  try {
    const response = await api.get("/themes/");

    templates.value = Array.isArray(response.data)
      ? response.data
      : response.data.results || [];
  } catch (err) {
    console.error("Failed to load templates:", err);

    error.value =
      err.response?.data?.detail ||
      i18nStore.t("portfolio.unableToLoadTemplates");
  } finally {
    templatesLoading.value = false;
  }
};

const createPortfolio = async () => {
  error.value = null;

  if (!form.title.trim()) {
    error.value = i18nStore.t("portfolio.enterTitle");
    return;
  }

  if (!form.slug.trim()) {
    error.value = i18nStore.t("portfolio.enterUrl");
    return;
  }

  if (!form.template) {
    error.value = i18nStore.t("portfolio.chooseTemplate");
    return;
  }

  loading.value = true;

  try {
    const response = await api.post("/portfolios/", {
      title: form.title.trim(),
      slug: form.slug.trim(),
      bio: form.bio.trim(),
      template: form.template,
    });

    const portfolioId = response.data?.id;

    if (!portfolioId) {
      throw new Error(i18nStore.t("portfolio.idMissing"));
    }

    await router.push(`/portfolio/${portfolioId}/setup`);
  } catch (err) {
    console.error("Failed to create portfolio:", err);

    const data = err.response?.data;

    if (data && typeof data === "object") {
      const firstError = Object.values(data).flat().find(Boolean);

      error.value =
        firstError || i18nStore.t("portfolio.unableToCreate");
    } else {
      error.value = i18nStore.t("portfolio.unableToCreate");
    }
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  loadTemplates();
});
</script>