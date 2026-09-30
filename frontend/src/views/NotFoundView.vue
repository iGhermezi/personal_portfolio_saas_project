<script setup>
import { useRouter } from "vue-router";
import { useI18nStore } from "../stores/i18n";

const router = useRouter();
const i18nStore = useI18nStore();
</script>

<template>
  <div
    class="flex min-h-screen items-center justify-center bg-[#faf9ff] px-6 dark:bg-[#100b1c]"
  >
    <div
      class="w-full max-w-lg rounded-[28px] border border-violet-100 bg-white p-8 text-center shadow-sm"
    >
      <p
        class="text-sm font-semibold uppercase tracking-[0.3em] text-violet-400"
      >
        404
      </p>
      <h1 class="mt-3 text-4xl font-bold tracking-tight text-slate-900">
        {{ i18nStore.t("publicPortfolio.pageNotFound") }}
      </h1>
      <p class="mt-3 text-sm leading-6 text-slate-400">
        {{ i18nStore.t("publicPortfolio.notFoundDescription") }}
      </p>

      <div class="mt-7 flex flex-col gap-3 sm:flex-row sm:justify-center">
        <button
          type="button"
          class="rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white transition hover:bg-violet-500"
          @click="router.push('/')"
        >
          {{ i18nStore.t("publicPortfolio.backHome") }}
        </button>
        <button
          type="button"
          class="rounded-full border border-slate-200 px-7 py-3 text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
          @click="router.push('/dashboard')"
        >
          {{ i18nStore.t("dashboard.dashboard") }}
        </button>
      </div>
    </div>
  </div>
</template>
