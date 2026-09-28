import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import CreatePortfolioView from "../views/CreatePortfolioView.vue";
import PortfolioPreviewView from "../views/PortfolioPreviewView.vue";
import PublicPortfolioView from "../views/PublicPortfolioView.vue";

const routes = [
  { path: "/", name: "home", component: HomeView },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
    meta: { guestOnly: true },
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/RegisterView.vue"),
    meta: { guestOnly: true },
  },
  {
    path: "/forgot-password",
    name: "forgot-password",
    component: () => import("../views/ForgotPasswordView.vue"),
    meta: { guestOnly: true },
  },
  {
    path: "/reset-password/:uid/:token",
    name: "reset-password",
    component: () => import("../views/ResetPasswordView.vue"),
  },
  {
    path: "/verify-email/:uid/:token",
    name: "verify-email",
    component: () => import("../views/VerifyEmailView.vue"),
  },

  {
    path: "/dashboard",
    name: "dashboard",
    component: () => import("../views/DashboardView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/dashboard/portfolio",
    name: "dashboard-portfolio",
    component: () => import("../views/EditPortfolioView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("../views/ProfileView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/account/security",
    name: "account-security",
    component: () => import("../views/AccountSecurityView.vue"),
    meta: { requiresAuth: true },
  },

  {
    path: "/portfolio/create",
    name: "create-portfolio",
    component: CreatePortfolioView,
    meta: { requiresAuth: true },
  },
  {
    path: "/portfolio/:id/setup",
    name: "portfolio-setup",
    component: () => import("../views/PortfolioSetupView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/portfolio/:id/edit",
    name: "edit-portfolio",
    component: () => import("../views/EditPortfolioView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/portfolio/:id/preview",
    name: "portfolio-preview",
    component: PortfolioPreviewView,
    meta: { requiresAuth: true },
  },

  {
    path: "/templates",
    name: "templates",
    component: () => import("../views/TemplatesView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/upgrade",
    name: "upgrade",
    component: () => import("../views/UpgradeView.vue"),
    meta: { requiresAuth: true },
  },

  {
    path: "/verify-email/:uid/:token",
    name: "verify-email",
    component: () => import("../views/VerifyEmailView.vue"),
  },

  {
    path: "/portfolio/:slug",
    name: "public-portfolio",
    component: PublicPortfolioView,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("../views/NotFoundView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  const isAuthenticated =
    !!localStorage.getItem("access_token") ||
    !!localStorage.getItem("refresh_token");

  if (to.meta.requiresAuth && !isAuthenticated) return { name: "login" };
  if (to.meta.guestOnly && isAuthenticated) return { name: "dashboard" };

  return true;
});

export default router;
