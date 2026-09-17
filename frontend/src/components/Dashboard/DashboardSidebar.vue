<template>

  <aside
    :class="[
      'fixed left-5 top-5 bottom-5 z-50',
      'flex flex-col',
      'rounded-3xl',
      'border border-violet-100',
      'bg-white',
      'shadow-[0_10px_40px_rgba(139,92,246,0.16)]',
      'transition-[width] duration-300 ease-in-out',
      collapsed ? 'w-[78px]' : 'w-64'
    ]"
  >

    <!-- Logo -->

    <div
      class="
        flex
        h-20
        shrink-0
        items-center
        border-b
        border-violet-50
        px-5
      "
    >

      <div
        class="
          flex
          h-10
          w-10
          shrink-0
          items-center
          justify-center
          rounded-xl
          bg-violet-400
        "
      >
        <span class="font-black text-white">
          P
        </span>
      </div>


      <span
        v-if="!collapsed"
        class="
          ml-3
          whitespace-nowrap
          text-lg
          font-bold
          tracking-tight
          text-slate-800
        "
      >
        Portify
      </span>

    </div>


    <!-- Navigation -->

    <nav class="flex-1 overflow-hidden px-3 py-6">

      <div
        v-for="item in navigation"
        :key="item.name"
        class="mb-2"
      >

        <router-link
          :to="item.to"
          :class="[
            'flex items-center rounded-xl',
            'px-3 py-3',
            'text-sm font-medium text-slate-500',
            'transition-colors duration-200',
            'hover:bg-violet-50 hover:text-violet-500',
            collapsed ? 'justify-center' : ''
          ]"
        >

          <!-- Icon -->

          <span
            class="
              flex
              h-9
              w-9
              shrink-0
              items-center
              justify-center
              rounded-lg
              bg-slate-50
              text-sm
            "
          >
            {{ item.icon }}
          </span>


          <span
            v-if="!collapsed"
            class="
              ml-3
              whitespace-nowrap
            "
          >
            {{ item.name }}
          </span>

        </router-link>

      </div>


      <!-- Upgrade -->

      <button
        :class="[
          'mt-4 flex w-full items-center rounded-xl',
          'bg-violet-50 px-3 py-3',
          'text-sm font-semibold text-violet-500',
          'transition-colors duration-200',
          'hover:bg-violet-100',
          collapsed ? 'justify-center' : ''
        ]"
      >

        <span
          class="
            flex
            h-9
            w-9
            shrink-0
            items-center
            justify-center
            rounded-lg
            bg-violet-100
          "
        >
          ✦
        </span>


        <span
          v-if="!collapsed"
          class="
            ml-3
            whitespace-nowrap
          "
        >
          Upgrade
        </span>

      </button>

    </nav>


    <!-- Bottom -->

    <div
      class="
        shrink-0
        border-t
        border-violet-50
        p-3
      "
    >

      <!-- Profile -->

      <router-link
        to="/profile"
        :class="[
          'flex items-center rounded-xl',
          'px-3 py-3',
          'transition-colors duration-200',
          'hover:bg-violet-50',
          collapsed ? 'justify-center' : ''
        ]"
      >

        <div
          class="
            flex
            h-9
            w-9
            shrink-0
            items-center
            justify-center
            overflow-hidden
            rounded-full
            bg-violet-100
            text-sm
            font-bold
            text-violet-500
          "
        >
          {{ userInitial }}
        </div>


        <div
          v-if="!collapsed"
          class="
            ml-3
            min-w-0
          "
        >

          <p
            class="
              truncate
              text-sm
              font-semibold
              text-slate-800
            "
          >
            {{ authStore.user?.username || 'User' }}
          </p>


          <p
            class="
              truncate
              text-xs
              text-slate-400
            "
          >
            Profile
          </p>

        </div>

      </router-link>


      <!-- Logout -->

      <button
        @click="logout"
        :class="[
          'mt-2 flex w-full items-center rounded-xl',
          'px-3 py-3',
          'text-sm font-medium text-slate-500',
          'transition-colors duration-200',
          'hover:bg-red-50 hover:text-red-500',
          collapsed ? 'justify-center' : ''
        ]"
      >

        <span
          class="
            flex
            h-9
            w-9
            shrink-0
            items-center
            justify-center
            rounded-lg
            bg-slate-50
          "
        >
          L
        </span>


        <span
          v-if="!collapsed"
          class="
            ml-3
            whitespace-nowrap
          "
        >
          Logout
        </span>

      </button>


      <!-- Collapse -->

      <button
        @click="emit('toggle')"
        class="
          mt-2
          flex
          w-full
          items-center
          justify-center
          rounded-xl
          py-2.5
          text-slate-400
          transition-colors
          duration-200
          hover:bg-slate-50
          hover:text-slate-600
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

import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

defineProps({
  collapsed: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['toggle'])

const router = useRouter()
const authStore = useAuthStore()


const logout = () => {

  authStore.logout()

  router.push('/')

}

</script>