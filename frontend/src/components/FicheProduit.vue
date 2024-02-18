<template>
  <div justify="center">

    <v-card class="editBox" fixed>

      <div class="card">
        <span>id : {{ this.localProduit.id || 'Nouveau produit' }}</span>
        <v-form ref="form" @submit.prevent="validate" @submit="saveProduit" id="produit-form">

          <v-text-field :model-value="localProduit.nom" @input="update('nom', $event.target.value)"
            label="Nom"></v-text-field>
          <v-text-field :model-value="localProduit.prixHT" @input="update('prixHT', $event.target.value, 'number')"
            label="prixHT" type="number" step="0.01"></v-text-field>
          <v-text-field :model-value="localProduit.poids" @input="update('poids', $event.target.value, 'number')"
            label="Poids">
          </v-text-field>
          <v-text-field :model-value="localProduit.reference" @input="update('reference', $event.target.value)"
            label="Reference">
          </v-text-field>

        </v-form>
      </div>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn depressed type="submit" form="produit-form" :loading="saving" :disabled="!editing">
          Sauvegarder
        </v-btn>
      </v-card-actions>
    </v-card>


  </div>
</template>

<script>
import { useProduitStore } from '../stores/produits.store.js';
import useVuelidate from '@vuelidate/core'
import {
  required,
  decimal
} from '@vuelidate/validators'

export default {
  name: "ficheProduit",
  props: ['editProduitId', 'editNewProduit'],
  setup() {
    return { v$: useVuelidate() }
  },
  data: () => ({
    editing: true,
    saving: false,
    localProduit: useProduitStore().getNewProduit(),
  }),
  validations() {
    return {
      localProduit: {
        nom: { required },
        reference: { required },
        prixHT: { required, decimal },
        poids: { required, decimal },
      }
    }
  },
  watch: {
    'editProduitId': function () {
      if (this.editProduitId) {
        this.editProduit(this.editProduitId);
      }
    },
    'editNewProduit': function () {
      if (this.editNewProduit) {
        this.editProduit();
      }
    },
  },
  methods: {
    validate() {
      this.v$.$validate()
      return !this.v$.$error;
    },
    update(key, value, type) {
      if (type == "number") {
        value = parseFloat(value);
      }
      this.updateProduitAtribute({ key: key, value: value });
    },
    editProduit: function (id) {
      if (id && typeof useProduitStore().products != 'undefined') {
        this.localProduit = useProduitStore().getProduit(id);
      } else {
        this.localProduit = {
          nom: ""
        }
      }
      console.log("this.localProduit", this.localProduit)
      this.editing = true;
    },
    updateProduitAtribute(val) {
      this.localProduit[val.key] = val.value;
    },
    saveProduit() {
      if (this.validate()) {
        console.log("saving")
        this.saving = true;
        this.$nextTick(() => {
          useProduitStore().saveProduit(this.localProduit).then(() => {
            this.editDone();
          })
        });
      } else {
        console.log("pas valide")
      }
    },
    editDone() {
      this.editing = false;
      this.saving = false;
      this.$emit('editDone', this.localProduit)
    }
  },
};
</script>