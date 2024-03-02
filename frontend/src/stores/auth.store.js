import { defineStore } from 'pinia'
import axios from 'axios';
import router from "../router";

const url = 'http://localhost:8000/';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: {},
        returnUrl: null
    }),
    actions: {
        async login(credentials) {
            const user = await this.remoteLogin(credentials);
            this.user = user;
            localStorage.setItem('user', JSON.stringify(user));

            // bearer token on every header :
            axios.defaults.headers.common = {
                'Authorization': `Bearer ${user.access}`
            };

            // homepage
            router.push(this.returnUrl || '/');
        },
        logout() {
            return axios
                .post(url + 'auth/logout/')
                .then(() => {
                    this.clearSession();
                    //router.push('/login');
                    //location.reload();
                });
        },
        clearSession() {
            this.user = null;
            localStorage.removeItem('user');
        },
        remoteLogin(credentials) {
            return axios
                .post(url + 'auth/login/', credentials)
                .then((response) => {
                    return Object.assign(credentials, response.data);
                })
                .catch((error) => { 
                    console.log("auth/login error", error); 
                    router.push('/login');
                    location.reload();
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
