<template>
  <div
    class="min-h-screen bg-[#faf9ff] px-5 py-5"
    :dir="i18nStore.isRTL ? 'rtl' : 'ltr'"
  >
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <DashboardHeader />

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
          <p class="text-sm font-semibold text-red-600">
            {{ i18nStore.t("dashboard.failedToLoadPortfolio") }}
          </p>

          <p class="mt-1 text-sm text-red-400">
            {{ error }}
          </p>
        </div>

        <!-- Dashboard -->
        <template v-else>
          <!-- Status cards -->
          <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <!-- Portfolio -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-400">
                    {{ i18nStore.t("dashboard.myPortfolios") }}
                  </p>

                  <p class="mt-2 text-2xl font-bold text-slate-900">
                    {{ portfolio ? "1" : "0" }}
                  </p>
                </div>

                <div
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-violet-50 text-violet-400"
                >
                  ✦
                </div>
              </div>

              <p class="mt-3 text-xs text-slate-400">
                {{
                  portfolio
                    ? i18nStore.t("dashboard.yourPortfolio")
                    : i18nStore.t("dashboard.emptyTitle")
                }}
              </p>
            </div>

            <!-- Verification -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-400">
                    {{ i18nStore.t("dashboard.verification") }}
                  </p>

                  <p
                    class="mt-2 text-lg font-bold"
                    :class="
                      authStore.user?.email_verified
                        ? 'text-emerald-500'
                        : 'text-amber-500'
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
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-500"
                >
                  ✓
                </div>
              </div>

              <p class="mt-3 text-xs text-slate-400">
                {{ authStore.user?.email }}
              </p>
            </div>

            <!-- Subscription -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-400">
                    {{ i18nStore.t("dashboard.subscription") }}
                  </p>

                  <p
                    class="mt-2 text-lg font-bold"
                    :class="
                      authStore.user?.has_active_subscription
                        ? 'text-violet-500'
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
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-violet-50 text-violet-500"
                >
                  ◆
                </div>
              </div>

              <router-link
                v-if="!authStore.user?.has_active_subscription"
                to="/upgrade"
                class="mt-3 inline-block text-xs font-semibold text-violet-400 hover:text-violet-500"
              >
                {{ i18nStore.t("dashboard.upgrade") }} →
              </router-link>

              <p
                v-else
                class="mt-3 text-xs font-medium text-violet-400"
              >
                {{ i18nStore.t("dashboard.activeSubscription") }}
              </p>
            </div>

            <!-- Status -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-5 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-xs font-medium text-slate-400">
                    {{ i18nStore.t("dashboard.status") }}
                  </p>

                  <p
                    class="mt-2 text-lg font-bold"
                    :class="
                      portfolio
                        ? 'text-emerald-500'
                        : 'text-slate-700'
                    "
                  >
                    {{
                      portfolio
                        ? i18nStore.t("dashboard.live")
                        : i18nStore.t("dashboard.notCreated")
                    }}
                  </p>
                </div>

                <div
                  class="flex h-10 w-10 items-center justify-center rounded-2xl bg-emerald-50 text-emerald-500"
                >
                  ●
                </div>
              </div>

              <p class="mt-3 text-xs text-slate-400">
                {{
                  portfolio
                    ? i18nStore.t("dashboard.portfolioAvailable")
                    : i18nStore.t("dashboard.createPortfolioFirst")
                }}
              </p>
            </div>
          </div>

          <!-- Main portfolio area -->
          <div class="mt-6">
            <PortfolioCard
              v-if="portfolio"
              :portfolio="portfolio"
            />

            <PortfolioEmpty v-else />
          </div>

          <!-- Quick actions -->
          <div class="mt-6 grid gap-6 lg:grid-cols-2">
            <!-- Quick actions -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-6 shadow-sm"
            >
              <div>
                <p class="text-xs font-medium text-violet-400">
                  {{ i18nStore.t("dashboard.quickActions") }}
                </p>

                <h2 class="mt-1 text-lg font-bold text-slate-900">
                  {{ i18nStore.t("dashboard.managePortfolio") }}
                </h2>
              </div>

              <div class="mt-5 grid gap-3 sm:grid-cols-2">
                <router-link
                  v-if="portfolio"
                  :to="`/portfolio/${portfolio.id}/edit`"
                  class="rounded-2xl border border-violet-100 bg-violet-50 px-4 py-4 transition hover:border-violet-200 hover:bg-violet-100"
                >
                  <p class="text-sm font-semibold text-slate-800">
                    {{ i18nStore.t("dashboard.editPortfolio") }}
                  </p>

                  <p class="mt-1 text-xs text-slate-400">
                    {{ i18nStore.t("dashboard.editPortfolioDescription") }}
                  </p>
                </router-link>

                <router-link
                  v-else
                  to="/portfolio/create"
                  class="rounded-2xl border border-violet-100 bg-violet-50 px-4 py-4 transition hover:border-violet-200 hover:bg-violet-100"
                >
                  <p class="text-sm font-semibold text-slate-800">
                    {{ i18nStore.t("common.createPortfolio") }}
                  </p>

                  <p class="mt-1 text-xs text-slate-400">
                    {{ i18nStore.t("dashboard.createPortfolioFirst") }}
                  </p>
                </router-link>

                <router-link
                  to="/profile"
                  class="rounded-2xl border border-slate-100 bg-slate-50 px-4 py-4 transition hover:border-violet-100 hover:bg-violet-50"
                >
                  <p class="text-sm font-semibold text-slate-800">
                    {{ i18nStore.t("dashboard.profile") }}
                  </p>

                  <p class="mt-1 text-xs text-slate-400">
                    {{ i18nStore.t("dashboard.viewProfile") }}
                  </p>
                </router-link>
              </div>
            </div>

            <!-- Next step -->
            <div
              class="rounded-3xl border border-violet-100 bg-white p-6 shadow-sm"
            >
              <p class="text-xs font-medium text-violet-400">
                {{ i18nStore.t("dashboard.nextStep") }}
              </p>

              <h2 class="mt-1 text-lg font-bold text-slate-900">
                {{
                  !portfolio
                    ? i18nStore.t("dashboard.createPortfolio")
                    : !authStore.user?.email_verified
                      ? i18nStore.t("dashboard.verifyEmail")
                      : !authStore.user?.has_active_subscription
                        ? i18nStore.t("dashboard.upgrade")
                        : i18nStore.t("dashboard.keepPortfolioUpdated")
                }}
              </h2>

              <p class="mt-2 text-sm leading-6 text-slate-400">
                {{
                  !portfolio
                    ? i18nStore.t("dashboard.createPortfolioFirst")
                    : !authStore.user?.email_verified
                      ? i18nStore.t("dashboard.verifyEmailDescription")
                      : !authStore.user?.has_active_subscription
                        ? i18nStore.t("dashboard.upgradeDescription")
                        : i18nStore.t("dashboard.keepPortfolioUpdatedDescription")
                }}
              </p>

              <router-link
                v-if="!portfolio"
                to="/portfolio/create"
                class="mt-5 inline-flex rounded-full bg-violet-400 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-500"
              >
                {{ i18nStore.t("common.createPortfolio") }}
              </router-link>

              <router-link
                v-else-if="!authStore.user?.has_active_subscription"
                to="/upgrade"
                class="mt-5 inline-flex rounded-full bg-violet-400 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-500"
              >
                {{ i18nStore.t("dashboard.upgrade") }}
              </router-link>

              <router-link
                v-else
                to="/profile"
                class="mt-5 inline-flex rounded-full bg-violet-400 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-500"
              >
                {{ i18nStore.t("dashboard.viewProfile") }}
              </router-link>
            </div>
          </div>
        </template>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../api/axios";
import { useAuthStore } from "../stores/auth";
import { useI18nStore } from "../stores/i18n";

import DashboardSidebar from "../components/Dashboard/DashboardSidebar.vue";
import DashboardHeader from "../components/Dashboard/DashboardHeader.vue";
import PortfolioEmpty from "../components/Dashboard/PortfolioEmpty.vue";
import PortfolioCard from "../components/Dashboard/PortfolioCard.vue";

const authStore = useAuthStore();
const i18nStore = useI18nStore();

const sidebarCollapsed = ref(false);
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
      Array.isArray(portfolios) && portfolios.length > 0
        ? portfolios[0]
        : null;
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