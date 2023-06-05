import React from 'react';
import foofle from '../assets/foofle.png';
import insta from '../assets/insta.png';
import facebook from '../assets/facebook.png';


const RedesSociais = () => {
  return ( 
    <div className="flex items-center justify-evenly mt-6" >
    <a href="https://www.historiasdecasa.com.br/tag/apartamento-colorido-inspirado-por-luis-barragan/"  target="_blank" rel="noreferrer">
    <img src={foofle} alt="google" className="flex items-center justify-evenly mt-6 h-7" />
    </a>
   
     <a href="https://pt-br.facebook.com/historiasdecasa" target="_blank" rel="noreferrer">
     <img src={facebook} alt="facebook" className="flex items-center justify-evenly mt-6 h-7" />
     </a>
     
     <a href="httpgs://www.instagram.com/historiasdecasa/" target="_blank" rel="noreferrer">
     <img src={insta} alt="insta" className="flex items-center justify-evenly mt-6 h-7"  />
     </a>
    </div>
    )
  }

export default RedesSociais;