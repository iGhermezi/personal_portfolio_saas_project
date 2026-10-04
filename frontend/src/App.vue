<template>
  <div
    class="min-h-screen bg-[#faf9ff] text-slate-900 transition-colors duration-300 dark:bg-[#100b1c] dark:text-slate-100"
  >
    <router-view />

    <!-- Global language switcher -->
    <button
      type="button"
      @click="i18nStore.toggleLanguage()"
      class="fixed bottom-5 right-5 z-[100] rounded-lg border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-700 shadow-lg transition hover:-translate-y-0.5 hover:bg-slate-50 dark:border-slate-700 dark:bg-[#171124] dark:text-slate-100 dark:hover:bg-[#21182f]"
      :aria-label="
        i18nStore.language === 'en'
          ? i18nStore.t('common.switchToPersian')
          : i18nStore.t('common.switchToEnglish')
      "
    >
      {{ i18nStore.language === "en" ? "فا" : "EN" }}
    </button>

    <!-- Global toast -->
    <Transition name="toast">
      <div
        v-if="uiStore.toast.visible"
        class="fixed bottom-5 left-5 z-[100] max-w-sm rounded-2xl border px-5 py-3.5 text-sm font-medium shadow-xl backdrop-blur"
        :class="
          uiStore.toast.type === 'error'
            ? 'border-red-200 bg-red-50 text-red-700 dark:border-red-900/50 dark:bg-red-950/40 dark:text-red-300'
            : 'border-emerald-200 bg-emerald-50 text-emerald-700 dark:border-emerald-900/50 dark:bg-emerald-950/40 dark:text-emerald-300'
        "
      >
        <div class="flex items-center gap-3">
          <span>
            {{ uiStore.toast.type === "error" ? "!" : "✓" }}
          </span>

          <span>
            {{ uiStore.toast.message }}
          </span>

          <button
            type="button"
            :aria-label="i18nStore.t('common.close')"
            @click="uiStore.hideToast()"
            class="ml-2 opacity-60 transition hover:opacity-100"
          >
            ×
          </button>
        </div>
      </div>
    </Transition>

    <!-- Global loading indicator -->
    <Transition name="loading">
      <div
        v-if="uiStore.loading"
        class="fixed inset-x-0 top-0 z-[200] h-1 overflow-hidden bg-violet-100 dark:bg-violet-950"
      >
        <div
          class="h-full w-1/3 animate-[loading_1.2s_ease-in-out_infinite] rounded-full bg-violet-500"
        ></div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { onMounted } from "vue";

import { useI18nStore } from "./stores/i18n";
import { useUiStore } from "./stores/ui";

const i18nStore = useI18nStore();
const uiStore = useUiStore();

onMounted(() => {
  i18nStore.initializeLanguage();
});
</script>

<style scoped>
.toast-enter-active,
.toast-leave-active {
  transition: all 0.25s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(12px);
}

.loading-enter-active,
.loading-leave-active {
  transition: opacity 0.2s ease;
}

.loading-enter-from,
.loading-leave-to {
  opacity: 0;
}
</style>