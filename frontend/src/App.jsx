import { Routes, Route, Navigate } from "react-router-dom";
import AuthLayout from "./layouts/auth/AuthLayout";
import Login from "./pages/auth/Login";
import Home from "./pages/home";
import Cliente from "./pages/cliente";
import Err404 from "./pages/404";
import { useSelector } from "react-redux";

export function App() {
  const { isLogin } = useSelector((state) => state.user);

  console.log(isLogin);

  return (
    <Routes>
      <Route path="/" element={<AuthLayout />}>
        <Route index element={<Login />} />
        <Route path="*" element={<Err404 />}></Route>
      </Route>
      <Route path="/client" element={<Cliente />}></Route>
      {isLogin ? ( //arreglar esto
        <Route path="/home/*" element={<Home />}></Route>
      ) : (
        <Route path="/home" element={<Navigate to="/" replace />} />
      )}
    </Routes>
  );
}
