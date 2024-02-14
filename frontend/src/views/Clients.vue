<template>
  <div class="mx-auto max-width-dt">
    <v-progress-linear v-show="isLoading" indeterminate color="blue-grey"></v-progress-linear>

    <v-row class="tableHeader">
      <v-col cols="12" sm="6" md="8">
        <h1>Clients</h1>
      </v-col>

      <v-col cols="6" md="4" class="d-flex align-end">
        <v-spacer></v-spacer>
        <v-btn depressed @click="newClient()" class="ml-auto">
          Ajouter un client
        </v-btn>
      </v-col>
    </v-row>


    <v-data-table :headers="headers" :items="listeClients" :items-per-page="10" class="elevation-1">
      <template v-slot:item="row">
        <tr>
          <td>
            {{ row.item.nom }}
          </td>
          <td>
            <v-layout justify-center>
              <v-icon small class="mr-2" @click="editClient(row.item.id)">mdi-pencil</v-icon>
              <v-icon small @click="dialogDeleteClient(row.item.id)">mdi-delete</v-icon>
            </v-layout>
          </td>
        </tr>
      </template>
    </v-data-table>

    <FicheClient :editClientId="this.editClientId" :editNewClient="this.editNewClient" @editDone="editDone">
    </FicheClient>

    <v-dialog v-model="confirmDeleteClient" max-width="800">
      <v-card class="editBox">
        <v-card-actions>
          Supprimer ce client ?
          <v-spacer></v-spacer>
          <v-btn depressed @click="confirmDeleteClient = false">
            Annuler
          </v-btn>
          <v-btn depressed @click="deleteClient()">
            Supprimer
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <SnackBar />
    <Progress></Progress>
  </div>
</template>

<script>
import FicheClient from './components/FicheClient.vue'
import SnackBar from '../components/SnackBar.vue'
import Progress from '../components/Progress.vue'

export default {
  name: 'Clients',
  components: {
    FicheClient,
    SnackBar,
    Progress
  },
  mounted() {
    this.$store.dispatch('clients/getClients').then(() => {
      this.listeClients = this.$store.state.clients.all;
      this.isLoading = false;
    });
  },
  computed: {
  },
  data: () => ({
    isLoading: true,
    listeClients: [],
    editClientId: null,
    editNewClient: false,
    confirmDeleteClient: false,
    clientToDeleteId: false,
    headers: [
      { text: 'Client', value: 'nom', sortable: false, align: 'start' },
      { text: 'Actions', value: 'actions', sortable: false, align: 'center' },
    ],
  }),
  methods: {
    editClient: function (id) {
      this.editClientId = id;
    },
    newClient: function () {
      this.editNewClient = true;
    },
    dialogDeleteClient: function (id) {
      this.clientToDeleteId = id;
      this.confirmDeleteClient = true;
    },
    deleteClient: function () {
      this.$store.dispatch('clients/deleteClient', this.clientToDeleteId);
      this.confirmDeleteClient = false;
    },
    editDone: function (client) {
      this.editClientId = null;
      this.editNewClient = false;
    }
  }
}
</script>