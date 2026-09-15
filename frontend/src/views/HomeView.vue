<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 font-sans p-4 md:p-8 flex flex-col items-center justify-center dir-rtl" dir="rtl">
    
    <!-- Main UI Card Container (طرح اصلی بر اساس عکس) -->
    <main class="w-full max-w-6xl bg-gradient-to-br from-indigo-700 via-purple-700 to-indigo-900 rounded-3xl p-6 md:p-12 shadow-2xl relative overflow-hidden border border-indigo-500/30">
      
      <!-- Navbar inside Card -->
      <nav class="flex items-center justify-between pb-8 mb-4 border-b border-white/10 relative z-20">
        <!-- Logo -->
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-white text-indigo-700 rounded-lg flex items-center justify-center font-black text-lg shadow-md">
            P
          </div>
          <span class="font-extrabold text-xl text-white tracking-tight">Portfolio SaaS</span>
        </div>

        <!-- Links -->
        <div class="hidden md:flex items-center gap-8 text-sm font-medium text-purple-100">
          <a href="#templates" class="hover:text-white transition-colors">قالب‌ها</a>
          <a href="#features" class="hover:text-white transition-colors">امکانات</a>
          <a href="#pricing" class="hover:text-white transition-colors">تعرفه‌ها</a>
          <a href="#about" class="hover:text-white transition-colors">درباره ما</a>
        </div>

        <!-- Auth Button -->
        <router-link to="/login" class="bg-white hover:bg-slate-100 text-indigo-800 font-bold px-5 py-2.5 rounded-full text-sm shadow-md transition-all hover:scale-105">
          ورود / ثبت‌نام
        </router-link>
      </nav>

      <!-- Decorative Elements (ستاره‌ها و افکت‌های پس‌زمینه) -->
      <div class="absolute top-28 right-12 text-yellow-300 text-2xl animate-pulse">✦</div>
      <div class="absolute bottom-20 left-16 text-yellow-300 text-3xl animate-bounce">✦</div>
      <div class="absolute -bottom-20 -right-20 w-80 h-80 bg-pink-500/20 rounded-full blur-3xl pointer-events-none"></div>

      <!-- Hero Content -->
      <div class="text-center max-w-2xl mx-auto mt-4 relative z-10">
        <h1 class="text-3xl md:text-5xl font-black text-white leading-tight mb-4">
          قالب مناسب را برای <br />
          پورتفولیو و رزومه خود انتخاب کنید
        </h1>
        <p class="text-purple-100 text-sm md:text-base leading-relaxed mb-8 opacity-90">
          با بیش از ۱۰ تمپلیت حرفه‌ای، پورتفولیوی اختصاصی خود را بدون نیاز به کدنویسی در چند دقیقه بسازید و لینک اختصاصی دریافت کنید.
        </p>
      </div>

      <!-- Hero Visual Section with Floating Cards -->
      <div class="relative max-w-4xl mx-auto mt-6 flex justify-center items-end min-h-[320px]">
        
        <!-- Left Floating Card (امتیاز کاربران / ویژگی) -->
        <div class="absolute top-8 right-4 md:right-12 z-20 bg-white/95 backdrop-blur-md text-slate-900 p-4 rounded-2xl shadow-2xl border border-white/50 max-w-[200px] transform -rotate-3 hover:rotate-0 transition-transform">
          <div class="flex items-center gap-1 text-yellow-400 mb-1 text-sm">
            ★ ★ ★ ★ ★ <span class="text-slate-700 font-bold text-xs mr-1">4.9</span>
          </div>
          <p class="text-xs text-slate-600 font-semibold leading-snug">
            مورد اعتماد بیش از ۱,۰۰۰ توسعه‌دهنده و طراح
          </p>
        </div>

        <!-- Center Image (تصویر شاخص) -->
        <div class="relative z-10 w-64 md:w-80 h-72 md:h-80 overflow-hidden rounded-t-full border-4 border-white/20 shadow-2xl bg-gradient-to-b from-purple-400 to-indigo-600 flex items-center justify-center">
          <img 
            src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=800&auto=format&fit=crop" 
            alt="User Portfolio Preview" 
            class="w-full h-full object-cover object-top"
          />
        </div>

        <!-- Right Floating Card (آمار قالب‌ها / نمونه‌ها) -->
        <div class="absolute top-16 left-4 md:left-12 z-20 bg-white/95 backdrop-blur-md text-slate-900 p-4 rounded-2xl shadow-2xl border border-white/50 max-w-[210px] transform rotate-3 hover:rotate-0 transition-transform">
          <div class="flex items-center gap-2 mb-2">
            <!-- Avatar Stack -->
            <div class="flex -space-x-2 space-x-reverse">
              <span class="w-7 h-7 rounded-full bg-indigo-500 text-white text-xs font-bold flex items-center justify-center border-2 border-white">UI</span>
              <span class="w-7 h-7 rounded-full bg-purple-500 text-white text-xs font-bold flex items-center justify-center border-2 border-white">Py</span>
              <span class="w-7 h-7 rounded-full bg-pink-500 text-white text-xs font-bold flex items-center justify-center border-2 border-white">JS</span>
            </div>
            <span class="font-black text-indigo-700 text-base">+۱۰ قالب</span>
          </div>
          <p class="text-xs text-slate-600 font-semibold leading-snug">
            تمپلیت‌های اماده برای برنامه نویسان، طراحان و فریلنسرها
          </p>
        </div>

      </div>

    </main>

  </div>
</template>

<script setup>
</script>