// src/views/Login.vue
<template>
  <v-container fluid fill-height id="login-page">
    <v-layout align-center justify-center>
      <v-flex :style="{ 'max-width': '500px' }">
        <v-card>
          <v-card-text>
            <div class="text-center mb-4">
              {{ message }}
            </div>
            <transition name="fade" mode="out-in">

              <v-form ref="form" @submit.prevent="validate">
                <v-text-field id="username" label="Username" prepend-icon="mdi-username" v-model="form.username"
                  :rules="rules.username">
                </v-text-field>

                <v-text-field id="login" label="Email" prepend-icon="mdi-email" v-model="form.email" :rules="rules.email">
                </v-text-field>

                <v-text-field id="password" label="Mot de passe" prepend-icon="mdi-lock" type="password"
                  v-model="form.password" :rules="rules.password"></v-text-field>

                <div class="text-center">
                  <v-btn :loading="loading" color="primary" large type="submit" text rounded>Se connecter</v-btn>
                </div>
              </v-form>

            </transition>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import AuthService from '../services/AuthService.js';

export default {
  data() {
    return {
      email: '',
      password: '',
      message: "Connection",
      form: {
        username: null,
        email: null,
        password: null,
      },
      rules: {},
      loading: false,
    };
  },
  methods: {
    validate() {
      this.rules = {
        username: [v => !!v || 'Required'],
        email: [v => !!v || 'Required'],
        password: [v => !!v || 'Required']
      }
      this.$nextTick(() => {
        if (this.$refs.form.validate()) {
          this.loading = true;
          this.login(this.form);
        }
      });
    },
    async login(form) {
      try {
        const credentials = {
          username: form.username,
          email: form.email,
          password: form.password
        };
        const response = await AuthService.login(credentials);
        this.loading = false;
        this.message = response.msg;
        const token = response.token;
        const user = {
          id: response.userId,
          email: response.userEmail,
          username: response.userName
        };
        this.$store.dispatch('login', { token, user });
        this.$router.push('/');
        
      } catch (error) {
        this.loading = false;
        console.log("error", error);
        if (error.response.status == 401) {
          this.message = "Mauvais login/mot de passe";
        } else {
          this.message = error.message;
        }
      }
    }
  }
};
</script>