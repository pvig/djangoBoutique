import { createPinia } from 'pinia'
import { createApp } from 'vue'
import router from "./router";
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import "./assets/styles/app.css";

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)

app.use(createPinia())
app.use(vuetify)
app.use(router)
app.mount('#app')

