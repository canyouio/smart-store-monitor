import { defineStore } from 'pinia'
import { ref } from 'vue'
import { realtimeApi } from '@/api/realtime'
import { io } from 'socket.io-client'

export const useRealtimeStore = defineStore('realtime', () => {
  const revenue = ref(0)
  const visitors = ref(0)
  const currentInside = ref(0)
  const timeData = ref([])
  const insideData = ref([])
  const socket = ref(null)
  const connected = ref(false)

  const connectSocket = () => {
    if (socket.value) return
    
    socket.value = io('http://127.0.0.1:5001', {
      path: '/socket.io',
      transports: ['websocket', 'polling'],
      withCredentials: true
    })

    socket.value.on('connect', () => {
      console.log('Socket connected')
      connected.value = true
    })

    socket.value.on('store_update', (data) => {
      revenue.value = data.revenue
      visitors.value = data.visitors
      currentInside.value = data.current_inside
      
      timeData.value.push(data.time)
      insideData.value.push(data.current_inside)
      
      if (timeData.value.length > 30) {
        timeData.value.shift()
        insideData.value.shift()
      }
    })

    socket.value.on('disconnect', () => {
      console.log('Socket disconnected')
      connected.value = false
    })
  }

  const disconnectSocket = () => {
    if (socket.value) {
      socket.value.disconnect()
      socket.value = null
      connected.value = false
    }
  }

  const fetchInitialState = async () => {
    try {
      const res = await realtimeApi.getState()
      if (res.code === 200) {
        revenue.value = res.data.revenue
        visitors.value = res.data.visitors
        currentInside.value = res.data.current_inside
      }
    } catch (e) {
      console.error('Failed to fetch initial state:', e)
    }
  }

  return {
    revenue,
    visitors,
    currentInside,
    timeData,
    insideData,
    connected,
    connectSocket,
    disconnectSocket,
    fetchInitialState
  }
})
