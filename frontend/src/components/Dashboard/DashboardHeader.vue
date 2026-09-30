<template>
  <header
    class="flex items-center justify-between rounded-3xl border border-violet-100 bg-white px-6 py-4 shadow-[0_10px_40px_rgba(139,92,246,0.12)]"
  >
    <div>
      <p class="text-xs font-medium text-violet-400">
        {{ i18nStore.t("dashboard.dashboard") }}
      </p>
      <h1 class="mt-1 text-xl font-bold text-slate-800">
        {{ i18nStore.t("dashboard.welcomeBack") }} 👋
      </h1>
    </div>

    <router-link
      to="/profile"
      class="flex items-center gap-3 rounded-full p-1.5 pr-4 transition hover:bg-violet-50"
    >
      <div
        class="flex h-10 w-10 items-center justify-center overflow-hidden rounded-full bg-violet-100 font-semibold text-violet-500"
      >
        {{ initial }}
      </div>
      <div class="hidden text-left sm:block">
        <p class="text-sm font-semibold text-slate-800">
          {{ authStore.user?.username || i18nStore.t("common.user") }}
        </p>
        <p class="text-xs text-slate-400">
          {{ i18nStore.t("dashboard.viewProfile") }}
        </p>
      </div>
    </router-link>
  </header>
</template>

<script setup>
import { computed } from "vue";
import { useAuthStore } from "../../stores/auth";
import { useI18nStore } from "../../stores/i18n";

const authStore = useAuthStore();
const i18nStore = useI18nStore();

const initial = computed(() => {
  return (
    authStore.user?.username?.charAt(0)?.toUpperCase() ||
    i18nStore.t("common.user").charAt(0)
  );
});
</script>
