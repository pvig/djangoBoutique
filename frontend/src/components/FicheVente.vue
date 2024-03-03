<template>
  <v-row justify="center">
    <v-dialog v-model="editing" persistent max-width="800">
      <v-card class="editBox text-lg-right">

        <div>
          <span>id : {{ this.localVente.id }}</span>
          <v-form ref="formVente" @submit.prevent="saveVente" id="vente-form">
            <v-container>

              <v-row>
                <v-col cols="11" md="11">
                  <v-text-field :model-value="localVente.numeroVente"
                    @input="update('numeroVente', $event.target.value)" label="Numero de vente" type="string"
                    class="mx-4" :rules="rules.required"></v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="11" md="11">
                  <v-autocomplete v-model="client" item-title="nom" item-value="id" :loading="loading" return-object 
                    :items="listeClients" :search-input="searchClient" class="mx-4" flat hide-no-data hide-details
                    label="Client"></v-autocomplete>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="11" md="11">
                  <v-text-field :model-value="localVente.dateVente" @input="update('dateVente', $event.target.value)"
                    label="Date" type="date" class="mx-4"></v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="11" md="11">
                  <v-text-field :model-value="prixProduitsHT" label="Total HT" type="number" step="0.01" readonly
                    class="mx-4" @input="update('prixProduitsHT', $event.target.value)"></v-text-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="11" md="11">
                  <v-autocomplete v-model="produit" item-title="nom" item-value="@id" :loading="loading" return-object
                    :items="listeProduits" :search-input="searchProduit" class="mx-4" flat hide-no-data hide-details
                    :label="labelProduit">
                  </v-autocomplete>
                </v-col>

                <v-col cols="1" md="1" class="d-flex flex-column">
                  <v-spacer></v-spacer>
                  <v-btn small bottom v-on:click="addProduit" v-show="produit && produit.id">
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </v-col>
              </v-row>

              <v-row>
                <v-col cols="11" md="11">
                  <v-toolbar dense color="grey lighten-5" flat>
                    <v-toolbar-title class="text-left">Produits</v-toolbar-title>
                  </v-toolbar>

                  <v-table dense>
                    <template v-slot:default>
                      <thead>
                        <tr>
                          <th class="text-left">
                            Nom
                          </th>
                          <th class="text-left">
                            Quantité
                          </th>
                          <th>
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="item in venteProduits" :key="item.id">
                          <td class="text-left">{{ item.produit.nom }}</td>
                          <td class="text-left">
                            <v-text-field :model-value="item.quantite" @change="updateQuantite(item, $event)"
                              type="number" min="1" class="mx-4" :rules="rules.required"></v-text-field>
                          </td>
                          <td class="text-left">
                            <v-btn plain @click="supprimeLigneVente(item)">
                              <v-icon>mdi-delete</v-icon>
                            </v-btn>
                          </td>
                        </tr>
                      </tbody>
                    </template>
                  </v-table>

                </v-col>
              </v-row>

            </v-container>
          </v-form>
        </div>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn depressed @click="closeMe()" :disabled="saving">
            Annuler
          </v-btn>
          <v-btn depressed type="submit" form="vente-form" :loading="saving">
            Sauvegarder
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-row>
</template>

<script>
import { useVenteStore } from '../stores/ventes.store.js';
import { useProduitStore } from '../stores/produits.store.js';
import { useClientStore } from '../stores/clients.store.js';
import useVuelidate from '@vuelidate/core'
import {
  required
} from '@vuelidate/validators'

