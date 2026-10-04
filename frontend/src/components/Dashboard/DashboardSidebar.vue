<template>
  <aside
    class="fixed left-3 top-3 z-50 flex h-[calc(100vh-24px)] flex-col rounded-2xl border border-violet-100 bg-white text-slate-700 shadow-[0_10px_40px_rgba(139,92,246,0.10)] transition-[width] duration-300 ease-in-out"
    :class="collapsed ? 'w-[78px]' : 'w-64'"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
  >
    <!-- Logo -->
    <div
      class="flex h-20 shrink-0 items-center border-b border-violet-50 px-5"
      :class="collapsed ? 'justify-center' : 'gap-4'"
    >
      <div
        class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-violet-400"
      >
        <span class="font-black text-white">P</span>
      </div>

      <span
        class="overflow-hidden whitespace-nowrap text-lg font-bold tracking-tight text-slate-800 transition-all duration-200"
        :class="
          collapsed
            ? 'max-w-0 translate-x-2 opacity-0'
            : 'max-w-[160px] translate-x-0 opacity-100 delay-100'
        "
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
          v-slot="{ isActive }"
          :to="item.to"
          class="group flex w-full items-center rounded-xl px-3 py-3 text-sm font-medium transition-colors duration-200"
          :class="[
            collapsed ? 'justify-center' : 'gap-4',
            isActive
              ? 'bg-violet-50 text-violet-600'
              : 'text-slate-600 hover:bg-violet-50 hover:text-violet-600',
          ]"
        >
          <!-- Icon -->
          <span
            class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg text-sm transition-colors duration-200"
            :class="
              isActive
                ? 'bg-violet-100 text-violet-600'
                : 'bg-slate-50 text-slate-600 group-hover:bg-violet-100 group-hover:text-violet-600'
            "
          >
            {{ item.icon }}
          </span>

          <!-- Label -->
          <span
            class="overflow-hidden whitespace-nowrap transition-all duration-200"
            :class="
              collapsed
                ? 'max-w-0 translate-x-2 opacity-0'
                : 'max-w-[160px] translate-x-0 opacity-100 delay-100'
            "
          >
            {{ item.name }}
          </span>
        </router-link>
      </div>

      <!-- Upgrade -->
      <router-link
        v-slot="{ isActive }"
        to="/upgrade"
        class="group mt-4 flex w-full items-center rounded-xl px-3 py-3 text-sm font-semibold transition-colors duration-200"
        :class="[
          collapsed ? 'justify-center' : 'gap-4',
          isActive
            ? 'bg-violet-50 text-violet-600'
            : 'text-violet-600 hover:bg-violet-50',
        ]"
      >
        <!-- Upgrade Icon -->
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg text-lg transition-colors duration-200"
          :class="
            isActive
              ? 'bg-violet-100 text-violet-600'
              : 'bg-transparent text-violet-500 group-hover:bg-violet-50 group-hover:text-violet-600'
          "
        >
          ✦
        </span>

        <!-- Upgrade Label -->
        <span
          class="overflow-hidden whitespace-nowrap transition-all duration-200"
          :class="
            collapsed
              ? 'max-w-0 translate-x-2 opacity-0'
              : 'max-w-[160px] translate-x-0 opacity-100 delay-100'
          "
        >
          {{ i18nStore.t("dashboard.upgrade") }}
        </span>
      </router-link>
    </nav>

    <!-- Bottom Actions -->
    <div class="shrink-0 border-t border-violet-50 p-3">
      <!-- Profile -->
      <router-link
        to="/profile"
        class="group flex items-center rounded-xl px-3 py-3 transition-colors duration-200 hover:bg-violet-50"
        :class="collapsed ? 'justify-center' : 'gap-4'"
      >
        <!-- Profile Icon -->
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-violet-100 text-sm font-bold text-violet-600 transition-colors duration-200"
        >
          {{ userInitial }}
        </span>

        <!-- Profile Label -->
        <span
          class="overflow-hidden whitespace-nowrap text-sm font-medium text-slate-700 transition-all duration-200 group-hover:text-violet-600"
          :class="
            collapsed
              ? 'max-w-0 translate-x-2 opacity-0'
              : 'max-w-[160px] translate-x-0 opacity-100 delay-100'
          "
        >
          {{ i18nStore.t("common.profile") }}
        </span>
      </router-link>

      <!-- Theme -->
      <button
        type="button"
        class="group mt-2 flex w-full items-center rounded-xl px-3 py-3 text-sm font-medium text-slate-600 transition-colors duration-200 hover:bg-violet-50 hover:text-violet-500"
        :class="collapsed ? 'justify-center' : 'gap-4'"
        @click="themeStore.toggleTheme()"
      >
        <!-- Theme Icon -->
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-slate-600 transition-colors duration-200 group-hover:bg-violet-100 group-hover:text-violet-500"
        >
          {{ themeStore.isDark ? "☀" : "☾" }}
        </span>

        <!-- Theme Label -->
        <span
          class="overflow-hidden whitespace-nowrap transition-all duration-200"
          :class="
            collapsed
              ? 'max-w-0 translate-x-2 opacity-0'
              : 'max-w-[160px] translate-x-0 opacity-100 delay-100'
          "
        >
          {{
            themeStore.isDark
              ? i18nStore.t("common.lightMode")
              : i18nStore.t("common.darkMode")
          }}
        </span>
      </button>

      <!-- Logout -->
      <button
        type="button"
        class="group mt-2 flex w-full items-center rounded-xl px-3 py-3 text-sm font-medium text-slate-600 transition-colors duration-200 hover:bg-red-50 hover:text-red-500"
        :class="collapsed ? 'justify-center' : 'gap-4'"
        @click="logout"
      >
        <!-- Logout Icon -->
        <span
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-slate-50 text-slate-600 transition-colors duration-200 group-hover:bg-red-100 group-hover:text-red-500"
        >
          L
        </span>

        <!-- Logout Label -->
        <span
          class="overflow-hidden whitespace-nowrap transition-all duration-200"
          :class="
            collapsed
              ? 'max-w-0 translate-x-2 opacity-0'
              : 'max-w-[160px] translate-x-0 opacity-100 delay-100'
          "
        >
          {{ i18nStore.t("common.logout") }}
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

const props = defineProps({
  collapsed: {
    type: Boolean,
    default: true,
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

const userInitial = computed(
  () =>
    authStore.user?.username?.charAt(0)?.toUpperCase() ||
    i18nStore.t("common.user").charAt(0)
);

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

const handleMouseEnter = () => {
  if (props.collapsed) {
    emit("toggle");
  }
};

const handleMouseLeave = () => {
  if (!props.collapsed) {
    emit("toggle");
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