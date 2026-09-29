<template>
  <div class="min-h-screen bg-[#faf9ff] px-5 py-5">
    <DashboardSidebar :collapsed="sidebarCollapsed" @toggle="sidebarCollapsed = !sidebarCollapsed" />

    <main class="min-h-[calc(100vh-40px)] transition-transform duration-300 ease-in-out" :class="sidebarCollapsed ? 'ml-[98px]' : 'ml-[284px]'">
      <div class="mx-auto max-w-4xl px-6 py-8">
        <p class="text-sm font-medium text-violet-400">Premium</p>
        <h1 class="mt-1 text-3xl font-bold tracking-tight text-slate-900">Unlock premium templates</h1>
        <p class="mt-2 text-sm text-slate-400">Premium access is reviewed manually. There is no payment flow in this version.</p>

        <section class="mt-8 rounded-[28px] border border-violet-100 bg-white p-8 shadow-sm">
          <div v-if="loading" class="text-sm text-slate-400">Loading subscription status...</div>
          <template v-else>
            <div class="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between">
              <div>
                <p class="text-xs font-semibold uppercase tracking-widest text-violet-400">Subscription status</p>
                <h2 class="mt-1 text-xl font-bold text-slate-800">{{ subscribed ? 'Premium is active' : 'Premium is not active' }}</h2>
                <p class="mt-2 text-sm text-slate-400">{{ subscribed ? 'You can use all premium templates.' : statusText }}</p>
              </div>
              <span class="rounded-full px-4 py-2 text-sm font-semibold" :class="subscribed ? 'bg-emerald-50 text-emerald-600' : 'bg-violet-50 text-violet-500'">
                {{ subscribed ? 'Active' : 'Manual approval' }}
              </span>
            </div>

            <div class="mt-8 rounded-2xl border border-violet-100 bg-violet-50 p-5 text-sm leading-6 text-slate-600">
              This project intentionally keeps premium access experimental and admin-controlled. Payment processing is not included.
            </div>

            <div class="mt-6 flex flex-wrap gap-3">
              <button
                v-if="!subscribed && requestStatus !== 'pending'"
                type="button"
                :disabled="requesting"
                class="rounded-full bg-violet-400 px-7 py-3 text-sm font-semibold text-white shadow-lg shadow-violet-100 transition hover:bg-violet-500 disabled:opacity-60"
                @click="requestPremium"
              >
                {{ requesting ? 'Sending...' : 'Request premium access' }}
              </button>
              <span v-else-if="!subscribed" class="rounded-full border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-500">Request pending</span>
              <router-link to="/templates" class="rounded-full border border-violet-200 bg-violet-50 px-7 py-3 text-sm font-semibold text-violet-500 transition hover:bg-violet-100">
                Back to templates
              </router-link>
            </div>
          </template>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import api from '../api/axios'
import { useAuthStore } from '../stores/auth'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar.vue'


const authStore = useAuthStore()
const sidebarCollapsed = ref(false)
const loading = ref(true)
const subscribed = ref(false)
const requestStatus = ref(null)
const requesting = ref(false)
const statusText = ref('Request premium access for manual admin review.')
onMounted(async () => {
  try {
    await authStore.getProfile()

    const { data } = await api.get('accounts/premium/request/')

    subscribed.value = authStore.hasSubscription
    requestStatus.value = data.request_status || null

    if (requestStatus.value === 'pending') {
      statusText.value =
        'Your request is waiting for manual admin review.'
    }
  } catch (error) {
    statusText.value =
      error.response?.data?.detail ||
      'Unable to load subscription status.'
  } finally {
    loading.value = false
  }
})

const requestPremium = async () => {
  requesting.value = true

  try {
    const { data } = await api.post(
      '/accounts/premium/request/'
    )

    await authStore.getProfile()

    subscribed.value = data.has_subscription ?? authStore.hasSubscription
    requestStatus.value =
      data.request_status || 'pending'

    statusText.value =
      data.detail ||
      'Your request is waiting for manual admin review.'
  } catch (error) {
    statusText.value =
      error.response?.data?.detail ||
      'Unable to submit the premium request.'
  } finally {
    requesting.value = false
  }
}
</script>
