import { defineStore } from 'pinia'
import api from '../api/axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken:
      localStorage.getItem('access_token') || null,

    refreshToken:
      localStorage.getItem('refresh_token') || null,

    user: JSON.parse(
      localStorage.getItem('user') || 'null'
    ),

    initialized: false,
  }),

  getters: {
    isAuthenticated: (state) => {
      return !!state.accessToken
    },
  },

  actions: {
    async login(email, password) {
      const response = await api.post(
        'accounts/login/',
        {
          email,
          password,
        }
      )

      const data = response.data

      this.setTokens(
        data.access,
        data.refresh
      )

      if (data.user) {
        this.setUser(data.user)
      }

      return data
    },

    async register(formData) {
      const response = await api.post(
        'accounts/register/',
        formData
      )

      return response.data
    },

    async getProfile() {
      const response = await api.get(
        'accounts/me/'
      )

      this.setUser(response.data)

      return response.data
    },
    

    async refreshAccessToken() {
      const refreshToken =
        this.refreshToken ||
        localStorage.getItem('refresh_token')

      if (!refreshToken) {
        this.logout()
        return null
      }

      try {
        const response = await api.post(
          'accounts/token/refresh/',
          {
            refresh: refreshToken,
          }
        )

        const newAccessToken =
          response.data.access

        this.accessToken = newAccessToken

        localStorage.setItem(
          'access_token',
          newAccessToken
        )

        return newAccessToken

      } catch (error) {
        this.logout()
        throw error
      }
    },

    async initializeAuth() {
      if (this.initialized) {
        return
      }

      const accessToken =
        localStorage.getItem('access_token')

      const refreshToken =
        localStorage.getItem('refresh_token')

      this.accessToken = accessToken
      this.refreshToken = refreshToken

      if (!accessToken && !refreshToken) {
        this.initialized = true
        return
      }

      try {
        await this.getProfile()
      } catch (error) {
        if (refreshToken) {
          try {
            await this.refreshAccessToken()
            await this.getProfile()
          } catch (refreshError) {
            this.logout()
          }
        } else {
          this.logout()
        }
      } finally {
        this.initialized = true
      }
    },

    updateUser(userData) {
      this.setUser(userData)
    },

    setTokens(accessToken, refreshToken) {
      this.accessToken = accessToken
      this.refreshToken = refreshToken

      localStorage.setItem(
        'access_token',
        accessToken
      )

      localStorage.setItem(
        'refresh_token',
        refreshToken
      )
    },

    setUser(userData) {
      this.user = userData

      localStorage.setItem(
        'user',
        JSON.stringify(userData)
      )
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null

      localStorage.removeItem(
        'access_token'
      )

      localStorage.removeItem(
        'refresh_token'
      )

      localStorage.removeItem(
        'user'
      )
    },
  },
})