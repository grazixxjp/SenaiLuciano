import React from 'react';
import imgLogo from '../assets/logo.jpg';

console.log(imgLogo);

const Logo = () => {
  return ( 
    <img src={imgLogo} alt="Logo" className='w-10 inline-block' />
   );
}
 
export default Logo;
