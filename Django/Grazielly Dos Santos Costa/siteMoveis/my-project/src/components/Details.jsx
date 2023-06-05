import React from 'react';
import details from '../assets/details.png';
import { Link } from 'react-router-dom';

console.log(details);

const Detalhe = () => {
  return ( 
    <Link to='/Details'><img src={details} alt="Detalhe" className='mt-6 w-60 inline-block' /></Link>
   );
}
 
export default Detalhe;
