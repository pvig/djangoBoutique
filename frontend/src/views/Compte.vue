<template>

    <v-container justify="center">
        <v-card class="pl-4 pr-4 mt-4 ml-auto mr-auto" outlined max-width="800">

            <div class="text-center mb-4">
                Mon compte
            </div>

            <div class="text-center mb-4">
                {{ message }}
            </div>

            <v-form ref="form" @submit.prevent="validate">
                <v-text-field label="Nom" prepend-icon="mdi-account" v-model="username" :rules="rules.required">
                </v-text-field>

                <v-text-field id="login" label="Email" prepend-icon="mdi-email" v-model="useremail"
                    :rules="rules.email">
                </v-text-field>

                <div class="text-center">
                    <v-btn :loading="loading" color="primary" large type="submit" text rounded>Sauvegarder</v-btn>
                </div>
            </v-form>

        </v-card>

    </v-container>

</template>

<script>
import AuthService from '../services/AuthService.js';

export default {
    data() {
        return {
            usernameInput: '',
            emailInput: '',
            password: '',
            message: '',
            rules: {},
            loading: false,
        };
    },
    computed: {
        username: {
            get() {
                return this.$store.getters.getUser.username;
            },

            set(usernameInput) {
                if (this.usernameInput !== usernameInput) {
                    this.usernameInput = usernameInput;
                }
            }
        },
        useremail: {
            get() {
                return this.$store.getters.getUser.email;
            },

            set(emailInput) {
                if (this.emailInput !== emailInput) {
                    this.emailInput = emailInput;
                }
            }
        },
    },
    methods: {
        validate() {
            this.rules = {
                email: [v => !!v || 'Required'],
                password: [v => !!v || 'Required']
            }
            this.$nextTick(() => {
                if (this.$refs.form.validate()) {
                    this.loading = true;
                    this.update(this.form);
                }
            });
        },
        async update(form) {
            try {
                const credentials = {
                    email: form.email,
                    password: form.password
                };
                const response = await AuthService.login(credentials);
                this.loading = false;
                this.message = response.msg;
                const token = response.token;
                const user = {
                    email: response.email,
                    username: response.username
                };
                this.$store.dispatch('login', { token, user });
                this.$router.push('/');
            } catch (error) {
                this.loading = false;
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