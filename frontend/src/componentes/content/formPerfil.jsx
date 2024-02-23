
import React, { useState, useEffect } from 'react';
import { FaEdit } from 'react-icons/fa';

const formPerfil = () => {
    const [formData, setFormData] = useState({
        nombre: 'Juan',
        apellidos: 'Pérez Garcia',
        correo: 'juan.perez@example.com',
        telefono: '123456789',
        dni: '12345678A',
      });
    
      const [editMode, setEditMode] = useState({
        nombre: false,
        apellidos: false,
        correo: false,
        telefono: false,
        dni: false,
      });
    
      const [changesMade, setChangesMade] = useState(false);
    
      useEffect(() => {
        // Verifica si hay cambios en los datos
        const isDataChanged = Object.values(editMode).some((value) => value);
        setChangesMade(isDataChanged);
      }, [editMode]);
    
      const handleEditClick = (campo) => {
        setEditMode((prevEditMode) => ({
          ...prevEditMode,
          [campo]: !prevEditMode[campo],
        }));
      };
    
      const handleChange = (campo, valor) => {
        setChangesMade(true);
        setFormData((prevFormData) => ({
          ...prevFormData,
          [campo]: valor,
        }));
      };
    
      const handleGuardarCambios = () => {
        // Aquí puedes realizar alguna acción con los datos actualizados
        console.log('Datos actualizados:', formData);
        // Reinicia el estado de edición y cambios realizados
        setEditMode({
          nombre: false,
          apellidos: false,
          correo: false,
          telefono: false,
          dni: false,
        });
        setChangesMade(false);
      };
  return (
    <div className=' text-white flex flex-col gap-6 items-center  bg-neutral-800 h-full  mt-32'>
    <h1 className=' text-2xl'>Información Personal</h1>
    <form className=' flex flex-col  gap-5 '>
      <div className=' flex flex-row items-center gap-2 border-2 border-neutral-600 rounded-lg p-2 '>
        <label>Nombre:</label>
        {editMode.nombre ? (
          <>
            <input
              className=' bg-gris-oscuro w-full focus:outline-none'
              type="text"
              value={formData.nombre}
              onChange={(e) => handleChange('nombre', e.target.value)}
            />
            <FaEdit onClick={() => handleEditClick('nombre')} />
          </>
        ) : (
          <>
            <span>{formData.nombre}</span>
            <FaEdit onClick={() => handleEditClick('nombre')} 
            className=' ml-auto'/>
          </>
        )}
      </div>
      <div className=' flex flex-row items-center gap-2 bg-slate-500'>
        <label>Apellidos:</label>
        {editMode.apellidos ? (
          <>
            <input
              type="text"
              value={formData.apellidos}
              onChange={(e) => handleChange('apellidos', e.target.value)}
            />
            <FaEdit onClick={() => handleEditClick('apellidos')} />
          </>
        ) : (
          <>
            <span>{formData.apellidos}</span>
            <FaEdit onClick={() => handleEditClick('apellidos')} />
          </>
        )}
      </div>
      {/* Repite la estructura anterior para otros campos (apellidos, correo, etc.) */}
      <div className=' flex flex-row items-center gap-2 bg-slate-500'>
        <label>Correo:</label>
        {editMode.correo ? (
          <>
            <input
              type="text"
              value={formData.correo}
              onChange={(e) => handleChange('correo', e.target.value)}
            />
            <FaEdit onClick={() => handleEditClick('correo')} />
          </>
        ) : (
          <>
            <span>{formData.correo}</span>
            <FaEdit onClick={() => handleEditClick('correo')} />
          </>
        )}
      </div>
    </form>
    <div className=' bg-sky-600 rounded-lg p-2 '>
        <button 
          type="button" onClick={handleGuardarCambios} disabled={!changesMade}
          className='hover:cursor-pointer'
        >
          Guardar cambios
        </button>
      </div>
  </div>
  );
};

export default formPerfil