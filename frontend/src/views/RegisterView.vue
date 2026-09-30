<template>
  <div
    class="min-h-screen bg-[#faf9ff] flex items-center justify-center px-6 bg-linear-210 from-purple-300 to-purple-600"
  >
    <div
      class="w-full max-w-md rounded-3xl bg-white border border-violet-100 p-8 shadow-xl shadow-violet-100"
    >
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-slate-900">
          {{ i18nStore.t("auth.registerTitle") }}
        </h1>

        <p class="mt-2 text-sm text-slate-500">
          {{ i18nStore.t("auth.registerDescription") }}
        </p>
      </div>

      <div
        v-if="errorMessage"
        class="mb-5 rounded-xl bg-red-50 border border-red-100 px-4 py-3 text-sm text-red-500"
      >
        {{ errorMessage }}
      </div>

      <form @submit.prevent="register" class="space-y-5">
        <div>
          <label class="mb-2 block text-sm font-medium text-slate-700">
            {{ i18nStore.t("auth.username") }}
          </label>

          <input
            v-model="form.username"
            type="text"
            :placeholder="i18nStore.t('auth.username')"
            required
            autocomplete="username"
            class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium text-slate-700">
            {{ i18nStore.t("auth.email") }}
          </label>

          <input
            v-model="form.email"
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
            v-model="form.password"
            type="password"
            :placeholder="i18nStore.t('auth.password')"
            required
            autocomplete="new-password"
            class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium text-slate-700">
            {{ i18nStore.t("auth.confirmPassword") }}
          </label>

          <input
            v-model="form.password2"
            type="password"
            :placeholder="i18nStore.t('auth.confirmPassword')"
            required
            autocomplete="new-password"
            class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
          />
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full rounded-xl bg-violet-400 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
        >
          {{
            loading
              ? i18nStore.t("auth.creatingAccount")
              : i18nStore.t("auth.createAccount")
          }}
        </button>
      </form>

      <div class="mt-6 text-center text-sm text-slate-500">
        {{ i18nStore.t("auth.hasAccount") }}

        <router-link
          to="/login"
          class="font-semibold text-violet-400 hover:text-violet-500"
        >
          {{ i18nStore.t("auth.logIn") }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { useI18nStore } from "../stores/i18n";

const router = useRouter();
const authStore = useAuthStore();
const i18nStore = useI18nStore();

const form = reactive({
  username: "",
  email: "",
  password: "",
  password2: "",
});

const loading = ref(false);
const errorMessage = ref("");

const register = async () => {
  errorMessage.value = "";
  loading.value = true;

  try {
    await authStore.register({
      username: form.username,
      email: form.email,
      password: form.password,
      password2: form.password2,
    });

    await router.push("/login");
  } catch (error) {
    console.error("Register failed:", error);

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
