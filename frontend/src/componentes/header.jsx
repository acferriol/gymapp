import React from "react";
import Dropdown from "./dropdown";
import { IoNotifications } from "react-icons/io5";

const header = ({user}) => {
  return (
    <>
      <div
        className=" h-16 bg-neutral-600 text-white border-b-2
        border-neutral-500 flex items-center justify-between px-4 "
      >
        <div className=" text-neutral-600 lg:text-white">LOGO</div>
          <div className=" flex items-center text-xl gap-2 text-gray-200  hover:text-white">
            <IoNotifications className=" transition-colors cursor-pointer"/>
            <p className=" text-base ml-3">
              {user.nombre}
            </p>
            {<Dropdown />}
          </div>
      </div>
    </>
  );
};

export default header;
