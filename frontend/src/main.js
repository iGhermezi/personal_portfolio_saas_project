import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import { useAuthStore } from "./stores/auth";
import { useThemeStore } from "./stores/theme";
import { useI18nStore } from "./stores/i18n";

import "./style.css";

const app = createApp(App);

const pinia = createPinia();

app.use(pinia);
app.use(router);

const authStore = useAuthStore(pinia);
const themeStore = useThemeStore(pinia);
const i18nStore = useI18nStore(pinia);

themeStore.initializeTheme();
i18nStore.initializeLanguage();

await authStore.initializeAuth();

app.mount("#app");