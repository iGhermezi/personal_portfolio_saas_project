import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import CreatePortfolioView from "../views/portfolio/CreatePortfolioView.vue";
import PortfolioPreviewView from "../views/portfolio/PortfolioPreviewView.vue";
import PublicPortfolioView from "../views/portfolio/PublicPortfolioView.vue";

const routes = [
  { path: "/", name: "home", component: HomeView },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/auth/LoginView.vue"),
    meta: { guestOnly: true },
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/auth/RegisterView.vue"),
    meta: { guestOnly: true },
  },
  {
    path: "/forgot-password",
    name: "forgot-password",
    component: () => import("../views/auth/ForgotPasswordView.vue"),
    meta: { guestOnly: true },
  },
  {
    path: "/reset-password/:uid/:token",
    name: "reset-password",
    component: () => import("../views/auth/ResetPasswordView.vue"),
  },
  {
    path: "/verify-email/:uid/:token",
    name: "verify-email",
    component: () => import("../views/auth/VerifyEmailView.vue"),
  },

  {
    path: "/dashboard",
    name: "dashboard",
    component: () => import("../views/dashboard/DashboardView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/dashboard/portfolio",
    name: "dashboard-portfolio",
    component: () => import("../views/portfolio/EditPortfolioView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("../views/account/ProfileView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/account/security",
    name: "account-security",
    component: () => import("../views/account/AccountSecurityView.vue"),
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
    component: () => import("../views/portfolio/PortfolioSetupView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/portfolio/:id/edit",
    name: "edit-portfolio",
    component: () => import("../views/portfolio/EditPortfolioView.vue"),
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
    component: () => import("../views/dashboard/TemplatesView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/upgrade",
    name: "upgrade",
    component: () => import("../views/dashboard/UpgradeView.vue"),
    meta: { requiresAuth: true },
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
