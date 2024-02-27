import React from 'react'
import { Carousel } from "flowbite-react";
const carousel = () => {
  return (
    <>
    <div className=" h-full w-full p-4 ">
    <Carousel className=''>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="" />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="" />
      </Carousel>
    </div>
    </>
  )
}

export default carousel