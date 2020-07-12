import React from 'react';

import { Cards, CountryPicker, Chart } from './components';
import { fetchData } from './api/';
import styles from './App.module.css';

import 'bootstrap/dist/css/bootstrap.min.css';
class App extends React.Component {
  state = {
    data: {},
  }

  async componentDidMount() {
    const data = await fetchData("World");
    this.setState({ data });
  }

  handleCountryChange = async (country) => {
    const data = await fetchData(country);

    this.setState({ data });
  }

  render() {
    const { data } = this.state;

    return (
      <div className={styles.container}>
        <Cards data={data} />
        <h3>select a country :</h3>
        <CountryPicker handleCountryChange={this.handleCountryChange} />
        <Chart data={data} /> 
      </div>
    );
  }
}

export default App;