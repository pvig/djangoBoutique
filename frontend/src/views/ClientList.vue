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

    <v-row>
      <v-col cols="12">        
        <v-data-table :headers="headers" :items="listeClients" :items-per-page="10" class="elevation-1">
          <template v-slot:item="row">
            <tr>
              <td>
                {{ row.item.username }}
              </td>
              <td>
                {{ row.item.nom }}
              </td>
              <td>
                {{ row.item.prenom }}
              </td>
              <td>
                {{ row.item.email }}
              </td>
              <td>
                <v-layout justify-center>
                  <v-icon small class="mr-2" @click="editClient(row.item.id)">mdi-pencil</v-icon>
                  <v-icon small @click="dialogDeleteClient(row.item)">mdi-delete</v-icon>
                </v-layout>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>

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
import FicheClient from '../components/FicheClient.vue'
import SnackBar from '../components/SnackBar.vue'
import Progress from '../components/ProgressBar.vue'
import { useClientStore } from '../stores/clients.store.js';

export default {
  name: 'ClientList',
  components: {
    FicheClient,
    SnackBar,
    Progress
  },
  mounted() {
    this.refreshList();
  },
  data: () => ({
    isLoading: true,
    listeClients: [],
    editClientId: null,
    editNewClient: false,
    confirmDeleteClient: false,
    ClientToDelete: false,
    headers: [
      { title: 'Username', value: 'username', sortable: false, align: 'center' },
      { title: 'Nom', value: 'nom', sortable: false, align: 'center' },
      { title: 'Prenom', value: 'prenom', sortable: false, align: 'center' },
      { title: 'Email', value: 'email', sortable: false, align: 'center' },
      { title: 'Actions', value: 'actions', sortable: false, align: 'center' },
    ],
  }),
  methods: {
    refreshList: function() {
      useClientStore().getClients().then(() => {
        this.listeClients = useClientStore().clients;
        this.isLoading = false;
      });
    },
    editClient: function (id) {
      this.editClientId = id;
      this.editNewClient = false;
    },
    newClient: function () {
      this.editNewClient = true;
    },
    dialogDeleteClient: function (client) {
      this.ClientToDelete = client;
      this.confirmDeleteClient = true;
    },
    async deleteClient() {
      let clientToDelete = {...this.ClientToDelete};

      await useClientStore().deleteClient(clientToDelete);

      this.confirmDeleteClient = false;
      this.refreshList();
    },
    editDone: function () {
      this.editClientId = null;
      this.editNewClient = false;
    }
  }
}

</script>