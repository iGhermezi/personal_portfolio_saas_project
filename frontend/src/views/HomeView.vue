<template>
  <div class="min-h-screen bg-[#faf9ff] text-slate-900">

    <section id="home" class="px-4 py-4 sm:px-6 lg:px-8">
      <div
        class="relative mx-auto min-h-[calc(100vh-32px)] max-w-[1400px] overflow-hidden rounded-[32px] bg-violet-500"
      >

        <div class="pointer-events-none absolute inset-0 z-0 overflow-hidden">

          <div
            class="absolute left-1/2 top-[72%] h-[900px] w-[900px] -translate-x-1/2 rounded-full bg-violet-300/25"
          ></div>


          <div
            class="absolute left-1/2 top-[76%] h-[760px] w-[760px] -translate-x-1/2 rounded-full bg-violet-300/30"
          ></div>


          <div
            class="absolute left-1/2 top-[80%] h-[620px] w-[620px] -translate-x-1/2 rounded-full bg-violet-300/35"
          ></div>


          <div
            class="absolute left-1/2 top-[84%] h-[480px] w-[480px] -translate-x-1/2 rounded-full bg-violet-300/40"
          ></div>
        </div>


        <header
          class="relative z-30 px-5 pt-5 sm:px-8 sm:pt-7 lg:px-12 lg:pt-8"
        >
          <div class="relative mx-auto h-[76px] max-w-6xl">


            <div
              class="absolute left-10 right-10 top-7 h-[76px] rounded-[26px] bg-violet-200"
            ></div>

            <div
              class="absolute left-7 right-7 top-5 h-[76px] rounded-[26px] bg-violet-300"
            ></div>


            <div
              class="absolute left-3 right-3 top-2 h-[76px] rounded-[26px] bg-violet-400"
            ></div>

            <div
              class="absolute inset-x-0 top-0 z-40 h-[76px] rounded-[26px] border border-white/10 bg-violet-500 shadow-xl shadow-violet-700/10"
            >
              <div
                class="flex h-full items-center justify-between px-5 sm:px-7"
              >

                <a href="#home" class="flex items-center gap-2.5">
                  <div
                    class="flex h-9 w-9 items-center justify-center rounded-xl bg-white"
                  >
                    <span class="text-base font-black text-violet-500">
                      P
                    </span>
                  </div>

                  <span class="text-lg font-bold tracking-tight text-white">
                    Portify
                  </span>
                </a>

                <nav class="hidden items-center gap-8 md:flex">
                  <a href="#home" class="text-sm font-medium text-white">
                    Home
                  </a>

                  <a
                    href="#templates"
                    class="text-sm font-medium text-white/65 transition hover:text-white"
                  >
                    Templates
                  </a>

                  <a
                    href="#features"
                    class="text-sm font-medium text-white/65 transition hover:text-white"
                  >
                    Features
                  </a>

                  <a
                    href="#about"
                    class="text-sm font-medium text-white/65 transition hover:text-white"
                  >
                    About
                  </a>

                  <a
                    href="#contact"
                    class="text-sm font-medium text-white/65 transition hover:text-white"
                  >
                    Contact
                  </a>
                </nav>


                <div class="flex items-center gap-3">
                  
                  <router-link
                    to="/login"
                    class="hidden text-sm font-medium text-white/80 sm:block"
                  >
                    Login
                  </router-link>

                  <router-link
                    to="/register"
                    class="rounded-full bg-white px-5 py-2.5 text-sm font-semibold text-violet-500 shadow-sm"
                  >
                    Get Started
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </header>


        <div
          class="relative z-20 mx-auto flex min-h-[calc(100vh-32px)] max-w-5xl flex-col items-center px-6 pb-32 pt-28 text-center sm:pt-32"
        >

          <div
            class="mb-6 rounded-full border border-white/15 bg-white/10 px-4 py-2 backdrop-blur-sm"
          >
            <span
              class="text-xs font-medium tracking-wide text-white/90 sm:text-sm"
            >
              Build your personal portfolio
            </span>
          </div>



          <h1
            class="max-w-4xl text-4xl font-bold leading-[1.08] tracking-tight text-white sm:text-5xl md:text-6xl lg:text-7xl"
          >
            Create a portfolio

            <span class="block text-violet-100"> that represents you. </span>
          </h1>


          <p
            class="mt-6 max-w-2xl text-sm leading-7 text-violet-100/75 sm:text-base sm:leading-8 lg:text-lg"
          >
            Create, customize and publish your personal portfolio with a
            beautiful design that showcases your work, skills and experience.
          </p>


          <div class="mt-8 flex flex-col items-center gap-3 sm:flex-row">
            <router-link
              to="/register"
              class="inline-flex h-12 items-center justify-center rounded-full bg-white px-7 text-sm font-semibold text-violet-500 shadow-lg transition hover:-translate-y-0.5"
            >
              Create my portfolio
            </router-link>

            <a
              href="#templates"
              class="inline-flex h-12 items-center justify-center rounded-full border border-white/20 bg-white/10 px-7 text-sm font-semibold text-white backdrop-blur-sm transition duration-200 hover:bg-white/15"
            >
              Explore templates
            </a>
          </div>



          <div class="mt-10 flex items-center gap-2">
            <span class="h-1.5 w-1.5 rounded-full bg-white/40"></span>

            <span class="h-1.5 w-1.5 rounded-full bg-white/60"></span>

            <span class="h-1.5 w-1.5 rounded-full bg-white/40"></span>
          </div>
        </div>


        <div
          class="pointer-events-none absolute bottom-0 left-0 right-0 z-10 h-32 bg-gradient-to-t from-violet-500 to-transparent"
        ></div>
      </div>
    </section>


    <section id="templates" class="px-6 py-28 sm:px-8">
      <div class="mx-auto max-w-6xl">
        <div class="text-center">
          <span class="text-sm font-semibold text-violet-400"> Templates </span>

          <h2
            class="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
          >
            Choose your starting point
          </h2>

          <p class="mx-auto mt-4 max-w-xl text-slate-500">
            Start with a template and customize it to match your personal style.
          </p>
        </div>
      </div>
    </section>


    <section id="features" class="bg-white px-6 py-28 sm:px-8">
      <div class="mx-auto max-w-6xl">
        <div class="text-center">
          <span class="text-sm font-semibold text-violet-400"> Features </span>

          <h2
            class="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
          >
            Everything for your portfolio
          </h2>
        </div>
      </div>
    </section>


    <section id="about" class="px-6 py-28 sm:px-8">
      <div class="mx-auto max-w-4xl text-center">
        <span class="text-sm font-semibold text-violet-400">
          About Portify
        </span>

        <h2
          class="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
        >
          Your work deserves a place to shine.
        </h2>
      </div>
    </section>


    <section id="contact" class="bg-slate-50 px-6 py-28 sm:px-8">
      <div class="mx-auto max-w-4xl text-center">
        <h2 class="text-3xl font-bold text-slate-900">
          Ready to build your portfolio?
        </h2>
      </div>
    </section>
  </div>
</template>
