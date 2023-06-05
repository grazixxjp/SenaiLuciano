import React, { Component } from 'react';

const NavBar = ({nome, deslogar}) => {
    return ( <>
        <div className='w-screen flex bg-blue-900 justify-center  p-3'>
            <ul className='flex justify-around flex-row list-none text-white w-1/2'>
                <li>Home</li>
                <li>Produtos</li>
                { nome == null ? 
                    <li>Logar</li>
                    : null
                }
                {
                    nome != null ?
                    <>
                        <li>Bem vindo {nome}</li>
                        <li>
                            <button onClick={deslogar}>
                                Sair
                            </button>
                        </li>
                    </>
                    : null
                }
            </ul>
        </div>
        </> );
}
 
export default NavBar;