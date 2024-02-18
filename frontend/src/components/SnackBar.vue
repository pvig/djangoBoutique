<template>
    <v-snackbar
      v-model="snackbarShow"
      :timeout="snackbarTimeout"
      :color="snackbarColor"
    >
      {{ snackbarText }}

      <template v-slot:actions>
        <v-btn
          color="white"
          variant="text"
          @click="snackbarShow = false"
        >
          Ok
        </v-btn>
      </template>
    </v-snackbar>
</template>

<script>
import { useSnackBarStore } from '../stores/snackbar.store.js';

export default {
  computed: {
    snackbarShow: {
      get: function () {
        return useSnackBarStore().show;
      },
      set: function (newValue) {
        useSnackBarStore().setShow(newValue);
      }
    },
    snackbarTimeout () {
      return useSnackBarStore().timeout
    },
    snackbarText () {
      return useSnackBarStore().text
    },
    snackbarColor () {
      return useSnackBarStore().color
    },
  },
  methods: {
  },
};
</script>

