import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const isLoggedIn = ref(false)

  const login = async (username, password) => {
    const res = await authApi.login(username, password)
    if (res.code === 200) {
      user.value = res.data
      isLoggedIn.value = true
      return true
    }
    throw new Error(res.msg)
  }

  const logout = async () => {
    await authApi.logout()
    user.value = null
    isLoggedIn.value = false
  }

  const checkAuth = async () => {
    try {
      const res = await authApi.check()
      if (res.code === 200 && res.data.logged_in) {
        user.value = res.data
        isLoggedIn.value = true
      } else {
        user.value = null
        isLoggedIn.value = false
      }
    } catch {
      user.value = null
      isLoggedIn.value = false
    }
  }

  return {
    user,
    isLoggedIn,
    login,
    logout,
    checkAuth
  }
})
