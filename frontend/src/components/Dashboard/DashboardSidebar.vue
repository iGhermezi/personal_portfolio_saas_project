<template>
  <aside
    class="fixed left-0 top-0 z-50 flex h-screen flex-col border-r border-violet-100 bg-white text-slate-700 transition-all duration-300"
    :class="collapsed ? 'w-[78px]' : 'w-64'"
  >
    <!-- Logo -->
    <div
      class="flex h-20 shrink-0 items-center border-b border-violet-50 px-5"
      :class="collapsed ? 'justify-center' : ''"
    >
      <div
        class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-violet-400"
      >
        <span class="font-black text-white">P</span>
      </div>

      <span
        v-if="!collapsed"
        class="ml-4 text-lg font-bold tracking-tight text-slate-800"
      >
        {{ i18nStore.t("common.appName") }}
      </span>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 px-3 py-6">
      <div
        v-for="item in navigation"
        :key="item.name"
        class="mb-2"
      >
        <router-link
          :to="item.to"
          class="group flex w-full items-center rounded-xl px-3 py-3 text-sm font-medium text-slate-600 transition hover:bg-violet-50 hover:text-violet-500"
          :class="collapsed ? 'justify-center' : ''"
        >
          <span
            class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-sm text-slate-600 transition group-hover:bg-violet-100 group-hover:text-violet-500"
          >
            {{ item.icon }}
          </span>

          <span
            v-if="!collapsed"
            class="ml-4 whitespace-nowrap text-slate-700"
          >
            {{ item.name }}
          </span>
        </router-link>
      </div>

      <!-- Upgrade -->
      <router-link
        to="/upgrade"
        class="mt-4 flex w-full items-center rounded-xl bg-violet-50 px-3 py-3 text-sm font-semibold text-violet-600 transition hover:bg-violet-100"
        :class="collapsed ? 'justify-center' : ''"
      >
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-violet-100 text-violet-600"
        >
          ✦
        </span>

        <span
          v-if="!collapsed"
          class="ml-4 whitespace-nowrap"
        >
          {{ i18nStore.t("dashboard.upgrade") }}
        </span>
      </router-link>
    </nav>

    <!-- Bottom -->
    <div class="shrink-0 border-t border-violet-50 p-3">
      <!-- Profile -->
      <router-link
        to="/profile"
        class="flex items-center rounded-xl px-3 py-3 transition hover:bg-violet-50"
        :class="collapsed ? 'justify-center' : ''"
      >
        <div
          class="flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-full bg-violet-100 text-sm font-bold text-violet-500"
        >
          {{ userInitial }}
        </div>

        <div
          v-if="!collapsed"
          class="ml-4 min-w-0"
        >
          <p class="truncate text-sm font-semibold text-slate-800">
            {{ authStore.user?.username || i18nStore.t("common.user") }}
          </p>

          <p class="truncate text-xs text-slate-500">
            {{ i18nStore.t("dashboard.profile") }}
          </p>
        </div>
      </router-link>

      <!-- Theme -->
      <button
        type="button"
        @click="themeStore.toggleTheme()"
        class="mt-2 flex w-full items-center rounded-xl px-3 py-3 text-sm font-medium text-slate-600 transition hover:bg-violet-50 hover:text-violet-500"
        :class="collapsed ? 'justify-center' : ''"
      >
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-slate-600"
        >
          {{ themeStore.isDark ? "☀" : "☾" }}
        </span>

        <span
          v-if="!collapsed"
          class="ml-4 whitespace-nowrap"
        >
          {{
            i18nStore.t(
              themeStore.isDark
                ? "common.lightMode"
                : "common.darkMode",
            )
          }}
        </span>
      </button>

      <!-- Logout -->
      <button
        type="button"
        @click="logout"
        class="mt-2 flex w-full items-center rounded-xl px-3 py-3 text-sm font-medium text-slate-600 transition hover:bg-red-50 hover:text-red-500"
        :class="collapsed ? 'justify-center' : ''"
      >
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-slate-600"
        >
          L
        </span>

        <span
          v-if="!collapsed"
          class="ml-4 whitespace-nowrap"
        >
          {{ i18nStore.t("common.logout") }}
        </span>
      </button>

      <!-- Collapse -->
      <button
        type="button"
        @click="emit('toggle')"
        class="mt-2 flex w-full items-center justify-center rounded-xl py-2.5 text-slate-500 transition hover:bg-slate-50 hover:text-slate-700"
      >
        <span class="text-lg">
          {{ collapsed ? "→" : "←" }}
        </span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { useRouter } from "vue-router";

import api from "../../api/axios";
import { useThemeStore } from "../../stores/theme";
import { useAuthStore } from "../../stores/auth";
import { useI18nStore } from "../../stores/i18n";

defineProps({
  collapsed: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["toggle"]);

const router = useRouter();
const themeStore = useThemeStore();
const authStore = useAuthStore();
const i18nStore = useI18nStore();

const portfolioId = ref(null);

const navigation = computed(() => [
  {
    name: i18nStore.t("dashboard.dashboard"),
    icon: "⌂",
    to: "/dashboard",
  },
  {
    name: i18nStore.t("dashboard.myPortfolios"),
    icon: "▣",
    to: portfolioId.value
      ? `/portfolio/${portfolioId.value}/edit`
      : "/portfolio/create",
  },
  {
    name: i18nStore.t("common.templates"),
    icon: "◈",
    to: "/templates",
  },
]);

const userInitial = computed(() => {
  return (
    authStore.user?.username?.charAt(0)?.toUpperCase() ||
    i18nStore.t("common.user").charAt(0)
  );
});

const loadPortfolio = async () => {
  try {
    const response = await api.get("/portfolios/");

    const portfolios = Array.isArray(response.data)
      ? response.data
      : response.data.results || [];

    if (portfolios.length) {
      portfolioId.value = portfolios[0].id;
    }
  } catch (error) {
    console.error("Failed to load portfolio for sidebar:", error);
  }
};

const logout = () => {
  authStore.logout();
  router.push("/");
};

onMounted(() => {
  loadPortfolio();
});
</script>