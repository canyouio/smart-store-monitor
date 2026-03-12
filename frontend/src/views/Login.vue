<template>
  <div class="min-h-screen flex items-center justify-center relative overflow-hidden">
    <div ref="threeContainer" class="absolute inset-0 z-0"></div>
    
    <div class="glass-card p-8 w-full max-w-md z-10 relative">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gradient mb-2">智慧便利店</h1>
        <p class="text-gray-400">实时监控系统</p>
      </div>
      
      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">用户名</label>
          <input
            v-model="form.username"
            type="text"
            class="w-full px-4 py-3 bg-dark-400 border border-gray-700 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition text-white placeholder-gray-500"
            placeholder="请输入用户名"
            required
          />
        </div>
        
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">密码</label>
          <input
            v-model="form.password"
            type="password"
            class="w-full px-4 py-3 bg-dark-400 border border-gray-700 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition text-white placeholder-gray-500"
            placeholder="请输入密码"
            required
          />
        </div>
        
        <div v-if="error" class="text-red-400 text-sm text-center bg-red-500/10 py-2 rounded-lg">
          {{ error }}
        </div>
        
        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 bg-gradient-to-r from-primary-500 to-primary-600 text-white font-medium rounded-lg hover:from-primary-600 hover:to-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <span v-if="loading">登录中...</span>
          <span v-else>登录</span>
        </button>
      </form>
      
      <p class="text-center text-gray-500 text-sm mt-6">
        默认账号: admin / 123456
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import * as THREE from 'three'

const router = useRouter()
const authStore = useAuthStore()

const form = ref({
  username: '',
  password: ''
})
const error = ref('')
const loading = ref(false)
const threeContainer = ref(null)

let scene, camera, renderer, particles
let animationId

const initThree = () => {
  if (!threeContainer.value) return
  
  scene = new THREE.Scene()
  
  camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  )
  camera.position.z = 50
  
  renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  threeContainer.value.appendChild(renderer.domElement)
  
  const particleCount = 500
  const positions = new Float32Array(particleCount * 3)
  const colors = new Float32Array(particleCount * 3)
  
  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 100
    positions[i * 3 + 1] = (Math.random() - 0.5) * 100
    positions[i * 3 + 2] = (Math.random() - 0.5) * 100
    
    colors[i * 3] = 0.1 + Math.random() * 0.2
    colors[i * 3 + 1] = 0.5 + Math.random() * 0.3
    colors[i * 3 + 2] = 0.8 + Math.random() * 0.2
  }
  
  const geometry = new THREE.BufferGeometry()
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3))
  
  const material = new THREE.PointsMaterial({
    size: 0.5,
    vertexColors: true,
    transparent: true,
    opacity: 0.8
  })
  
  particles = new THREE.Points(geometry, material)
  scene.add(particles)
  
  animate()
}

const animate = () => {
  animationId = requestAnimationFrame(animate)
  
  if (particles) {
    particles.rotation.x += 0.0005
    particles.rotation.y += 0.001
  }
  
  renderer.render(scene, camera)
}

const handleResize = () => {
  if (!camera || !renderer) return
  camera.aspect = window.innerWidth / window.innerHeight
  camera.updateProjectionMatrix()
  renderer.setSize(window.innerWidth, window.innerHeight)
}

const handleLogin = async () => {
  error.value = ''
  loading.value = true
  
  try {
    await authStore.login(form.value.username, form.value.password)
    router.push('/')
  } catch (e) {
    error.value = e.message || '登录失败，请检查用户名和密码'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  initThree()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
  if (renderer) {
    renderer.dispose()
  }
})
</script>
