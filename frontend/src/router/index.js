import {
  createRouter,
  createWebHistory,
} from 'vue-router'

import HomeView from '../views/HomeView.vue'
import CreatePortfolioView from '../views/CreatePortfolioView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },

  {
    path: '/login',
    name: 'login',
    component: () =>
      import('../views/LoginView.vue'),

    meta: {
      guestOnly: true,
    },
  },

  {
    path: '/register',
    name: 'register',
    component: () =>
      import('../views/RegisterView.vue'),

    meta: {
      guestOnly: true,
    },
  },

  {
    path: '/dashboard',
    name: 'dashboard',
    component: () =>
      import('../views/DashboardView.vue'),

    meta: {
      requiresAuth: true,
    },
  },

  {
    path: '/profile',
    name: 'profile',
    component: () =>
      import('../views/ProfileView.vue'),

    meta: {
      requiresAuth: true,
    },
  },
  
  {
  path: '/portfolio/create',
  name: 'create-portfolio',
  component: CreatePortfolioView,
  meta: {
    requiresAuth: true,
  },
},
  
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const accessToken =
    localStorage.getItem('access_token')

  const refreshToken =
    localStorage.getItem('refresh_token')

  const isAuthenticated =
    !!accessToken || !!refreshToken

  // Protected route
  if (
    to.meta.requiresAuth &&
    !isAuthenticated
  ) {
    return {
      name: 'login',
    }
  }

  // Guest-only route
  if (
    to.meta.guestOnly &&
    isAuthenticated
  ) {
    return {
      name: 'dashboard',
    }
  }

  return true
})

export default router