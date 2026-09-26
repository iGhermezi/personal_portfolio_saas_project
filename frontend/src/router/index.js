import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import CreatePortfolioView from "../views/CreatePortfolioView.vue";
import PortfolioPreviewView from "../views/PortfolioPreviewView.vue";
import PublicPortfolioView from "../views/PublicPortfolioView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },

  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
    meta: {
      guestOnly: true,
    },
  },

  {
    path: "/register",
    name: "register",
    component: () => import("../views/RegisterView.vue"),
    meta: {
      guestOnly: true,
    },
  },

  {
    path: "/dashboard",
    name: "dashboard",
    component: () => import("../views/DashboardView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/dashboard/portfolio",
    name: "dashboard-portfolio",
    component: () => import("../views/EditPortfolioView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/profile",
    name: "profile",
    component: () => import("../views/ProfileView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/portfolio/create",
    name: "create-portfolio",
    component: CreatePortfolioView,
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/portfolio/:id/setup",
    name: "portfolio-setup",
    component: () => import("../views/PortfolioSetupView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/portfolio/:id/edit",
    name: "edit-portfolio",
    component: () => import("../views/EditPortfolioView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/portfolio/:id/preview",
    name: "portfolio-preview",
    component: PortfolioPreviewView,
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/templates",
    name: "templates",
    component: () => import("../views/TemplatesView.vue"),
    meta: {
      requiresAuth: true,
    },
  },

  {
    path: "/portfolio/:slug",
    name: "public-portfolio",
    component: PublicPortfolioView,
  },

  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("../views/HomeView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  const accessToken = localStorage.getItem("access_token");
  const refreshToken = localStorage.getItem("refresh_token");

  const isAuthenticated = !!accessToken || !!refreshToken;

  if (to.meta.requiresAuth && !isAuthenticated) {
    return {
      name: "login",
    };
  }

  if (to.meta.guestOnly && isAuthenticated) {
    return {
      name: "dashboard",
    };
  }

  return true;
});

export default router;