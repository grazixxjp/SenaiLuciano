import logo from './logo.svg';
import axios from 'axios';
import { useEffect, useState } from 'react';
import './App.css';

function App() {

  useEffect(() => {
    console.log(cep.length)
    console.log('usuario digitou')
  },[cep])

  useEffect(() => {
      if (cep.length == 8){
          consumirAPI();
      }
      else{
        limpartudo();
      }
  }, [cep])

  const limpartudo = () => {
    setLogradouro('')
    setBairro("")
  }

  const consumirAPI = () => {
      axios.get(`https://viacep.com.br/ws/${cep}/json/`)
      .then((res) => {
          //logradouro e o bairro
          //criar os inputs para cada atributo que compõe 
          //o endereço retornado pea api:
          //logradouro - bairro,cidade, uf, numero
          //atribuir o valor presente no 'data' para cada
          //input

          //extra - ao apagar completamente o CEP, voce deve
          //limpar os inputs

          setLogradouro(res.data.logradouro + ' ' + res.data.bairro)
          console.log(res)
      })
  }

  //criar um component CEP que contenha todos os inputs.
  //as funções devem permanecer no app.jsx
  //pasar para o component as funções e "valores" via props


}

export default App;
