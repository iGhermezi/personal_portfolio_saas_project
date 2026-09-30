import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", {
  state: () => ({
    toast: {
      visible: false,
      type: "success",
      message: "",
    },

    loading: false,
  }),

  actions: {
    showToast(message, type = "success") {
      this.toast = {
        visible: true,
        type,
        message,
      };

      clearTimeout(this._toastTimer);

      this._toastTimer = setTimeout(() => {
        this.hideToast();
      }, 3500);
    },

    hideToast() {
      this.toast.visible = false;
    },

    setLoading(value) {
      this.loading = !!value;
    },
  },
});