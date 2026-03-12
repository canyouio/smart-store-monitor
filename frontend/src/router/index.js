import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/manage',
    name: 'Manage',
    component: () => import('@/views/Manage.vue'),
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  if (to.meta.requiresAuth) {
    if (!authStore.isLoggedIn) {
      await authStore.checkAuth()
    }
    if (!authStore.isLoggedIn) {
      return next('/login')
    }
  }
  
  if (to.path === '/login' && authStore.isLoggedIn) {
    return next('/')
  }
  
  next()
})

export default router
