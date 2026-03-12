<template>
  <div class="min-h-screen relative overflow-hidden">
    <div ref="threeContainer" class="absolute inset-0 z-0"></div>
    
    <div class="relative z-10">
      <header class="glass-card m-4 p-4 flex items-center justify-between">
        <div class="flex items-center space-x-4">
          <div class="w-10 h-10 bg-gradient-to-br from-primary-400 to-primary-600 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
          </div>
          <div>
            <h1 class="text-xl font-bold text-gradient">智慧便利店实时监控</h1>
            <p class="text-xs text-gray-400">Smart Store Real-time Monitor</p>
          </div>
        </div>
        
        <div class="flex items-center space-x-4">
          <div class="flex items-center space-x-2">
            <span class="relative flex h-3 w-3">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
            </span>
            <span class="text-sm text-gray-400">实时在线</span>
          </div>
          
          <span class="text-gray-400">|</span>
          
          <span class="text-sm text-gray-300">欢迎, {{ authStore.user?.username }}</span>
          
          <router-link to="/manage" class="px-4 py-2 bg-primary-500/20 text-primary-400 rounded-lg hover:bg-primary-500/30 transition text-sm">
            订单管理
          </router-link>
          
          <button @click="handleLogout" class="px-4 py-2 bg-red-500/20 text-red-400 rounded-lg hover:bg-red-500/30 transition text-sm">
            退出登录
          </button>
        </div>
      </header>
      
      <div class="grid grid-cols-4 gap-4 p-4">
        <div class="glass-card p-6 hover:glow-effect transition-all duration-300">
          <div class="flex items-center justify-between mb-4">
            <span class="text-gray-400 text-sm">总营业额</span>
            <div class="w-10 h-10 bg-green-500/20 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
          <div class="stat-number">¥{{ realtimeStore.revenue.toFixed(2) }}</div>
          <div class="text-xs text-green-400 mt-2 flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
            </svg>
            实时更新
          </div>
        </div>
        
        <div class="glass-card p-6 hover:glow-effect transition-all duration-300">
          <div class="flex items-center justify-between mb-4">
            <span class="text-gray-400 text-sm">进店人次</span>
            <div class="w-10 h-10 bg-blue-500/20 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </div>
          </div>
          <div class="stat-number">{{ realtimeStore.visitors }}</div>
          <div class="text-xs text-blue-400 mt-2">今日累计</div>
        </div>
        
        <div class="glass-card p-6 hover:glow-effect transition-all duration-300">
          <div class="flex items-center justify-between mb-4">
            <span class="text-gray-400 text-sm">店内人数</span>
            <div class="w-10 h-10 bg-purple-500/20 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
          </div>
          <div class="stat-number">{{ realtimeStore.currentInside }}</div>
          <div class="text-xs text-purple-400 mt-2">实时在店</div>
        </div>
        
        <div class="glass-card p-6 hover:glow-effect transition-all duration-300">
          <div class="flex items-center justify-between mb-4">
            <span class="text-gray-400 text-sm">设备状态</span>
            <div class="w-10 h-10 bg-cyan-500/20 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z" />
              </svg>
            </div>
          </div>
          <div class="stat-number text-green-400">正常</div>
          <div class="text-xs text-cyan-400 mt-2">全部在线</div>
        </div>
      </div>
      
      <div class="grid grid-cols-2 gap-4 p-4">
        <div class="glass-card p-6">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
            <span class="w-2 h-2 bg-primary-500 rounded-full mr-2"></span>
            品类营业额排行
          </h3>
          <div ref="offlineChartRef" class="h-80"></div>
        </div>
        
        <div class="glass-card p-6">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
            <span class="w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></span>
            实时客流监控
          </h3>
          <div ref="realtimeChartRef" class="h-80"></div>
        </div>
      </div>
      
      <div class="glass-card m-4 p-6">
        <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
          <span class="w-2 h-2 bg-purple-500 rounded-full mr-2"></span>
          店内3D热力图
        </h3>
        <div ref="heatmapContainer" class="h-64 rounded-lg overflow-hidden"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import { useRealtimeStore } from '@/store/realtime'
import { realtimeApi } from '@/api/realtime'
import * as THREE from 'three'
import * as echarts from 'echarts'

const router = useRouter()
const authStore = useAuthStore()
const realtimeStore = useRealtimeStore()

