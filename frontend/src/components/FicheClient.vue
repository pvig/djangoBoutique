<template>
  <v-row justify="center">
    <v-dialog v-model="editing" persistent max-width="800">
      <v-card class="editBox">

        <div>
          <span>id : {{ this.localClient.id }}</span>
          <v-form ref="form" @submit.prevent="validate" @submit="saveClient" id="client-form">
            <v-container>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field :model-value="localClient.username" @input="update('username', $event.target.value)" label="Username"></v-text-field>
                  <v-text-field :model-value="localClient.nom" @input="update('nom', $event.target.value)" label="Nom"></v-text-field>
                  <v-text-field :model-value="localClient.prenom" @input="update('prenom', $event.target.value)" label="Prenom"></v-text-field>
                  <v-text-field :model-value="localClient.email" @input="update('email', $event.target.value)" label="Email"></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </div>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn depressed @click="editDone()" :disabled="saving">
            Annuler
          </v-btn>
          <v-btn depressed type="submit" form="client-form" :loading="saving">
            Sauvegarder
          </v-btn>
        </v-card-actions>

      </v-card>
    </v-dialog>

  </v-row>

</template>

<script>
import { useClientStore } from '../stores/clients.store.js';
import useVuelidate from '@vuelidate/core'
import {
  required
} from '@vuelidate/validators'

export default {
  name: "ficheClient",
  props: ['editClientId', 'editNewClient'],
  setup() {
    return { v$: useVuelidate() }
  },
  data: () => ({
    editing: false,
    saving: false,
    localClient: {},
    rules: {},
  }),
  validations() {
    return {
      localClient: {
        nom: { required },
        username: { required },
      }
    }
  },
  watch: {
    'editClientId': function () {
      if (this.editClientId) {
        this.editClient(this.editClientId);
      }
    },
    'editNewClient': function () {
      if (this.editNewClient) {
        this.editClient();
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
      this.updateClientAtribute({ key: key, value: value });
    },
    editClient: function (id) {
      if (id && typeof useClientStore().clients != 'undefined') {
        this.localClient = useClientStore().getClient(id);
      } else {
        this.localClient = {
          username: ""
        }
      }
      this.editing = true;
    },
    updateClientAtribute(val) {
      this.localClient[val.key] = val.value;
    },
    saveClient() {
      if (this.validate()) {
        console.log("saving")
        this.saving = true;
        this.$nextTick(() => {
          useClientStore().saveClient(this.localClient).then(() => {
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