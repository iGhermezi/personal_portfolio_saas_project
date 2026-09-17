<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">

    <!-- Sidebar -->
    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />

    <!-- Main Area -->
    <main
      class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out"
      :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'"
    >

      <!-- Simple header -->
      <header
        class="flex items-center justify-between rounded-3xl border border-violet-100 bg-white px-6 py-4 shadow-[0_10px_40px_rgba(139,92,246,0.12)]"
      >
        <div>
          <p class="text-xs font-medium text-violet-400">Account</p>
          <h1 class="mt-1 text-xl font-bold text-slate-800">Profile settings</h1>
        </div>

        <router-link
          to="/dashboard"
          class="text-sm font-medium text-violet-400 hover:text-violet-500"
        >
          ← Back to dashboard
        </router-link>
      </header>

      <!-- Content -->
      <div class="mx-auto max-w-3xl px-6 py-8">

        <div
          v-if="loading"
          class="flex min-h-[300px] items-center justify-center text-sm text-slate-400"
        >
          Loading your profile...
        </div>

        <form
          v-else
          @submit.prevent="saveProfile"
          class="rounded-[28px] border border-violet-100 bg-white p-8 shadow-sm"
        >

          <!-- Avatar + email (read-only) -->
          <div class="mb-8 flex items-center gap-4">
            <div
              class="flex h-16 w-16 shrink-0 items-center justify-center overflow-hidden rounded-full bg-violet-100 text-xl font-bold text-violet-500"
            >
              <img
                v-if="form.profile_image_url"
                :src="form.profile_image_url"
                alt="Profile"
                class="h-full w-full object-cover"
                @error="form.profile_image_url = ''"
              />
              <span v-else>{{ initial }}</span>
            </div>
            <div>
              <p class="text-sm font-semibold text-slate-800">{{ email }}</p>
              <p class="text-xs text-slate-400">Email cannot be changed here</p>
            </div>
          </div>

          <!-- Success / error banners -->
          <div
            v-if="successMessage"
            class="mb-5 rounded-xl border border-emerald-100 bg-emerald-50 px-4 py-3 text-sm text-emerald-600"
          >
            {{ successMessage }}
          </div>
          <div
            v-if="errorMessage"
            class="mb-5 rounded-xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
          >
            {{ errorMessage }}
          </div>

          <div class="grid grid-cols-1 gap-5 sm:grid-cols-2">

            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">Username</label>
              <input
                v-model="form.username"
                type="text"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">Job title</label>
              <input
                v-model="form.job_title"
                type="text"
                placeholder="e.g. Backend Developer"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">First name</label>
              <input
                v-model="form.first_name"
                type="text"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">Last name</label>
              <input
                v-model="form.last_name"
                type="text"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">Phone</label>
              <input
                v-model="form.phone"
                type="text"
                maxlength="11"
                placeholder="09xxxxxxxxx"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <div>
              <label class="mb-2 block text-sm font-medium text-slate-700">Location</label>
              <input
                v-model="form.location"
                type="text"
                placeholder="e.g. Amsterdam, Netherlands"
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

            <div class="sm:col-span-2">
              <label class="mb-2 block text-sm font-medium text-slate-700">Profile image URL</label>
              <input
                v-model="form.profile_image_url"
                type="text"
                placeholder="https://..."
                class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100"
              />
            </div>

          </div>

          <button
            type="submit"
            :disabled="saving"
            class="mt-8 rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {{ saving ? 'Saving...' : 'Save changes' }}
          </button>

        </form>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import api from '../api/axios'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar.vue'

const authStore = useAuthStore()
const sidebarCollapsed = ref(false)

const loading = ref(true)
const saving = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const email = ref('')

const form = reactive({
  username: '',
  first_name: '',
  last_name: '',
  job_title: '',
  phone: '',
  location: '',
  profile_image_url: ''
})

const initial = computed(() => {
  return (form.username || 'U').charAt(0).toUpperCase()
})

onMounted(async () => {
  try {
    const response = await api.get('accounts/me/')
    const data = response.data

    email.value = data.email
    form.username = data.username || ''
    form.first_name = data.first_name || ''
    form.last_name = data.last_name || ''
    form.job_title = data.job_title || ''
    form.phone = data.phone || ''
    form.location = data.location || ''
    form.profile_image_url = data.profile_image_url || ''
  } catch (error) {
    console.error('Failed to load profile:', error)
    errorMessage.value = 'دریافت اطلاعات پروفایل با خطا مواجه شد.'
  } finally {
    loading.value = false
  }
})

const saveProfile = async () => {
  errorMessage.value = ''
  successMessage.value = ''
  saving.value = true

  try {
    const response = await api.patch('accounts/me/', form)

    // هماهنگ کردن Sidebar/Header با نام جدید کاربر
    authStore.updateUser(response.data)

    successMessage.value = 'پروفایل با موفقیت به‌روزرسانی شد.'
  } catch (error) {
    console.error('Failed to update profile:', error)
    if (error.response?.data) {
      const errors = error.response.data
      errorMessage.value = Object.values(errors).flat().join(' ')
    } else {
      errorMessage.value = 'ارتباط با سرور برقرار نشد.'
    }
  } finally {
    saving.value = false
  }
}
</script>