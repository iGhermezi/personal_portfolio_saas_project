<template>

  <div
    class="
      flex
      min-h-[420px]
      flex-col
      items-center
      justify-center
      rounded-[28px]
      border
      border-violet-100
      bg-white
      px-6
      text-center
      shadow-sm
    "
  >

    <!-- Icon -->

    <div
      class="
        flex
        h-20
        w-20
        items-center
        justify-center
        rounded-3xl
        bg-violet-50
        text-3xl
      "
    >
      ✦
    </div>


    <h2
      class="
        mt-6
        text-2xl
        font-bold
        text-slate-800
      "
    >
      You don't have a portfolio yet
    </h2>


    <p
      class="
        mt-3
        max-w-md
        text-sm
        leading-6
        text-slate-400
      "
    >
      Create your first portfolio and start
      showcasing your work, skills and experience.
    </p>


    <button
      class="
        mt-7
        rounded-full
        bg-violet-400
        px-7
        py-3
        text-sm
        font-semibold
        text-white
        shadow-lg
        shadow-violet-100
        transition
        hover:-translate-y-0.5
        hover:bg-violet-500
      "
    >
      + Create Portfolio
    </button>


    <router-link
      to="/templates"
      class="
        mt-4
        text-sm
        font-medium
        text-violet-400
        hover:text-violet-500
      "
    >
      Browse templates first
    </router-link>

  </div>

</template>