import logo from './logo.svg';
import axios from 'axios';
import { getLyrics, getSong } from 'genius-lyrics-api';
import './App.css';

function App() {

  const options = {
    apiKey: '154904640fmsh615882c14b253d1p1b934cjsnab983c8da167',
    title: 'Blinding Lights',
    artist: 'The Weeknd',
    optimizeQuery: true
  };
  
  getLyrics(options).then((lyrics) => console.log(lyrics));
  
  getSong(options).then((song) =>
    console.log(`
    ${song.id}
    ${song.title}
    ${song.url}
    ${song.albumArt}
    ${song.lyrics}`)
  );


  return (
    <div className="App">
      <input type="text"  placeholder={'Artist'}/><br></br><br />
      <input type="text"  placeholder={'Song'}/>
      <h1></h1>
    </div>
  );
}

export default App;
