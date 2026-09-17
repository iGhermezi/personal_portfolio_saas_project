<template>

  <div
    class="
      min-h-screen
      bg-[#faf9ff]
      px-5
      py-5
    "
  >

    <!-- Sidebar -->

    <DashboardSidebar
      :collapsed="sidebarCollapsed"
      @toggle="sidebarCollapsed = !sidebarCollapsed"
    />


    <!-- Main Area -->

    <main
      class="
        min-h-[calc(100vh-40px)]
        transition-transform
        duration-300
        ease-in-out
      "
      :class="
        sidebarCollapsed
          ? 'ml-[98px]'
          : 'ml-[284px]'
      "
    >

      <!-- Header -->

      <DashboardHeader />


      <!-- Content -->

      <div
        class="
          mx-auto
          max-w-7xl
          px-6
          py-8
        "
      >

        <!-- Page heading -->

        <div class="mb-8">

          <p
            class="
              text-sm
              font-medium
              text-violet-400
            "
          >
            Overview
          </p>


          <h1
            class="
              mt-1
              text-3xl
              font-bold
              tracking-tight
              text-slate-900
            "
          >
            Your workspace
          </h1>


          <p
            class="
              mt-2
              text-sm
              text-slate-400
            "
          >
            Manage your portfolio and customize your online presence.
          </p>

        </div>


        <!-- Portfolio -->

        <PortfolioEmpty
          v-if="!portfolio"
        />


        <PortfolioCard
          v-else
          :portfolio="portfolio"
        />

      </div>

    </main>

  </div>

</template>


<script setup>

import { ref } from 'vue'

import DashboardSidebar
  from '../components/dashboard/DashboardSidebar.vue'

import DashboardHeader
  from '../components/dashboard/DashboardHeader.vue'

import PortfolioEmpty
  from '../components/dashboard/PortfolioEmpty.vue'

import PortfolioCard
  from '../components/dashboard/PortfolioCard.vue'


/*
 * Sidebar state
 *
 * false = باز
 * true  = بسته
 */

const sidebarCollapsed = ref(false)


/*
 * فعلاً Mock Data
 */

const portfolio = null

</script>