import { defineStore } from 'pinia'
import { useSnackBarStore } from './snackbar.store.js';
import axios from 'axios';
import router from "../router";

const url = 'http://localhost:8000/';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null
    }),
    actions: {
        async login(credentials) {
            const user = await this.remoteLogin(credentials);

            if (user) {
                this.user = user;
                localStorage.setItem('user', JSON.stringify(user));
                this.setBearer(user.access);
                // homepage
                router.push('/');
            }
        },
        isLocalLoggedIn() {
            var localUser = localStorage.getItem('user');

            if (localUser) {
                localUser = JSON.parse(localUser);
                if (localUser.access) {
                    this.user = localUser;
                    this.setBearer(localUser.access);

                    return true;
                }
            }
            return false;
        },
        setBearer(bearer) {
            // bearer token on every header :
            axios.defaults.headers.common = {
                'Authorization': `Bearer ${bearer}`
            };
        },
        logout() {
            return axios
            .post(url + 'auth/logout/')
            .then(() => {
                    this.clearSession();
                    router.push('/login');
                });
        },
        clearSession() {
            this.user = null;
            this.setBearer();
            localStorage.removeItem('user');
        },
        remoteLogin(credentials) {
            return axios
                .post(url + 'auth/login/', credentials)
                .then((response) => {
                    return Object.assign(credentials, response.data);
                })
                .catch((error) => {
                    if (error.response) {
                        useSnackBarStore().setSnackBarState({ text: error.response.data.detail });
                    }
                });
        },
        signUp(credentials) {
            return axios
                .post(url + 'auth/register/', credentials)
                .then(response => response.data)
                .catch((error) => { console.log("auth/register error", error); });
        },
        isLogged() {
            if (!this.user) {
                return false;
            } else {
                return true;
            }
        },
        authHeader() {
            let user = JSON.parse(localStorage.getItem('user'));

            if (user && user.accessToken) {
                return { Authorization: 'Bearer ' + user.accessToken };
            } else {
                return {};
            }
        }
    }
})
