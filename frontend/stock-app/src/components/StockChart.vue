<template>
  <div>
    <div class="stock-info">
      <h1 :class="{ highlight: highlight }">{{ stockCode }}</h1>
    </div>
    <div ref="chart" style="width: 100%; height: 400px;"></div>
    <div class="controls">
      <input v-model="inputStockCode" placeholder="Enter stock code" />
      <button @click="fetchStockData">Get Stock Data</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
  name: 'StockChart',
  data() {
    return {
      stockCode: 'sh600519',
      inputStockCode: 'sh600519',
      stockData: [],
      highlight: false,
      chart: null,
    };
  },
  mounted() {
    this.initChart();
    this.fetchStockData();
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.chart);
    },
    async fetchStockData() {
      this.stockCode = this.inputStockCode;
      try {
        const response = await axios.get(`http://localhost:8000/stock/${this.stockCode}`);
        this.stockData = response.data.stock_data;
        this.highlight = response.data.highlight;
        this.updateChart();
      } catch (error) {
        console.error('Error fetching stock data:', error);
      }
    },
    updateChart() {
      const dates = this.stockData.map(item => item.day || item.time);
      const data = this.stockData.map(item => [item.open, item.close, item.low, item.high]);

      const option = {
        title: {
          text: `${this.stockCode} K-line Chart`,
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
          },
        },
        xAxis: {
          data: dates,
        },
        yAxis: {},
        series: [
          {
            type: 'candlestick',
            data: data,
          },
        ],
      };
      this.chart.setOption(option);
    },
  },
};
</script>

<style scoped>
.stock-info {
  text-align: center;
  margin-bottom: 20px;
}
.highlight {
  color: red;
}
.controls {
  text-align: center;
  margin-top: 20px;
}
</style>
