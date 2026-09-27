import { defineStore } from 'pinia'

const STORAGE_KEY = 'portify_theme'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: false,
  }),

  actions: {
    initializeTheme() {
      const saved = localStorage.getItem(STORAGE_KEY)

      if (saved === 'dark' || saved === 'light') {
        this.isDark = saved === 'dark'
      } else {
        this.isDark = false
      }

      this.applyTheme()
    },

    applyTheme() {
      document.documentElement.classList.toggle('dark', this.isDark)
      document.documentElement.style.colorScheme = this.isDark ? 'dark' : 'light'
    },

    toggleTheme() {
      this.isDark = !this.isDark
      localStorage.setItem(STORAGE_KEY, this.isDark ? 'dark' : 'light')
      this.applyTheme()
    },
  },
})
