<template>
  <div
    class="min-h-screen overflow-x-hidden bg-white text-slate-900 transition-colors duration-300 dark:bg-[#100b1c] dark:text-slate-100"
  >
    <!-- ========================================================= -->
    <!-- NAVBAR -->
    <!-- ========================================================= -->

    <section id="home" class="px-3 pt-3 sm:px-5 sm:pt-5">
      <div
        class="relative mx-auto min-h-[calc(100vh-24px)] max-w-[1440px] overflow-hidden rounded-[30px] bg-violet-600 shadow-2xl shadow-violet-500/10 sm:rounded-[38px]"
      >
        <!-- Background -->
        <div class="pointer-events-none absolute inset-0 overflow-hidden">
          <!-- Three-layer Hero rings -->
          <div
            class="absolute left-1/2 bottom-[-280px] h-[760px] w-[760px] -translate-x-1/2 rounded-full bg-violet-300/20"
          ></div>

          <div
            class="absolute left-1/2 bottom-[-210px] h-[620px] w-[620px] -translate-x-1/2 rounded-full bg-violet-300/25"
          ></div>

          <div
            class="absolute left-1/2 bottom-[-140px] h-[480px] w-[480px] -translate-x-1/2 rounded-full bg-violet-300/30"
          ></div>
          <div
            class="absolute -left-32 -top-32 h-[420px] w-[420px] rounded-full bg-violet-400/30 blur-3xl"
          ></div>

          <div
            class="absolute -right-40 top-20 h-[520px] w-[520px] rounded-full bg-fuchsia-400/20 blur-3xl"
          ></div>

          <div
            class="absolute bottom-[-260px] left-1/2 h-[700px] w-[700px] -translate-x-1/2 rounded-full border border-white/10"
          ></div>

          <div
            class="absolute bottom-[-190px] left-1/2 h-[560px] w-[560px] -translate-x-1/2 rounded-full border border-white/10"
          ></div>

          <div
            class="absolute bottom-[-120px] left-1/2 h-[420px] w-[420px] -translate-x-1/2 rounded-full border border-white/10"
          ></div>

          <div
            class="absolute inset-x-0 bottom-0 h-72 bg-gradient-to-t from-violet-600 via-violet-600/70 to-transparent"
          ></div>
        </div>

        <!-- Navbar -->
        <header
          class="relative z-40 px-4 pt-4 sm:px-7 sm:pt-7 lg:px-10 lg:pt-8"
        >
          <div
            class="mx-auto max-w-6xl rounded-[24px] border border-white/10 bg-white/10 px-4 py-3 shadow-2xl shadow-violet-950/10 backdrop-blur-xl sm:px-5"
          >
            <div class="flex items-center justify-between">
              <!-- Logo -->
              <a href="#home" class="flex items-center gap-2.5">
                <div
                  class="flex h-10 w-10 items-center justify-center rounded-xl bg-white shadow-sm"
                >
                  <span class="text-lg font-black text-violet-600">P</span>
                </div>

                <span
                  class="text-lg font-black tracking-tight text-white sm:text-xl"
                >
                  Portify
                </span>
              </a>

              <!-- Desktop navigation -->
              <nav class="hidden items-center gap-7 md:flex">
                <a
                  href="#home"
                  class="text-sm font-medium text-white transition hover:text-violet-100"
                >
                  {{ i18nStore.t("common.home") }}
                </a>

                <a
                  href="#templates"
                  class="text-sm font-medium text-white/65 transition hover:text-white"
                >
                  {{ i18nStore.t("common.templates") }}
                </a>

                <a
                  href="#features"
                  class="text-sm font-medium text-white/65 transition hover:text-white"
                >
                  {{ i18nStore.t("common.features") }}
                </a>

                <a
                  href="#about"
                  class="text-sm font-medium text-white/65 transition hover:text-white"
                >
                  {{ i18nStore.t("common.about") }}
                </a>
              </nav>

              <!-- Actions -->
              <div class="flex items-center gap-2 sm:gap-3">
                <router-link
                  to="/login"
                  class="hidden rounded-full px-3 py-2 text-sm font-medium text-white/80 transition hover:bg-white/10 hover:text-white sm:block"
                >
                  {{ i18nStore.t("common.login") }}
                </router-link>

                <router-link
                  to="/register"
                  class="rounded-full bg-white px-4 py-2.5 text-sm font-bold text-violet-600 shadow-lg shadow-violet-950/10 transition duration-200 hover:-translate-y-0.5 hover:shadow-xl sm:px-5"
                >
                  {{ i18nStore.t("common.getStarted") }}
                </router-link>
              </div>
            </div>
          </div>
        </header>

        <!-- ===================================================== -->
        <!-- HERO -->
        <!-- ===================================================== -->

        <div
          class="relative z-20 mx-auto max-w-6xl px-5 pb-20 pt-20 sm:px-8 sm:pb-24 sm:pt-24 lg:px-10 lg:pt-28"
        >
          <div class="grid items-center gap-14 lg:grid-cols-[0.95fr_1.05fr]">
            <!-- Hero copy -->
            <div class="text-center lg:text-left rtl:lg:text-right">
              <div
                class="mx-auto inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/10 px-4 py-2 backdrop-blur-md lg:mx-0"
              >
                <span class="h-2 w-2 rounded-full bg-emerald-300"></span>

                <span
                  class="text-xs font-semibold tracking-wide text-white/90 sm:text-sm"
                >
                  {{ i18nStore.t("home.badge") }}
                </span>
              </div>

              <h1
                class="mx-auto mt-7 max-w-2xl text-4xl font-black leading-[1.05] tracking-tight text-white sm:text-5xl md:text-6xl lg:mx-0 lg:text-7xl"
              >
                {{ i18nStore.t("home.title") }}

                <span class="mt-2 block text-violet-100">
                  {{ i18nStore.t("home.titleAccent") }}
                </span>
              </h1>

              <p
                class="mx-auto mt-7 max-w-xl text-sm leading-7 text-violet-100/75 sm:text-base sm:leading-8 lg:mx-0 lg:text-lg"
              >
                {{ i18nStore.t("home.description") }}
              </p>

              <div
                class="mt-9 flex flex-col justify-center gap-3 sm:flex-row lg:justify-start rtl:lg:flex-row-reverse"
              >
                <router-link
                  to="/register"
                  class="inline-flex h-13 items-center justify-center rounded-full bg-white px-7 text-sm font-bold text-violet-600 shadow-xl shadow-violet-950/20 transition duration-200 hover:-translate-y-1 hover:shadow-2xl"
                >
                  {{ i18nStore.t("common.createPortfolio") }}
                </router-link>

                <a
                  href="#templates"
                  class="inline-flex h-13 items-center justify-center rounded-full border border-white/20 bg-white/10 px-7 text-sm font-semibold text-white backdrop-blur-md transition duration-200 hover:bg-white/15"
                >
                  {{ i18nStore.t("common.exploreTemplates") }}
                </a>
              </div>

              <!-- Small value points -->
              <div
                class="mt-9 flex flex-wrap justify-center gap-x-6 gap-y-3 text-xs font-medium text-white/60 lg:justify-start"
              >
                <span class="flex items-center gap-2">
                  <span
                    class="flex h-5 w-5 items-center justify-center rounded-full bg-white/10 text-[10px] text-white"
                  >
                    ✓
                  </span>
                  {{
                    i18nStore.language === "fa" ? "ویرایش آسان" : "Easy editing"
                  }}
                </span>

                <span class="flex items-center gap-2">
                  <span
                    class="flex h-5 w-5 items-center justify-center rounded-full bg-white/10 text-[10px] text-white"
                  >
                    ✓
                  </span>
                  {{
                    i18nStore.language === "fa"
                      ? "قالب‌های متنوع"
                      : "Multiple templates"
                  }}
                </span>

                <span class="flex items-center gap-2">
                  <span
                    class="flex h-5 w-5 items-center justify-center rounded-full bg-white/10 text-[10px] text-white"
                  >
                    ✓
                  </span>
                  {{
                    i18nStore.language === "fa"
                      ? "انتشار عمومی"
                      : "Public publishing"
                  }}
                </span>
              </div>
            </div>

            <!-- Product Preview -->
            <div class="relative mx-auto w-full max-w-[620px]">
              <div
                class="absolute -inset-8 rounded-[50px] bg-white/10 blur-3xl"
              ></div>

              <div
                class="relative overflow-hidden rounded-[28px] border border-white/15 bg-white/95 p-3 shadow-2xl shadow-violet-950/30 backdrop-blur-xl transition duration-500 hover:-translate-y-2 sm:p-4"
              >
                <!-- Browser top -->
                <div
                  class="flex items-center justify-between rounded-2xl bg-slate-100 px-4 py-3"
                >
                  <div class="flex gap-1.5">
                    <span class="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
                    <span class="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
                    <span class="h-2.5 w-2.5 rounded-full bg-slate-300"></span>
                  </div>

                  <div
                    class="hidden rounded-full bg-white px-4 py-1.5 text-[10px] font-medium text-slate-400 shadow-sm sm:block"
                  >
                    portify.app/your-name
                  </div>

                  <div
                    class="flex h-7 w-7 items-center justify-center rounded-full bg-violet-100 text-xs font-bold text-violet-500"
                  >
                    P
                  </div>
                </div>

                <!-- Portfolio mockup -->
                <div class="mt-3 overflow-hidden rounded-2xl bg-[#fff8f5]">
                  <div
                    class="flex items-center justify-between border-b border-[#ead8d3] px-5 py-4"
                  >
                    <div class="flex items-center gap-2">
                      <div
                        class="flex h-8 w-8 items-center justify-center rounded-lg bg-[#542631] text-xs font-black text-white"
                      >
                        P
                      </div>

                      <div>
                        <div
                          class="h-2 w-20 rounded-full bg-[#542631]/80"
                        ></div>
                        <div
                          class="mt-1.5 h-1.5 w-12 rounded-full bg-[#805861]/30"
                        ></div>
                      </div>
                    </div>

                    <div class="flex gap-2">
                      <span
                        class="hidden h-5 w-12 rounded-full bg-[#ead8d3] sm:block"
                      ></span>
                      <span
                        class="hidden h-5 w-12 rounded-full bg-[#ead8d3] sm:block"
                      ></span>
                      <span class="h-5 w-8 rounded-full bg-[#d83f55]/20"></span>
                    </div>
                  </div>

                  <div class="grid gap-5 p-5 sm:grid-cols-[1fr_0.8fr] sm:p-7">
                    <div class="flex flex-col justify-center">
                      <div
                        class="inline-flex w-fit rounded-full bg-[#d83f55]/10 px-3 py-1"
                      >
                        <span class="text-[9px] font-bold text-[#d83f55]">
                          AVAILABLE FOR WORK
                        </span>
                      </div>

                      <div
                        class="mt-4 h-4 w-44 rounded-full bg-[#542631]"
                      ></div>

                      <div
                        class="mt-2 h-4 w-32 rounded-full bg-[#d83f55]"
                      ></div>

                      <div class="mt-5 space-y-2">
                        <div
                          class="h-2 w-full max-w-[250px] rounded-full bg-[#805861]/25"
                        ></div>

                        <div
                          class="h-2 w-4/5 max-w-[200px] rounded-full bg-[#805861]/20"
                        ></div>

                        <div
                          class="h-2 w-3/5 max-w-[160px] rounded-full bg-[#805861]/15"
                        ></div>
                      </div>

                      <div class="mt-6 flex gap-2">
                        <span class="h-8 w-20 rounded-full bg-[#542631]"></span>

                        <span
                          class="h-8 w-20 rounded-full border border-[#d83f55]/30 bg-white"
                        ></span>
                      </div>
                    </div>

                    <div
                      class="relative min-h-[190px] overflow-hidden rounded-[24px] bg-[#f5d8dc]"
                    >
                      <div
                        class="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-[#d83f55]/20"
                      ></div>

                      <div
                        class="absolute bottom-5 left-5 right-5 rounded-2xl bg-white/80 p-4 shadow-lg backdrop-blur"
                      >
                        <div class="h-2 w-20 rounded-full bg-[#542631]"></div>

                        <div class="mt-3 grid grid-cols-3 gap-2">
                          <div class="h-12 rounded-lg bg-[#d83f55]/15"></div>

                          <div class="h-12 rounded-lg bg-[#542631]/10"></div>

                          <div class="h-12 rounded-lg bg-[#d83f55]/10"></div>
                        </div>
                      </div>

                      <div
                        class="absolute left-1/2 top-10 flex h-20 w-20 -translate-x-1/2 items-center justify-center rounded-full border-4 border-white bg-[#d83f55] text-2xl shadow-xl"
                      >
                        ✦
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Floating editor badge -->
                <div
                  class="absolute bottom-8 left-6 hidden rounded-2xl border border-white/70 bg-white px-4 py-3 shadow-xl sm:block"
                >
                  <div class="flex items-center gap-3">
                    <div
                      class="flex h-9 w-9 items-center justify-center rounded-xl bg-violet-100 text-violet-500"
                    >
                      ✦
                    </div>

                    <div>
                      <p class="text-[10px] font-bold text-slate-800">
                        {{
                          i18nStore.language === "fa"
                            ? "ویرایشگر پورتفولیو"
                            : "Portfolio editor"
                        }}
                      </p>

                      <p class="mt-0.5 text-[9px] text-slate-400">
                        {{
                          i18nStore.language === "fa"
                            ? "آماده انتشار"
                            : "Ready to publish"
                        }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Bottom hero line -->
          <div
            class="mx-auto mt-16 flex max-w-5xl flex-col items-center justify-between gap-5 border-t border-white/10 pt-6 text-center sm:flex-row sm:text-left"
          >
            <p class="text-xs font-medium text-white/50">
              {{
                i18nStore.language === "fa"
                  ? "از اطلاعات شخصی تا پروژه‌ها، همه‌چیز در یکجا."
                  : "From your profile to your projects — everything in one place."
              }}
            </p>

            <a
              href="#templates"
              class="text-xs font-bold text-white/80 transition hover:text-white"
            >
              {{
                i18nStore.language === "fa"
                  ? "پایین‌تر برو ↓"
                  : "Explore below ↓"
              }}
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- VALUE STRIP -->
    <!-- ========================================================= -->

    <section class="px-5 py-10 sm:px-8">
      <div
        class="mx-auto grid max-w-6xl overflow-hidden rounded-[28px] border border-violet-100 bg-white shadow-sm dark:border-white/10 dark:bg-white/[0.04] sm:grid-cols-3"
      >
        <div
          class="flex items-center gap-4 border-b border-violet-100 p-6 dark:border-white/10 sm:border-b-0 sm:border-r"
        >
          <div
            class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/15"
          >
            01
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900 dark:text-white">
              {{ i18nStore.language === "fa" ? "ساخت" : "Create" }}
            </p>

            <p class="mt-1 text-xs text-slate-500 dark:text-slate-400">
              {{
                i18nStore.language === "fa"
                  ? "اطلاعات خودت را وارد کن"
                  : "Add your information"
              }}
            </p>
          </div>
        </div>

        <div
          class="flex items-center gap-4 border-b border-violet-100 p-6 dark:border-white/10 sm:border-b-0 sm:border-r"
        >
          <div
            class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/15"
          >
            02
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900 dark:text-white">
              {{ i18nStore.language === "fa" ? "شخصی‌سازی" : "Customize" }}
            </p>

            <p class="mt-1 text-xs text-slate-500 dark:text-slate-400">
              {{
                i18nStore.language === "fa"
                  ? "قالب و محتوا را تنظیم کن"
                  : "Shape your portfolio"
              }}
            </p>
          </div>
        </div>

        <div class="flex items-center gap-4 p-6">
          <div
            class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/15"
          >
            03
          </div>

          <div>
            <p class="text-sm font-bold text-slate-900 dark:text-white">
              {{ i18nStore.language === "fa" ? "انتشار" : "Publish" }}
            </p>

            <p class="mt-1 text-xs text-slate-500 dark:text-slate-400">
              {{
                i18nStore.language === "fa"
                  ? "پورتفولیوی خودت را نمایش بده"
                  : "Share your portfolio"
              }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- TEMPLATES -->
    <!-- ========================================================= -->

    <section id="templates" class="px-5 py-24 sm:px-8 lg:py-32">
      <div class="mx-auto max-w-6xl">
        <div
          class="flex flex-col justify-between gap-6 md:flex-row md:items-end"
        >
          <div class="max-w-2xl">
            <span class="text-sm font-bold text-violet-500">
              {{ i18nStore.t("home.templatesLabel") }}
            </span>

            <h2
              class="mt-3 text-3xl font-black tracking-tight text-slate-900 dark:text-white sm:text-5xl"
            >
              {{ i18nStore.t("home.templatesTitle") }}
            </h2>

            <p
              class="mt-5 max-w-xl text-sm leading-7 text-slate-500 dark:text-slate-400 sm:text-base"
            >
              {{ i18nStore.t("home.templatesDescription") }}
            </p>
          </div>

          <router-link
            to="/templates"
            class="inline-flex w-fit items-center rounded-full border border-violet-200 bg-white px-5 py-3 text-sm font-bold text-violet-600 transition hover:-translate-y-0.5 hover:border-violet-300 dark:border-white/10 dark:bg-white/[0.04] dark:text-violet-300"
          >
            {{ i18nStore.t("common.exploreTemplates") }}
            <span class="ml-2">→</span>
          </router-link>
        </div>

        <!-- Template cards -->
        <div class="mt-12 grid gap-5 md:grid-cols-2 lg:grid-cols-3">
          <!-- Arsam -->
          <div
            class="group overflow-hidden rounded-[28px] border border-[#ead8d3] bg-[#fff8f5] shadow-sm transition duration-300 hover:-translate-y-2 hover:shadow-xl"
          >
            <div class="relative h-56 overflow-hidden bg-[#f5d8dc] p-5">
              <div
                class="absolute -right-12 -top-12 h-40 w-40 rounded-full bg-[#d83f55]/20"
              ></div>

              <div
                class="relative h-full overflow-hidden rounded-2xl bg-white p-5 shadow-lg"
              >
                <div class="flex items-center justify-between">
                  <div class="h-3 w-20 rounded-full bg-[#542631]"></div>
                  <div class="h-5 w-5 rounded-full bg-[#d83f55]"></div>
                </div>

                <div class="mt-7">
                  <div class="h-4 w-32 rounded-full bg-[#542631]"></div>
                  <div class="mt-2 h-3 w-24 rounded-full bg-[#d83f55]"></div>
                </div>

                <div class="mt-7 grid grid-cols-3 gap-2">
                  <div class="h-12 rounded-xl bg-[#d83f55]/10"></div>
                  <div class="h-12 rounded-xl bg-[#542631]/10"></div>
                  <div class="h-12 rounded-xl bg-[#d83f55]/10"></div>
                </div>
              </div>

              <div
                class="absolute bottom-4 left-4 rounded-full bg-white px-3 py-1.5 text-[10px] font-bold text-[#d83f55] shadow-lg"
              >
                Arsam
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-center justify-between gap-3">
                <h3 class="font-black text-slate-900">
                  {{ i18nStore.templateName({ template_key: "arsam" }) }}
                </h3>

                <span
                  class="rounded-full bg-emerald-50 px-3 py-1 text-[10px] font-bold text-emerald-600"
                >
                  {{ i18nStore.t("templates.free") }}
                </span>
              </div>

              <p class="mt-3 text-xs leading-6 text-slate-500">
                {{ i18nStore.templateDescription({ template_key: "arsam" }) }}
              </p>
            </div>
          </div>

          <!-- Minimal Dark -->
          <div
            class="group overflow-hidden rounded-[28px] border border-slate-800 bg-[#101010] shadow-sm transition duration-300 hover:-translate-y-2 hover:shadow-xl"
          >
            <div class="relative h-56 overflow-hidden p-5">
              <div
                class="absolute right-8 top-8 h-32 w-32 rounded-full bg-violet-500/10 blur-2xl"
              ></div>

              <div
                class="relative h-full rounded-2xl border border-white/10 bg-[#161616] p-5"
              >
                <div class="flex items-center justify-between">
                  <div class="h-3 w-24 rounded-full bg-white/80"></div>
                  <div class="h-5 w-5 rounded-full bg-violet-400"></div>
                </div>

                <div class="mt-7">
                  <div class="h-4 w-40 rounded-full bg-white/80"></div>
                  <div class="mt-2 h-2.5 w-28 rounded-full bg-white/20"></div>
                </div>

                <div class="mt-7 grid grid-cols-2 gap-2">
                  <div class="h-10 rounded-lg bg-white/5"></div>
                  <div class="h-10 rounded-lg bg-violet-500/10"></div>
                </div>
              </div>

              <div
                class="absolute bottom-4 left-4 rounded-full border border-white/10 bg-black/70 px-3 py-1.5 text-[10px] font-bold text-white"
              >
                Minimal Dark
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-center justify-between gap-3">
                <h3 class="font-black text-white">
                  {{ i18nStore.templateName({ template_key: "template_2" }) }}
                </h3>

                <span
                  class="rounded-full bg-violet-500/10 px-3 py-1 text-[10px] font-bold text-violet-300"
                >
                  {{ i18nStore.t("templates.premium") }}
                </span>
              </div>

              <p class="mt-3 text-xs leading-6 text-slate-400">
                {{
                  i18nStore.templateDescription({
                    template_key: "template_2",
                  })
                }}
              </p>
            </div>
          </div>

          <!-- Creative Brutalist -->
          <div
            class="group overflow-hidden rounded-[28px] border-2 border-black bg-[#f5f0e8] shadow-sm transition duration-300 hover:-translate-y-2 hover:shadow-xl dark:border-white"
          >
            <div class="relative h-56 overflow-hidden bg-[#ffdd00] p-5">
              <div
                class="absolute right-6 top-5 rotate-6 border-2 border-black bg-white px-3 py-1 text-[9px] font-black text-black"
              >
                CREATIVE
              </div>

              <div
                class="relative h-full border-2 border-black bg-[#f5f0e8] p-5"
              >
                <div class="text-[10px] font-black text-black">
                  PORTFOLIO / 01
                </div>

                <div
                  class="mt-5 text-3xl font-black leading-none text-black sm:text-4xl"
                >
                  MAKE<br />THINGS.
                </div>

                <div
                  class="absolute bottom-4 right-4 h-10 w-10 rounded-full border-2 border-black bg-[#ff4d00]"
                ></div>
              </div>
            </div>

            <div class="bg-[#f5f0e8] p-6">
              <div class="flex items-center justify-between gap-3">
                <h3 class="font-black text-black">
                  {{
                    i18nStore.templateName({
                      template_key: "template_3",
                    })
                  }}
                </h3>

                <span
                  class="rounded-full border border-black bg-black px-3 py-1 text-[10px] font-bold text-white"
                >
                  {{ i18nStore.t("templates.premium") }}
                </span>
              </div>

              <p class="mt-3 text-xs leading-6 text-slate-600">
                {{
                  i18nStore.templateDescription({
                    template_key: "template_3",
                  })
                }}
              </p>
            </div>
          </div>

          <!-- Editorial -->
          <div
            class="group overflow-hidden rounded-[28px] border border-stone-200 bg-[#f7f4ef] shadow-sm transition duration-300 hover:-translate-y-2 hover:shadow-xl"
          >
            <div class="h-56 overflow-hidden bg-[#ebe4d9] p-5">
              <div class="h-full border border-stone-300 bg-[#f7f4ef] p-6">
                <div
                  class="flex items-center justify-between border-b border-stone-300 pb-3"
                >
                  <span
                    class="font-serif text-xs font-bold tracking-[0.25em] text-stone-800"
                  >
                    EDITORIAL
                  </span>

                  <span class="text-[9px] text-stone-500">2026</span>
                </div>

                <div class="mt-8 grid grid-cols-[1.3fr_0.7fr] gap-5">
                  <div>
                    <div
                      class="font-serif text-3xl leading-none text-stone-900"
                    >
                      Your<br />Story.
                    </div>

                    <div class="mt-5 h-1 w-16 bg-stone-800"></div>
                  </div>

                  <div class="rounded-sm bg-stone-300/60"></div>
                </div>
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-center justify-between gap-3">
                <h3 class="font-black text-slate-900">
                  {{
                    i18nStore.templateName({
                      template_key: "template_4",
                    })
                  }}
                </h3>

                <span
                  class="rounded-full bg-violet-50 px-3 py-1 text-[10px] font-bold text-violet-600"
                >
                  {{ i18nStore.t("templates.premium") }}
                </span>
              </div>

              <p class="mt-3 text-xs leading-6 text-slate-500">
                {{
                  i18nStore.templateDescription({
                    template_key: "template_4",
                  })
                }}
              </p>
            </div>
          </div>

          <!-- Terminal -->
          <div
            class="group overflow-hidden rounded-[28px] border border-emerald-900/30 bg-[#07120d] shadow-sm transition duration-300 hover:-translate-y-2 hover:shadow-xl"
          >
            <div class="h-56 overflow-hidden p-5">
              <div
                class="h-full rounded-2xl border border-emerald-400/20 bg-[#020805] p-5 font-mono"
              >
                <div class="flex items-center gap-2">
                  <span class="text-emerald-400">$</span>
                  <span class="text-xs text-emerald-200/80"> whoami </span>
                </div>

                <div class="mt-4 text-sm font-bold text-emerald-300">
                  developer
                </div>

                <div class="mt-5 space-y-2 text-[9px] text-emerald-200/50">
                  <div>&gt; building products...</div>
                  <div>&gt; writing clean code...</div>
                  <div>&gt; shipping ideas...</div>
                </div>

                <div class="mt-5 flex gap-2">
                  <span class="h-5 w-16 rounded bg-emerald-400/10"></span>
                  <span class="h-5 w-20 rounded bg-emerald-400/10"></span>
                  <span class="h-5 w-12 rounded bg-emerald-400/10"></span>
                </div>
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-center justify-between gap-3">
                <h3 class="font-black text-white">
                  {{
                    i18nStore.templateName({
                      template_key: "template_5",
                    })
                  }}
                </h3>

                <span
                  class="rounded-full bg-emerald-400/10 px-3 py-1 text-[10px] font-bold text-emerald-300"
                >
                  {{ i18nStore.t("templates.premium") }}
                </span>
              </div>

              <p class="mt-3 text-xs leading-6 text-slate-400">
                {{
                  i18nStore.templateDescription({
                    template_key: "template_5",
                  })
                }}
              </p>
            </div>
          </div>

          <!-- Emerald -->
          <div
            class="group overflow-hidden rounded-[28px] border border-emerald-950 bg-[#06120e] shadow-sm transition duration-300 hover:-translate-y-2 hover:shadow-xl"
          >
            <div class="h-56 overflow-hidden p-5">
              <div
                class="relative h-full overflow-hidden rounded-2xl border border-emerald-400/10 bg-[#091b15] p-6"
              >
                <div
                  class="absolute -right-12 -top-12 h-40 w-40 rounded-full bg-emerald-400/10 blur-2xl"
                ></div>

                <div
                  class="text-[9px] font-bold tracking-[0.3em] text-emerald-400"
                >
                  SIGNATURE
                </div>

                <div class="mt-7">
                  <div class="h-4 w-36 rounded-full bg-white/80"></div>
                  <div
                    class="mt-2 h-2.5 w-24 rounded-full bg-emerald-400/60"
                  ></div>
                </div>

                <div class="mt-8 grid grid-cols-2 gap-2">
                  <div
                    class="h-10 rounded-xl border border-emerald-400/10 bg-emerald-400/5"
                  ></div>

                  <div
                    class="h-10 rounded-xl border border-emerald-400/10 bg-white/5"
                  ></div>
                </div>
              </div>
            </div>

            <div class="p-6">
              <div class="flex items-center justify-between gap-3">
                <h3 class="font-black text-white">
                  {{
                    i18nStore.templateName({
                      template_key: "template_6",
                    })
                  }}
                </h3>

                <span
                  class="rounded-full bg-emerald-400/10 px-3 py-1 text-[10px] font-bold text-emerald-300"
                >
                  {{ i18nStore.t("templates.premium") }}
                </span>
              </div>

              <p class="mt-3 text-xs leading-6 text-slate-400">
                {{
                  i18nStore.templateDescription({
                    template_key: "template_6",
                  })
                }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- HOW IT WORKS -->
    <!-- ========================================================= -->

    <section
      class="border-y border-violet-100 bg-white px-5 py-24 dark:border-white/10 dark:bg-white/[0.025] sm:px-8 lg:py-32"
    >
      <div class="mx-auto max-w-6xl">
        <div class="mx-auto max-w-2xl text-center">
          <span class="text-sm font-bold text-violet-500">
            {{
              i18nStore.language === "fa" ? "چطور کار می‌کند؟" : "How it works"
            }}
          </span>

          <h2
            class="mt-3 text-3xl font-black tracking-tight text-slate-900 dark:text-white sm:text-5xl"
          >
            {{
              i18nStore.language === "fa"
                ? "ساده شروع کن، حرفه‌ای منتشر کن."
                : "Simple to start. Easy to publish."
            }}
          </h2>
        </div>

        <div class="relative mt-16 grid gap-8 md:grid-cols-3">
          <div
            class="absolute left-[16%] right-[16%] top-10 hidden border-t border-dashed border-violet-200 dark:border-violet-500/20 md:block"
          ></div>

          <div class="relative text-center">
            <div
              class="mx-auto flex h-20 w-20 items-center justify-center rounded-[24px] border-8 border-violet-50 bg-violet-500 text-xl font-black text-white shadow-lg shadow-violet-500/20 dark:border-violet-500/10"
            >
              01
            </div>

            <h3 class="mt-7 text-lg font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa"
                  ? "حساب خودت را بساز"
                  : "Create your account"
              }}
            </h3>

            <p
              class="mx-auto mt-3 max-w-xs text-sm leading-6 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "ثبت‌نام کن و اطلاعات اولیه پورتفولیوت را وارد کن."
                  : "Sign up and add the basic information for your portfolio."
              }}
            </p>
          </div>

          <div class="relative text-center">
            <div
              class="mx-auto flex h-20 w-20 items-center justify-center rounded-[24px] border-8 border-violet-50 bg-violet-500 text-xl font-black text-white shadow-lg shadow-violet-500/20 dark:border-violet-500/10"
            >
              02
            </div>

            <h3 class="mt-7 text-lg font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa"
                  ? "پورتفولیوت را بساز"
                  : "Customize your portfolio"
              }}
            </h3>

            <p
              class="mx-auto mt-3 max-w-xs text-sm leading-6 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "قالب، مهارت‌ها، تجربه‌ها و پروژه‌هایت را اضافه کن."
                  : "Choose a template and add your skills, experience and projects."
              }}
            </p>
          </div>

          <div class="relative text-center">
            <div
              class="mx-auto flex h-20 w-20 items-center justify-center rounded-[24px] border-8 border-violet-50 bg-violet-500 text-xl font-black text-white shadow-lg shadow-violet-500/20 dark:border-violet-500/10"
            >
              03
            </div>

            <h3 class="mt-7 text-lg font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa" ? "منتشرش کن" : "Publish and share"
              }}
            </h3>

            <p
              class="mx-auto mt-3 max-w-xs text-sm leading-6 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "پورتفولیوی آماده‌ات را منتشر کن و لینک آن را به اشتراک بگذار."
                  : "Publish your portfolio and share your public link."
              }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- FEATURES -->
    <!-- ========================================================= -->

    <section id="features" class="px-5 py-24 sm:px-8 lg:py-32">
      <div class="mx-auto max-w-6xl">
        <div class="max-w-2xl">
          <span class="text-sm font-bold text-violet-500">
            {{ i18nStore.t("home.featuresLabel") }}
          </span>

          <h2
            class="mt-3 text-3xl font-black tracking-tight text-slate-900 dark:text-white sm:text-5xl"
          >
            {{ i18nStore.t("home.featuresTitle") }}
          </h2>
        </div>

        <div class="mt-12 grid gap-5 md:grid-cols-2 lg:grid-cols-3">
          <!-- Feature -->
          <div
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-white/10 dark:bg-white/[0.04]"
          >
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/10"
            >
              ✦
            </div>

            <h3 class="mt-6 font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa" ? "ویرایشگر کامل" : "Full editor"
              }}
            </h3>

            <p
              class="mt-3 text-sm leading-7 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "تمام اطلاعات اصلی پورتفولیوت را از یک محیط مدیریت کن."
                  : "Manage the important parts of your portfolio from one place."
              }}
            </p>
          </div>

          <div
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-white/10 dark:bg-white/[0.04]"
          >
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/10"
            >
              ◇
            </div>

            <h3 class="mt-6 font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa"
                  ? "قالب‌های متفاوت"
                  : "Multiple styles"
              }}
            </h3>

            <p
              class="mt-3 text-sm leading-7 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "از طراحی مینیمال تا خلاقانه، سبک مناسب خودت را انتخاب کن."
                  : "From minimal to creative, choose a visual style that fits you."
              }}
            </p>
          </div>

          <div
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-white/10 dark:bg-white/[0.04]"
          >
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/10"
            >
              ↗
            </div>

            <h3 class="mt-6 font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa"
                  ? "انتشار عمومی"
                  : "Public portfolio"
              }}
            </h3>

            <p
              class="mt-3 text-sm leading-7 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "پورتفولیوی خودت را منتشر کن و یک صفحه عمومی داشته باش."
                  : "Publish your work and give people a dedicated public page."
              }}
            </p>
          </div>

          <div
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-white/10 dark:bg-white/[0.04]"
          >
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/10"
            >
              ◎
            </div>

            <h3 class="mt-6 font-black text-slate-900 dark:text-white">
              {{ i18nStore.language === "fa" ? "پروژه‌ها" : "Projects" }}
            </h3>

            <p
              class="mt-3 text-sm leading-7 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "پروژه‌هایی که برایت مهم هستند را با جزئیات نمایش بده."
                  : "Showcase the projects that best represent your work."
              }}
            </p>
          </div>

          <div
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-white/10 dark:bg-white/[0.04]"
          >
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/10"
            >
              ◌
            </div>

            <h3 class="mt-6 font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa"
                  ? "مهارت و تجربه"
                  : "Skills & experience"
              }}
            </h3>

            <p
              class="mt-3 text-sm leading-7 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "مهارت‌ها، تحصیلات و سابقه کاری را مرتب و حرفه‌ای ارائه کن."
                  : "Present your skills, education and experience in a structured way."
              }}
            </p>
          </div>

          <div
            class="rounded-[28px] border border-violet-100 bg-white p-7 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-white/10 dark:bg-white/[0.04]"
          >
            <div
              class="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-100 text-violet-500 dark:bg-violet-500/10"
            >
              ✓
            </div>

            <h3 class="mt-6 font-black text-slate-900 dark:text-white">
              {{
                i18nStore.language === "fa"
                  ? "مدیریت ساده"
                  : "Simple management"
              }}
            </h3>

            <p
              class="mt-3 text-sm leading-7 text-slate-500 dark:text-slate-400"
            >
              {{
                i18nStore.language === "fa"
                  ? "داشبورد ساده‌ای برای مدیریت پورتفولیوی خودت داشته باش."
                  : "Keep everything organized through a focused dashboard."
              }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- SHOWCASE -->
    <!-- ========================================================= -->

    <section class="px-5 pb-24 sm:px-8 lg:pb-32">
      <div
        class="relative mx-auto max-w-6xl overflow-hidden rounded-[36px] bg-[#151021] px-6 py-12 shadow-2xl shadow-violet-500/10 sm:px-10 lg:px-16 lg:py-16"
      >
        <div
          class="absolute -right-40 -top-40 h-96 w-96 rounded-full bg-violet-500/20 blur-3xl"
        ></div>

        <div
          class="absolute -bottom-40 -left-40 h-96 w-96 rounded-full bg-fuchsia-500/10 blur-3xl"
        ></div>

        <div
          class="relative grid items-center gap-12 lg:grid-cols-[0.8fr_1.2fr]"
        >
          <div>
            <span class="text-sm font-bold text-violet-300">
              {{
                i18nStore.language === "fa"
                  ? "پورتفولیوی تو، برند تو"
                  : "Your portfolio. Your identity."
              }}
            </span>

            <h2
              class="mt-4 text-3xl font-black leading-tight text-white sm:text-5xl"
            >
              {{
                i18nStore.language === "fa"
                  ? "فقط یک رزومه آنلاین نباش."
                  : "Don't just make another online resume."
              }}
            </h2>

            <p class="mt-5 text-sm leading-7 text-slate-400 sm:text-base">
              {{
                i18nStore.language === "fa"
                  ? "پورتفولیویی بساز که پروژه‌ها، مهارت‌ها و شخصیت حرفه‌ای تو را در یک تجربه منسجم نشان دهد."
                  : "Create a portfolio that brings your projects, skills and professional identity together in one focused experience."
              }}
            </p>

            <router-link
              to="/register"
              class="mt-8 inline-flex rounded-full bg-white px-6 py-3 text-sm font-bold text-violet-600 transition hover:-translate-y-0.5"
            >
              {{ i18nStore.t("common.createPortfolio") }}
            </router-link>
          </div>

          <!-- Dashboard visual -->
          <div
            class="relative overflow-hidden rounded-[28px] border border-white/10 bg-white/[0.04] p-3 shadow-2xl"
          >
            <div class="rounded-[22px] border border-white/10 bg-[#0d0a15] p-5">
              <div class="flex items-center justify-between">
                <div>
                  <div class="h-2.5 w-24 rounded-full bg-white/80"></div>
                  <div class="mt-2 h-2 w-16 rounded-full bg-white/20"></div>
                </div>

                <div
                  class="rounded-full bg-emerald-400/10 px-3 py-1 text-[9px] font-bold text-emerald-300"
                >
                  LIVE
                </div>
              </div>

              <div class="mt-6 grid gap-3 sm:grid-cols-3">
                <div
                  class="rounded-2xl border border-white/5 bg-white/[0.03] p-4"
                >
                  <div class="h-2 w-12 rounded-full bg-violet-400/70"></div>
                  <div class="mt-4 h-5 w-16 rounded bg-white/80"></div>
                  <div class="mt-2 h-2 w-20 rounded bg-white/10"></div>
                </div>

                <div
                  class="rounded-2xl border border-white/5 bg-white/[0.03] p-4"
                >
                  <div class="h-2 w-12 rounded-full bg-emerald-400/70"></div>
                  <div class="mt-4 h-5 w-16 rounded bg-white/80"></div>
                  <div class="mt-2 h-2 w-20 rounded bg-white/10"></div>
                </div>

                <div
                  class="rounded-2xl border border-white/5 bg-white/[0.03] p-4"
                >
                  <div class="h-2 w-12 rounded-full bg-fuchsia-400/70"></div>
                  <div class="mt-4 h-5 w-16 rounded bg-white/80"></div>
                  <div class="mt-2 h-2 w-20 rounded bg-white/10"></div>
                </div>
              </div>

              <div
                class="mt-3 rounded-2xl border border-white/5 bg-white/[0.03] p-5"
              >
                <div class="flex items-center justify-between">
                  <div class="h-3 w-32 rounded-full bg-white/70"></div>
                  <div class="h-7 w-20 rounded-full bg-violet-500/20"></div>
                </div>

                <div class="mt-5 grid gap-2 sm:grid-cols-2">
                  <div class="h-20 rounded-xl bg-white/5"></div>
                  <div class="h-20 rounded-xl bg-white/5"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- ABOUT -->
    <!-- ========================================================= -->

    <section
      id="about"
      class="border-t border-violet-100 bg-white px-5 py-24 dark:border-white/10 dark:bg-white/[0.025] sm:px-8 lg:py-32"
    >
      <div class="mx-auto max-w-4xl text-center">
        <span class="text-sm font-bold text-violet-500">
          {{ i18nStore.t("home.aboutLabel") }}
        </span>

        <h2
          class="mt-4 text-3xl font-black tracking-tight text-slate-900 dark:text-white sm:text-5xl"
        >
          {{ i18nStore.t("home.aboutTitle") }}
        </h2>

        <p
          class="mx-auto mt-6 max-w-2xl text-sm leading-8 text-slate-500 dark:text-slate-400 sm:text-base"
        >
          {{
            i18nStore.language === "fa"
              ? "Portify برای این ساخته شده که ساخت یک پورتفولیوی حرفه‌ای را از یک کار پیچیده به یک تجربه ساده و قابل مدیریت تبدیل کند."
              : "Portify is built to turn the process of creating a professional portfolio from a complicated task into a simple, focused experience."
          }}
        </p>

        <div class="mt-10 flex flex-wrap justify-center gap-3">
          <span
            class="rounded-full border border-violet-100 bg-violet-50 px-4 py-2 text-xs font-bold text-violet-600 dark:border-white/10 dark:bg-violet-500/10 dark:text-violet-300"
          >
            {{
              i18nStore.language === "fa" ? "پروفایل شخصی" : "Personal profile"
            }}
          </span>

          <span
            class="rounded-full border border-violet-100 bg-violet-50 px-4 py-2 text-xs font-bold text-violet-600 dark:border-white/10 dark:bg-violet-500/10 dark:text-violet-300"
          >
            {{ i18nStore.language === "fa" ? "پروژه‌ها" : "Projects" }}
          </span>

          <span
            class="rounded-full border border-violet-100 bg-violet-50 px-4 py-2 text-xs font-bold text-violet-600 dark:border-white/10 dark:bg-violet-500/10 dark:text-violet-300"
          >
            {{ i18nStore.language === "fa" ? "مهارت‌ها" : "Skills" }}
          </span>

          <span
            class="rounded-full border border-violet-100 bg-violet-50 px-4 py-2 text-xs font-bold text-violet-600 dark:border-white/10 dark:bg-violet-500/10 dark:text-violet-300"
          >
            {{ i18nStore.language === "fa" ? "تجربه" : "Experience" }}
          </span>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- FINAL CTA -->
    <!-- ========================================================= -->

    <section id="contact" class="px-5 py-20 sm:px-8 lg:py-28">
      <div
        class="relative mx-auto max-w-5xl overflow-hidden rounded-[36px] bg-violet-600 px-6 py-16 text-center shadow-2xl shadow-violet-500/20 sm:px-10"
      >
        <div
          class="pointer-events-none absolute -left-20 -top-20 h-64 w-64 rounded-full bg-white/10 blur-3xl"
        ></div>

        <div
          class="pointer-events-none absolute -bottom-24 -right-20 h-72 w-72 rounded-full bg-fuchsia-300/20 blur-3xl"
        ></div>

        <div class="relative">
          <div
            class="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-white text-xl font-black text-violet-600 shadow-xl"
          >
            P
          </div>

          <h2
            class="mx-auto mt-7 max-w-2xl text-3xl font-black tracking-tight text-white sm:text-5xl"
          >
            {{ i18nStore.t("home.contactTitle") }}
          </h2>

          <p
            class="mx-auto mt-5 max-w-xl text-sm leading-7 text-violet-100/75 sm:text-base"
          >
            {{
              i18nStore.language === "fa"
                ? "چند دقیقه وقت بگذار و اولین نسخه پورتفولیوی حرفه‌ای خودت را بساز."
                : "Take a few minutes and build the first version of your professional portfolio."
            }}
          </p>

          <router-link
            to="/register"
            class="mt-8 inline-flex rounded-full bg-white px-7 py-3.5 text-sm font-bold text-violet-600 shadow-xl transition duration-200 hover:-translate-y-1 hover:shadow-2xl"
          >
            {{ i18nStore.t("common.getStarted") }}
          </router-link>
        </div>
      </div>
    </section>

    <!-- ========================================================= -->
    <!-- FOOTER -->
    <!-- ========================================================= -->

    <footer
      class="border-t border-violet-100 bg-white px-5 py-10 dark:border-white/10 dark:bg-[#100b1c] sm:px-8"
    >
      <div
        class="mx-auto flex max-w-6xl flex-col gap-8 sm:flex-row sm:items-center sm:justify-between"
      >
        <div>
          <div class="flex items-center gap-2.5">
            <div
              class="flex h-9 w-9 items-center justify-center rounded-xl bg-violet-500"
            >
              <span class="font-black text-white">P</span>
            </div>

            <span class="font-black text-slate-900 dark:text-white">
              Portify
            </span>
          </div>

          <p class="mt-3 text-xs text-slate-400">
            {{
              i18nStore.language === "fa"
                ? "پورتفولیوی حرفه‌ای، ساده‌تر."
                : "Professional portfolios, made simpler."
            }}
          </p>
        </div>

        <div
          class="flex flex-wrap gap-x-6 gap-y-3 text-xs font-medium text-slate-500 dark:text-slate-400"
        >
          <a href="#home" class="transition hover:text-violet-500">
            {{ i18nStore.t("common.home") }}
          </a>

          <a href="#templates" class="transition hover:text-violet-500">
            {{ i18nStore.t("common.templates") }}
          </a>

          <a href="#features" class="transition hover:text-violet-500">
            {{ i18nStore.t("common.features") }}
          </a>

          <a href="#about" class="transition hover:text-violet-500">
            {{ i18nStore.t("common.about") }}
          </a>

          <router-link to="/login" class="transition hover:text-violet-500">
            {{ i18nStore.t("common.login") }}
          </router-link>
        </div>
      </div>

      <div
        class="mx-auto mt-8 max-w-6xl border-t border-violet-100 pt-6 text-xs text-slate-400 dark:border-white/10"
      >
        © {{ new Date().getFullYear() }} Portify. All rights reserved.
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useI18nStore } from "../stores/i18n";

const i18nStore = useI18nStore();
</script>
