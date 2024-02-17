import { defineStore } from 'pinia'
import axios from 'axios';
import router from "../router";

const url = 'http://localhost:8000/';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        user: JSON.parse(localStorage.getItem('user')),
        returnUrl: null
    }),
    actions: {
        async login(credentials) {
            const user = await this.remoteLogin(credentials);
            this.user = user;
            localStorage.setItem('user', JSON.stringify(user));
            router.push(this.returnUrl || '/');
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
            router.push('/login');
        },
        remoteLogin(credentials) {
            console.log("remoteLogin", credentials);
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
        }
    }
  })
  