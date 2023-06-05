import { useState } from 'react'
import { Link } from 'react-router-dom'
import NavBar from '../components/NavBar'

function Details() {
  const [count, setCount] = useState(0)

  return (
    <><div className="Details">
          <NavBar></NavBar>
        <p className="text-black text-base ml-2 mb-6 ">Details</p>
        </div>
        <img className='w-4/6 items-center justify-center flex ' src="img/details.png"  />        
        <h1 className='mt-10 items-start justify-start flex text-2xl'>Sisalana</h1>
        <p className='items-start justify-start text-left mt-6 text-slate-400 '>Made-to-measure special line sisal rug, produced in rustic vertical loom and manual sisal dyeing.</p>
        <h2 className='items-start justify-start flex text-lg mt-6'>Cep</h2>
  
        <input className="items-center justify-center flex bg-gray-300 mt-3 h-12 w-3/5" type="text" name="name" />
        <h3 className='items-start justify-start text-left mt-6 text-base'>1,00 x 1,50</h3>
        <h4 className='items-start justify-start text-left mt-4'>USD 150,00</h4>
    

        <Link to="/Carrinho"><button className='mt-10 bg-blue-300 rounded-2xl h-10 w-4/12 '>Buy</button></Link>

    </>
    )
}
    
export default Details