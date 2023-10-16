import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'

const vm = createApp(App)

vm.mount('#app')
