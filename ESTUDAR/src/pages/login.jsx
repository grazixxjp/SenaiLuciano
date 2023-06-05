import logo from "../assets/Logo.png"
import perfil from "../assets/perfil.png"
import { useNavigate } from "react-router-dom";
import Input from "../components/input";
import Button from '../components/button'
import { useState } from "react";

function Login({logar}) {
    const [login, setLogin] = useState('')
    const [senha, setSenha] = useState('')

    const esqueci = () =>{
        console.log("esqueci minha senha...")
    }

    return (
        <>
        <div className="flex items-center justify-center w-screen h-screen bg-gradient-to-bl from-blue-gradient to-purple-gradient p-5">
            <div className="cards flex shadow-lg shadow-black">
                <img src={logo} className='block md:hidden'/>
                <div className="bg-[#442DB3] w-[450px] flex flex-col items-center md2:w-full">
                    <img src={perfil} className='w-[150px] h-[150px] rounded-full m-8'/>
                    <div className="w-[355px] md2:w-full my-4">
                        <h3 className="text-2xl text-white font-sans p-3">Email</h3>
                        {/* <input type="text" onChange={(e) => setLogin(e.target.value)} /> */}

                        <Input onChange={(e) => setLogin(e.target.value)}/>
                    </div>
                    <div className="w-[355px] md2:w-full">
                        <h3 className="text-2xl text-white font-sans p-3">Password</h3>
                        <Input onChange={(e) => setSenha(e.target.value) }/>
                    </div>
                    <div className="mt-16">

                        <Button onClick={() => logar(login, senha)} >Login</Button>
                        <Button onClick={esqueci} >Esqueci a senha</Button>
                    </div>
                </div>
            </div>
        </div>
        </>

    );
}


export default Login;
