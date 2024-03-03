// src/views/SignUp.vue
<template>
  <v-container fluid fill-height id="login-page">
    <v-row>
      <v-col></v-col>
      <v-col >
        <v-card>
          <v-card-text>
            <div class="text-center mb-4">
              Inscription
            </div>
            <transition name="fade" mode="out-in">

              <v-form ref="form" @submit.prevent="validate">
                <v-text-field label="Nom d'utilisateur" prepend-icon="mdi-account" v-model="username"> </v-text-field>
                <v-text-field label="Nom" prepend-icon="mdi-account" v-model="nom"></v-text-field>
                <v-text-field label="Prenom" prepend-icon="mdi-account" v-model="prenom"> </v-text-field>
                <v-text-field label="Email" prepend-icon="mdi-account" v-model="email"> </v-text-field>
                <v-text-field label="Mot de passe" prepend-icon="mdi-lock" type="password" v-model="password"></v-text-field>
                <v-text-field label="Confirmation mot de passe" prepend-icon="mdi-lock" type="password" v-model="password_repeat"></v-text-field>

                <div class="text-center">
                  <v-btn :loading="loading" color="primary" large type="submit" text rounded>Créer le compte</v-btn>
                </div>

                <p v-if="msg">{{ msg }}</p>

              </v-form>

            </transition>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col></v-col>
    </v-row>
  </v-container>
</template>
<script>
import { useAuthStore } from '../stores/auth.store.js';
import useVuelidate from '@vuelidate/core'
import { required, email, minLength, sameAs} from '@vuelidate/validators'

export default {
  setup() {
    return { v$: useVuelidate() }
  },
  validations() {
    return {
      username: { required },
      email: { required, email },
      nom: { required },
      prenom: { required },
      password: { required, minLength: minLength(8) },
      password_repeat:  { required, sameAsPassword: sameAs('password') }
    }
  },
  data() {
    return {
      username: '',
      email: '',
      nom: '',
      prenom: '',
      password: '',
      password_repeat: '',
      msg: '',
      loading: false,
    };
  },
  methods: {

    validate() {
      this.v$.$validate()
      this.$nextTick(() => {
        if (!this.v$.$error) {
          this.loading = true;
          this.signUp(this.form);
        }
      });
    },
    async signUp() {
      try {
        const credentials = {
          username: this.username,
          email: this.email,
          password: this.password,
          password2: this.password_repeat,
          first_name: this.nom,
          last_name: this.prenom,
        };
        useAuthStore().signUp(credentials).then((signupDone) => {

          const credentials = {
            username: this.username,
            email: this.email,
            password: this.password,
            password2: this.password_repeat,
            first_name: this.nom,
            last_name: this.prenom,
          };

          useAuthStore().login(credentials).then(() => {
            this.loading = false;
            this.msg = signupDone.msg;
          });

        });
      } catch (error) {
        this.msg = error.response.data.msg;
      }
    }
  }
};
</script>