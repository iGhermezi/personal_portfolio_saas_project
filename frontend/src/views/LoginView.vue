<template>
  <div class="min-h-screen bg-slate-950 text-white flex items-center justify-center p-4 font-sans dir-rtl" dir="rtl">
    <div class="w-full max-w-md bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-2xl">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold mb-2">ورود به حساب کاربری</h2>
        <p class="text-slate-400 text-sm">ایمیل و رمز عبور خود را وارد کنید</p>
      </div>

      <form @submit.prevent class="space-y-4">
        <div>
          <label class="block text-xs font-medium text-slate-300 mb-1">ایمیل</label>
          <input 
            type="email" 
            placeholder="example@gmail.com" 
            class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500 transition"
          />
        </div>

        <div>
          <label class="block text-xs font-medium text-slate-300 mb-1">رمز عبور</label>
          <input 
            type="password" 
            placeholder="••••••••" 
            class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500 transition"
          />
        </div>

        <button 
          type="submit" 
          class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-2.5 rounded-xl transition shadow-lg shadow-indigo-600/30 mt-2"
        >
          ورود
        </button>
      </form>

      <div class="mt-6 text-center text-xs text-slate-400">
        حساب کاربری ندارید؟ 
        <router-link to="/" class="text-indigo-400 font-semibold hover:underline">بازگشت به صفحه اصلی</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>