<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">
    <!-- Sidebar -->

    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <!-- Main Area -->

    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <!-- Header -->

      <DashboardHeader />

      <!-- Content -->

      <div class="mx-auto max-w-7xl px-6 py-8">
        <!-- Page heading -->

        <div class="mb-8">
          <p class="text-sm font-medium text-violet-400">
            {{ i18nStore.t("dashboard.overview") }}
          </p>

          <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
            {{ i18nStore.t("dashboard.workspace") }}
          </h1>

          <p class="mt-2 text-sm text-slate-400">
            {{ i18nStore.t("dashboard.workspaceDescription") }}
          </p>
        </div>

        <!-- Loading -->

        <div
          v-if="loading"
          class="rounded-3xl border border-slate-100 bg-white p-10 text-center shadow-sm"
        >
          <p class="text-sm text-slate-400">
            {{ i18nStore.t("dashboard.loadingPortfolio") }}
          </p>
        </div>

        <!-- Error -->

        <div
          v-else-if="error"
          class="rounded-3xl border border-red-100 bg-red-50 p-6"
        >
          <p class="text-sm font-medium text-red-600">
            {{ i18nStore.t("dashboard.failedToLoadPortfolio") }}
          </p>

          <p class="mt-1 text-sm text-red-400">
            {{ error }}
          </p>
        </div>

        <!-- Portfolio -->

        <PortfolioEmpty v-else-if="!portfolio" />

        <PortfolioCard v-else :portfolio="portfolio" />
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

import api from "../api/axios";
import { useI18nStore } from "../stores/i18n";

import DashboardSidebar from "../components/Dashboard/DashboardSidebar.vue";

import DashboardHeader from "../components/Dashboard/DashboardHeader.vue";

import PortfolioEmpty from "../components/Dashboard/PortfolioEmpty.vue";

import PortfolioCard from "../components/Dashboard/PortfolioCard.vue";

/*
 * Sidebar state
 *
 * false = باز
 * true  = بسته
 */

const sidebarCollapsed = ref(false);

/*
 * Portfolio state
 */

const portfolio = ref(null);

const loading = ref(true);

const error = ref(null);
const i18nStore = useI18nStore();

/*
 * Load user's portfolio
 */

const loadPortfolio = async () => {
  loading.value = true;
  error.value = null;

  try {
    const response = await api.get("/portfolios/");

    const portfolios = response.data;

    /*
     * فعلاً اولین Portfolio کاربر را نمایش می‌دهیم.
     *
     * چون در طراحی نهایی قرار است هر User
     * فقط یک Portfolio داشته باشد.
     */

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
