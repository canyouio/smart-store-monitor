<template>
  <div class="min-h-screen">
    <header class="glass-card m-4 p-4 flex items-center justify-between">
      <div class="flex items-center space-x-4">
        <router-link to="/" class="flex items-center space-x-2 text-gray-400 hover:text-white transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
          <span>返回监控</span>
        </router-link>
        <span class="text-gray-600">|</span>
        <h1 class="text-xl font-bold text-gradient">订单管理</h1>
      </div>
      
      <div class="flex items-center space-x-4">
        <span class="text-sm text-gray-400">欢迎, {{ authStore.user?.username }}</span>
        <button @click="handleLogout" class="px-4 py-2 bg-red-500/20 text-red-400 rounded-lg hover:bg-red-500/30 transition text-sm">
          退出登录
        </button>
      </div>
    </header>
    
    <div class="glass-card m-4 p-6">
      <div class="flex items-center justify-between mb-6">
        <div class="flex items-center space-x-4">
          <select
            v-model="filters.category"
            @change="fetchOrders(1)"
            class="px-4 py-2 bg-dark-400 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-primary-500 outline-none"
          >
            <option value="">全部品类</option>
            <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
          </select>
          
          <input
            v-model.number="filters.min_amount"
            type="number"
            placeholder="最小金额"
            @change="fetchOrders(1)"
            class="px-4 py-2 bg-dark-400 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-primary-500 outline-none w-32"
          />
          
          <input
            v-model.number="filters.max_amount"
            type="number"
            placeholder="最大金额"
            @change="fetchOrders(1)"
            class="px-4 py-2 bg-dark-400 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-primary-500 outline-none w-32"
          />
          
          <button
            @click="resetFilters"
            class="px-4 py-2 bg-gray-700 text-gray-300 rounded-lg hover:bg-gray-600 transition"
          >
            重置
          </button>
        </div>
        
        <button
          @click="openAddModal"
          class="px-4 py-2 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-lg hover:from-primary-600 hover:to-primary-700 transition flex items-center space-x-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          <span>新增订单</span>
        </button>
      </div>
      
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead>
            <tr class="border-b border-gray-700">
              <th class="text-left py-3 px-4 text-gray-400 font-medium">ID</th>
              <th class="text-left py-3 px-4 text-gray-400 font-medium">品类</th>
              <th class="text-left py-3 px-4 text-gray-400 font-medium">金额</th>
              <th class="text-left py-3 px-4 text-gray-400 font-medium">时间</th>
              <th class="text-right py-3 px-4 text-gray-400 font-medium">操作</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="order in orders"
              :key="order.id"
              class="border-b border-gray-800 hover:bg-white/5 transition"
            >
              <td class="py-3 px-4 text-gray-300">{{ order.id }}</td>
              <td class="py-3 px-4">
                <span class="px-2 py-1 rounded-full text-xs" :class="getCategoryClass(order.category)">
                  {{ order.category }}
                </span>
              </td>
              <td class="py-3 px-4 text-green-400 font-medium">¥{{ order.amount }}</td>
              <td class="py-3 px-4 text-gray-400">{{ order.timestamp }}</td>
              <td class="py-3 px-4 text-right space-x-2">
                <button
                  @click="openEditModal(order)"
                  class="px-3 py-1 bg-primary-500/20 text-primary-400 rounded hover:bg-primary-500/30 transition text-sm"
                >
                  编辑
                </button>
                <button
                  @click="handleDelete(order.id)"
                  class="px-3 py-1 bg-red-500/20 text-red-400 rounded hover:bg-red-500/30 transition text-sm"
                >
                  删除
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div v-if="loading" class="text-center py-8 text-gray-400">
        加载中...
      </div>
      
      <div v-if="!loading && orders.length === 0" class="text-center py-8 text-gray-400">
        暂无数据
      </div>
      
      <div v-if="totalPages > 1" class="flex items-center justify-center space-x-2 mt-6">
        <button
          @click="fetchOrders(currentPage - 1)"
          :disabled="currentPage === 1"
          class="px-3 py-1 bg-gray-700 text-gray-300 rounded hover:bg-gray-600 transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          上一页
        </button>
        
        <template v-for="page in visiblePages" :key="page">
          <span v-if="page === '...'" class="px-3 py-1 text-gray-500">...</span>
          <button
            v-else
            @click="fetchOrders(page)"
            :class="[
              'px-3 py-1 rounded transition',
              page === currentPage
                ? 'bg-primary-500 text-white'
                : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
            ]"
          >
            {{ page }}
          </button>
        </template>
        
        <button
          @click="fetchOrders(currentPage + 1)"
          :disabled="currentPage === totalPages"
          class="px-3 py-1 bg-gray-700 text-gray-300 rounded hover:bg-gray-600 transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          下一页
        </button>
      </div>
    </div>
    
    <div v-if="showModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50" @click.self="closeModal">
      <div class="glass-card p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-white mb-4">{{ isEdit ? '编辑订单' : '新增订单' }}</h3>
        
        <form @submit.prevent="handleSubmit" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">品类</label>
            <select
              v-model="form.category"
              required
              class="w-full px-4 py-2 bg-dark-400 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-primary-500 outline-none"
            >
              <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
            </select>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">金额</label>
            <input
              v-model.number="form.amount"
              type="number"
              step="0.01"
              required
              class="w-full px-4 py-2 bg-dark-400 border border-gray-700 rounded-lg text-white focus:ring-2 focus:ring-primary-500 outline-none"
            />
          </div>
          
          <div class="flex space-x-4 pt-4">
            <button
              type="button"
              @click="closeModal"
              class="flex-1 py-2 bg-gray-700 text-gray-300 rounded-lg hover:bg-gray-600 transition"
            >
              取消
            </button>
            <button
              type="submit"
              :disabled="submitting"
              class="flex-1 py-2 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-lg hover:from-primary-600 hover:to-primary-700 transition disabled:opacity-50"
            >
              {{ submitting ? '提交中...' : '确定' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import { ordersApi } from '@/api/orders'

const router = useRouter()
const authStore = useAuthStore()

const categories = ['鲜食便当', '碳酸饮料', '休闲零食', '乳制品', '日用百货']

const orders = ref([])
const loading = ref(false)
const currentPage = ref(1)
const totalPages = ref(1)
const totalRecords = ref(0)

const filters = ref({
  category: '',
  min_amount: null,
  max_amount: null
})

const showModal = ref(false)
const isEdit = ref(false)
const submitting = ref(false)
const form = ref({
  id: null,
  category: '',
  amount: 0
})

const visiblePages = computed(() => {
  const total = totalPages.value
  const current = currentPage.value
  
  if (total <= 7) {
    return Array.from({ length: total }, (_, i) => i + 1)
  }
  
  if (current <= 4) {
    return [1, 2, 3, 4, 5, '...', total]
  }
  
  if (current >= total - 3) {
    return [1, '...', total - 4, total - 3, total - 2, total - 1, total]
  }
  
  return [1, '...', current - 1, current, current + 1, '...', total]
})

const getCategoryClass = (category) => {
  const classes = {
    '鲜食便当': 'bg-orange-500/20 text-orange-400',
    '碳酸饮料': 'bg-blue-500/20 text-blue-400',
    '休闲零食': 'bg-yellow-500/20 text-yellow-400',
    '乳制品': 'bg-green-500/20 text-green-400',
    '日用百货': 'bg-purple-500/20 text-purple-400'
  }
  return classes[category] || 'bg-gray-500/20 text-gray-400'
}

const fetchOrders = async (page = 1) => {
  loading.value = true
  currentPage.value = page
  
  try {
    const params = {
      page,
      category: filters.value.category || undefined,
      min_amount: filters.value.min_amount || undefined,
      max_amount: filters.value.max_amount || undefined
    }
    
    const res = await ordersApi.getOrders(params)
    if (res.code === 200) {
      orders.value = res.data.orders
      totalPages.value = res.data.total_pages
      totalRecords.value = res.data.total_records
    }
  } catch (e) {
    console.error('Failed to fetch orders:', e)
  } finally {
    loading.value = false
  }
}

const resetFilters = () => {
  filters.value = {
    category: '',
    min_amount: null,
    max_amount: null
  }
  fetchOrders(1)
}

const openAddModal = () => {
  isEdit.value = false
  form.value = {
    id: null,
    category: categories[0],
    amount: 0
  }
  showModal.value = true
}

const openEditModal = (order) => {
  isEdit.value = true
  form.value = {
    id: order.id,
    category: order.category,
    amount: order.amount
  }
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
}

const handleSubmit = async () => {
  submitting.value = true
  
  try {
    if (isEdit.value) {
      await ordersApi.updateOrder(form.value)
    } else {
      await ordersApi.addOrder(form.value)
    }
    closeModal()
    fetchOrders(currentPage.value)
  } catch (e) {
    console.error('Failed to submit:', e)
  } finally {
    submitting.value = false
  }
}

const handleDelete = async (id) => {
  if (!confirm('确定要删除这条订单吗？')) return
  
  try {
    await ordersApi.deleteOrder(id)
    fetchOrders(currentPage.value)
  } catch (e) {
    console.error('Failed to delete:', e)
  }
}

const handleLogout = async () => {
  await authStore.logout()
  router.push('/login')
}

onMounted(() => {
  fetchOrders()
})
</script>
