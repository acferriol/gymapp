import React from 'react'
import { FaCheck } from "react-icons/fa6";

const card = ({plan}) => {
  
  return (
    <div className={` ${ plan === 'plata'? ' bg-sky-700':' bg-neutral-700'} text-gray-50 
      py-7 min-w-72 min-h-96 px-5 rounded-lg flex flex-col items-center shadow-2xl shadow-neutral-950 hover:shadow-xl
      hover:shadow-neutral-950 hover:cursor-pointer hover:scale-105 transition`} 
      >
        <section className=' flex flex-col justify-center items-center'>
            <h1 className=' my-3 text-2xl font-light tracking-widest uppercase '>{plan}</h1>
            <h1 className={`mt-2 py-3  px-5 rounded-xl ${plan==='plata'? ' bg-neutral-700' :' bg-sky-600'}
              font-semibold text-4xl  shadow-lg shadow-gray-800`
              }>
              $ 2.00/ <span className=' text-lg text-gray-300'>Mes</span>
            </h1>
        </section>
            <ul className=' flex gap-5 mt-10 flex-col w-full'>
                <li className=' flex flex-row'>
                <FaCheck className={`p-1 rounded-full  text-2xl ${plan=='plata'? ' bg-white'+' text-neutral-700':' bg-sky-500'}`}/>
                <span className=' ml-2 text-neutral-300'>Description 1 iugeoirehb</span> 
                </li>
                <li className=' flex flex-row'>
                <FaCheck className={`p-1 rounded-full  text-2xl ${plan=='plata'? ' bg-white'+' text-neutral-700':' bg-sky-500'}`}/>
                <span className=' ml-2 text-neutral-300'>Description 2 egtryter </span> 
                </li>
                <li className=' flex flex-row'>
                <FaCheck className={`p-1 rounded-full  text-2xl ${plan=='plata'? ' bg-white'+' text-neutral-700':' bg-sky-500'}`}/>
                <span className=' ml-2 text-neutral-300'>Description 3 e eyeey</span> 
                </li>
                <li className=' flex flex-row'>
                <FaCheck className={`p-1 rounded-full  text-2xl ${plan=='plata'? ' bg-white'+' text-neutral-700':' bg-sky-500'}`}/>
                <span className=' ml-2 text-neutral-300'>Description 4 eyety</span> 
                </li>
            </ul>
    </div>
  )
}

export default card