export default {
  name: "ficheVente",
  props: ['editVenteId', 'editNewVente'],
  setup() {
    return { v$: useVuelidate() }
  },
  data: () => ({
    loading: false,
    editing: false,
    saving: false,
    localVente: {},
    prixProduitsHT: 0,
    rules: {},
    client: { nom: "" },
    venteProduits: [],
    rechercheClient: '',
    listeClients: [],
    labelClient: "Choisissez un client",
    produit: { nom: "" },
    rechercheProduit: '',
    listeProduits: [],
    labelProduit: "Ajouter un produit"
  }),
  mounted() {
    useClientStore().getClients().then(() => {
      this.listeClients = useClientStore().clients;
    })
    useProduitStore().getProducts().then(() => {
      this.listeProduits = useProduitStore().products;
    })
  },
  validations() {
    return {
      localVente: {
        numeroVente: { required },
        dateVente: { required },
      },
      client: { required },
    }
  },
  watch: {
    client(val) {
      if (!val) {
        this.labelClient = "Choisissez un client";
      } else {
        this.labelClient = "";
      }
    },
    produit(val) {
      if (!val) {
        this.labelProduit = "Ajouter un produit";
      } else {
        this.labelProduit = "";
      }
    },
    'editVenteId': function () {
      if (this.editVenteId) {
        this.editVente(this.editVenteId);
      }
    },
    'editNewVente': function () {
      if (this.editNewVente) {
        this.editVente();
        console.log("localVente", this.localVente);
      }
    },
  },
  computed: {
    searchClient: {
      get() {
        return this.rechercheClient
      },

      set(searchInput) {
        if (this.rechercheClient !== searchInput) {
          this.rechercheClient = searchInput;
        }
      }
    },
    searchProduit: {
      get() {
        return this.rechercheProduit
      },
      set(searchInput) {
        if (this.rechercheProduit !== searchInput) {
          this.rechercheProduit = searchInput;
        }
      }
    },
  },
  methods: {
    supprimeLigneVente(ligneSelected) {
      this.venteProduits = this.venteProduits.filter(ligne => ligne != ligneSelected);
      this.calcTotal();
    },
    addProduit() {
      if (this.produit && this.produit.id) {
        let existingIndex = this.venteProduits.findIndex(ligne => ligne.produit.id == this.produit.id);
        if (existingIndex >= 0) {
          this.venteProduits[existingIndex].quantite += 1;
        } else {
          let newLigneVente = {
            produit: this.produit,
            prixHT: this.produit.prixHT,
            quantite: 1
          }
          if (this.editVenteId) {
            newLigneVente.idVente = this.editVenteId;
          }
          this.venteProduits.push(newLigneVente);
        }
      }
      this.calcTotal();
    },
    calcTotal() {
      let total = 0;
      for (let index in this.venteProduits) {
        const ligne = this.venteProduits[index];
        total += parseFloat(ligne.prixHT) * parseInt(ligne.quantite);
      }
      this.prixProduitsHT = total;
    },
    validate() {
      this.v$.$validate()
      return !this.v$.$error;
    },
    updateQuantite(item, $event) {
      item.quantite = parseInt($event.target.value);
      this.calcTotal();
    },
    update(key, value, type) {
      if (type == "number") {
        value = parseFloat(value);
      }
      this.updateVenteAtribute({ ...this.value, key: key, value: value });
    },
    editVente(id) {
      if (id) {
        this.localVente = useVenteStore().ventes.find(element => element.id == id);
        this.venteProduits = this.localVente.lignesVente;
      } else {
        var now = new Date();
        this.localVente = {
          prixProduitsHT: 0,
          lignesVente: [],
          dateVente: now.toISOString().substring(0, 10),
        }
        console.log("localVente", this.localVente);
        this.venteProduits = [];
      }
      this.client = this.localVente.client;
      this.rules = {};
      this.editing = true;
      this.calcTotal();
    },
    updateVenteAtribute(val) {
      this.localVente[val.key] = val.value;
    },
    saveVente() {
      if (this.validate()) {
        this.localVente.prixProduitsHT = this.prixProduitsHT;
        this.localVente.prixProduitsTTC = this.prixProduitsHT * 1.2;
        this.localVente.client = this.client;
        this.localVente.lignesVente = this.venteProduits;
        this.saving = true;
        console.log("saveVente", this.localVente, this.client)
        this.$nextTick(() => {
          useVenteStore().saveVente(this.localVente).then(() => {
            this.closeMe();
          })
        });
      } else {
        console.log("pas valide")
      }
    },
    closeMe() {
      this.editing = false;
      this.saving = false;
      this.$emit('editDone', this.localVente)
    }
  },
};
</script>