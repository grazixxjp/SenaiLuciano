import React, { Component } from 'react';

const Home = () => {
    const dados = JSON.parse(localStorage.getItem("dados"))
    // if (dados.login == ''){

    // }

    return ( 
        <>
            <h1>Página Home - 
                {dados !== null ?
                    <>
                     {dados.login} - {dados.senha} 
                    </>
                    : null
                }
            </h1>
        </>
     );
}
 
export default Home;