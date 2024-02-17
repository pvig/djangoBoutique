<template>
  <v-container fluid fill-height id="login-page">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">login</router-link> |
      <router-link to="/signup">signup</router-link> |
      <router-link to="/produits">Produits</router-link>
    </div>
    <router-view />
  </v-container>
</template>

<script>

export default {
  name: 'App',
  components: {},
  data() {
    return {
      loading: false,
    };
  },
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
