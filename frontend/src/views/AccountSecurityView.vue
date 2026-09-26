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
        <p class="text-sm font-medium text-violet-400">
          Account
        </p>

        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">
          Security
        </h1>

        <p class="mt-2 text-sm text-slate-400">
          Manage your password, email address and verification status.
        </p>

        <div
          v-if="message"
          class="mt-6 rounded-2xl border border-emerald-100 bg-emerald-50 p-4"
        >
          <p class="text-sm font-medium text-emerald-700">
            {{ message }}
          </p>
        </div>

        <div
          v-if="error"
          class="mt-6 rounded-2xl border border-red-100 bg-red-50 p-4"
        >
          <p class="text-sm font-medium text-red-600">
            {{ error }}
          </p>
        </div>

        <div class="mt-8 grid gap-6 lg:grid-cols-2">
          <section
            class="rounded-3xl border border-violet-100 bg-white p-6 shadow-sm"
          >
            <h2 class="text-lg font-bold text-slate-800">
              Change password
            </h2>

            <p class="mt-2 text-sm leading-6 text-slate-400">
              Update your account password.
            </p>

            <form
              class="mt-6 space-y-4"
              @submit.prevent="changePassword"
            >
              <input
                v-model="passwordForm.current_password"
                type="password"
                autocomplete="current-password"
                required
                placeholder="Current password"
                class="w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
              />

              <input
                v-model="passwordForm.new_password"
                type="password"
                autocomplete="new-password"
                required
                placeholder="New password"
                class="w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
              />

              <input
                v-model="passwordForm.confirm_password"
                type="password"
                autocomplete="new-password"
                required
                placeholder="Confirm new password"
                class="w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
              />

              <button
                type="submit"
                :disabled="passwordLoading"
                class="w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {{
                  passwordLoading
                    ? 'Updating...'
                    : 'Change password'
                }}
              </button>
            </form>
          </section>

          <section
            class="rounded-3xl border border-violet-100 bg-white p-6 shadow-sm"
          >
            <h2 class="text-lg font-bold text-slate-800">
              Change email
            </h2>

            <p class="mt-2 text-sm leading-6 text-slate-400">
              Request a verification code for your new email address.
            </p>

            <form
              v-if="!emailCodeRequested"
              class="mt-6 space-y-4"
              @submit.prevent="requestEmailChange"
            >
              <input
                v-model="emailForm.new_email"
                type="email"
                autocomplete="email"
                required
                placeholder="New email address"
                class="w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
              />

              <button
                type="submit"
                :disabled="emailLoading"
                class="w-full rounded-2xl border border-violet-200 bg-violet-50 px-5 py-3 text-sm font-semibold text-violet-700 transition hover:bg-violet-100 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {{
                  emailLoading
                    ? 'Sending code...'
                    : 'Send verification code'
                }}
              </button>
            </form>

            <form
              v-else
              class="mt-6 space-y-4"
              @submit.prevent="confirmEmailChange"
            >
              <p
                class="rounded-2xl bg-violet-50 p-4 text-sm leading-6 text-violet-700"
              >
                A verification code was sent to
                <strong>{{ emailForm.new_email }}</strong>.
              </p>

              <input
                v-model="emailForm.code"
                type="text"
                inputmode="numeric"
                maxlength="6"
                required
                placeholder="6-digit verification code"
                class="w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm tracking-[0.3em] outline-none focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
              />

              <button
                type="submit"
                :disabled="emailLoading"
                class="w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {{
                  emailLoading
                    ? 'Confirming...'
                    : 'Confirm new email'
                }}
              </button>

              <button
                type="button"
                class="w-full rounded-2xl border border-slate-200 px-5 py-3 text-sm font-semibold text-slate-600 transition hover:bg-slate-50"
                @click="emailCodeRequested = false"
              >
                Use another email
              </button>
            </form>
          </section>
        </div>

        <section
          class="mt-6 rounded-3xl border border-violet-100 bg-white p-6 shadow-sm"
        >
          <div
            class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between"
          >
            <div>
              <h2 class="text-lg font-bold text-slate-800">
                Email verification
              </h2>

              <p class="mt-2 text-sm leading-6 text-slate-400">
                If your email is not verified, request a new verification email.
              </p>
            </div>

            <button
              type="button"
              :disabled="verificationLoading"
              class="rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-3 text-sm font-semibold text-emerald-700 transition hover:bg-emerald-100 disabled:cursor-not-allowed disabled:opacity-60"
              @click="resendVerification"
            >
              {{
                verificationLoading
                  ? 'Sending...'
                  : 'Resend verification'
              }}
            </button>
          </div>
        </section>

        <button
          type="button"
          class="mt-6 text-sm font-semibold text-violet-500 hover:text-violet-600"
          @click="router.push('/dashboard')"
        >
          ← Back to dashboard
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

