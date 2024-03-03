import { createWebHistory, createRouter } from "vue-router";
import { useAuthStore } from '../stores/auth.store.js';
import axios from 'axios';
import Home from '../views/HomePage'
import Login from '../views/LoginForm'
import SignUp from '../views/SignUp'
import Clients from '../views/ClientList'
import Ventes from '../views/VenteList'
import Produits from '../views/ProduitList'

const routes = [
  { path: '/', component: Home, name: 'home' },
  { path: '/signup', component: SignUp, name: 'signup' },
  { path: '/login', component: Login, name: 'login' },
  { path: '/logout', component: Login, name: 'logout' },
  { path: '/clients', component: Clients, name: 'clients' },
  { path: '/ventes', component: Ventes, name: 'ventes' },
  { path: '/produits', component: Produits, name: 'produits' }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  if (to.name == "logout") {
    useAuthStore().logout();
  }
})

axios.interceptors.response.use(response => {
  return response;
}, error => {
  if (error.response.status === 401) {

    if (!useAuthStore().isLocalLoggedIn()) {
      useAuthStore().clearSession()
      router.push({ path: '/login' })
    } else {
      return Promise.resolve(error).finally(()=> {
        // not really an error, resolve to homepage with a step to soft refresh
        router.push({ path: '/blank'}).then(() => {
          router.push({ path: '/'})
        })
      })
    }

  }
  return Promise.reject(error);
});

export default router;