const threeContainer = ref(null)
const heatmapContainer = ref(null)
const offlineChartRef = ref(null)
const realtimeChartRef = ref(null)

let mainScene, mainCamera, mainRenderer, mainAnimationId
let heatmapScene, heatmapCamera, heatmapRenderer, heatmapAnimationId
let offlineChart, realtimeChart

const initMainThree = () => {
  if (!threeContainer.value) return
  
  mainScene = new THREE.Scene()
  mainCamera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
  mainCamera.position.z = 30
  
  mainRenderer = new THREE.WebGLRenderer({ alpha: true, antialias: true })
  mainRenderer.setSize(window.innerWidth, window.innerHeight)
  mainRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  threeContainer.value.appendChild(mainRenderer.domElement)
  
  const particleCount = 300
  const positions = new Float32Array(particleCount * 3)
  const colors = new Float32Array(particleCount * 3)
  
  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 80
    positions[i * 3 + 1] = (Math.random() - 0.5) * 80
    positions[i * 3 + 2] = (Math.random() - 0.5) * 80
    
    colors[i * 3] = 0.02 + Math.random() * 0.1
    colors[i * 3 + 1] = 0.4 + Math.random() * 0.2
    colors[i * 3 + 2] = 0.6 + Math.random() * 0.3
  }
  
  const geometry = new THREE.BufferGeometry()
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3))
  
  const material = new THREE.PointsMaterial({
    size: 0.3,
    vertexColors: true,
    transparent: true,
    opacity: 0.6
  })
  
  const particles = new THREE.Points(geometry, material)
  mainScene.add(particles)
  
  const animateMain = () => {
    mainAnimationId = requestAnimationFrame(animateMain)
    particles.rotation.y += 0.0003
    mainRenderer.render(mainScene, mainCamera)
  }
  animateMain()
}

const initHeatmap = () => {
  if (!heatmapContainer.value) return
  
  const width = heatmapContainer.value.clientWidth
  const height = heatmapContainer.value.clientHeight
  
  heatmapScene = new THREE.Scene()
  heatmapScene.background = new THREE.Color(0x0a0e14)
  
  heatmapCamera = new THREE.PerspectiveCamera(60, width / height, 0.1, 1000)
  heatmapCamera.position.set(15, 15, 15)
  heatmapCamera.lookAt(0, 0, 0)
  
  heatmapRenderer = new THREE.WebGLRenderer({ antialias: true })
  heatmapRenderer.setSize(width, height)
  heatmapContainer.value.appendChild(heatmapRenderer.domElement)
  
  const gridHelper = new THREE.GridHelper(20, 20, 0x1e3a5f, 0x0f1520)
  heatmapScene.add(gridHelper)
  
  const floorGeometry = new THREE.PlaneGeometry(20, 20)
  const floorMaterial = new THREE.MeshBasicMaterial({
    color: 0x0f1520,
    transparent: true,
    opacity: 0.8
  })
  const floor = new THREE.Mesh(floorGeometry, floorMaterial)
  floor.rotation.x = -Math.PI / 2
  heatmapScene.add(floor)
  
  const shelfPositions = [
    { x: -6, z: -6 }, { x: -2, z: -6 }, { x: 2, z: -6 }, { x: 6, z: -6 },
    { x: -6, z: 0 }, { x: 6, z: 0 },
    { x: -6, z: 6 }, { x: -2, z: 6 }, { x: 2, z: 6 }, { x: 6, z: 6 }
  ]
  
  shelfPositions.forEach(pos => {
    const shelfGeometry = new THREE.BoxGeometry(3, 4, 1)
    const shelfMaterial = new THREE.MeshBasicMaterial({ color: 0x1e3a5f })
    const shelf = new THREE.Mesh(shelfGeometry, shelfMaterial)
    shelf.position.set(pos.x, 2, pos.z)
    heatmapScene.add(shelf)
  })
  
  const heatmapPoints = []
  for (let i = 0; i < 50; i++) {
    const geometry = new THREE.SphereGeometry(0.3, 16, 16)
    const material = new THREE.MeshBasicMaterial({
      color: new THREE.Color().setHSL(0.6 - Math.random() * 0.3, 0.8, 0.5),
      transparent: true,
      opacity: 0.6
    })
    const sphere = new THREE.Mesh(geometry, material)
    sphere.position.set(
      (Math.random() - 0.5) * 18,
      0.3,
      (Math.random() - 0.5) * 18
    )
    heatmapPoints.push(sphere)
    heatmapScene.add(sphere)
  }
  
  const animateHeatmap = () => {
    heatmapAnimationId = requestAnimationFrame(animateHeatmap)
    
    heatmapPoints.forEach((point, i) => {
      point.position.y = 0.3 + Math.sin(Date.now() * 0.002 + i) * 0.2
      point.material.opacity = 0.4 + Math.sin(Date.now() * 0.003 + i) * 0.2
    })
    
    heatmapCamera.position.x = 15 * Math.cos(Date.now() * 0.0003)
    heatmapCamera.position.z = 15 * Math.sin(Date.now() * 0.0003)
    heatmapCamera.lookAt(0, 0, 0)
    
    heatmapRenderer.render(heatmapScene, heatmapCamera)
  }
  animateHeatmap()
}

