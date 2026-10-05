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
      <!-- Header -->
      <header
        class="flex items-center justify-between rounded-3xl border border-violet-100 bg-white px-6 py-4 shadow-[0_10px_40px_rgba(139,92,246,0.12)]"
      >
        <div>
          <p class="text-xs font-medium text-violet-500">
            {{ i18nStore.t("profile.account") }}
          </p>

          <h1 class="mt-1 text-xl font-bold text-slate-900">
            {{ i18nStore.t("profile.settings") }}
          </h1>
        </div>

        <router-link
          to="/dashboard"
          class=" inline-flex items-center rounded-lg border border-slate-200 bg-white px-3.5 py-2 text-sm font-medium text-slate-600 shadow-sm transition hover:border-violet-200 hover:bg-violet-50 hover:text-violet-600"
        >
          ← {{ i18nStore.t("profile.backToDashboard") }}
        </router-link>
      </header>

      <div class="mx-auto max-w-3xl px-6 py-8">
        <!-- Loading -->
        <div
          v-if="loading"
          class="flex min-h-[300px] items-center justify-center text-sm text-slate-500"
        >
          {{ i18nStore.t("profile.loading") }}
        </div>

        <!-- Form -->
        <form
          v-else
          @submit.prevent="saveProfile"
          class="rounded-[28px] border border-violet-100 bg-white p-8 text-slate-900 shadow-sm"
        >
          <!-- Account identity -->
          <div class="mb-8 flex items-center gap-4">
            <div
              class="flex h-16 w-16 shrink-0 items-center justify-center overflow-hidden rounded-full bg-violet-100 text-xl font-bold text-violet-600"
            >
              <img
                v-if="form.profile_image_url"
                :src="form.profile_image_url"
                :alt="i18nStore.t('profile.imageAlt')"
                class="h-full w-full object-cover"
                @error="form.profile_image_url = ''"
              />

              <span v-else>{{ initial }}</span>
            </div>

            <div>
              <p class="text-sm font-semibold text-slate-900">
                {{ email }}
              </p>

              <p class="text-xs text-slate-500">
                {{ i18nStore.t("profile.emailLocked") }}
              </p>
            </div>
          </div>

          <!-- Success -->
          <div
            v-if="successMessage"
            class="mb-5 rounded-xl border border-emerald-100 bg-emerald-50 px-4 py-3 text-sm text-emerald-700"
          >
            {{ successMessage }}
          </div>

          <!-- Error -->
          <div
            v-if="errorMessage"
            class="mb-5 rounded-xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-600"
          >
            {{ errorMessage }}
          </div>

          <!-- Fields -->
          <div class="grid grid-cols-1 gap-5 sm:grid-cols-2">
            <!-- Username -->
            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.username") }}
              </label>

              <input
                v-model="form.username"
                type="text"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <!-- Job title -->
            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.jobTitle") }}
              </label>

              <input
                v-model="form.job_title"
                type="text"
                :placeholder="i18nStore.t('profile.jobPlaceholder')"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <!-- First name -->
            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.firstName") }}
              </label>

              <input
                v-model="form.first_name"
                type="text"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <!-- Last name -->
            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.lastName") }}
              </label>

              <input
                v-model="form.last_name"
                type="text"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <!-- Phone -->
            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.phone") }}
              </label>

              <input
                v-model="form.phone"
                type="text"
                maxlength="11"
                :placeholder="i18nStore.t('profile.phonePlaceholder')"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <!-- Location -->
            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.location") }}
              </label>

              <input
                v-model="form.location"
                type="text"
                :placeholder="i18nStore.t('profile.locationPlaceholder')"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <!-- Profile image -->
            <div class="sm:col-span-2">
              <label class="mb-2 block text-sm font-medium text-slate-700">
                {{ i18nStore.t("profile.imageUrl") }}
              </label>

              <input
                v-model="form.profile_image_url"
                type="text"
                :placeholder="i18nStore.t('profile.imagePlaceholder')"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>
          </div>

          <!-- Actions -->
          <div class="mt-8 flex flex-wrap items-center gap-3">
            <button
              type="submit"
              :disabled="saving"
              class="rounded-lg bg-violet-500 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-600 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {{
                i18nStore.t(
                  saving ? "profile.saving" : "profile.saveChanges",
                )
              }}
            </button>

            <router-link
              to="/account/security"
              class="rounded-lg border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-600 transition hover:bg-violet-100"
            >
              {{ i18nStore.t("profile.securitySettings") }}
            </router-link>
          </div>
        </form>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from "vue";
import { useAuthStore } from "../../stores/auth";
import api from "../../api/axios";
import { useI18nStore } from "../../stores/i18n";
import DashboardSidebar from "../../components/Dashboard/DashboardSidebar.vue";

const authStore = useAuthStore();
const i18nStore = useI18nStore();
const sidebarCollapsed = ref(true);

const loading = ref(true);
const saving = ref(false);
const errorMessage = ref("");
const successMessage = ref("");

const email = ref("");

const form = reactive({
  username: "",
  first_name: "",
  last_name: "",
  job_title: "",
  phone: "",
  location: "",
  profile_image_url: "",
});

const initial = computed(() => {
  return (form.username || i18nStore.t("common.user")).charAt(0).toUpperCase();
});

onMounted(async () => {
  try {
    const response = await api.get("accounts/me/");
    const data = response.data;

    email.value = data.email;
    form.username = data.username || "";
    form.first_name = data.first_name || "";
    form.last_name = data.last_name || "";
    form.job_title = data.job_title || "";
    form.phone = data.phone || "";
    form.location = data.location || "";
    form.profile_image_url = data.profile_image_url || "";
  } catch (error) {
    console.error("Failed to load profile:", error);
    errorMessage.value = i18nStore.t("profile.loadError");
  } finally {
    loading.value = false;
  }
});

const saveProfile = async () => {
  errorMessage.value = "";
  successMessage.value = "";
  saving.value = true;

  try {
    const response = await api.patch("accounts/me/", form);

    authStore.updateUser(response.data);

    successMessage.value = i18nStore.t("profile.updateSuccess");
  } catch (error) {
    console.error("Failed to update profile:", error);

    if (error.response?.data) {
      const errors = error.response.data;
      errorMessage.value = Object.values(errors).flat().join(" ");
    } else {
      errorMessage.value = i18nStore.t("profile.updateError");
    }
  } finally {
    saving.value = false;
  }
};
</script>