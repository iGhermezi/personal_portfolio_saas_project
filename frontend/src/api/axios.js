import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    'Content-Type': 'application/json',
  },
})

let isRefreshing = false
let failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach((promise) => {
    if (error) {
      promise.reject(error)
    } else {
      promise.resolve(token)
    }
  })

  failedQueue = []
}

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  },
  (error) => Promise.reject(error)
)

api.interceptors.response.use(
  (response) => response,

  async (error) => {
    const originalRequest = error.config

    if (
      error.response?.status !== 401 ||
      originalRequest?._retry
    ) {
      return Promise.reject(error)
    }

    if (originalRequest?.url?.includes('accounts/token/refresh/')) {
      return Promise.reject(error)
    }

    const refreshToken = localStorage.getItem('refresh_token')

    if (!refreshToken) {
      clearAuthStorage()
      return Promise.reject(error)
    }

    if (isRefreshing) {
      return new Promise((resolve, reject) => {
        failedQueue.push({
          resolve,
          reject,
        })
      })
        .then((token) => {
          originalRequest.headers.Authorization = `Bearer ${token}`
          return api(originalRequest)
        })
        .catch((refreshError) => {
          return Promise.reject(refreshError)
        })
    }

    originalRequest._retry = true
    isRefreshing = true

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/accounts/token/refresh/',
        {
          refresh: refreshToken,
        }
      )

      const newAccessToken = response.data.access

      localStorage.setItem(
        'access_token',
        newAccessToken
      )

      processQueue(null, newAccessToken)

      originalRequest.headers.Authorization =
        `Bearer ${newAccessToken}`

      return api(originalRequest)

    } catch (refreshError) {

      processQueue(refreshError, null)

      clearAuthStorage()

      return Promise.reject(refreshError)

    } finally {
      isRefreshing = false
    }
  }
)

function clearAuthStorage() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  localStorage.removeItem('user')
}

export default api