const initCharts = async () => {
  if (offlineChartRef.value) {
    offlineChart = echarts.init(offlineChartRef.value)
    
    try {
      const res = await realtimeApi.getOfflineStats()
      if (res.code === 200) {
        updateOfflineChart(res.data)
      }
    } catch (e) {
      console.error('Failed to fetch offline stats:', e)
    }
  }
  
  if (realtimeChartRef.value) {
    realtimeChart = echarts.init(realtimeChartRef.value)
    updateRealtimeChart()
  }
}

const updateOfflineChart = (data) => {
  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: data.categories,
      axisLine: { lineStyle: { color: '#334155' } },
      axisLabel: { color: '#94a3b8' }
    },
    yAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: '#334155' } },
      axisLabel: { color: '#94a3b8' },
      splitLine: { lineStyle: { color: '#1e293b' } }
    },
    series: [{
      data: data.values,
      type: 'bar',
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: '#38bdf8' },
          { offset: 1, color: '#0ea5e9' }
        ]),
        borderRadius: [4, 4, 0, 0]
      }
    }]
  }
  offlineChart.setOption(option)
}

const updateRealtimeChart = () => {
  const option = {
    backgroundColor: 'transparent',
    tooltip: { trigger: 'axis' },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: realtimeStore.timeData,
      axisLine: { lineStyle: { color: '#334155' } },
      axisLabel: { color: '#94a3b8' }
    },
    yAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: '#334155' } },
      axisLabel: { color: '#94a3b8' },
      splitLine: { lineStyle: { color: '#1e293b' } }
    },
    series: [{
      data: realtimeStore.insideData,
      type: 'line',
      smooth: true,
      lineStyle: { color: '#22c55e', width: 2 },
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: 'rgba(34, 197, 94, 0.3)' },
          { offset: 1, color: 'rgba(34, 197, 94, 0)' }
        ])
      },
      itemStyle: { color: '#22c55e' }
    }]
  }
  realtimeChart.setOption(option)
}

watch(
  () => realtimeStore.insideData.length,
  () => {
    if (realtimeChart) {
      updateRealtimeChart()
    }
  }
)

const handleResize = () => {
  if (mainCamera && mainRenderer) {
    mainCamera.aspect = window.innerWidth / window.innerHeight
    mainCamera.updateProjectionMatrix()
    mainRenderer.setSize(window.innerWidth, window.innerHeight)
  }
  
  if (offlineChart) {
    offlineChart.resize()
  }
  if (realtimeChart) {
    realtimeChart.resize()
  }
}

const handleLogout = async () => {
  await authStore.logout()
  realtimeStore.disconnectSocket()
  router.push('/login')
}

onMounted(async () => {
  await realtimeStore.fetchInitialState()
  realtimeStore.connectSocket()
  
  initMainThree()
  initHeatmap()
  initCharts()
  
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  
  if (mainAnimationId) cancelAnimationFrame(mainAnimationId)
  if (heatmapAnimationId) cancelAnimationFrame(heatmapAnimationId)
  
  if (mainRenderer) mainRenderer.dispose()
  if (heatmapRenderer) heatmapRenderer.dispose()
  
  if (offlineChart) offlineChart.dispose()
  if (realtimeChart) realtimeChart.dispose()
  
  realtimeStore.disconnectSocket()
})
</script>
