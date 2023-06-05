import React from 'react';
import imgMaps from '../assets/maps.png';

console.log(imgMaps);

const Maps = () => {
  return ( 
    <img src={imgMaps} alt="Maps" className='w-36 content-center grid grid-cols-3 gap-4 mt-6' />
   );
}
 
export default Maps;
