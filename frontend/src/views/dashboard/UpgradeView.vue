<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <div class="mx-auto max-w-4xl px-6 py-8">
        <p class="text-sm font-medium text-violet-400">
          {{ i18nStore.t("templates.premium") }}
        </p>
        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          {{ i18nStore.t("premium.title") }}
        </h1>
        <p class="mt-2 text-sm text-slate-400">
          {{ i18nStore.t("premium.description") }}
        </p>

        <section
          class="mt-8 rounded-[28px] border border-violet-100 bg-white p-8 shadow-sm"
        >
          <div v-if="loading" class="text-sm text-slate-400">
            {{ i18nStore.t("premium.loading") }}
          </div>
          <template v-else>
            <div
              class="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between"
            >
              <div>
                <p
                  class="text-xs font-semibold uppercase tracking-widest text-violet-400"
                >
                  {{ i18nStore.t("premium.status") }}
                </p>
                <h2 class="mt-1 text-xl font-bold text-slate-800">
                  {{
                    i18nStore.t(
                      subscribed ? "premium.active" : "premium.inactive",
                    )
                  }}
                </h2>
                <p class="mt-2 text-sm text-slate-400">
                  {{
                    subscribed
                      ? i18nStore.t("premium.allTemplates")
                      : statusText
                  }}
                </p>
              </div>
              <span
                class="rounded-full px-4 py-2 text-sm font-semibold"
                :class="
                  subscribed
                    ? 'bg-emerald-50 text-emerald-600'
                    : 'bg-violet-50 text-violet-500'
                "
              >
                {{
                  i18nStore.t(
                    subscribed ? "premium.active" : "premium.manualApproval",
                  )
                }}
              </span>
            </div>

            <div
              class="mt-8 rounded-2xl border border-violet-100 bg-violet-50 p-5 text-sm leading-6 text-slate-600"
            >
              {{ i18nStore.t("premium.note") }}
            </div>

            <div class="mt-6 flex flex-wrap gap-3">
              <button
                v-if="!subscribed && requestStatus !== 'pending'"
                type="button"
                :disabled="requesting"
                class="rounded-lg bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-500 disabled:opacity-60"
                @click="requestPremium"
              >
                {{
                  i18nStore.t(
                    requesting ? "premium.sending" : "premium.request",
                  )
                }}
              </button>
              <span
                v-else-if="!subscribed"
                class="rounded-full border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-500"
                >{{ i18nStore.t("premium.pending") }}</span
              >
              <router-link
                to="/templates"
                class="rounded-lg border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-500 transition hover:bg-violet-100"
              >
                {{ i18nStore.t("premium.backToTemplates") }}
              </router-link>
            </div>
          </template>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../../api/axios";
import { useAuthStore } from "../../stores/auth";
import DashboardSidebar from "../../components/Dashboard/DashboardSidebar.vue";
import { useI18nStore } from "../../stores/i18n";

const authStore = useAuthStore();
const i18nStore = useI18nStore();
const sidebarCollapsed = ref(false);
const loading = ref(true);
const subscribed = ref(false);
const requestStatus = ref(null);
const requesting = ref(false);
const statusText = ref(i18nStore.t("premium.reviewDefault"));
onMounted(async () => {
  try {
    await authStore.getProfile();

    const { data } = await api.get("accounts/premium/request/");

    subscribed.value = authStore.hasSubscription;
    requestStatus.value = data.request_status || null;

    if (requestStatus.value === "pending") {
      statusText.value = i18nStore.t("premium.reviewPending");
    }
  } catch (error) {
    statusText.value =
      error.response?.data?.detail || i18nStore.t("premium.unableLoad");
  } finally {
    loading.value = false;
  }
});

const requestPremium = async () => {
  requesting.value = true;

  try {
    const { data } = await api.post("/accounts/premium/request/");

    await authStore.getProfile();

    subscribed.value = data.has_subscription ?? authStore.hasSubscription;
    requestStatus.value = data.request_status || "pending";

    statusText.value = data.detail || i18nStore.t("premium.reviewPending");
  } catch (error) {
    statusText.value =
      error.response?.data?.detail || i18nStore.t("premium.unableRequest");
  } finally {
    requesting.value = false;
  }
};
</script>
