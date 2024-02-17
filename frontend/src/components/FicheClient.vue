<template>
  <v-row justify="center">
    <v-dialog v-model="editing" persistent max-width="800">
      <v-card class="editBox">

        <div class="card">
          <span>id : {{ this.localClient.id }}</span>
          <v-form ref="form" @submit.prevent="validate" id="client-form">
            <v-container>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field :model-value="localClient.nom" @input="update('nom', $event)" label="Nom"
                    :rules="rules.required"></v-text-field>
                  <v-text-field :model-value="localClient.prenom" @input="update('prenom', $event)" label="Prenom"
                    :rules="rules.required"></v-text-field>
                  <v-text-field :model-value="localClient.email" @input="update('email', $event)" label="Email"
                    :rules="rules.email"></v-text-field>
                  <v-text-field :model-value="localClient.dateCommande1 | formatDate" @input="update('dateCommande1', $event)"
                    label="Date de première commande" type="datetime-local"></v-text-field>
                  <v-text-field :model-value="localClient.dateLastCommande | formatDate"
                    @input="update('dateLastCommande', $event)" label="Date de la dernière commande"
                    type="datetime-local"></v-text-field>
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
          <v-btn depressed type="submit" form="client-form" :loading="saving">
            Sauvegarder
          </v-btn>
        </v-card-actions>

      </v-card>
    </v-dialog>

  </v-row>

</template>

<script>

export default {
  name: "ficheClient",
  props: ['editClientId', 'editNewClient'],
  data: () => ({
    editing: false,
    saving: false,
    localClient: {},
    rules: {},
  }),
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
      this.rules = {
        email: [v => !!v || 'Required'],
        required: [v => !!v || 'Required']
      }
      this.$nextTick(() => {
        if (this.$refs.form.validate()) {
          this.saveClient();
        }
      });
    },
    update(key, value, type) {
      if (type == "number") {
        value = parseFloat(value);
      }
      this.updateClientAtribute({ ...this.value, key: key, value: value });
    },
    editClient: function (id) {
      if (id && typeof this.$store.state.clients.all != 'undefined') {
        this.localClient = { ...this.$store.state.clients.all.find(element => element.id == id) };
      } else {
        this.localClient = {
          nom: ""
        }
      }
      this.rules = {};
      this.editing = true;
    },
    updateClientAtribute(val) {
      this.localClient[val.key] = val.value;
    },
    saveClient(e) {
      this.saving = true;
      this.$nextTick(() => {
        this.$store.dispatch('clients/saveClient', this.localClient).then(() => {
          this.closeMe();
        });
      });
    },
    closeMe() {
      this.editing = false;
      this.saving = false;
      this.$emit('editDone', this.localClient)
    }
  },
};
</script>