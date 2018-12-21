// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
var endpoint = "/api/google_trend/";

$.ajax({
  method: "GET",
  url: endpoint,
  success: function(data){
    console.log(data);
    var dates = [];
    // insts = interest
    var insts = [];
    var keys = Object.keys(data[0]);
    var kw = keys[1];
    console.log(kw);
    for (i in data) {
      dates.push(moment(data[i]["date"]).format("YYYY/MM/DD"));
      insts.push(data[i][kw]);
    }
    var ctx = document.getElementById("myAreaChart").getContext('2d');
    var myLineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: dates,
        datasets: [{
          label: "Sessions",
          lineTension: 0.3,
          backgroundColor: "rgba(2,117,216,0.2)",
          borderColor: "rgba(2,117,216,1)",
          pointRadius: 3,
          pointBackgroundColor: "rgba(2,117,216,1)",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: insts,
        }],
      },
      options: {
        title: {
          display: true,
          text: kw
        },
        scales: {
          xAxes: [{
            time: {
              unit: 'date'
            },
            gridLines: {
              display: false
            },
            ticks: {
              maxTicksLimit: 7
            }
          }],
          yAxes: [{
            ticks: {
              min: 0,
              max: 100,
              maxTicksLimit: 5
            },
            gridLines: {
              color: "rgba(0, 0, 0, .125)",
            }
          }],
        },
        legend: {
          display: false
        }
      }
    });
  },
  error: function(error){
    console.log(error);
  }
});
