<script setup>
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import api from "../api/axios";
import { useI18nStore } from "../stores/i18n";

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();
const i18nStore = useI18nStore();
const loading = ref(true);
const success = ref("");
const error = ref("");

onMounted(async () => {
  try {
    await api.get(
      `/accounts/email/verify/${route.params.uid}/${route.params.token}/`,
    );
    await authStore.getProfile();
    success.value = i18nStore.t("auth.emailAdded");
  } catch (err) {
    error.value =
      err.response?.data?.detail || i18nStore.t("auth.invalidExpiredLink");
  } finally {
    loading.value = false;
  }
});

const continueToApp = () => {
  router.push(
    localStorage.getItem("access_token") ||
      localStorage.getItem("refresh_token")
      ? "/dashboard"
      : "/login",
  );
};
</script>

<template>
  <div
    class="flex min-h-screen items-center justify-center bg-[#faf9ff] px-6 dark:bg-[#100b1c]"
  >
    <div
      class="w-full max-w-md rounded-3xl border border-violet-100 bg-white p-8 text-center shadow-xl shadow-violet-100"
    >
      <div v-if="loading">
        <div
          class="mx-auto h-10 w-10 animate-spin rounded-full border-4 border-violet-100 border-t-violet-400"
        />
        <h1 class="mt-6 text-2xl font-bold text-slate-900">
          {{ i18nStore.t("auth.verifyingEmail") }}
        </h1>
      </div>

      <div v-else-if="success">
        <div
          class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-emerald-50 text-2xl text-emerald-500"
        >
          ✓
        </div>
        <h1 class="mt-6 text-2xl font-bold text-slate-900">
          {{ i18nStore.t("auth.emailVerified") }}
        </h1>
        <p class="mt-3 text-sm text-slate-500">{{ success }}</p>
        <button
          class="mt-7 w-full rounded-xl bg-violet-400 py-3 text-sm font-semibold text-white hover:bg-violet-500"
          @click="continueToApp"
        >
          {{ i18nStore.t("auth.continue") }}
        </button>
      </div>

      <div v-else>
        <div
          class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-red-50 text-2xl text-red-500"
        >
          !
        </div>
        <h1 class="mt-6 text-2xl font-bold text-slate-900">
          {{ i18nStore.t("auth.verificationFailed") }}
        </h1>
        <p class="mt-3 text-sm text-red-500">{{ error }}</p>
        <button
          class="mt-7 w-full rounded-xl border border-slate-200 py-3 text-sm font-semibold text-slate-700 hover:bg-slate-50"
          @click="router.push('/login')"
        >
          {{ i18nStore.t("auth.backToLogin") }}
        </button>
      </div>
    </div>
  </div>
</template>
