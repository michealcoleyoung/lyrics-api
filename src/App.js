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
      <h1></h1>
      <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>

    </div>
  );
}

export default App;
