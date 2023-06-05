import React from "react";
import NavBar from '../components/NavBar'
import Maps from '../components/Maps'
import tipoPagamento from '../assets/tipoPagamento.png';
import frame from '../assets/frame.png';
import { Link } from "react-router-dom";

const Carrinho = () => { 
    return( 
      <div>
     <NavBar></NavBar>
      <h1>Shopping Bag</h1>
      
      <div className="justify-center content-center w-56 grid grid-cols-2 gap-4 mt-6 ">
      <img src={frame} className='h-16 justify-center flex-1 w-16'></img>
        <p className="flex mt-6 text-xs "> Pink Frame (Brinde)</p>
        </div>
        <p className="font-bol mt-6 ">Shipping To</p>
      <div className="justify-center content-center w-56 grid grid-cols-2 gap-4 mt-6 ">
      <Maps></Maps>
        <p className="flex mt-6 text-xs "> 916 Water St, Ketchikan, Alaska 99901, USA</p>
        </div>
        <p className="text-sm h-10 w-1/12 mt-6"> Add Payment Method:</p>
        <div className="justify-center content-center w-56 grid grid-cols-2 gap-4 mt-6 ">
        <img src={tipoPagamento} className='h-7 justify-center flex-1 w-full'></img>
        </div>
        <Link to='/Categories'><button className='mt-10 bg-blue-300 rounded-2xl h-12 w-4/12 '>Realizar Pedido</button></Link>
      <p className="font-bol mt-6 ">Total Payment</p>
      <Link to='/Home'><button className='mt-10 bg-blue-300 rounded-2xl h-12 w-4/12 '>Buy</button></Link>
    </div>
    );
  }

  
  export default Carrinho