import { defineStore } from 'pinia'
import { useSnackBarStore } from '../stores/snackbar.store.js';
import axios from 'axios';
const apiUrl = 'http://localhost:8000/api/produit/';

const actions = {
    getNewProduit() {
        return {
            nom: "",
            prixHT: null,
            poids: null,
            reference: ""
        };
    },
    getProduit(id) {
        return this.products.find((element) => element.id == id);
    },
    async getProducts() {
        await axios.get(apiUrl).then((response) => {
            this.products = response.data;
        });
    },
    async saveProduit(produit) {
        if (produit.id != undefined) {
            await axios.put(apiUrl + produit.id + "/", produit).then(() => {
                useSnackBarStore().setSnackBarState({ text: "Produit " + produit.nom + " sauvegardé" });
            });
        } else {
            await axios.post(apiUrl, produit).then((response) => {
                this.products.push(response.data);
                useSnackBarStore().setSnackBarState({ text: "Produit " + produit.nom + " créé" });
            });
        }
    },
    async deleteProduit(produit) {
        await axios.delete(apiUrl + produit.id + "/").then(() => {
            useSnackBarStore().setSnackBarState({ text: "Produit " + produit.nom + " supprimé" });
        });
    },
};

export const useProduitStore = defineStore('produit', {
    state: () => ({
        products: []
    }),
    actions: actions
})
