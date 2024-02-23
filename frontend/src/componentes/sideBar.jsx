import React from "react";
import { Link } from "react-router-dom";
import { FaHouse , FaMessage, FaUserTag } from "react-icons/fa6";
import { HiUsers } from "react-icons/hi2";
import {  RiCalendarFill , RiPriceTag2Fill} from "react-icons/ri";
import { BiSolidReport } from "react-icons/bi";
import { useState } from "react";
import {  } from "./content/content";


const sideBar = ( {user} ) => {

  const [activeButton, setActiveButton] = useState(null);

  const handleClick = (buttonId) => {
    setActiveButton((prevActiveButton) =>
      prevActiveButton === buttonId ? null : buttonId
    );
  };

  const isButtonActive = (buttonId) => activeButton === buttonId;


  return (
    <div className=" h-full w-0 lg:w-72 bg-gris-oscuro border-r-2 border-neutral-500
      text-neutral-400 text-xl">
      <div className=" flex flex-col items-center mb-7  gap-1">
        <img src="" className=" border-2 border-neutral-700 w-28 h-28 rounded-full mt-4"/>
        <h1 className=" text-neutral-50 font-medium ">
          {user.nombre}
        </h1>
        <hr className=" w-48 border-neutral-500 mt-4" />
      </div>
      <div className=" flex flex-col pl-5 gap-2 mb-7">
        <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('inicio')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('inicio')}
        >
          <FaHouse />
          <span className="">Inicio</span>
        </Link >
        <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('cliente')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('cliente')}
        >
          <HiUsers />
          <span className="">Clientes</span>
        </Link>
        <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('planes')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('planes')}
        to={'/home/planes'}
        >           
          <RiPriceTag2Fill/>
          <span className=" ">Planes</span>
        </Link>
        <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('msj')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('msj')}
        >            
          <FaMessage/>
          <span className=" ">Mensajes</span>
        </Link>
        <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('h')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('h')}
        >          
          < RiCalendarFill/>
          <span className="">Horario</span>
        </Link>
      </div>
      <div className=" flex flex-col pl-5 gap-2">
      <hr className="  w-48 border-neutral-500 mb-4" />
      <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('rep')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('rep')}
        >          
        <BiSolidReport />
          <span className="">Reportes</span>
        </Link >
        <Link className={`flex items-center gap-4 hover:bg-blue-400
        hover:text-white rounded-md p-1 w-48 transition-colors 
        ${isButtonActive('empl')? 'text-blue-400':' text-gray-100'}
        `}
        onClick={()=>handleClick('empl')}
        >          
        <FaUserTag />
          <span className="">Empleados</span>
        </Link>
      </div>
    </div>
  );
};

export default sideBar;
