<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api/axios'

const route = useRoute()
const router = useRouter()
const newPassword = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const success = ref('')
const error = ref('')

const messageFromError = (err) => {
  const data = err?.response?.data
  if (!data) return 'ارتباط با سرور برقرار نشد.'
  if (typeof data.detail === 'string') return data.detail
  return Object.values(data).flat().find(Boolean) || 'اطلاعات واردشده صحیح نیست.'
}

const submit = async () => {
  success.value = ''
  error.value = ''

  if (!newPassword.value) {
    error.value = 'رمز عبور جدید را وارد کنید.'
    return
  }

  if (newPassword.value !== confirmPassword.value) {
    error.value = 'رمز عبور و تکرار آن یکسان نیستند.'
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

    success.value = 'رمز عبور با موفقیت تغییر کرد.'
    setTimeout(() => router.push('/login'), 1200)
  } catch (err) {
    error.value = messageFromError(err)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-[#faf9ff] px-6 dark:bg-[#100b1c]">
    <div class="w-full max-w-md rounded-3xl border border-violet-100 bg-white p-8 shadow-xl shadow-violet-100">
      <div class="mb-8 text-center">
        <p class="text-sm font-semibold text-violet-400">Account recovery</p>
        <h1 class="mt-1 text-3xl font-bold text-slate-900">New password</h1>
        <p class="mt-2 text-sm text-slate-500">رمز عبور جدید خود را وارد کنید.</p>
      </div>

      <form class="space-y-5" @submit.prevent="submit">
        <input v-model="newPassword" type="password" autocomplete="new-password" placeholder="New password" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />
        <input v-model="confirmPassword" type="password" autocomplete="new-password" placeholder="Confirm password" class="w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none transition focus:border-violet-300 focus:bg-white focus:ring-4 focus:ring-violet-100" />

        <div v-if="error" class="rounded-xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500">{{ error }}</div>
        <div v-if="success" class="rounded-xl border border-emerald-100 bg-emerald-50 px-4 py-3 text-sm text-emerald-600">{{ success }}</div>

        <button type="submit" :disabled="loading" class="w-full rounded-xl bg-violet-400 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60">
          {{ loading ? 'Changing...' : 'Change password' }}
        </button>
      </form>
    </div>
  </div>
</template>
