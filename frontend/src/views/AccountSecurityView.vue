<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <div class="mx-auto max-w-4xl px-6 py-8">
        <button
          type="button"
          class="mb-5 text-sm font-medium text-slate-400 transition hover:text-violet-500"
          @click="router.push('/profile')"
        >
          ← {{ i18nStore.t("security.backToProfile") }}
        </button>

        <p class="text-sm font-medium text-violet-400">
          {{ i18nStore.t("profile.account") }}
        </p>
        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          {{ i18nStore.t("security.title") }}
        </h1>
        <p class="mt-2 text-sm text-slate-400">
          {{ i18nStore.t("security.description") }}
        </p>

        <div class="mt-8 space-y-6">
          <section
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm"
          >
            <div>
              <p
                class="text-xs font-semibold uppercase tracking-widest text-violet-400"
              >
                01 · {{ i18nStore.t("security.password") }}
              </p>
              <h2 class="mt-1 text-xl font-bold text-slate-800">
                {{ i18nStore.t("security.changePassword") }}
              </h2>
            </div>

            <form
              class="mt-6 grid gap-5 md:grid-cols-3"
              @submit.prevent="changePassword"
            >
              <input
                v-model="passwordForm.current_password"
                type="password"
                autocomplete="current-password"
                :placeholder="i18nStore.t('security.currentPassword')"
                class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
              <input
                v-model="passwordForm.new_password"
                type="password"
                autocomplete="new-password"
                :placeholder="i18nStore.t('security.newPassword')"
                class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
              <input
                v-model="passwordForm.confirm_password"
                type="password"
                autocomplete="new-password"
                :placeholder="i18nStore.t('security.confirmPassword')"
                class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />

              <div
                class="md:col-span-3 flex items-center justify-between gap-4"
              >
                <p
                  v-if="passwordMessage"
                  class="text-sm"
                  :class="passwordSuccess ? 'text-emerald-600' : 'text-red-500'"
                >
                  {{ passwordMessage }}
                </p>
                <button
                  type="submit"
                  :disabled="passwordLoading"
                  class="ml-auto rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 hover:bg-violet-500 disabled:opacity-60"
                >
                  {{
                    i18nStore.t(
                      passwordLoading
                        ? "security.changing"
                        : "security.changePassword",
                    )
                  }}
                </button>
              </div>
            </form>
          </section>

          <section
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm"
          >
            <div>
              <p
                class="text-xs font-semibold uppercase tracking-widest text-violet-400"
              >
                02 · {{ i18nStore.t("security.email") }}
              </p>
              <h2 class="mt-1 text-xl font-bold text-slate-800">
                {{ i18nStore.t("security.changeEmail") }}
              </h2>
              <p class="mt-2 text-sm text-slate-400">
                {{ i18nStore.t("security.currentEmail") }}
                {{ currentEmail || i18nStore.t("security.loading") }}
              </p>
            </div>

            <div class="mt-6 grid gap-5 md:grid-cols-[1fr_auto]">
              <input
                v-model="newEmail"
                type="email"
                autocomplete="email"
                :placeholder="i18nStore.t('security.newEmail')"
                class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
              <button
                type="button"
                :disabled="emailRequestLoading"
                class="rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60"
                @click="requestEmailChange"
              >
                {{
                  i18nStore.t(
                    emailRequestLoading
                      ? "security.sending"
                      : "security.sendCode",
                  )
                }}
              </button>
            </div>

            <div
              v-if="emailCodeRequested"
              class="mt-5 grid gap-5 md:grid-cols-[1fr_auto]"
            >
              <input
                v-model="emailCode"
                type="text"
                inputmode="numeric"
                maxlength="6"
                :placeholder="i18nStore.t('security.verificationCode')"
                class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm tracking-[0.35em] outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
              <button
                type="button"
                :disabled="emailConfirmLoading"
                class="rounded-full border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-500 hover:bg-violet-100 disabled:opacity-60"
                @click="confirmEmailChange"
              >
                {{
                  i18nStore.t(
                    emailConfirmLoading
                      ? "security.confirming"
                      : "security.confirmEmail",
                  )
                }}
              </button>
            </div>

            <p
              v-if="emailMessage"
              class="mt-4 text-sm"
              :class="emailSuccess ? 'text-emerald-600' : 'text-red-500'"
            >
              {{ emailMessage }}
            </p>
          </section>

          <section
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm"
          >
            <div
              class="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between"
            >
              <div>
                <p
                  class="text-xs font-semibold uppercase tracking-widest text-violet-400"
                >
                  03 · {{ i18nStore.t("security.verification") }}
                </p>
                <h2 class="mt-1 text-xl font-bold text-slate-800">
                  {{ i18nStore.t("security.emailVerification") }}
                </h2>
                <p class="mt-2 text-sm text-slate-400">
                  {{
                    emailVerified
                      ? i18nStore.t("security.emailVerified")
                      : i18nStore.t("security.emailNotVerified")
                  }}
                </p>
              </div>

              <div
                v-if="emailVerified"
                class="rounded-full bg-emerald-50 px-4 py-2 text-sm font-semibold text-emerald-600"
              >
                {{ i18nStore.t("security.verified") }} ✓
              </div>
              <button
                v-else
                type="button"
                :disabled="resendLoading"
                class="rounded-full bg-violet-400 px-6 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60"
                @click="resendVerification"
              >
                {{
                  i18nStore.t(
                    resendLoading
                      ? "security.sending"
                      : "security.resendVerification",
                  )
                }}
              </button>
            </div>
            <p
              v-if="verificationMessage"
              class="mt-4 text-sm"
              :class="verificationSuccess ? 'text-emerald-600' : 'text-red-500'"
            >
              {{ verificationMessage }}
            </p>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import api from "../api/axios";
