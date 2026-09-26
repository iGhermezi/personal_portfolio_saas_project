<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-10">
    <div class="mx-auto flex min-h-[80vh] max-w-md items-center">
      <div
        class="w-full rounded-3xl border border-violet-100 bg-white p-8 shadow-sm"
      >
        <p class="text-sm font-semibold text-violet-400">
          Account Recovery
        </p>

        <h1
          class="mt-2 text-3xl font-bold tracking-tight text-slate-900"
        >
          Reset password
        </h1>

        <div
          v-if="success"
          class="mt-6 rounded-2xl border border-emerald-100 bg-emerald-50 p-4"
        >
          <p class="text-sm font-medium leading-6 text-emerald-700">
            {{ success }}
          </p>
        </div>

        <div
          v-if="error"
          class="mt-6 rounded-2xl border border-red-100 bg-red-50 p-4"
        >
          <p class="text-sm font-medium leading-6 text-red-600">
            {{ error }}
          </p>
        </div>

        <form
          v-if="!success"
          class="mt-6 space-y-5"
          @submit.prevent="submit"
        >
          <div>
            <label class="text-sm font-semibold text-slate-700">
              New password
            </label>

            <input
              v-model="newPassword"
              type="password"
              autocomplete="new-password"
              required
              class="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
            />
          </div>

          <div>
            <label class="text-sm font-semibold text-slate-700">
              Confirm password
            </label>

            <input
              v-model="confirmPassword"
              type="password"
              autocomplete="new-password"
              required
              class="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {{ loading ? 'Resetting...' : 'Reset password' }}
          </button>
        </form>

        <button
          v-if="success"
          type="button"
          class="mt-6 w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500"
          @click="router.push('/login')"
        >
          Go to login
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api/axios'

const route = useRoute()
const router = useRouter()

const newPassword = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const error = ref('')
const success = ref('')

const getErrorMessage = (err) => {
  const data = err.response?.data

  if (typeof data === 'string') {
    return data
  }

  if (data?.detail) {
    return data.detail
  }

  if (data?.new_password?.[0]) {
    return data.new_password[0]
  }

  if (data?.confirm_password?.[0]) {
    return data.confirm_password[0]
  }

  if (data?.token?.[0]) {
    return data.token[0]
  }

  if (data?.uid?.[0]) {
    return data.uid[0]
  }

  return 'Unable to reset your password.'
}

const submit = async () => {
  error.value = ''

  if (newPassword.value !== confirmPassword.value) {
    error.value = 'Passwords do not match.'
    return
  }

  loading.value = true

  try {
    await api.post('/accounts/password/reset/', {
      uid: route.params.uid,
      token: route.params.token,
      new_password: newPassword.value,
      confirm_password: confirmPassword.value,
    })

    success.value = 'Your password has been reset successfully.'
  } catch (err) {
    console.error('Reset password failed:', err)
    error.value = getErrorMessage(err)
  } finally {
    loading.value = false
  }
}
</script>