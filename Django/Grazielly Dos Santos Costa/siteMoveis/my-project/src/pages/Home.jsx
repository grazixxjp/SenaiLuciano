import { useEffect, useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import Logo from '../components/Logo'
import axios from "axios"
import Categories from './Categories'
import Produto from '../components/Produto';
import Details from '../components/Details'
import NavBar from '../components/NavBar'

const GoHome = () => {
  const dados = JSON.parse(localStorage.getItem("dados"))
    
    return(
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
const Produtos = () => {
  const [lista, setLista] = useState([])
  useEffect(()=>{
    
  })
  axios.get("http://127.0.0.1:8000/loja/produtos/")
  .then((res)=>{
    setLista(res.data)
    console.log(res.data)
  })
}
function Home() {
  return (
    <>
    <div>
    <NavBar></NavBar>
       <Logo />
       <p className="text-black text-base">Hi, User</p>
       <Produto/>
       <Details></Details>
          <h1 className='mt-20 text-2xl  items-center justify-center flex'>Retro Matte Sofa</h1>
          <p className="text-gray-700 text-sm items-center justify-center flex ">$120,20</p>
          <div className="w-full items-center justify-center flex "><img src="img/sofa.png"/></div>
            
        <h2 className='items-center justify-center text-2xl flex mt-16'>Categories</h2>
          <div className="flex items-center justify-evenly mt-10"></div>
          <img className='rounded-xl w-2/5 inline-block' src="img/categoria1.png"/>
          
          <img className='rounded-xl w-2/5 inline-block ml-8' src="img/categoria2.png"/>
          </div>

        <h3 className='items-center justify-center text-2xl flex mt-16'>Principal Categories</h3>
          <p className="text-black mt-10" >Arts in cotton made by hand using traditional techniques of Minas artisanal loom and using residual raw material from the large industry.</p>
          <div className="flex items-center justify-evenly mt-10">
          <img className='rounded-xl w-2/5 inline-block' src="img/categoria3.png"/>
          <img className='rounded-xl w-2/5 inline-block' src="img/categoria4.png"/>
          </div>
          <Link to='/Categories'><button className='mt-10 bg-blue-300 rounded-2xl h-10 w-4/12 '>Show More</button></Link>
    </>
)
}


export default Home