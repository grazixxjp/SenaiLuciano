import React from 'react';
import { Link } from 'react-router-dom'
import RedesSociais from '../components/RedesSociais';

const Cadastro = () => { 
    return(
    <div> 
        <h1 class="text-black text-xl" >Create your <corDifirent class="text-amber-300">account</corDifirent></h1>
        <RedesSociais/>
        <div className='Signin' class>
        <p class="mt-10 items-center justify-center flex ">User</p>
            <input class="items-center justify-center  bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="text" name="name" />
            <p class="mt-10 items-center justify-center flex ">Email</p>
            <input class="items-center justify-center  bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="text" name="name" />
            <p class="mt-10 items-center justify-center flex ">Birthday</p>
            <input class="items-center justify-center  bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="text" name="name" />
            <p class="mt-10 items-center justify-center flex ">Phone</p>
            <input class="items-center justify-center  bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="text" name="name" />
            <p class="mt-10 items-center justify-center flex ">Password</p>
            <input class="items-center justify-center  bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="text" name="name" />
        </div>
        <Link to='/Home'><button className='mt-10 bg-blue-300 rounded-2xl h-10 w-4/12 '>Register</button></Link>
    </div>
  );
}

export default Cadastro
