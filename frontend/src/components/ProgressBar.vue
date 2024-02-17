<template>
    <v-progress-linear
      v-show="progressShow"
      indeterminate
      color="green darken-2"
      class="absolute-top"
    ></v-progress-linear>
</template>
<script>
import { useProgressBarStore } from '../stores/progressbar.store.js';

export default {
  computed: {
    progressShow: {
      get: function () {
        return useProgressBarStore().progressShow;
      },
      set: function (newValue) {
        useProgressBarStore().setProgressBarState(newValue);
      }
    }
  },
};
</script>