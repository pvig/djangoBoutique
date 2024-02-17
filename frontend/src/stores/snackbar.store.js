import { defineStore } from 'pinia'

export const useSnackBarStore = defineStore('SnackBar', {
    state: () => ({
        snackbarShow: false,
        snackbarText: "",
        snackbarColor: "",
        snackbarTimeout: 2000,
    }),
    actions: {
        getSnackBarState() {
            return this.snackbarShow;
        },
        setSnackBarState(state) {
            this.snackbarShow = state;
        }
    }
  })
  