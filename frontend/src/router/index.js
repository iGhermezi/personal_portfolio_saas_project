import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    // بارگذاری تنبل برای جلوگیری از ارور قبل از ساخت کامپوننت
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('../views/DashboardView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/register',
    name: 'register',
    // بارگذاری تنبل برای جلوگیری از ارور قبل از ساخت کامپوننت
    component: () => import('../views/RegisterView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation Guard برای امنیت مسیرها
router.beforeEach((to, from, next) => {
  // بررسی وجود توکن لاگین در LocalStorage بدون وابستگی مستقیم در این مرحله
  const token = localStorage.getItem('access_token')

  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router