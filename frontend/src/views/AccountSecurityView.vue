<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">
    <DashboardSidebar :collapsed="sidebarCollapsed" @toggle="sidebarCollapsed = !sidebarCollapsed" />

    <main class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out" :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'">
      <div class="mx-auto max-w-4xl px-6 py-8">
        <button type="button" class="mb-5 text-sm font-medium text-slate-400 transition hover:text-violet-500" @click="router.push('/profile')">← Back to profile</button>

        <p class="text-sm font-medium text-violet-400">Account</p>
        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">Security settings</h1>
        <p class="mt-2 text-sm text-slate-400">Manage your password, email address and verification status.</p>

        <div class="mt-8 space-y-6">
          <section class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm">
            <div>
              <p class="text-xs font-semibold uppercase tracking-widest text-violet-400">01 · Password</p>
              <h2 class="mt-1 text-xl font-bold text-slate-800">Change password</h2>
            </div>

            <form class="mt-6 grid gap-5 md:grid-cols-3" @submit.prevent="changePassword">
              <input v-model="passwordForm.current_password" type="password" autocomplete="current-password" placeholder="Current password" class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />
              <input v-model="passwordForm.new_password" type="password" autocomplete="new-password" placeholder="New password" class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />
              <input v-model="passwordForm.confirm_password" type="password" autocomplete="new-password" placeholder="Confirm password" class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />

              <div class="md:col-span-3 flex items-center justify-between gap-4">
                <p v-if="passwordMessage" class="text-sm" :class="passwordSuccess ? 'text-emerald-600' : 'text-red-500'">{{ passwordMessage }}</p>
                <button type="submit" :disabled="passwordLoading" class="ml-auto rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 hover:bg-violet-500 disabled:opacity-60">{{ passwordLoading ? 'Changing...' : 'Change password' }}</button>
              </div>
            </form>
          </section>

          <section class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm">
            <div>
              <p class="text-xs font-semibold uppercase tracking-widest text-violet-400">02 · Email</p>
              <h2 class="mt-1 text-xl font-bold text-slate-800">Change email address</h2>
              <p class="mt-2 text-sm text-slate-400">Current email: {{ currentEmail || 'Loading...' }}</p>
            </div>

            <div class="mt-6 grid gap-5 md:grid-cols-[1fr_auto]">
              <input v-model="newEmail" type="email" autocomplete="email" placeholder="New email address" class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />
              <button type="button" :disabled="emailRequestLoading" class="rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60" @click="requestEmailChange">{{ emailRequestLoading ? 'Sending...' : 'Send code' }}</button>
            </div>

            <div v-if="emailCodeRequested" class="mt-5 grid gap-5 md:grid-cols-[1fr_auto]">
              <input v-model="emailCode" type="text" inputmode="numeric" maxlength="6" placeholder="6-digit verification code" class="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm tracking-[0.35em] outline-none focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />
              <button type="button" :disabled="emailConfirmLoading" class="rounded-full border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-500 hover:bg-violet-100 disabled:opacity-60" @click="confirmEmailChange">{{ emailConfirmLoading ? 'Confirming...' : 'Confirm email' }}</button>
            </div>

            <p v-if="emailMessage" class="mt-4 text-sm" :class="emailSuccess ? 'text-emerald-600' : 'text-red-500'">{{ emailMessage }}</p>
          </section>

          <section class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm">
            <div class="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between">
              <div>
                <p class="text-xs font-semibold uppercase tracking-widest text-violet-400">03 · Verification</p>
                <h2 class="mt-1 text-xl font-bold text-slate-800">Email verification</h2>
                <p class="mt-2 text-sm text-slate-400">{{ emailVerified ? 'Your email address is verified.' : 'Your email address is not verified yet.' }}</p>
              </div>

              <div v-if="emailVerified" class="rounded-full bg-emerald-50 px-4 py-2 text-sm font-semibold text-emerald-600">Verified ✓</div>
              <button v-else type="button" :disabled="resendLoading" class="rounded-full bg-violet-400 px-6 py-3 text-sm font-semibold text-white hover:bg-violet-500 disabled:opacity-60" @click="resendVerification">{{ resendLoading ? 'Sending...' : 'Resend verification' }}</button>
            </div>
            <p v-if="verificationMessage" class="mt-4 text-sm" :class="verificationSuccess ? 'text-emerald-600' : 'text-red-500'">{{ verificationMessage }}</p>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api/axios'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar.vue'

