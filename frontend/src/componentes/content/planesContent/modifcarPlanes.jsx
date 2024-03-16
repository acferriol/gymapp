import React , { useState }  from "react";
import { IoMdAddCircle } from "react-icons/io";
import Table from "./tablePlanes";
import {Tooltip}from "react-tooltip";
import NewPlan from "./addPlan";
const modifcarPlanes = () => {

  const planes = [
    {
      id: 1,
      nombre: "Oro",
      precio: "5",
      descripcion: "ejbfefefhheknfef eg",
    },
    {
      id: 2,
      nombre: "Plata",
      precio: "1",
      descripcion: "ejbfefefhheknfef eg",
    },
    {
      id: 3,
      nombre: "Bronce",
      precio: "23",
      descripcion: "ejbfefefhheknfef eg",
    },
  ];

  const [isNewPlan, setisNewPlan] = useState(false);
  const changeNewPlan =()=>{
    setisNewPlan(!isNewPlan);
    console.log(isNewPlan);
  }

  return (

    <div className=" w-full h-full mt-5">
      <div className=" flex items-center  justify-between m-4 border-b-gray-500 border-b-2 pb-5">
        {
          isNewPlan?
          <h1 className=" text-2xl uppercase text-gray-50 font-semibold ml-5">
            Nuevo <span className=" text-sky-500">Plan</span>
          </h1>
          :
          <h1 className=" text-2xl uppercase text-gray-50 font-semibold ml-5">
            Modificar <span className=" text-sky-500">Planes</span> Existentes
          </h1>
        }
        {
          isNewPlan?
          <button className=" flex items-center gap-1 bg-red-600 rounded-lg p-2 text-gray-100 shadow-lg
          hover:bg-red-500 text-md mr-5  shadow-neutral-800"
          data-tooltip-id="my-tooltip"
          data-tooltip-content=" Cancelar Plan"
          data-tooltip-place="top"
          onClick={changeNewPlan}>
          Cancelar
          <Tooltip id="my-tooltip" style={{ backgroundColor: "rgb(70, 70, 70)", color: "rgb(255, 255, 255)" }}/>
        </button>
        :
        <button className=" flex items-center gap-1 bg-sky-600 rounded-lg p-2 text-white shadow-lg
        hover:bg-sky-500 text-md mr-5"
        data-tooltip-id="my-tooltip"
        data-tooltip-content=" Añadir Plan"
        data-tooltip-place="top"
        onClick={changeNewPlan}>
        <span><IoMdAddCircle className=" text-white"/></span> plan
        <Tooltip id="my-tooltip" style={{ backgroundColor: "rgb(70, 70, 70)", color: "rgb(255, 255, 255)" }}/>
      </button>
        }
        
      </div>
      {
        isNewPlan 
        ? <NewPlan/>
        :
        <div className=" m-8">
        <section className=" mb-4">
          <ul className="flex flex-row justify-between text-xl text-gray-200">
            <div className=" flex ml-1">
            <li className=" w-64">Nombre</li>
            <li className=" w-14">Precio</li>
            </div>
            <li className=" mr-6">Acciòn</li>
          </ul>
        </section>
        <div className=" flex flex-col gap-2 ">
          {
            planes.map(function(plan){
              return <Table p={plan}/>
            })
          }
        </div>
        </div>
      }
      
    </div>
  );
};

export default modifcarPlanes;
