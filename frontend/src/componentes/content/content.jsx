import axios from 'axios'
import React from 'react'
import Planes from "./planesContent";
import { Routes,Route } from "react-router-dom";
import Perfil from "../content/formPerfil";
const content = () => {


  return (
    <div className='bg-neutral-700 h-full flex flex-col overflow-hidden'>
      <div className=' flex flex-col items-center overflow-auto justify-center mx-4 mt-4 mb-4 bg-gris-oscuro border-2 border-neutral-500 rounded-md h-full'>
      <Routes>
        <Route path='/planes' element={<Planes />}></Route>
        <Route path='/perfil' element={ <Perfil />}></Route>
      </Routes>
      
      </div>
    </div>
  )
}

export default content ;