import React from 'react'
import Card from "./card";
import  axios from "axios";
import { MdEditSquare } from "react-icons/md";
import { Link } from "react-router-dom";
import {Tooltip}from "react-tooltip";
//import 'react-tooltip/dist/index.css';
const planesContent = () => {

  const getPlanes = async()=>{
    try {
      const response = await axios.get(`url para obtener los planes`);
      return response.data;
    } catch (err) {
      alert('Error en la peticion de los Planes', err.message);
    }
  }

  return (
    <>
    <div className=' flex w-full justify-end '>
      <Link to='#' 
        data-tooltip-id="my-tooltip"
        data-tooltip-content=" Modificar Planes!"
        data-tooltip-place="top"
        className='  bg-sky-600  hover:bg-sky-700  transition-all p-2  mt-2 mr-4 rounded-full
        shadow-md shadow-neutral-900'
      >
        <MdEditSquare className=' text-xl text-neutral-200 hover:text-white'/>
      </Link>
      <Tooltip id="my-tooltip" style={{ backgroundColor: "rgb(70, 70, 70)", color: "rgb(255, 255, 255)" }}/>
    </div>
    <div className='pt-100 flex flex-col lg:flex-row lg:p-0 gap-10 justify-center  h-full w-full items-center px-5'>
            <Card plan={'oro'}/>
            <Card plan={'plata'}/>
            <Card plan={'bronce'}/>
    </div>
    </>
  )
}

export default planesContent