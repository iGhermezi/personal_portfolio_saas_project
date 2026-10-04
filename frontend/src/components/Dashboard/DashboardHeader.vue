<template>
  <header
    class="flex min-h-[76px] items-center justify-between rounded-2xl border border-violet-100 bg-white px-5 py-4 text-slate-800 shadow-sm sm:px-6"
    :dir="i18nStore.isRTL ? 'rtl' : 'ltr'"
  >
    <!-- Welcome -->
    <div class="min-w-0">
      <p class="text-xs font-semibold uppercase tracking-wide text-violet-500">
        {{ i18nStore.t("dashboard.dashboard") }}
      </p>

      <h1 class="mt-1 truncate text-lg font-bold text-slate-800 sm:text-xl">
        {{ i18nStore.t("dashboard.welcome") }},
        {{ authStore.user?.username || i18nStore.t("common.user") }} 👋
      </h1>
    </div>

    <!-- Profile Button -->
    <router-link
      to="/profile"
      class="group flex shrink-0 items-center gap-3 rounded-xl border border-slate-200 bg-white px-3 py-2 transition-all duration-200 hover:border-violet-200 hover:bg-violet-50/50"
    >
      <!-- Avatar -->
      <div
        class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-lg bg-violet-100 text-sm font-bold text-violet-600 transition-colors group-hover:bg-violet-200"
      >
        {{ initial }}
      </div>

      <!-- User Info -->
      <div
        class="hidden min-w-0 sm:block"
        :class="i18nStore.isRTL ? 'text-right' : 'text-left'"
      >
        <p
          class="max-w-[130px] truncate text-sm font-semibold text-slate-800"
        >
          {{ authStore.user?.username || i18nStore.t("common.user") }}
        </p>

        <p class="text-[11px] text-slate-500">
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