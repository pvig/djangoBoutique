import { defineStore } from 'pinia'
import { useSnackBarStore } from '../stores/snackbar.store.js';
import axios from 'axios';
const apiUrl = 'http://localhost:8000/api/vente/';

const actions = {
    async getVentes() {
        await axios.get(apiUrl).then((response) => {
            this.ventes = response.data;
        });
    },
    getVente(id) {
        return this.ventes.find((element) => element.id == id);
    },
    async saveVente(_vente) {
        var vente = structuredClone(_vente);

        // post id only
        vente.client = vente.client.id;

        for (var rr in vente.lignesVente) {
            vente.lignesVente[rr]["produit"] = vente.lignesVente[rr]["produit"].id
        }

        if (vente.id != undefined) {
            await axios.put(apiUrl + vente.id + "/", vente).then(() => {
                useSnackBarStore().setSnackBarState({ text: "vente " + vente.numeroVente + " sauvegardé" });
            });
        } else {
            await axios.post(apiUrl, vente).then((response) => {
                this.ventes.push(response.data);
                useSnackBarStore().setSnackBarState({ text: "vente " + vente.numeroVente + " créé" });
            });
        }

    },
    async deleteVente(venteId) {
        await axios.delete(apiUrl + venteId + "/").then(() => {
            useSnackBarStore().setSnackBarState({ text: "vente " + venteId + " supprimé" });
        });
    },
};

export const useVenteStore = defineStore('vente', {
    state: () => ({
        ventes: []
    }),
    actions: actions
})
