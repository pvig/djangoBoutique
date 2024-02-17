import { defineStore } from 'pinia'

export const useProgressBarStore = defineStore('ProgressBar', {
    state: () => ({
        progressShow:false,
    }),
    actions: {
        setProgressBarState(state) {
            this.progressShow = state;
        }
    }
  })
  