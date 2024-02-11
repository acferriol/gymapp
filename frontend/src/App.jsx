import {Routes,Route } from "react-router-dom";
import AuthLayout from "./layouts/auth/AuthLayout";
import  Login  from "./pages/auth/Login";
import  Err404  from "./pages/404";

export function App() {
  return (
        <Routes>
          <Route path="/" element={<AuthLayout/>}>
            <Route index element={<Login/>} />
            </Route>
          <Route path="*" element={<Err404/>} ></Route>
        </Routes>
  )
}

