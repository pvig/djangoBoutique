<template>
  <v-container fluid fill-height id="login-page">
    <div id="nav" v-if="authenticated">
      <router-link to="/">Home</router-link> |
      <router-link to="/logout">logout</router-link> |
      <router-link to="/produits">Produits</router-link> |
      <router-link to="/clients">Clients</router-link> |
      <router-link to="/ventes">Ventes</router-link>
    </div>
    <div id="nav" v-if="!authenticated">
      <router-link to="/login">login</router-link>
    </div>
    <router-view />
    <SnackBar></SnackBar>
  </v-container>
</template>

<script>
import { useAuthStore } from './stores/auth.store.js';

export default {
  name: 'App',
  components: { },
  data() {
    return {
      loading: false,
    };
  },
  computed: {
    authenticated: () => useAuthStore().isLogged()
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
