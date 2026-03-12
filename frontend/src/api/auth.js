import api from './index'

export const authApi = {
  login: (username, password) => 
    api.post('/auth/login', { username, password }),
  
  logout: () => 
    api.post('/auth/logout'),
  
  check: () => 
    api.get('/auth/check')
}
