<template>

<header
  class="
    mx-0
    rounded-3xl
    border
    border-violet-100
    bg-white
    shadow-[0_10px_40px_rgba(139,92,246,0.12)]
  "
>


    <div>

      <p
        class="
          text-xs
          font-medium
          text-violet-400
        "
      >
        Dashboard
      </p>

      <h1
        class="
          mt-1
          text-xl
          font-bold
          text-slate-800
        "
      >
        Welcome back 👋
      </h1>

    </div>



    <router-link
      to="/profile"
      class="
        flex
        items-center
        gap-3
        rounded-full
        p-1.5
        pr-4
        transition
        hover:bg-violet-50
      "
    >

      <div
        class="
          flex
          h-10
          w-10
          items-center
          justify-center
          overflow-hidden
          rounded-full
          bg-violet-100
          font-semibold
          text-violet-500
        "
      >
        {{ initial }}
      </div>

      <div class="hidden text-left sm:block">

        <p
          class="
            text-sm
            font-semibold
            text-slate-800
          "
        >
          {{ authStore.user?.username || 'User' }}
        </p>

        <p
          class="
            text-xs
            text-slate-400
          "
        >
          View profile
        </p>

      </div>

    </router-link>

  </header>

</template>


<script setup>

import { computed } from 'vue'
import { useAuthStore } from '../../stores/auth'


const authStore = useAuthStore()


const initial = computed(() => {

  return (
    authStore.user?.username
      ?.charAt(0)
      ?.toUpperCase() || 'U'
  )

})

</script>