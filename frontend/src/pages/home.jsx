import React, { useState } from 'react'
import  SideBar  from "../componentes/sideBar";
import Header from "../componentes/header";
import Content from "../componentes/content/content";
import { Routes,Route } from "react-router-dom";
import { RiMenu3Fill } from "react-icons/ri";

const getUser =()=>{
  let user = localStorage.getItem('user');
  user = (user ? JSON.parse(user) : null) ;
  return user;
}

const home = ()=> {
  //console.log(getUser().users);
  return (
    <div className=' h-screen w-screen flex flex-row font-sans'>
      {<SideBar user={getUser().users} />}
      <div className=' flex flex-col w-full h-full '>
        {< Header user={getUser().users}/>}
        {< Content/>}
      </div>
    </div>
  )
}
export default home ;
