import React, { useState, useEffect } from 'react';

import '../index.css';

const axios = require('axios');
var FormData = require('form-data');

function Developer(props) {

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
        <div class="row">
    <div className="center">
      <p class="pointa">Write to Developers 🧐</p>
      <textarea className="roundeda" type="text" name="sande" value={upatt} onChange={(e) => setUPatt(e.target.value)}/><br></br>
      <br></br>
      <button onClick={InputField} class="roudnbtn">Submit</button>

    </div>
    <div class="column" >



    </div>

  </div>




        </div>

    );
}

export default Developer;
