<template>
  <div
    class="min-h-screen bg-[#faf9ff] flex items-center justify-center px-6 bg-linear-130 from-purple-300 to-purple-600"
  >
    <div
      class="w-full max-w-md rounded-3xl border border-violet-100 bg-white p-8 shadow-xl shadow-violet-100"
    >
      <div class="mb-8 text-center">
        <h1 class="text-3xl font-bold text-slate-900">
          {{ i18nStore.t("auth.loginTitle") }}
        </h1>

        <p class="mt-2 text-sm text-slate-500">
          {{ i18nStore.t("auth.signInDescription") }}
        </p>
      </div>

      <div
        v-if="errorMessage"
        class="mb-5 rounded-xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
      >
        {{ errorMessage }}
      </div>

      <form @submit.prevent="login" class="space-y-5">
        <div>
          <label class="mb-2 block text-sm font-medium text-slate-700">
            {{ i18nStore.t("auth.email") }}
          </label>

          <input
            v-model="email"
            type="email"
            :placeholder="i18nStore.t('auth.emailPlaceholder')"
            required
            autocomplete="email"
            class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium text-slate-700">
            {{ i18nStore.t("auth.password") }}
          </label>

          <input
            v-model="password"
            type="password"
            :placeholder="i18nStore.t('auth.password')"
            required
            autocomplete="current-password"
            class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
          />
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full rounded-xl bg-violet-400 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
        >
          {{ i18nStore.t(loading ? "auth.signingIn" : "auth.signIn") }}
        </button>
      </form>

      <div class="mt-4 text-center">
        <router-link
          to="/forgot-password"
          class="text-sm font-semibold text-violet-400 transition hover:text-violet-500"
        >
          {{ i18nStore.t("auth.forgotPassword") }}
        </router-link>
      </div>

      <div class="mt-6 text-center text-sm text-slate-500">
        {{ i18nStore.t("auth.noAccount") }}

        <router-link
          to="/register"
          class="font-semibold text-violet-400 transition hover:text-violet-500"
        >
          {{ i18nStore.t("auth.register") }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { useI18nStore } from "../stores/i18n";

const router = useRouter();
const authStore = useAuthStore();
const i18nStore = useI18nStore();

const email = ref("");
const password = ref("");

const loading = ref(false);
const errorMessage = ref("");

const login = async () => {
  errorMessage.value = "";
  loading.value = true;

  try {
    await authStore.login(email.value, password.value);

    await router.push("/dashboard");
  } catch (error) {
    console.error("Login failed:", error);

    if (error.response?.data) {
      const errors = error.response.data;

      errorMessage.value = Object.values(errors).flat().join(" ");
    } else {
      errorMessage.value = i18nStore.t("auth.connectionError");
    }
  } finally {
    loading.value = false;
  }
};
</script>
