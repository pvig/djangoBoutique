// src/services/AuthService.js
import axios from 'axios';
const url = 'http://localhost:8000/';

export default {
    login(credentials) {
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
};