import ImagensCategorias from '../components/ImgensCategorias'
import Logo from '../components/Logo'
import NavBar from '../components/NavBar'

const Categories = () => { 
  return(
    <div>
    <NavBar></NavBar>
    <Logo />
    <p className=" text-black text-base ">Hi, Grazie</p>
    <p className=" text-black text-2xl mt-10 ">Produtos</p>
    <input className="items-center justify-center flex bg-gray-300 rounded-2xl mt-3 h-12 w-full mb-8" type="text" />
    <ImagensCategorias/>

  </div>
  );
}

export default Categories