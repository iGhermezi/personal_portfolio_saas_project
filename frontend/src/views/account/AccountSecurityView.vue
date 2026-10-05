
<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5 text-slate-900">
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >
      <div class="mx-auto max-w-4xl px-6 py-8">
        <!-- Back -->
        <button
          type="button"
          class="mb-6 inline-flex items-center rounded-lg border border-slate-200 bg-white px-3.5 py-2 text-sm font-medium text-slate-600 shadow-sm transition hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600"
          @click="router.push('/profile')"
        >
          ← {{ i18nStore.t("security.backToProfile") }}
        </button>

        <!-- Header -->
        <div class="mb-8">
          <p
            class="text-xs font-semibold uppercase tracking-[0.18em] text-violet-500"
          >
            {{ i18nStore.t("profile.account") }}
          </p>

          <h1
            class="mt-2 text-3xl font-bold tracking-tight text-slate-900"
          >
            {{ i18nStore.t("security.title") }}
          </h1>

          <p
            class="mt-2 max-w-2xl text-sm leading-6 text-slate-500"
          >
            {{ i18nStore.t("security.description") }}
          </p>
        </div>

        <div class="space-y-5">
          <!-- Password -->
          <section
            class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div
              class="border-b border-slate-100 px-6 py-5"
            >
              <p
                class="text-xs font-semibold uppercase tracking-[0.16em] text-violet-500"
              >
                01 · {{ i18nStore.t("security.password") }}
              </p>

              <h2
                class="mt-1 text-xl font-bold text-slate-900"
              >
                {{ i18nStore.t("security.changePassword") }}
              </h2>
            </div>

            <form
              class="grid gap-4 p-6 md:grid-cols-3"
              @submit.prevent="changePassword"
            >
              <input
                v-model="passwordForm.current_password"
                type="password"
                autocomplete="current-password"
                :placeholder="i18nStore.t('security.currentPassword')"
                class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />

              <input
                v-model="passwordForm.new_password"
                type="password"
                autocomplete="new-password"
                :placeholder="i18nStore.t('security.newPassword')"
                class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />

              <input
                v-model="passwordForm.confirm_password"
                type="password"
                autocomplete="new-password"
                :placeholder="i18nStore.t('security.confirmPassword')"
                class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />

              <div
                class="flex flex-col gap-3 pt-1 md:col-span-3 sm:flex-row sm:items-center sm:justify-between"
              >
                <p
                  v-if="passwordMessage"
                  class="text-sm font-medium"
                  :class="
                    passwordSuccess
                      ? 'text-emerald-600'
                      : 'text-red-500'
                  "
                >
                  {{ passwordMessage }}
                </p>

                <button
                  type="submit"
                  :disabled="passwordLoading"
                  class="ml-auto rounded-lg bg-violet-500 px-6 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-violet-600 hover:shadow-md disabled:cursor-not-allowed disabled:opacity-60"
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

          <!-- Email -->
          <section
            class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div
              class="border-b border-slate-100 px-6 py-5"
            >
              <p
                class="text-xs font-semibold uppercase tracking-[0.16em] text-violet-500"
              >
                02 · {{ i18nStore.t("security.email") }}
              </p>

              <h2
                class="mt-1 text-xl font-bold text-slate-900"
              >
                {{ i18nStore.t("security.changeEmail") }}
              </h2>

              <p
                class="mt-2 text-sm text-slate-500"
              >
                {{ i18nStore.t("security.currentEmail") }}

                <span class="font-medium text-slate-700">
                  {{ currentEmail || i18nStore.t("security.loading") }}
                </span>
              </p>
            </div>

            <div class="p-6">
              <div
                class="grid gap-4 md:grid-cols-[1fr_auto]"
              >
                <input
                  v-model="newEmail"
                  type="email"
                  autocomplete="email"
                  :placeholder="i18nStore.t('security.newEmail')"
                  class="w-full rounded-lg border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
                />

                <button
                  type="button"
                  :disabled="emailRequestLoading"
                  class="rounded-lg bg-violet-500 px-6 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-violet-600 hover:shadow-md disabled:cursor-not-allowed disabled:opacity-60"
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
                class="mt-4 grid gap-4 rounded-xl border border-violet-100 bg-violet-50/60 p-4 md:grid-cols-[1fr_auto]"
              >
                <input
                  v-model="emailCode"
                  type="text"
                  inputmode="numeric"
                  maxlength="6"
                  :placeholder="i18nStore.t('security.verificationCode')"
                  class="w-full rounded-lg border border-violet-200 bg-white px-4 py-3 text-sm tracking-[0.35em] text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-400 focus:ring-4 focus:ring-violet-100"
                />

                <button
                  type="button"
                  :disabled="emailConfirmLoading"
                  class="rounded-lg border border-violet-200 bg-violet-50 px-6 py-3 text-sm font-semibold text-violet-600 transition hover:bg-violet-100 disabled:cursor-not-allowed disabled:opacity-60"
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
                class="mt-4 text-sm font-medium"
                :class="
                  emailSuccess
                    ? 'text-emerald-600'
                    : 'text-red-500'
                "
              >
                {{ emailMessage }}
              </p>
            </div>
          </section>

          <!-- Verification -->
          <section
            class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm"
          >
            <div
              class="flex flex-col gap-5 px-6 py-5 sm:flex-row sm:items-center sm:justify-between"
            >
              <div>
                <p
                  class="text-xs font-semibold uppercase tracking-[0.16em] text-violet-500"
                >
                  03 · {{ i18nStore.t("security.verification") }}
                </p>

                <h2
                  class="mt-1 text-xl font-bold text-slate-900"
                >
                  {{ i18nStore.t("security.emailVerification") }}
                </h2>

                <p
                  class="mt-2 text-sm text-slate-500"
                >
                  {{
                    emailVerified
                      ? i18nStore.t("security.emailVerified")
                      : i18nStore.t("security.emailNotVerified")
                  }}
                </p>
              </div>

              <div
                v-if="emailVerified"
                class="inline-flex w-fit items-center rounded-lg border border-emerald-200 bg-emerald-50 px-4 py-2 text-sm font-semibold text-emerald-600"
              >
                {{ i18nStore.t("security.verified") }} ✓
              </div>

              <button
                v-else
                type="button"
                :disabled="resendLoading"
                class="rounded-lg bg-violet-500 px-6 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-violet-600 hover:shadow-md disabled:cursor-not-allowed disabled:opacity-60"
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

            <div
              v-if="verificationMessage"
              class="border-t border-slate-100 px-6 py-4"
            >
              <p
                class="text-sm font-medium"
                :class="
                  verificationSuccess
                    ? 'text-emerald-600'
                    : 'text-red-500'
                "
              >
                {{ verificationMessage }}
              </p>
            </div>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import api from "../../api/axios";
import { useAuthStore } from "../../stores/auth";
import { useI18nStore } from "../../stores/i18n";
import DashboardSidebar from "../../components/Dashboard/DashboardSidebar.vue";

const router = useRouter();
const sidebarCollapsed = ref(true);
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
