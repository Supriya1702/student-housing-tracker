// src/apiClient.ts
import axios from 'axios'

const client = axios.create({
  baseURL: import.meta.env.VITE_API_URL,   // from your .env
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,                   // only if you use cookie auth
})

// inject the bearer token on every request
client.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken')
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default client
