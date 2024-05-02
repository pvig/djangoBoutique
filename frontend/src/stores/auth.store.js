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
            const response = await this.remoteLogin(credentials);

            if (response.user && response.access_token) {
                this.setSession(response);
                // homepage
                router.push('/');
            }
        },
        async refreshAccessToken() {
            var localUser = localStorage.getItem('user');

            if (localUser) {
                localUser = JSON.parse(localUser);
                if (localUser.access) {
                    const user = await this.remoteRefresh({ refresh: localUser.refreshToken });
                    if (user && user.access) {
                        this.setSession(user);
                        return true;
                    }
                }
                this.clearSession();
            }
            return false;
        },
        setSession(response) {
            this.user = response.user;
            localStorage.setItem('user', JSON.stringify(this.user));
            localStorage.setItem("accessToken", response.access_token);
            localStorage.setItem("refreshToken", response.refresh_token);
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
            localStorage.removeItem('user');
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
        },
        remoteLogin(credentials) {
            return axios
                .post(url + 'api/v1/auth/login/', credentials)
                .then((response) => {
                    return Object.assign(credentials, response.data);
                })
                .catch((error) => {
                    if (error.response) {
                        useSnackBarStore().setSnackBarState({ text: error.response.data.detail });
                    }
                });
        },
        remoteRefresh(refresh) {
            return axios
                .post(url + 'api/v1/auth/login/refresh/', refresh)
                .then((response) => {
                    return Object.assign(refresh, response.data);
                })
                .catch((error) => {
                    if (error.response) {
                        useSnackBarStore().setSnackBarState({ text: error.response.data.detail });
                    }
                });
        },
        signUp(credentials) {
            return axios
                .post(url + 'api/v1/auth/registration/', credentials)
                .then((response) => {
                    console.log("response", response);
                    useSnackBarStore().setSnackBarState({ text: response.data.detail });
                })
                .catch((error) => { console.log("auth/register error", error); });
        },
        isLogged() {
            if (!this.user) {
                return false;
            } else {
                return true;
            }
        }
    }
})
