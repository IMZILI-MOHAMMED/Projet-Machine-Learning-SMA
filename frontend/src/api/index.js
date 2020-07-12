import axios from 'axios';

const url = 'http://127.0.0.1:8000/countries/World';

export const fetchData = async (country) => {
  let changeableUrl = url;

  if (country) {
    changeableUrl = `http://127.0.0.1:8000/countries/${country}`;
 }

  try {
    const { data: { infos, lastUpdate } } = await axios.get(changeableUrl);

    return { infos, lastUpdate };
  } catch (error) {
    return error;
  }
};

export const fetchCountries = async () => {
  try {
    const { data: { countries } } = await axios.get(`http://127.0.0.1:8000/countries`);

    return countries.map((country) => country.name);
  } catch (error) {
    return error;
  }
};
