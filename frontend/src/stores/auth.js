import { defineStore } from 'pinia'
import api from '../api/axios'


export const useAuthStore = defineStore('auth', {

  state: () => ({

    accessToken:
      localStorage.getItem('access_token') || null,

    refreshToken:
      localStorage.getItem('refresh_token') || null,

    user:
      JSON.parse(
        localStorage.getItem('user') || 'null'
      ),

  }),


  getters: {

    isAuthenticated: (state) => {
      return !!state.accessToken
    }

  },


  actions: {

    async login(email, password) {

      const response = await api.post(
        'accounts/login/',
        {
          email,
          password
        }
      )


      const data = response.data


      this.accessToken = data.access

      this.refreshToken = data.refresh

      this.user = data.user


      localStorage.setItem(
        'access_token',
        data.access
      )

      localStorage.setItem(
        'refresh_token',
        data.refresh
      )

      localStorage.setItem(
        'user',
        JSON.stringify(data.user)
      )


      return data

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

    }

  }

})