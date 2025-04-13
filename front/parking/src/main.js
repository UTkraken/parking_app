import './assets/reset.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { routes } from './routes.js'
import App from './App.vue'
import Toast from 'vue-toastification'
import { createPinia } from 'pinia'
import 'vue-toastification/dist/index.css'

const router = createRouter({
    history: createWebHistory(),
    routes, 
})

const app = createApp(App)
const pinia = createPinia()


app.use(pinia)
app.use(router)
app.use(Toast, {
  position: 'top-right',
  timeout: 3000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
})
app.mount('#app')
