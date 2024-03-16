
import React, { useState, useEffect } from 'react';
import { FaEdit } from 'react-icons/fa';
import {
  Button,
  Checkbox,
  FileInput,
  Label,
  Radio,
  RangeSlider,
  Select,
  Textarea,
  TextInput,
  ToggleSwitch,
} from 'flowbite-react';

import { HiMail ,HiAtSymbol } from 'react-icons/hi';
import { FaPhone } from "react-icons/fa";
import { FaAddressCard } from "react-icons/fa6";

  const formPerfil = () => {
      const[save,setsave]=useState(true);
      const[modific,setmodific]=useState(false);

  const changeUser=()=>{
    setmodific(!modific);
  }

  return (
    <div className=' text-gray-300 flex flex-col gap-6 items-center  h-full mt-12 '>
      <h1 className=' text-4xl font-medium uppercase text-white mb-2'>Informaciòn <span className=' text-sky-500'>Personal</span></h1>
      <div className=" flex flex-col ">
        <Label htmlFor="name" value="Nombre" class=' mb-2'/>
        <TextInput id="name" type="text" rightIcon={HiAtSymbol}  placeholder="Nombre" readOnly={!modific} 
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5"/>
      </div>
      <div className={`flex flex-col `}>
        <Label htmlFor="lastname" value="Apellidos" class=' mb-2'/>
        <TextInput id="lastname" type="text" rightIcon={HiAtSymbol} readOnly={!modific} placeholder="Apellidos"  
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5" />
      </div>
      <div className=" flex flex-col mb-2">
        <Label htmlFor="email4" value="Correo" class=' mb-2'/>
        <TextInput id="email4" type="email" rightIcon={HiMail} placeholder="name@gmail.com" readOnly={!modific}
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5" />
      </div>
      <div className=" flex flex-col mb-2">
        <Label htmlFor="phone" value="Numero de telèfono" class=' mb-2'/>
        <TextInput id="phone" type="text" rightIcon={FaPhone} placeholder="+5358457812" readOnly={!modific}
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5"/>
      </div>
      <div className=" flex flex-col mb-2 pb-10">
        <Label htmlFor="dni" value="Carnet de identidad" class=' mb-2'/>
        <TextInput id="dni" type="text" rightIcon={FaAddressCard} placeholder="78469578542" readOnly={!modific}
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5" />
      </div>
      <div className=' flex gap-5 pb-10 '>
            <Button onClick={changeUser} gradientMonochrome={modific ? 'failure' : 'info'} as="span" className="cursor-pointer shadow-lg">
            {modific? 'Cancelar': 'Modificar Datos'}
            </Button>
        <Button gradientMonochrome="success" disabled={!modific}>
          Guardar Datos
        </Button>
      </div>
    </div>
  );
};

export default formPerfil