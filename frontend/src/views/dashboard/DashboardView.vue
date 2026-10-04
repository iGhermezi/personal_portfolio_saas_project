<template>
  <div
    class="min-h-screen bg-[#faf9ff] px-5 py-5 text-slate-900"
    :dir="i18nStore.isRTL ? 'rtl' : 'ltr'"
  >
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <main
      class="min-h-[calc(100vh-40px)] text-slate-900 transition-all duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <DashboardHeader />

      <div class="mx-auto max-w-7xl px-6 py-8">
        <!-- Page heading -->
        <div class="mb-8">
          <p class="text-sm font-medium text-violet-500">
            {{ i18nStore.t("dashboard.overview") }}
          </p>

          <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
            {{ i18nStore.t("dashboard.workspace") }}
          </h1>

          <p class="mt-2 text-sm text-slate-500">
            {{ i18nStore.t("dashboard.workspaceDescription") }}
          </p>
        </div>

        <!-- Loading -->
        <div
          v-if="loading"
          class="rounded-3xl border border-slate-200 bg-white p-10 text-center shadow-sm"
        >
          <p class="text-sm text-slate-500">
            {{ i18nStore.t("dashboard.loadingPortfolio") }}
          </p>
        </div>

        <!-- Error -->
        <div
          v-else-if="error"
          class="rounded-3xl border border-red-100 bg-red-50 p-6"
        >
          <p class="text-sm font-semibold text-red-600">
            {{ i18nStore.t("dashboard.failedToLoadPortfolio") }}
          </p>

          <p class="mt-1 text-sm text-red-500">
            {{ error }}
          </p>
        </div>

        <!-- Dashboard -->
        <template v-else>
          <!-- Status cards -->
          <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <!-- Publication Status -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 text-slate-900 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-500">
                    {{ i18nStore.t("dashboard.publicationStatus") }}
                  </p>

                  <p
                    class="mt-2 text-lg font-bold"
                    :class="
                      portfolio?.is_published
                        ? 'text-emerald-600'
                        : 'text-amber-600'
                    "
                  >
                    {{
                      portfolio?.is_published
                        ? i18nStore.t("dashboard.published")
                        : i18nStore.t("dashboard.unpublished")
                    }}
                  </p>
                </div>

                <div
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-violet-50 text-violet-500"
                >
                  ●
                </div>
              </div>

              <p class="mt-3 text-xs text-slate-500">
                {{
                  portfolio?.is_published
                    ? i18nStore.t("dashboard.portfolioPublic")
                    : i18nStore.t("dashboard.portfolioNotPublic")
                }}
              </p>
            </div>

            <!-- Verification -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 text-slate-900 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-500">
                    {{ i18nStore.t("dashboard.verification") }}
                  </p>

                  <p
                    class="mt-2 text-lg font-bold"
                    :class="
                      authStore.user?.email_verified
                        ? 'text-emerald-600'
                        : 'text-amber-600'
                    "
                  >
                    {{
                      authStore.user?.email_verified
                        ? i18nStore.t("dashboard.verified")
                        : i18nStore.t("dashboard.notVerified")
                    }}
                  </p>
                </div>

                <div
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-600"
                >
                  ✓
                </div>
              </div>

              <p class="mt-3 truncate text-xs text-slate-500">
                {{ authStore.user?.email }}
              </p>
            </div>

            <!-- Subscription -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 text-slate-900 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-500">
                    {{ i18nStore.t("dashboard.subscription") }}
                  </p>

                  <p
                    class="mt-2 text-lg font-bold"
                    :class="
                      authStore.user?.has_active_subscription
                        ? 'text-violet-600'
                        : 'text-slate-700'
                    "
                  >
                    {{
                      authStore.user?.has_active_subscription
                        ? i18nStore.t("dashboard.premium")
                        : i18nStore.t("dashboard.free")
                    }}
                  </p>
                </div>

                <div
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-violet-50 text-violet-600"
                >
                  ◆
                </div>
              </div>

              <router-link
                v-if="!authStore.user?.has_active_subscription"
                to="/upgrade"
                class="mt-3 inline-block text-xs font-semibold text-violet-600 hover:text-violet-700"
              >
                {{ i18nStore.t("dashboard.upgrade") }} →
              </router-link>

              <p v-else class="mt-3 text-xs font-medium text-violet-600">
                {{ i18nStore.t("dashboard.activeSubscription") }}
              </p>
            </div>

            <!-- Current Template -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 text-slate-900 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-500">
                    {{ i18nStore.t("dashboard.currentTemplate") }}
                  </p>

                  <p class="mt-2 truncate text-lg font-bold text-violet-600">
                    {{
                      portfolio?.template_key
                        ? i18nStore.templateName({
                            template_key: portfolio.template_key,
                          })
                        : i18nStore.t("dashboard.noTemplate")
                    }}
                  </p>
                </div>

                <div
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-violet-50 text-violet-600"
                >
                  ◆
                </div>
              </div>

              <p class="mt-3 text-xs text-slate-500">
                {{
                  portfolio
                    ? i18nStore.t("dashboard.currentTemplateDescription")
                    : i18nStore.t("dashboard.createPortfolioFirst")
                }}
              </p>
            </div>
          </div>

          <!-- Main portfolio area -->
          <div class="mt-6">
            <PortfolioCard v-if="portfolio" :portfolio="portfolio" />

            <PortfolioEmpty v-else />
          </div>
        </template>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

import api from "../../api/axios";
import { useAuthStore } from "../../stores/auth";
import { useI18nStore } from "../../stores/i18n";

import DashboardSidebar from "../../components/Dashboard/DashboardSidebar.vue";
import DashboardHeader from "../../components/Dashboard/DashboardHeader.vue";
import PortfolioEmpty from "../../components/Dashboard/PortfolioEmpty.vue";
import PortfolioCard from "../../components/Dashboard/PortfolioCard.vue";

const authStore = useAuthStore();
const i18nStore = useI18nStore();

const sidebarCollapsed = ref(true);
const portfolio = ref(null);
const loading = ref(true);
const error = ref(null);

const loadPortfolio = async () => {
  loading.value = true;
  error.value = null;

  try {
    const response = await api.get("/portfolios/");

    const portfolios = response.data;

    portfolio.value =
      Array.isArray(portfolios) && portfolios.length > 0 ? portfolios[0] : null;
  } catch (err) {
    console.error("Failed to load portfolio:", err);

    error.value =
      err.response?.data?.detail ||
      i18nStore.t("dashboard.unableToLoadPortfolio");
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  loadPortfolio();
});
</script>
