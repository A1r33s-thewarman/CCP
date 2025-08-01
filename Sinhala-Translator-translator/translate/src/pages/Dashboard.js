import React, { useState, useEffect } from 'react';

import '../index.css';

const axios = require('axios');
var FormData = require('form-data');

function Dashboard(props) {

  const [upatt, setUPatt] = React.useState("");
  const [translated, settranslated] = React.useState("");
  const [english, setenglish] = React.useState("");


  function InputField () {
    let formData = new FormData();
formData.append('sentence', upatt);

axios({
  method: 'post',
  url: 'http://localhost:5000/sentence',
  data: formData,
  headers: { 'Content-Type': 'multipart/form-data' },
})
  .then(res => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res.data[0]['sinhala'])
    settranslated(res.data[0]['sinhala'])
    setenglish(res.data[0]['english'])
  })
  .catch(error => {
    console.error(error)
  })


  }
    return (
        <div className="dash" >
          <h2 style={{color: "white"}}>Let's translate that Text for you 😄</h2>
        <div class="row">
    <div class="column">
<div className="topset">
    <div className="center">
      <p class="point">English/Singlish</p>
      <textarea className="rounded" type="text" name="sande" value={upatt} onChange={(e) => setUPatt(e.target.value)}/> <br></br>
      <br></br>
      <button onClick={InputField} class="roudnbtn">Translate</button>
</div>
</div>

    </div>
    <div class="column" >

    <p class="point">English</p>

<textarea className="rounded" type="text" name="english" value={english} onChange={(e) => setenglish(e.target.value)}/>

<p class="point">Sinhala</p>
<textarea className="rounded" type="text" name="translated" value={translated} onChange={(e) => settranslated(e.target.value)}/>

    </div>

  </div>




        </div>

    );
}

export default Dashboard;
