import { useState } from 'react'

const Categories = () => { 
  return(
    <><div className="Home">
       <div class="border-t-8 border-amber-300"></div>
          <h1 class="text-black text-xl" >Create Your <corDifirent class="text-amber-300">Account!</corDifirent></h1>
          <redes/>
          <div className='Sign'>
          <form className='flex flex-col justify-center items-center'>
            <p class="mt-10 items-start justify-start flex ">User</p>
                <input class="items-center justify-center flex bg-gray-300 rounded-2xl mt-3 h-12 w-8/12" type="text" name="name" />
    
            <p class="mt-5 items-start justify-start flex ">Email</p>
                <input class="items-center justify-center flex bg-gray-300 rounded-2xl mt-3 h-12 w-8/12" type="text" name="name" />
               
            <p class="mt-5 items-start justify-start flex ">Birthday</p>
                <input class="items-center justify-center flex bg-gray-300 rounded-2xl mt-3 h-12 w-8/12" type="text" name="name" />

            <p class="mt-5 items-start justify-start flex ">Phone</p>
            <input class="items-center justify-center flex bg-gray-300 rounded-2xl mt-3 h-12 w-8/12" type="text" name="name" />
                
            <p class="mt-5 items-end justify-start flex ">Password</p>
            <input class="items-center justify-center flex bg-gray-300 rounded-2xl mt-3 h-12 w-8/12" type="text" name="name" />
              </form>
          
              <Link to='/Home'><button className='mt-10 bg-blue-300 rounded-2xl h-10 w-4/12 '>Register</button></Link>
            </div>
          </div>   
      </>
  )
}


export default Create