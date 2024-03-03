import { defineStore } from 'pinia'
import { useSnackBarStore } from '../stores/snackbar.store.js';
import axios from 'axios';
const apiUrl = 'http://localhost:8000/api/client/';

const actions = {
    async getClients() {
        await axios.get(apiUrl).then((response) => {
            this.clients = response.data;
        });
    },
    getClient(id) {
        return this.clients.find((element) => element.id == id);
    },
    async saveClient(client) {
        if (client.id != undefined) {
            await axios.put(apiUrl + client.id + "/", client).then(() => {
                useSnackBarStore().setSnackBarState({ text: "client " + client.nom + " sauvegardé" });
            });
        } else {
            await axios.post(apiUrl, client).then((response) => {
                this.clients.push(response.data);
                useSnackBarStore().setSnackBarState({ text: "client " + client.nom + " créé" });
            });
        }

    },
    async deleteClient(client) {
        await axios.delete(apiUrl + client.id + "/").then(() => {
            useSnackBarStore().setSnackBarState({ text: "client " + client.nom + " supprimé" });
        });
    },
};

export const useClientStore = defineStore('client', {
    state: () => ({
        clients: []
    }),
    actions: actions
})
