<template>
  <div class="mx-auto max-width-dt">
    <v-progress-linear v-show="isLoading" indeterminate color="blue-grey"></v-progress-linear>

    <v-row class="tableHeader">
      <v-col cols="12" sm="6" md="8">
        <h1>Ventes</h1>
      </v-col>
      <v-col cols="6" md="4" class="d-flex align-end">
        <v-spacer></v-spacer>
        <v-btn depressed @click="newVente()" class="ml-auto">
          Ajouter une vente
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-data-table :headers="headers" :items="listeVentes" :items-per-page="10" class="elevation-1">
          <template v-slot:item="row">
            <tr>
              <td>{{ row.item.numeroVente }}</td>
              <td>
                <v-layout justify-center>
                  <v-icon small class="mr-2" @click="editVente(row.item.id)">mdi-pencil</v-icon>
                  <v-icon small @click="dialogDeleteVente(row.item.id)">mdi-delete</v-icon>
                </v-layout>
              </td>
            </tr>
          </template>
        </v-data-table>

        <FicheVente :editVenteId="this.editVenteId" :editNewVente="this.editNewVente" @editDone="editDone"></FicheVente>
      </v-col>
    </v-row>

    <v-dialog v-model="confirmDeleteVente" max-width="800">
      <v-card class="editBox">
        <v-card-actions>
          Supprimer cette vente ?
          <v-spacer></v-spacer>
          <v-btn depressed @click="confirmDeleteVente = false">
            Annuler
          </v-btn>
          <v-btn depressed @click="deleteVente()">
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
import FicheVente from '../components/FicheVente.vue'
import SnackBar from '../components/SnackBar.vue'
import Progress from '../components/ProgressBar.vue'
import { useVenteStore } from '../stores/ventes.store.js';


export default {
  name: 'VenteList',
  components: {
    FicheVente,
    SnackBar,
    Progress
  },
  mounted() {
    this.refreshList();
  },
  computed: {
  },
  data: () => ({
    isLoading: true,
    listeVentes: [],
    editVenteId: null,
    editNewVente: false,
    confirmDeleteVente: false,
    venteToDeleteId: false,
    headers: [
      { text: 'Vente', value: 'id', sortable: false, align: 'start' },
      { text: 'Actions', value: 'actions', sortable: false, align: 'center' },
    ],
  }),
  methods: {
    refreshList: function () {
      useVenteStore().getVentes().then(() => {
        this.listeVentes = useVenteStore().ventes;
        this.isLoading = false;
        console.log("this.listeVentes", this.listeVentes);
      });
    },
    editVente: function (id) {
      this.editVenteId = id;
    },
    newVente: function () {
      this.editNewVente = true;
    },
    dialogDeleteVente: function (id) {
      this.venteToDeleteId = id;
      this.confirmDeleteVente = true;
    },
    async deleteVente() {
      await useVenteStore().deleteVente(this.venteToDeleteId);
      this.confirmDeleteProduit = false;
      this.refreshList();
    },
    editDone: function () {
      this.editVenteId = null;
      this.editNewVente = false;
    }
  }
}
</script>
