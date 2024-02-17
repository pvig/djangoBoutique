<template>
  <div class="mx-auto max-width-dt">
    <v-row>
      <v-col>
        <v-card max-width="1200">
          <v-progress-linear v-show="isLoading" indeterminate color="brown"></v-progress-linear>
          <apexchart type="bar" height="320" :options="graph1Options" :series="graph1series"></apexchart>
        </v-card>
        <v-card max-width="1200">
          <apexchart type="area" height="200" :options="graph2Optionsb" :series="graph2series"></apexchart>
          <apexchart type="bar" height="200" :options="graph2Options" :series="graph2series"></apexchart>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  props: {},
  data: () => ({
    isLoading: true,
    graph1Options: {
      chart: {
        type: 'bar',
        stacked: true
      },
      plotOptions: {
        bar: {
          borderRadius: 10,
        }
      },
      dataLabels: {
        enabled: true,
      },
      xaxis: {
        categories: [],
        position: 'top',
        axisBorder: {
          show: true
        },
        axisTicks: {
          show: true
        },
        crosshairs: {
          fill: {
            type: 'gradient',
            gradient: {
              colorFrom: '#D8E3F0',
              colorTo: '#BED1E6',
              stops: [0, 100],
              opacityFrom: 0.4,
              opacityTo: 0.5,
            }
          }
        },
        tooltip: {
          enabled: true,
        }
      },
      yaxis: {
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: true,
        },
        labels: {
          show: true,
          formatter: function (val) {
            return parseInt(val) + " ventes";
          }
        }
      },
      title: {
        text: 'Distribution des paniers',
        floating: false,
        offsetY: 0,
        align: 'left',
        style: {
          fontSize: '20px',
          color: '#444'
        }
      }
    },
    graph2Optionsb: {
      chart: {
        id: "chart2area",
        type: "area",
        height: 230,
        foreColor: "#ccc",
        toolbar: {
          autoSelected: "pan",
          show: false
        }
      },
      colors: ["#00BAEC"],
      stroke: {
        width: 3
      },
      grid: {
        borderColor: "#555",
        clipMarkers: false,
        yaxis: {
          lines: {
            show: false
          }
        }
      },
      dataLabels: {
        enabled: false
      },
      fill: {
        gradient: {
          enabled: true,
          opacityFrom: 0.55,
          opacityTo: 0
        }
      },
      markers: {
        size: 2,
        colors: ["#000524"],
        strokeColor: "#00BAEC",
        strokeWidth: 3
      },
      tooltip: {
        theme: "dark"
      },
      xaxis: {
        type: "datetime"
      },
      yaxis: {
        min: 0,
        tickAmount: 4
      },
      title: {
        text: 'Ventes',
        floating: false,
        offsetY: 0,
        align: 'left',
        style: {
          fontSize: '20px',
          color: '#444'
        }
      }
    },
    graph2Options: {
      chart: {
        height: 350,
        type: 'bar',
        brush: {
          target: "chart2area",
          enabled: true
        },
        selection: {
          enabled: true,
          fill: {
            color: "#fff",
            opacity: 0.4
          },
          xaxis: {
            min: new Date('01 Jan 2022').getTime(),
            max: new Date('01 Jun 2022').getTime()
          }
        },
      },
      dataLabels: {
        enabled: false,
      },
      xaxis: {
        type: 'datetime',

      },
      yaxis: {
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: true,
        },
        labels: {
          show: true,
        }
      }
    },
    graph1series: [],
    graph2series: [],
  }),
  async created() {
    this.$store.dispatch('ventes/getVentes').then(() => {
      //-------------------       charts preparation        -------------------
      let totalVentesAn = {};
      let graph1Values1 = [];
      let graph1Values2 = [];
      let graph1Values3 = [];
      let graph2Values = [];
      let ventesMensuelles = [];
      //-------------------       ventes list processing        -------------------
      for (let nn in this.$store.state.ventes.all) {
        let vente = this.$store.state.ventes.all[nn];
        let dateVente = vente.dateVente;
        let numProduits = vente.lignesVente.length;
        //-------------------
        let d = new Date(dateVente);
        let year = d.getFullYear().toString();
        let firstDayOfMonth = new Date(d.getFullYear(), d.getMonth(), 2);
        let monthStamp = firstDayOfMonth.getTime();
        //------------------- chart 1
        if (!totalVentesAn[year]) totalVentesAn[year] = { ventesCateg1: 0, ventesCateg2: 0, ventesCateg3: 0 };

        if (numProduits < 5)
          totalVentesAn[year].ventesCateg1++;
        else if (numProduits < 10)
          totalVentesAn[year].ventesCateg2++;
        else
          totalVentesAn[year].ventesCateg3++;
        //------------------- chart 2
        if (!ventesMensuelles[monthStamp]) ventesMensuelles[monthStamp] = { ventes: 0, date: monthStamp };
        ventesMensuelles[monthStamp].ventes += 1;
      }
      //------------------- graph1 chart
      for (const [key, value] of Object.entries(totalVentesAn)) {
        this.graph1Options.xaxis.categories.push(key);
        graph1Values1.push(value.ventesCateg1);
        graph1Values2.push(value.ventesCateg2);
        graph1Values3.push(value.ventesCateg3);
      }
      this.graph1series.push({
        name: '< 5 produits',
        data: graph1Values1
      });
      this.graph1series.push({
        name: '5 <= produits < 10 ',
        data: graph1Values2
      });
      this.graph1series.push({
        name: '>= 10 produits',
        data: graph1Values3
      });
      //------------------- graph2 chart
      let ventesKeys = Object.keys(ventesMensuelles);
      ventesKeys.sort();
      for (let index of ventesKeys) {
        let mois = ventesMensuelles[index];
        graph2Values.push([mois.date, mois.ventes]);
      }
      this.graph2series.push({
        name: 'ventes',
        data: graph2Values
      });

      this.isLoading = false;
    });
  },
  methods: {}
}
</script>
