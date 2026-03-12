import api from './index'

export const realtimeApi = {
  getState: () => 
    api.get('/realtime-state'),
  
  getOfflineStats: () => 
    api.get('/offline-stats')
}
