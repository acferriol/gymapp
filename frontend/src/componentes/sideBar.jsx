import React from "react";
import { Link } from "react-router-dom";
import { FaHouse , FaMessage, FaUserTag } from "react-icons/fa6";
import { HiUsers } from "react-icons/hi2";
import {  RiCalendarFill , RiPriceTag2Fill} from "react-icons/ri";
import { BiSolidReport } from "react-icons/bi";



const sideBar = ( {user} ) => {
  return (
    <div className=" h-full w-72 bg-gris-oscuro border-r-2 border-neutral-500 text-neutral-400 text-xl">
      <div className=" flex flex-col items-center mb-7  gap-1">
        <img src="" className=" border-2 border-neutral-700 w-28 h-28 rounded-full mt-4"/>
        <h1 className=" text-neutral-50 font-medium ">
          {user.nombre}
        </h1>
        <hr className=" w-48 border-neutral-500 mt-4" />
      </div>
      <div className=" flex flex-col pl-5 gap-2 mb-7">
        <Link className=" flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
          <FaHouse />
          <span>Inicio</span>
        </Link >
        <Link className=" flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
          <HiUsers />
          <span>Clientes</span>
        </Link>
        <Link className=" flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
            <RiPriceTag2Fill/>
          <span>Planes</span>
        </Link>
        <Link className="flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
            <FaMessage/>
          <span>Mensajes</span>
        </Link>
        <Link className=" flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
          < RiCalendarFill/>
          <span>Horario</span>
        </Link>
      </div>
      <div className=" flex flex-col pl-5 gap-2">
      <hr className="  w-48 border-neutral-500 mb-4" />
        <Link className=" flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
          <BiSolidReport />
          <span>Reportes</span>
        </Link >
        <Link className="flex items-center gap-4 hover:bg-blue-500 hover:text-white rounded-md p-1 w-48 transition-colors">
          <FaUserTag />
          <span>Empleados</span>
        </Link>
      </div>
    </div>
  );
};

export default sideBar;
