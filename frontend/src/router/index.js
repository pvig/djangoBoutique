import { createWebHistory, createRouter } from "vue-router";
import { useSnackBarStore } from '../stores/snackbar.store.js';
import axios from 'axios';
//import Home from '../views/HomePage'
import Login from '../views/LoginForm'
import SignUp from '../views/SignUp'
//import Compte from '../views/ComptePage'
import Clients from '../views/ClientList'
//import Ventes from '../views/VenteList'
import Produits from '../views/ProduitList'
//import VueRouter from 'vue-router';

const routes = [
  //{ path: '/', component: Home, name: 'home' },
  { path: '/signup', component: SignUp, name: 'signup' },
  { path: '/login', component: Login, name: 'login' },
  { path: '/logout', component: Login, name: 'logout' },
  //{ path: '/compte', component: Compte, name: 'compte'},
  { path: '/clients', component: Clients, name: 'clients'},
  //{ path: '/ventes', component: Ventes, name: 'ventes'},
  { path: '/produits', component: Produits, name: 'produits' }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

axios.interceptors.response.use(response => {
  return response;
}, error => {
  if (error.response.status === 401) {
      router
      .push({ path: '/login' })
      .then(() => { 
        location.reload();
        useSnackBarStore().setSnackBarState({ text: "Vous avez été déconnecté" });
      })
  }
  return Promise.reject(error);
});

export default router;
