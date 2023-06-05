import { useState, button } from 'react'
import RedesSociais from '../components/RedesSociais'
import HeaderLogin from '../components/HeaderLogin'
import { Link, useNavigate  } from 'react-router-dom'

function Login() {
  const [login, setLogin] = useState('')
  const [senha , setSenha] = useState('')
 
  const logar = () =>{
   localStorage.setItem("dados", JSON.stringify({login: login, senha: senha}))
    console.log("logando...")
    navigate('/home')
    console.log(login)
  }
  
  const navigate = useNavigate()

  const esqueci = ()=>{
    console.log("esqueci minha senha...")
    navigate('/sign')
  }
  return (
    <>
      <HeaderLogin/>
        <div class="w-full flex items-center justify-center mt-5">
              <img src="img/casaLogin.png" alt="casa amarela e laranja com quadros cama posta branca, com uma luminaria preta ao lado" />
            </div>
        <div className='Sign' class>
            <h2 class="text-black text-lg mt-10">Sign In</h2>
            <p class="mt-10 items-center justify-center flex ">User</p>
            <input onChange={(e) => setLogin(e.target.value)}class="items-center justify-center  bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="text" name="name" />
        
    
            <p class="mt-5 items-center justify-center flex ">Password</p>
                <input onChange={(e) => setSenha(e.target.value)} class="items-center justify-center bg-gray-300 rounded-2xl mt-3 h-12 w-full" type="password" name="name" />
                <button onClick={esqueci}><p1 class="mt-3 text-xs text-gray-400">Register/Forgot Password </p1></button>
                    </div>
          <RedesSociais/>
          <div className="items-center justify-center flex mt-7" >
          <button onClick={() => logar(login, senha)}><img class="w-16" src="img/seta.png"/></button>
          </div>
         
    </>
  )
}

export default Login