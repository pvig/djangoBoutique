// src/views/SignUp.vue
<template>
  <v-container fluid fill-height id="login-page">
    <v-layout align-center justify-center>
      <v-flex :style="{ 'max-width': '350px' }">
        <v-card>
          <v-card-text>
            <div class="text-center mb-4">
              Inscription
            </div>
            <transition name="fade" mode="out-in">

              <v-form ref="form" @submit.prevent="validate">
                <v-text-field label="Nom" prepend-icon="mdi-account" v-model="nom" :rules="rules.required">
                </v-text-field>
                <v-text-field label="Email" prepend-icon="mdi-account" v-model="email" :rules="rules.email">
                </v-text-field>
                <v-text-field label="Mot de passe" prepend-icon="mdi-lock" type="password" v-model="password"
                  :rules="rules.password"></v-text-field>
                <v-text-field label="Mot de passe" prepend-icon="mdi-lock" type="password" v-model="password_repeat"
                  :rules="rules.password"></v-text-field>

                <div class="text-center">
                  <v-btn :loading="loading" color="primary" large type="submit" text rounded>Créer le compte</v-btn>
                </div>

                <p v-if="msg">{{ msg }}</p>

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
      username: '',
      email: '',
      password: '',
      password_repeat: '',
      msg: '',
      rules: {},
      loading: false,
    };
  },
  methods: {
    validate() {
      this.rules = {
        required: [v => !!v || 'Required'],
        email: [v => !!v || 'Required'],
        password: [v => !!v || 'Required']
      }
      this.$nextTick(() => {
        if (this.$refs.form.validate()) {
          this.loading = true;
          this.signUp(this.form);
        }
      });
    },
    async signUp() {
      try {
        const credentials = {
          nom: this.nom,
          email: this.email,
          password: this.password,
          password_repeat: this.password_repeat
        };
        AuthService.signUp(credentials).then((signupDone) => {
          console.log("signupDone", signupDone);
          const credentials = {
            email: this.email,
            password: this.password
          };
          console.log("credentials", credentials);
          AuthService.login(credentials).then((reponse) => {
            this.loading = false;
            const token = reponse.token;
            const user = {
              email: reponse.email,
              nom: reponse.nom
            };
            this.$store.dispatch('login', { token, user });
            this.$router.push('/');
            this.msg = signupDone.msg;
            console.log("login done", reponse);
          });

        });
      } catch (error) {
        this.msg = error.response.data.msg;
      }
    }
  }
};
</script>