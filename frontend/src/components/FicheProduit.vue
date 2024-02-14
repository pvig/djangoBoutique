<template>
  <div justify="center">

      <v-card class="editBox" fixed>

        <div class="card">
          <span>id : {{ this.localProduit.id || 'Nouveau produit'}}</span>
          <v-form ref="form" @submit.prevent="validate" id="produit-form">

                  <v-text-field :value="localProduit.nom" @input="update('nom', $event)" label="Nom"
                    :rules="rules.required"></v-text-field>
                  <v-text-field :value="localProduit.prixHT" @input="update('prixHT', $event, 'number')" label="prixHT"
                    type="number" step="0.01" :rules="rules.prix"></v-text-field>
                  <v-text-field :value="localProduit.poids" @input="update('poids', $event, 'number')" label="Poids">
                  </v-text-field>
                  <v-text-field :value="localProduit.reference" @input="update('reference', $event)" label="Reference">
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
export default {
  name: "ficheProduit",
  props: ['editProduitId', 'editNewProduit'],
  data: () => ({
    editing: false,
    saving: false,
    localProduit: {},
    rules: {},
  }),
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
      this.rules = {
        prix: [v => (v && (parseFloat(v) == v)) || 'Le prix doit être un chiffre'],
        required: [v => !!v || 'Required']
      }
      this.$nextTick(() => {
        if (this.$refs.form.validate()) {
          this.saveProduit();
        }
      });
    },
    update(key, value, type) {
      if (type == "number") {
        value = parseFloat(value);
      }
      this.updateProduitAtribute({ ...this.value, key: key, value: value });
    },
    editProduit: function (id) {
      if (id && typeof this.$store.state.produits.all != 'undefined') {
        this.localProduit = { ...this.$store.state.produits.all.find(element => element.id == id) };
      } else {
        this.localProduit = {
          nom: ""
        }
      }
      this.rules = {};
      this.editing = true;
    },
    updateProduitAtribute(val) {
      this.localProduit[val.key] = val.value;
    },
    saveProduit(e) {
      this.saving = true;
      this.$nextTick(() => {
        this.$store.dispatch('produits/saveProduit', this.localProduit).then(() => {
          this.editDone();
        })
      });
    },
    editDone() {
      this.editing = false;
      this.saving = false;
      this.$emit('editDone', this.localProduit)
    }
  },
};
</script>