const router = useRouter()
const sidebarCollapsed = ref(false)
const currentEmail = ref('')
const emailVerified = ref(false)

const passwordForm = reactive({ current_password: '', new_password: '', confirm_password: '' })
const passwordLoading = ref(false)
const passwordMessage = ref('')
const passwordSuccess = ref(false)

const newEmail = ref('')
const emailCode = ref('')
const emailCodeRequested = ref(false)
const emailRequestLoading = ref(false)
const emailConfirmLoading = ref(false)
const emailMessage = ref('')
const emailSuccess = ref(false)

const resendLoading = ref(false)
const verificationMessage = ref('')
const verificationSuccess = ref(false)

const firstError = (err, fallback) => {
  const data = err?.response?.data
  if (!data) return fallback
  if (typeof data.detail === 'string') return data.detail
  return Object.values(data).flat().find(Boolean) || fallback
}

const loadProfile = async () => {
  try {
    const { data } = await api.get('/accounts/me/')
    currentEmail.value = data.email || ''
    emailVerified.value = !!data.email_verified
  } catch (err) {
    verificationMessage.value = firstError(err, 'Unable to load account information.')
  }
}

const changePassword = async () => {
  passwordMessage.value = ''
  passwordSuccess.value = false

  if (passwordForm.new_password !== passwordForm.confirm_password) {
    passwordMessage.value = 'New password and confirmation do not match.'
    return
  }

  passwordLoading.value = true
  try {
    await api.post('/accounts/change-password/', passwordForm)
    passwordSuccess.value = true
    passwordMessage.value = 'Password changed successfully. Please sign in again.'
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
    setTimeout(() => router.push('/login'), 900)
  } catch (err) {
    passwordMessage.value = firstError(err, 'Unable to change password.')
  } finally {
    passwordLoading.value = false
  }
}

const requestEmailChange = async () => {
  emailMessage.value = ''
  emailSuccess.value = false
  emailRequestLoading.value = true

  try {
    await api.post('/accounts/change-email/request/', { new_email: newEmail.value.trim() })
    emailCodeRequested.value = true
    emailSuccess.value = true
    emailMessage.value = 'Verification code sent to the new email address.'
  } catch (err) {
    emailMessage.value = firstError(err, 'Unable to request an email change.')
  } finally {
    emailRequestLoading.value = false
  }
}

const confirmEmailChange = async () => {
  emailMessage.value = ''
  emailSuccess.value = false
  emailConfirmLoading.value = true

  try {
    await api.post('/accounts/change-email/confirm/', { code: emailCode.value.trim() })
    emailSuccess.value = true
    emailMessage.value = 'Email changed successfully. A verification email was sent.'
    emailCodeRequested.value = false
    currentEmail.value = newEmail.value.trim()
    newEmail.value = ''
    emailCode.value = ''
    emailVerified.value = false
  } catch (err) {
    emailMessage.value = firstError(err, 'Unable to confirm the email change.')
  } finally {
    emailConfirmLoading.value = false
  }
}

const resendVerification = async () => {
  verificationMessage.value = ''
  verificationSuccess.value = false
  resendLoading.value = true

  try {
    await api.post('/accounts/email/verification/resend/', { email: currentEmail.value })
    verificationSuccess.value = true
    verificationMessage.value = 'Verification email sent.'
  } catch (err) {
    verificationMessage.value = firstError(err, 'Unable to resend verification email.')
  } finally {
    resendLoading.value = false
  }
}

onMounted(loadProfile)
</script>
