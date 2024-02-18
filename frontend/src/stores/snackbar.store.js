import { defineStore } from 'pinia'

export const useSnackBarStore = defineStore('SnackBar', {
    state: () => ({
        show: false,
        text: "message",
        color: "#fff",
        timeout: 2000,
    }),
    actions: {
        getSnackBarState() {
            return this.show;
        },
        setSnackBarState(state) {
            this.show = true;
            this.text = state.text;
            this.color = state.color;
            this.timeout = state.timeout;
        },
        setShow(state) {
            this.show = state;
        }
    }
  })
  