import { useAuthStore } from "../stores/auth";
import { useI18nStore } from "../stores/i18n";
import DashboardSidebar from "../components/Dashboard/DashboardSidebar.vue";

const router = useRouter();
const sidebarCollapsed = ref(false);
const authStore = useAuthStore();
const i18nStore = useI18nStore();

const currentEmail = computed(() => {
  return authStore.user?.email || "";
});

const emailVerified = computed(() => {
  return !!authStore.user?.email_verified;
});

const passwordForm = reactive({
  current_password: "",
  new_password: "",
  confirm_password: "",
});
const passwordLoading = ref(false);
const passwordMessage = ref("");
const passwordSuccess = ref(false);

const newEmail = ref("");
const emailCode = ref("");
const emailCodeRequested = ref(false);
const emailRequestLoading = ref(false);
const emailConfirmLoading = ref(false);
const emailMessage = ref("");
const emailSuccess = ref(false);

const resendLoading = ref(false);
const verificationMessage = ref("");
const verificationSuccess = ref(false);

const firstError = (err, fallback) => {
  const data = err?.response?.data;
  if (!data) return fallback;
  if (typeof data.detail === "string") return data.detail;
  return Object.values(data).flat().find(Boolean) || fallback;
};
const loadProfile = async () => {
  try {
    await authStore.getProfile();
  } catch (err) {
    verificationMessage.value = firstError(
      err,
      i18nStore.t("security.unableLoadAccount"),
    );
  }
};

const changePassword = async () => {
  passwordMessage.value = "";
  passwordSuccess.value = false;

  if (passwordForm.new_password !== passwordForm.confirm_password) {
    passwordMessage.value = i18nStore.t("security.passwordMismatch");
    return;
  }

  passwordLoading.value = true;
  try {
    await api.post("/accounts/change-password/", passwordForm);
    passwordSuccess.value = true;
    passwordMessage.value = i18nStore.t("security.passwordChanged");
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");
    setTimeout(() => router.push("/login"), 900);
  } catch (err) {
    passwordMessage.value = firstError(
      err,
      i18nStore.t("security.unableChangePassword"),
    );
  } finally {
    passwordLoading.value = false;
  }
};

const requestEmailChange = async () => {
  emailMessage.value = "";
  emailSuccess.value = false;
  emailRequestLoading.value = true;

  try {
    await api.post("/accounts/change-email/request/", {
      new_email: newEmail.value.trim(),
    });
    emailCodeRequested.value = true;
    emailSuccess.value = true;
    emailMessage.value = i18nStore.t("security.codeSent");
  } catch (err) {
    emailMessage.value = firstError(
      err,
      i18nStore.t("security.unableRequestEmail"),
    );
  } finally {
    emailRequestLoading.value = false;
  }
};

const confirmEmailChange = async () => {
  emailMessage.value = "";
  emailSuccess.value = false;
  emailConfirmLoading.value = true;

  try {
    await api.post("/accounts/change-email/confirm/", {
      code: emailCode.value.trim(),
    });
    emailSuccess.value = true;
    emailMessage.value = i18nStore.t("security.emailChanged");
    emailCodeRequested.value = false;
    await authStore.getProfile();

    newEmail.value = "";
    emailCode.value = "";
  } catch (err) {
    emailMessage.value = firstError(
      err,
      i18nStore.t("security.unableConfirmEmail"),
    );
  } finally {
    emailConfirmLoading.value = false;
  }
};

const resendVerification = async () => {
  verificationMessage.value = "";
  verificationSuccess.value = false;
  resendLoading.value = true;

  try {
    await api.post("/accounts/email/verification/resend/", {
      email: currentEmail.value,
    });
    verificationSuccess.value = true;
    verificationMessage.value = i18nStore.t("security.verificationSent");
  } catch (err) {
    verificationMessage.value = firstError(
      err,
      i18nStore.t("security.unableResendVerification"),
    );
  } finally {
    resendLoading.value = false;
  }
};

onMounted(loadProfile);
</script>
