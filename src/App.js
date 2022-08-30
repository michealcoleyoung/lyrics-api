import logo from './logo.svg';
// import axios from 'axios';
import { getLyrics, getSong } from 'genius-lyrics-api';
import './App.css';
import { getValue } from '@testing-library/user-event/dist/utils';

function App() {
  const axios = require("axios");

  const options = {
    method: 'POST',
    url: 'https://lyrics-search.p.rapidapi.com/search/lyrics',
    headers: {
      'content-type': 'application/json',
      'X-RapidAPI-Key': '154904640fmsh615882c14b253d1p1b934cjsnab983c8da167',
      'X-RapidAPI-Host': 'lyrics-search.p.rapidapi.com'
    },
    data: '{"searchTerm":"wisconsin death trip"}'
  };
  
  axios.request(options).then(function (response) {
    console.log(response.data);
  }).catch(function (error) {
    console.error(error);
  });
  


  return (
    <div className="App">

      <h1>Lyrics Search</h1>
      {/* <input type="text"  placeholder={'Artist'}/><br></br><br /> */}
      <input type="text"  placeholder={'Song'}/><br></br><br />
      <button>SEARCH</button>
      <p></p>

    </div>
  );
}

export default App;
