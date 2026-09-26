<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-10">
    <div class="mx-auto flex min-h-[80vh] max-w-md items-center">
      <div
        class="w-full rounded-3xl border border-violet-100 bg-white p-8 text-center shadow-sm"
      >
        <div
          v-if="loading"
          class="text-sm font-medium text-slate-400"
        >
          Verifying your email...
        </div>

        <template v-else-if="success">
          <div class="text-5xl">
            ✓
          </div>

          <h1 class="mt-4 text-2xl font-bold text-slate-900">
            Email verified
          </h1>

          <p class="mt-3 text-sm leading-6 text-slate-400">
            Your email address has been verified successfully.
          </p>

          <button
            type="button"
            class="mt-6 w-full rounded-2xl bg-violet-400 px-5 py-3 text-sm font-semibold text-white transition hover:bg-violet-500"
            @click="continueToApp"
          >
            Continue
          </button>
        </template>

        <template v-else>
          <div class="text-5xl">
            !
          </div>

          <h1 class="mt-4 text-2xl font-bold text-slate-900">
            Verification failed
          </h1>

          <p class="mt-3 text-sm leading-6 text-red-500">
            {{ error }}
          </p>

          <button
            type="button"
            class="mt-6 w-full rounded-2xl border border-violet-200 px-5 py-3 text-sm font-semibold text-violet-600 transition hover:bg-violet-50"
            @click="continueToApp"
          >
            Continue
          </button>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api/axios'

const route = useRoute()
const router = useRouter()

const loading = ref(true)
const success = ref(false)
const error = ref('')

const continueToApp = () => {
  const accessToken = localStorage.getItem('access_token')
  const refreshToken = localStorage.getItem('refresh_token')

  if (accessToken || refreshToken) {
    router.push('/dashboard')
  } else {
    router.push('/login')
  }
}

const verifyEmail = async () => {
  loading.value = true
  error.value = ''

  try {
    await api.get(
      `/accounts/email/verify/${route.params.uid}/${route.params.token}/`
    )

    success.value = true
  } catch (err) {
    console.error('Email verification failed:', err)

    error.value =
      err.response?.data?.detail ||
      'Unable to verify your email address.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  verifyEmail()
})
</script>