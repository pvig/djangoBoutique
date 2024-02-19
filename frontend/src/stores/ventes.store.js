import { defineStore } from 'pinia'
import { useSnackBarStore } from '../stores/snackbar.store.js';
import axios from 'axios';
const apiUrl = 'http://localhost:8000/api/vente/';

const actions = {
    async getVentes() {
        await axios.get(apiUrl).then((response) => {
            this.ventes = response.data;
            console.log("this.ventes", this.ventes)
        });
    },
    getVente(id) {
        return this.ventes.find((element) => element.id == id);
    },
    async saveVente(vente) {
        if (vente.id != undefined) {
            await axios.put(apiUrl + vente.id + "/", vente).then(() => {
                useSnackBarStore().setSnackBarState({ text: "vente " + vente.nom + " sauvegardé" });
            });
        } else {
            await axios.post(apiUrl, vente).then((response) => {
                this.ventes.push(response.data);
                useSnackBarStore().setSnackBarState({ text: "vente " + vente.nom + " créé" });
            });
        }

    },
    async deleteVente(vente) {
        await axios.delete(apiUrl + vente.id + "/").then(() => {
            useSnackBarStore().setSnackBarState({ text: "vente " + vente.nom + " supprimé" });
        });
    },
};

export const useVenteStore = defineStore('vente', {
    state: () => ({
        ventes: []
    }),
    actions: actions
})
