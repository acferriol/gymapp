import React from 'react'
import { Carousel } from "flowbite-react";
import img1JPG from "./vecteezy_pesas-en-el-piso-en-el-gimnasia-levantamiento-de-pesas_22653816-min.jpg";
import img2JPG from "./vecteezy_filas-de-pesas-en-el-gimnasio-cerca-arriba-de-moderno-pesas_22993370.jpg";
const carousel = () => {
  return (
    <>
    <div className=" h-full w-full p-4 ">
    <Carousel slideInterval={4000}>
        <img src={img1JPG} alt="" className=' hover:cursor-pointer'/>
        <img src={img2JPG} alt="" className=' hover:cursor-pointer'/>
      </Carousel>
    </div>
    </>
  )
}

export default carousel