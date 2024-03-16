import React from 'react'
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
import { Link} from "react-router-dom";
import { LuCircleDollarSign } from "react-icons/lu";

const addPlan = () => {
return (
    <div className=' flex justify-center'>
        <div className=' w-80 text-gray-300 mt-6 flex flex-col gap-3' >
        <div className=" flex flex-col ">
        <Label htmlFor="name" value="Nombre del plan" class=' mb-2 text-lg'/>
        <TextInput id="name" type="text" rightIcon={HiAtSymbol}  placeholder="Nombre.." 
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5"/>
        </div>
        <div className={`flex flex-col `}>
        <Label htmlFor="precio" value="Precio" class=' mb-2 text-lg'/>
        <TextInput id="precio" type="text" rightIcon={LuCircleDollarSign}  placeholder="23.300"  
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5" />
        </div>
        <div className=" flex flex-col mb-2">
        <Label htmlFor="comment" value="Descripciòn" class=' mb-2 text-lg'/>
        <Textarea id="comment" rightIcon={HiMail} placeholder="Descripcion del Plan..." rows={3}
        sizing="w-14 h-6 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5" />
        </div>
        <Link 
        className=' bg-sky-500 p-2 rounded-lg text-gray-100 mt-4
        hover:bg-sky-600 hover:text-white flex justify-center shadow-lg shadow-gray-900'
        to={'/home/planes'}>
        Guardar
        </Link>
        </div>
    </div>
)
}

export default addPlan