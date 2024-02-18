import { defineStore } from 'pinia'
import axios from 'axios';
import router from "../router";

const url = 'http://localhost:8000/';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
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
                    this.user = null;
                    localStorage.removeItem('user');
                    router.push('/login');
                });
        },
        remoteLogin(credentials) {
            return axios
                .post(url + 'auth/login/', credentials)
                .then((response) => {
                    let resp = Object.assign(credentials, response.data);
                    return resp;
                });
        },
        signUp(credentials) {
            return axios
                .post(url + 'auth/register/', credentials)
                .then(response => response.data);
        },
        isLogged() {
            console.log("this.user", this.user);
            if(!this.user) {
                router.push('/login');
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
