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
  { path: '/produits', component: Produits, name: 'produits' },
  // default redirect
  { path: '/:pathMatch(.*)*', redirect: '/login' }
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

axios.interceptors.request.use(
  function (config) {
    const accessToken = localStorage.getItem("accessToken");
    if (accessToken) {
      config.headers["Authorization"] = `Bearer ${accessToken}`
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(response => {
  return response;
}, async error => {
  if (error.response.status === 401) {

    await useAuthStore().refreshAccessToken().then((authentified) => {
      if (!authentified) {
        router.push({ path: '/login' })
        useAuthStore().clearSession()
      } else {
        // not really an error, resolve to homepage with a step to soft refresh
        var currentPage = router.path || "/";
        router.push({ path: '/login' }).then(() => {
          router.push({ path: currentPage })
        })
      }
    });

  }

  return Promise.resolve(error);
});

export default router;
