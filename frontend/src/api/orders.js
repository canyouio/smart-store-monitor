import api from './index'

export const ordersApi = {
  getOrders: (params) => 
    api.get('/orders', { params }),
  
  addOrder: (data) => 
    api.post('/order/add', data),
  
  updateOrder: (data) => 
    api.post('/order/update', data),
  
  deleteOrder: (id) => 
    api.delete(`/order/delete/${id}`)
}
