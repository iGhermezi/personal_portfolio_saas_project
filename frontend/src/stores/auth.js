import { defineStore } from 'pinia';
import api from '../api/axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    accessToken: localStorage.getItem('access_token') || '',
    refreshToken: localStorage.getItem('refresh_token') || '',
  }),
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
  actions: {
    async login(email, password) {
      try {
        const response = await api.post('accounts/login/', { email, password });
        this.accessToken = response.data.access;
        this.refreshToken = response.data.refresh;

        localStorage.setItem('access_token', this.accessToken);
        localStorage.setItem('refresh_token', this.refreshToken);
        
        await this.fetchUser();
        return true;
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },
    async fetchUser() {
      try {
        const response = await api.get('accounts/me/');
        this.user = response.data;
      } catch (error) {
        this.logout();
      }
    },
    logout() {
      this.user = null;
      this.accessToken = '';
      this.refreshToken = '';
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    }
  }
});