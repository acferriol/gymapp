import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { resetUserState } from "../store/userSlice";
import { persistor } from "../store/store";
import { useNavigate, Link} from "react-router-dom";
const Dropdown = () => {

  const [isOpen, setIsOpen] = useState(false);
  const dispatch = useDispatch();

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };
  const navigate = useNavigate();
  const handleLogout = () => {
    // Lógica para cerrar sesión
    localStorage.clear();
    //persistor.purge(); 
    navigate('/')
    dispatch(resetUserState());
    
  };

  const handleProfile = () => {
    setIsOpen(!isOpen);
    // Lógica para dirigirse a la página de perfil
    console.log('Ir a la página de perfil');
    // Puedes agregar aquí la lógica para navegar a la página de perfil.
  };

  return (
    <div className="relative inline-block text-left">
      <button
        type="button"
        onClick={toggleDropdown}
        className="inline-flex justify-center w-full px-2 py-2 text-sm font-medium text-white rounded-full focus:outline-none hover:bg-sky-700 hover:transition-opacity"
      >
        <svg
          className="w-5 h-5 text-white"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 origin-top-right bg-neutral-700 rounded-md shadow-lg">
          <div
            className="py-1"
            role="menu"
            aria-orientation="vertical"
            aria-labelledby="options-menu"
          >
            <Link to={'/home/perfil'}>
            <button
              onClick={handleProfile}
              className="block px-4 py-2 text-sm text-gray-200 hover:bg-gray-300 hover:text-gray-900 rounded-md"
              role="menuitem"
            >
              Perfil
            </button>
            </Link>
            <button
              onClick={handleLogout}
              className="block px-5 py-2 text-sm text-gray-200 hover:bg-gray-300 hover:text-gray-900 rounded-md"
              role="menuitem"
            >
              Salir
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dropdown;
