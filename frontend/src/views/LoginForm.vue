// src/views/Login.vue

<template>
  <div>
    <v-container fluid fill-height id="login-page">
      <v-row>
        <v-col></v-col>
        <v-col>
          <v-card>
            <v-card-text>
              <div class="text-center mb-4">
                {{ message }}
              </div>
              <transition name="fade" mode="out-in">

                <v-form ref="form" fast-fail @submit.prevent="validate">
                  <v-text-field id="username" label="Username" prepend-icon="mdi-username" v-model="form.username"
                    :rules="rules.username">
                  </v-text-field>

                  <v-text-field id="email" label="Email" prepend-icon="mdi-email" v-model="form.email"
                    :rules="rules.email">
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
        </v-col>
        <v-col></v-col>
      </v-row>

      <v-row>
        <v-col></v-col>
        <v-col :style="{ 'max-width': '500px' }">

          <div class="text-center">
            <v-btn color="secondary" type="button" text rounded @click="$router.push('/signUp')">Créer un compte</v-btn>
          </div>

        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>

    <SnackBar />
  </div>
</template>

<script>
import { useAuthStore } from '../stores/auth.store.js';
import SnackBar from '../components/SnackBar.vue'

export default {
  components: {
    SnackBar
  },
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

    async validate() {
      this.rules = {
        username: [v => !!v || 'Required'],
        email: [v => !!v || 'Required'],
        password: [v => !!v || 'Required']
      }
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        this.loading = true;
        this.login(this.form);
      }
    },
    async login(form) {
      const credentials = {
        username: form.username,
        email: form.email,
        password: form.password
      };
      useAuthStore().login(credentials).then(() => {
        this.loading = false;
      });
    }
  }
};
</script>