import React  from 'react';
import { Bar } from 'react-chartjs-2';


const Chart = ({ data : { infos} }) => {
  if (!infos) {
    return 'Chargement...';
  }
  console.log(infos)
  return (
     
      <Bar
        data={{
          labels: ['Infected', 'Recovered', 'Active', 'Deaths'],
          datasets: [
            {
              label: 'People',
              backgroundColor: ['rgba(0, 0, 255, 0.5)', 'rgba(0, 255, 0, 0.5)', 'rgba(255, 153, 0, 0.575)', 'rgba(255, 0, 0, 0.5)'],
              data: [infos.totalCases, infos.totalRecovered, infos.seriousCritical, infos.totalDeaths],
            },
          ],
        }}
        options={{
          legend: { display: false },
          title: { display: true, text: ` ` },
        }}
      />
     )


};

export default Chart;
