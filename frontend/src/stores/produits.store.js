import { defineStore } from 'pinia'
import { useSnackBarStore } from '../stores/snackbar.store.js';
import axios from 'axios';
const apiUrl = 'http://localhost:8000/api/produit/';

const actions = {
    getNewProduit() {
        return {
            nom: "",
            prixHT: 0,
            poids: 0,
            reference: ""
        };
    },
    getProduit(id) {
        return this.products.find((element) => element.id == id);
    },
    async getProducts() {
        await axios.get(apiUrl).then((response) => {
            console.log("getProducts", response.data);
            this.products = response.data;
        });
    },
    async saveProduit(produit) {
        if (produit.id != undefined) {
            axios.put(apiUrl + produit.id + "/", produit).then((response) => {
                this.products.push(response.data);
                useSnackBarStore().setSnackBarState({ message: "Produit " + produit.nom + " sauvegardé", snackbarShow: true });
            });
        } else {
            axios.post(apiUrl, produit).then((response) => {
                this.products.push(response.data);
                useSnackBarStore().setSnackBarState({ message: "Produit " + produit.nom + " créé", snackbarShow: true });
            });
        }
    },
    async deleteProduit(produit) {
        axios.delete(apiUrl + produit.id + "/").then(() => {
            useSnackBarStore().setSnackBarState({ message: "Produit " + produit.nom + " supprimé", snackbarShow: true });
        });
    },
};

export const useProduitStore = defineStore('produit', {
    state: () => ({
        products: []
    }),
    actions: actions
})
