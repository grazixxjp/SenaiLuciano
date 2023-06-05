import React from "react";
import { Link } from "react-router-dom";

function Login() {
    const [login, setLogin] = useState('')
    const [senha, setSenha] = useState('')
  
    const logar = () =>{
     localStorage.setItem("dados", JSON.stringify({login: login, senha: senha}))
      console.log("logando...")
      navigate('/home')
      console.log(login)
    }
}
    
const NavBar = ({nome, deslogar}) => {
    return (
        <>
            <nav className="flex justify-around w-full mb-12 h-7  ">
                <ul className="flex justify-around text-black flex-row content-center w-5/6 ">
                    <li><Link to="/Home">{(nome)}</Link></li>
        
                    <li><Link to="/Home">Home</Link></li>
                    <li><Link to="/Categories">Produtos</Link></li>
                    <li><Link to="/Carrinho">Carrinho</Link></li>
                    { nome == null ? 
                    <Link to="/Login"><li>Sair{localStorage.clear}</li></Link>
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
            </nav>
        </>
    )
}

export default NavBar