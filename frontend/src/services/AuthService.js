// src/services/AuthService.js
import axios from 'axios';
const url = 'http://localhost:8000/api/';

export default {
    login(credentials) {
        return axios
            .post(url + 'login_check', credentials)
            .then((response) => {
                let resp = Object.assign(credentials, response.data);
                return resp;
            });
    },
    signUp(credentials) {
        return axios
            .post(url + 'client/', credentials)
            .then(response => response.data);
    }
};