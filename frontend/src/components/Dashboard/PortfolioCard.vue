<template>
  <div
    class="overflow-hidden rounded-[28px] border border-violet-100 bg-white text-slate-900 shadow-sm"
  >
    <!-- Preview -->
    <div class="relative h-[320px] overflow-hidden bg-violet-50">
      <div class="absolute inset-8 rounded-2xl bg-white p-8 shadow-xl">
        <div class="h-4 w-32 rounded-full bg-violet-200"></div>

        <div class="mt-6 h-8 w-64 rounded-lg bg-slate-100"></div>

        <div
          class="mt-3 h-3 w-80 max-w-full rounded-full bg-slate-100"
        ></div>

        <div class="mt-8 grid grid-cols-3 gap-3">
          <div class="h-24 rounded-xl bg-violet-100"></div>
          <div class="h-24 rounded-xl bg-violet-50"></div>
          <div class="h-24 rounded-xl bg-violet-100"></div>
        </div>
      </div>
    </div>

    <!-- Portfolio info -->
    <div class="p-6 text-slate-900">
      <div
        class="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <!-- Portfolio title -->
        <div class="min-w-0">
          <p class="text-xs font-medium text-violet-500">
            {{ i18nStore.t("dashboard.yourPortfolio") }}
          </p>

          <h2 class="mt-1 truncate text-xl font-bold text-slate-900">
            {{ portfolio.title }}
          </h2>
        </div>

        <!-- Actions -->
        <div class="flex flex-wrap gap-3">
          <router-link
            :to="`/portfolio/${portfolio.id}/preview`"
            class="rounded-full bg-violet-500 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-600"
          >
            {{ i18nStore.t("dashboard.preview") }}
          </router-link>

          <router-link
            :to="`/portfolio/${portfolio.id}/edit`"
            class="rounded-full bg-violet-500 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-violet-600"
          >
            {{ i18nStore.t("dashboard.editPortfolio") }}
          </router-link>
        </div>
      </div>

      <!-- Public URL -->
      <div
        class="mt-6 rounded-2xl bg-slate-50 p-4"
      >
        <p class="text-xs font-medium text-slate-500">
          {{ i18nStore.t("dashboard.publicPortfolio") }}
        </p>

        <a
          :href="publicUrl"
          target="_blank"
          rel="noopener noreferrer"
          class="mt-1 block truncate text-sm font-medium text-violet-600 hover:text-violet-700"
        >
          {{ publicUrl }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useI18nStore } from "../../stores/i18n";

const i18nStore = useI18nStore();

const props = defineProps({
  portfolio: {
    type: Object,
    required: true,
  },
});

const publicUrl = computed(() => {
  return `${window.location.origin}/portfolio/${props.portfolio.slug}`;
});
</script>