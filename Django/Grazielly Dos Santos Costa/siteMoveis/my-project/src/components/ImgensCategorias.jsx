import React from 'react';
import imgCategorias from '../assets/categoria/almofadaas.png';
import banheiro from '../assets/categoria/banheiro.png';
import itens from '../assets/categoria/itens.png';
import quadro from '../assets/categoria/quadro.png';
import prateleira from '../assets/categoria/prateleira.png';
import rede from '../assets/categoria/rede.png';
import { Link } from 'react-router-dom'

console.log(imgCategorias);

const ImagensCategorias = () => {
    return ( 
        <div className='h-96 grid grid-cols-3 gap-4 content-center '>
        <Link to='/Details'><img src={imgCategorias} alt="Categoria"  className='rounded-xl' /></Link>
        <Link to='/Details'><img src={banheiro} alt="Categoria" className='rounded-xl'  /></Link>
        <Link to='/Details'><img src={itens} alt="Categoria" className='rounded-xl' /></Link>
        <Link to='/Details'><img src={quadro} alt="Categoria"  className='rounded-xl'/></Link>
        <Link to='/Details'><img src={prateleira} alt="Categoria"  className='rounded-xl ' /></Link>
        <Link to='/Details'><img src={rede} alt="Categoria"className='rounded-xl ' /></Link>
        </div>
     );
}

export default ImagensCategorias;