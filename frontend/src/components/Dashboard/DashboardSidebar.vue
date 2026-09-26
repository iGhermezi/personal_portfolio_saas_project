<template>
  <aside
    :class="[
      'fixed left-0 top-0 z-50 flex h-screen flex-col',
      'border-r border-violet-100 bg-white',
      'transition-all duration-300',
      collapsed ? 'w-[78px]' : 'w-64'
    ]"
  >
    <!-- Logo -->
    <div class="flex h-20 items-center border-b border-violet-50 px-5">
      <div
        class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-violet-400"
      >
        <span class="font-black text-white">P</span>
      </div>

      <span
        v-if="!collapsed"
        class="ml-3 text-lg font-bold tracking-tight text-slate-800"
      >
        Portify
      </span>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 px-3 py-6">
      <div
        v-for="item in navigation"
        :key="item.name"
        class="mb-2"
      >
        <router-link
          :to="item.to"
          class="
            flex w-full items-center rounded-xl
            px-3 py-3
            text-sm font-medium text-slate-500
            transition
            hover:bg-violet-50 hover:text-violet-500
          "
        >
          <span
            class="
              flex h-9 w-9 shrink-0 items-center justify-center
              rounded-lg bg-slate-50 text-sm
            "
          >
            {{ item.icon }}
          </span>

          <span
            v-if="!collapsed"
            class="ml-3"
          >
            {{ item.name }}
          </span>
        </router-link>
      </div>

      <!-- Upgrade -->
      <button
        type="button"
        class="
          mt-4 flex w-full items-center rounded-xl
          bg-violet-50 px-3 py-3
          text-sm font-semibold text-violet-500
          transition hover:bg-violet-100
        "
      >
        <span
          class="
            flex h-9 w-9 shrink-0 items-center justify-center
            rounded-lg bg-violet-100
          "
        >
          ✦
        </span>

        <span
          v-if="!collapsed"
          class="ml-3"
        >
          Upgrade
        </span>
      </button>
    </nav>

    <!-- Bottom -->
    <div class="border-t border-violet-50 p-3">
      <router-link
        to="/profile"
        class="
          flex items-center rounded-xl px-3 py-3
          transition hover:bg-violet-50
        "
      >
        <div
          class="
            flex h-9 w-9 shrink-0 items-center justify-center
            overflow-hidden rounded-full bg-violet-100
            text-sm font-bold text-violet-500
          "
        >
          {{ userInitial }}
        </div>

        <div
          v-if="!collapsed"
          class="ml-3 min-w-0"
        >
          <p
            class="truncate text-sm font-semibold text-slate-800"
          >
            {{ authStore.user?.username || 'User' }}
          </p>

          <p class="truncate text-xs text-slate-400">
            Profile
          </p>
        </div>
      </router-link>

      <button
        type="button"
        @click="logout"
        class="
          mt-2 flex w-full items-center rounded-xl
          px-3 py-3 text-sm font-medium text-slate-500
          transition hover:bg-red-50 hover:text-red-500
        "
      >
        <span
          class="
            flex h-9 w-9 shrink-0 items-center justify-center
            rounded-lg bg-slate-50
          "
        >
          L
        </span>

        <span
          v-if="!collapsed"
          class="ml-3"
        >
          Logout
        </span>
      </button>

      <button
        type="button"
        @click="emit('toggle')"
        class="
          mt-2 flex w-full items-center justify-center
          rounded-xl py-2.5 text-slate-400
          transition hover:bg-slate-50 hover:text-slate-600
        "
      >
        <span class="text-lg">
          {{ collapsed ? '→' : '←' }}
        </span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

import api from '../../api/axios'
import { useAuthStore } from '../../stores/auth'

defineProps({
  collapsed: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['toggle'])

const router = useRouter()
const authStore = useAuthStore()

const portfolioId = ref(null)

const navigation = computed(() => [
  {
    name: 'Dashboard',
    icon: '⌂',
    to: '/dashboard',
  },
  {
    name: 'My Portfolios',
    icon: '▣',
    to: portfolioId.value
      ? `/portfolio/${portfolioId.value}/edit`
      : '/portfolio/create',
  },
  {
    name: 'Templates',
    icon: '◈',
    to: '/templates',
  },
])

const userInitial = computed(() => {
  return (
    authStore.user?.username
      ?.charAt(0)
      ?.toUpperCase() || 'U'
  )
})

const loadPortfolio = async () => {
  try {
    const response = await api.get('/portfolios/')

    const portfolios = Array.isArray(response.data)
      ? response.data
      : response.data.results || []

    if (portfolios.length) {
      portfolioId.value = portfolios[0].id
    }
  } catch (error) {
    console.error(
      'Failed to load portfolio for sidebar:',
      error
    )
  }
}

const logout = () => {
  authStore.logout()
  router.push('/')
}

onMounted(() => {
  loadPortfolio()
})
</script>