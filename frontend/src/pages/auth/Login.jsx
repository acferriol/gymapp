import React, { useState } from "react";
import { RiEyeLine, RiEyeOffLine } from "react-icons/ri";
import { CgGym } from "react-icons/cg";
import { toast } from "react-toastify";
import { Link } from "react-router-dom";

const Login = () => {
  const [seePasw, setseePaw] = useState(false);
  const[userName, setuserName] =useState("");
  const[pasword, setPasword] =useState("");

  const handleSeePasw = () => {
    setseePaw(!seePasw);
  };

const handleSubmit = (e) =>{
  e.preventDefault();
  if([userName,pasword].includes("")){
    toast.error("Todos los campos son obligatorios",{
      theme: "dark"
    });
    return
  }
  console.log(userName,pasword);
}

  return (
    <>
      <div className="w-full h-full flex flex-col">
        <div className="  bg-gris-oscuro w-full h-20 flex justify-start items-center">
          <CgGym className=" text-white ml-10 text-2xl"/>
          <span className=" text-white m-2">Logo</span>
        </div>
        <div className=" bg-gris-oscuro w-full h-full flex items-center justify-center font-serif">
          <div className=" py-10 px-8 w-96 bg-neutral-700 rounded-lg">
            <div className=" flex justify-center mb-10">
              <h2 className=" text-white text-4xl font-bold ">
                Inicio <span className=" text-blue-500">de</span> Sesión
              </h2>
            </div>
            <form onSubmit={handleSubmit} action="" className=" flex flex-col gap-5 ">
              <div>
                <label htmlFor="text" className=" text-white">
                  Nombre de Usuario
                </label>
                <div className=" mt-1">
                  <input
                    type="text"
                    placeholder="usuario"
                    className="w-full bg-neutral-800 py-2 px-6 rounded outline-none text-white text-opacity-45"
                    value={userName}
                    onChange={(e)=> setuserName(e.target.value)}
                  />
                </div>
              </div>
              <div>
                <label htmlFor="text" className=" text-white">
                  Contraseña
                </label>
                <div className=" mt-1 relative mb-2">
                  <input
                    type={seePasw ? "text" : "password"}
                    placeholder="contraseña"
                    className="w-full bg-neutral-800 py-2 px-6 rounded outline-none text-white text-opacity-45"
                    value={pasword}
                    onChange={(e)=> setPasword(e.target.value)}
                  />
                  {!seePasw ? (
                    <RiEyeOffLine
                      onClick={handleSeePasw}
                      className="absolute text-gray-50 right-1 top-1/2 -translate-y-1/2 mr-1 hover: cursor-pointer opacity-85 hover:opacity-100"
                    />
                  ) : (
                    <RiEyeLine
                      onClick={handleSeePasw}
                      className="absolute text-gray-50 right-1 top-1/2 -translate-y-1/2 mr-1 hover: cursor-pointer opacity-85 hover:opacity-100"
                    />
                  )}
                </div>
                <Link to="" className=" text-blue-500 hover:text-sky-700">
                  ¿Has olvidado la contraseña?
                </Link>
              </div>
              <div className="flex justify-center mt-7">
                <button
                  className=" text-white text-xl px-5 py-2 bg-blue-500 rounded w-full 
                hover:bg-blue-600 transition-color font-bold shadow-md shadow-neutral-900"
                >
                  Entrar
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};
export default Login;
