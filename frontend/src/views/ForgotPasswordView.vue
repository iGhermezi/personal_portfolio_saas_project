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
          Forgot your password?
        </h1>

        <p class="mt-3 text-sm leading-6 text-slate-400">
          Enter your email address and we'll send you instructions to reset
          your password.
        </p>

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
              Email
            </label>

            <input
              v-model="email"
              type="email"
              autocomplete="email"
              required
              class="mt-2 w-full rounded-2xl border border-slate-200 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:ring-4 focus:ring-violet-100"
              placeholder="you@example.com"
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {{ loading ? 'Sending...' : 'Send reset link' }}
          </button>
        </form>

        <router-link
          to="/login"
          class="mt-6 block text-center text-sm font-semibold text-violet-500 hover:text-violet-600"
        >
          Back to login
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../api/axios'

const email = ref('')
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

  if (data?.email?.[0]) {
    return data.email[0]
  }

  return 'Unable to send the password reset request.'
}

const submit = async () => {
  loading.value = true
  error.value = ''
  success.value = ''

  try {
    await api.post('/accounts/password/forgot/', {
      email: email.value.trim(),
    })

    success.value =
      'If an account exists with this email, password reset instructions have been sent.'
  } catch (err) {
    console.error('Forgot password failed:', err)
    error.value = getErrorMessage(err)
  } finally {
    loading.value = false
  }
}
</script>