import api from '../api/axios'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar.vue'

const router = useRouter()

const sidebarCollapsed = ref(false)

const message = ref('')
const error = ref('')

const passwordLoading = ref(false)
const emailLoading = ref(false)
const verificationLoading = ref(false)

const emailCodeRequested = ref(false)

const passwordForm = reactive({
  current_password: '',
  new_password: '',
  confirm_password: '',
})

const emailForm = reactive({
  new_email: '',
  code: '',
})

const getErrorMessage = (err) => {
  const data = err.response?.data

  if (typeof data === 'string') {
    return data
  }

  if (data?.detail) {
    return data.detail
  }

  const keys = [
    'current_password',
    'new_password',
    'confirm_password',
    'new_email',
    'code',
    'email',
  ]

  for (const key of keys) {
    if (data?.[key]?.[0]) {
      return data[key][0]
    }
  }

  return 'Something went wrong. Please try again.'
}

const changePassword = async () => {
  message.value = ''
  error.value = ''

  if (
    passwordForm.new_password !==
    passwordForm.confirm_password
  ) {
    error.value = 'Passwords do not match.'
    return
  }

  passwordLoading.value = true

  try {
    await api.post('/accounts/change-password/', {
      current_password: passwordForm.current_password,
      new_password: passwordForm.new_password,
      confirm_password: passwordForm.confirm_password,
    })

    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')

    passwordForm.current_password = ''
    passwordForm.new_password = ''
    passwordForm.confirm_password = ''

    router.push('/login')
  } catch (err) {
    console.error('Change password failed:', err)
    error.value = getErrorMessage(err)
  } finally {
    passwordLoading.value = false
  }
}

const requestEmailChange = async () => {
  message.value = ''
  error.value = ''
  emailLoading.value = true

  try {
    await api.post('/accounts/change-email/request/', {
      new_email: emailForm.new_email.trim(),
    })

    emailCodeRequested.value = true

    message.value =
      'A verification code has been sent to your new email address.'
  } catch (err) {
    console.error('Email change request failed:', err)
    error.value = getErrorMessage(err)
  } finally {
    emailLoading.value = false
  }
}

const confirmEmailChange = async () => {
  message.value = ''
  error.value = ''
  emailLoading.value = true

  try {
    await api.post('/accounts/change-email/confirm/', {
      code: emailForm.code.trim(),
    })

    emailForm.new_email = ''
    emailForm.code = ''
    emailCodeRequested.value = false

    message.value =
      'Your email address has been changed successfully.'
  } catch (err) {
    console.error('Email change confirmation failed:', err)
    error.value = getErrorMessage(err)
  } finally {
    emailLoading.value = false
  }
}

const resendVerification = async () => {
  message.value = ''
  error.value = ''
  verificationLoading.value = true

  try {
    const meResponse = await api.get('/accounts/me/')
    const email = meResponse.data?.email

    if (!email) {
      throw new Error('No email address was found.')
    }

    await api.post(
      '/accounts/email/verification/resend/',
      {
        email,
      }
    )

    message.value =
      'A new verification email has been sent.'
  } catch (err) {
    console.error('Resend verification failed:', err)

    error.value =
      err.response?.data?.detail ||
      err.message ||
      'Unable to resend the verification email.'
  } finally {
    verificationLoading.value = false
  }
}
</script>