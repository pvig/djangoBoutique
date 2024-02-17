<template>
    <v-snackbar
      v-model="snackbarShow"
      :timeout="snackbarTimeout"
      :color="snackbarColor"
    >
      {{ snackbarText }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="black"
          text
          v-bind="attrs"
          @click="snackbarShow = false"
        >
          <b>X</b>
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
        return useSnackBarStore().snackbarShow;
      },
      set: function (newValue) {
        useSnackBarStore().setSnackBarState(newValue);
      }
    },
    snackbarTimeout () {
      return useSnackBarStore().snackbarTimeout
    },
    snackbarText () {
      return useSnackBarStore().snackbarText
    },
    snackbarColor () {
      return useSnackBarStore().snackbarColor
    },
  },
  methods: {
  },
};
</script>

