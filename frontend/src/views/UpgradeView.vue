
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
      <div class="mx-auto max-w-5xl">
        <!-- Header -->
        <section
          class="rounded-[32px] border border-violet-100 bg-white p-8 shadow-sm"
        >
          <div
            class="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between"
          >
            <div>
              <p
                class="text-xs font-bold uppercase tracking-[0.2em] text-violet-400"
              >
                Premium
              </p>

              <h1
                class="mt-3 text-4xl font-black tracking-tight text-slate-900"
              >
                Unlock your premium templates
              </h1>

              <p class="mt-4 max-w-2xl text-sm leading-7 text-slate-500">
                Get access to all premium portfolio templates and choose the
                style that fits your personal brand.
              </p>
            </div>

            <div
              class="flex h-20 w-20 shrink-0 items-center justify-center rounded-[28px] bg-violet-50 text-4xl"
            >
              ✦
            </div>
          </div>
        </section>

        <!-- Loading -->
        <section
          v-if="loading"
          class="mt-6 rounded-[28px] border border-violet-100 bg-white p-8 text-center shadow-sm"
        >
          <div
            class="mx-auto h-8 w-8 animate-spin rounded-full border-4 border-violet-100 border-t-violet-400"
          ></div>

          <p class="mt-4 text-sm text-slate-400">
            Checking your Premium status...
          </p>
        </section>

        <!-- Error -->
        <section
          v-else-if="error"
          class="mt-6 rounded-[28px] border border-red-100 bg-red-50 p-6 text-sm text-red-500"
        >
          {{ error }}
        </section>

        <!-- Premium Active -->
        <section
          v-else-if="status.has_subscription"
          class="mt-6 rounded-[28px] border border-emerald-100 bg-white p-8 shadow-sm"
        >
          <div class="flex flex-col gap-6 sm:flex-row sm:items-center">
            <div
              class="flex h-16 w-16 shrink-0 items-center justify-center rounded-2xl bg-emerald-50 text-2xl text-emerald-500"
            >
              ✓
            </div>

            <div class="flex-1">
              <p
                class="text-xs font-bold uppercase tracking-[0.16em] text-emerald-500"
              >
                Premium Active
              </p>

              <h2 class="mt-2 text-2xl font-black text-slate-900">
                Your Premium access is active.
              </h2>

              <p class="mt-2 text-sm leading-6 text-slate-500">
                All premium templates are now unlocked for your account.
              </p>
            </div>

            <button
              type="button"
              class="rounded-full bg-violet-400 px-6 py-3 text-sm font-bold text-white transition hover:bg-violet-500"
              @click="goToTemplates"
            >
              Browse Templates
            </button>
          </div>
        </section>

        <!-- Pending -->
        <section
          v-else-if="status.request_status === 'pending'"
          class="mt-6 rounded-[28px] border border-amber-100 bg-white p-8 shadow-sm"
        >
          <div class="flex flex-col gap-6 sm:flex-row sm:items-center">
            <div
              class="flex h-16 w-16 shrink-0 items-center justify-center rounded-2xl bg-amber-50 text-2xl"
            >
              ⏳
            </div>

            <div class="flex-1">
              <p
                class="text-xs font-bold uppercase tracking-[0.16em] text-amber-500"
              >
                Request Pending
              </p>

              <h2 class="mt-2 text-2xl font-black text-slate-900">
                Your Premium request is waiting for approval.
              </h2>

              <p class="mt-2 text-sm leading-6 text-slate-500">
                Your request has been submitted successfully. The support team
                will review it manually.
              </p>
            </div>

            <button
              type="button"
              class="rounded-full border border-violet-200 bg-white px-6 py-3 text-sm font-bold text-violet-500 transition hover:bg-violet-50"
              @click="goToTemplates"
            >
              Back to Templates
            </button>
          </div>
        </section>

        <!-- Request Premium -->
        <section
          v-else
          class="mt-6 grid gap-6 lg:grid-cols-[1.4fr_0.8fr]"
        >
          <div
            class="rounded-[28px] border border-violet-100 bg-white p-8 shadow-sm"
          >
            <p
              class="text-xs font-bold uppercase tracking-[0.16em] text-violet-400"
            >
              Premium Access
            </p>

            <h2 class="mt-3 text-3xl font-black text-slate-900">
              Unlock all five portfolio styles.
            </h2>

            <p class="mt-4 text-sm leading-7 text-slate-500">
              Your account currently has access to the free template. Request
              Premium to unlock the remaining premium designs.
            </p>

            <div class="mt-7 grid gap-3 sm:grid-cols-2">
              <div
                v-for="feature in features"
                :key="feature"
                class="flex items-center gap-3 rounded-2xl bg-[#faf9ff] px-4 py-4"
              >
                <span
                  class="flex h-7 w-7 items-center justify-center rounded-full bg-violet-100 text-sm text-violet-500"
                >
                  ✓
                </span>

                <span class="text-sm font-semibold text-slate-700">
                  {{ feature }}
                </span>
              </div>
            </div>

            <div
              v-if="requestError"
              class="mt-6 rounded-2xl border border-red-100 bg-red-50 px-4 py-3 text-sm text-red-500"
            >
              {{ requestError }}
            </div>

            <button
              type="button"
              class="mt-7 rounded-full bg-violet-400 px-7 py-3.5 text-sm font-bold text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-60"
              :disabled="requesting"
              @click="requestPremium"
            >
              {{ requesting ? 'Sending Request...' : 'Request Premium' }}
            </button>
          </div>

          <div
            class="rounded-[28px] border border-violet-100 bg-gradient-to-br from-violet-50 to-white p-8 shadow-sm"
          >
            <div
              class="flex h-14 w-14 items-center justify-center rounded-2xl bg-white text-2xl shadow-sm"
            >
              🔐
            </div>

            <h3 class="mt-6 text-xl font-black text-slate-900">
              Manual approval
            </h3>

            <p class="mt-3 text-sm leading-7 text-slate-500">
              This test version uses manual Premium approval. After you submit
              your request, it will be reviewed from the administration panel.
            </p>

            <div
              class="mt-6 rounded-2xl border border-violet-100 bg-white/80 p-4"
            >
              <p
                class="text-xs font-bold uppercase tracking-[0.14em] text-violet-400"
              >
                How it works
              </p>

              <ol class="mt-3 space-y-3 text-sm text-slate-600">
                <li>1. Submit your request.</li>
                <li>2. Support reviews it.</li>
                <li>3. Premium is activated after approval.</li>
              </ol>
            </div>
          </div>
        </section>

        <!-- Footer -->
        <div
          class="mt-6 flex flex-col gap-3 sm:flex-row sm:justify-between"
        >
          <button
            type="button"
            class="rounded-full px-6 py-3 text-sm font-semibold text-slate-500 transition hover:bg-white hover:text-slate-700"
            @click="router.push('/dashboard')"
          >
            ← Dashboard
          </button>

          <button
            type="button"
            class="rounded-full border border-violet-200 bg-white px-6 py-3 text-sm font-semibold text-violet-500 transition hover:bg-violet-50"
            @click="goToTemplates"
          >
            Browse Templates →
          </button>
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
const loading = ref(true)
const requesting = ref(false)

const error = ref(null)
const requestError = ref(null)

const status = reactive({
  has_subscription: false,
  request_status: null,
})

const features = [
  'Access to all premium templates',
  'Choose your portfolio style anytime',
  'Premium designs for your public portfolio',
  'Keep your existing portfolio content',
]

const loadStatus = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await api.get('/accounts/premium/request/')

    status.has_subscription = Boolean(
      response.data?.has_subscription
    )

    status.request_status =
      response.data?.request_status || null
  } catch (err) {
    console.error('Failed to load Premium status:', err)

    error.value =
      err.response?.data?.detail ||
      'Unable to load your Premium status.'
  } finally {
    loading.value = false
  }
}

const requestPremium = async () => {
  requesting.value = true
  requestError.value = null

  try {
    await api.post('/accounts/premium/request/')

    await loadStatus()
  } catch (err) {
    console.error('Failed to request Premium:', err)

    requestError.value =
      err.response?.data?.detail ||
      'Unable to submit your Premium request.'
  } finally {
    requesting.value = false
  }
}

const goToTemplates = () => {
  router.push('/templates')
}

onMounted(() => {
  loadStatus()
})
</script>

