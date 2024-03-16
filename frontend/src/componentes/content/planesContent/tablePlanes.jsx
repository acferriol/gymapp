import React from 'react'
import { MdEdit , MdDelete} from "react-icons/md";
import {Tooltip}from "react-tooltip";
const tablePlanes = ({p}) => {
  return (
    <div className=' flex text-gray-300 justify-between border-[1px]
    border-gray-400 rounded-lg p-1 items-center hover:cursor-pointer hover:text-gray-50 hover:bg-neutral-700'>
        <div className=' flex italic font-light'>
        <p className="  w-64 ">{p.nombre}</p>
        <p className="  w-14 flex justify-center">{p.precio} <span className=' ml-1 text-gray-100'>$</span> </p>
        </div>
        <div className=' flex gap-2 mr-4'>
            <button className=' p-1 bg-sky-400 rounded-full text-gray-800 hover:bg-sky-700 hover:text-white shadow-md shadow-gray-950'
            data-tooltip-id="my-tooltip"
            data-tooltip-content=" Editar Plan"
            data-tooltip-place="top">
              <MdEdit/>
              <Tooltip id="my-tooltip" style={{ backgroundColor: "rgb(70, 70, 70)", color: "rgb(255, 255, 255)" }}/>
            </button>
            <button className=' p-1 bg-red-600 rounded-full text-gray-100 hover:bg-red-500 hover:text-gray-900 shadow-md shadow-gray-950'
            data-tooltip-id="my-tooltip"
            data-tooltip-content="Eliminar Plan"
            data-tooltip-place="top"
            >
              <MdDelete/>
              <Tooltip id="my-tooltip" style={{ backgroundColor: "rgb(70, 70, 70)", color: "rgb(255, 255, 255)" }}/>
            </button>
            

        </div>
    </div>
  )
}

export default tablePlanes