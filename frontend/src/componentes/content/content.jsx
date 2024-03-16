import axios from 'axios'
import React from 'react'
import Planes from "./planesContent/planesContent";
import { Routes,Route } from "react-router-dom";
import Perfil from "./userContent/formPerfil";
import Carousel from "./inicioContent/carousel";
import ModificarPlanes from "./planesContent/modifcarPlanes";
import Clientes from "./clienteContent/clientes";
const content = () => {


  return (
    <div className='bg-neutral-700 h-full flex flex-col overflow-hidden'>
      <div className=' flex flex-col items-center overflow-y-auto justify-center mx-4 mt-4 mb-4 bg-gris-oscuro border-2 border-neutral-500 rounded-md h-full'>
      <Routes>
        <Route index element={<Carousel/>}></Route>
        <Route path='/planes' element={<Planes />}></Route>
        <Route path='/planes/modificar_planes' element={<ModificarPlanes />}/>
        <Route path='/perfil' element={ <Perfil />}></Route>
        <Route path='/clientes' element={ <Clientes />}></Route>
      </Routes>
      
      </div>
    </div>
  )
}

export default content ;