import { Routes, Route,Navigate} from "react-router-dom";
import AuthLayout from "./layouts/auth/AuthLayout";
import Login from "./pages/auth/Login";
import Home from "./pages/home";
import Err404 from "./pages/404";
import { useSelector } from "react-redux";

export function App() {
  const user = useSelector((state) => state.user);

  console.log(user);

  return (
    <Routes>
      <Route path="/" element={<AuthLayout />}>
        <Route index element={<Login />} />
      </Route>
      <Route path="*" element={<Err404 />}></Route>
      {user.isLogin ? (
        <Route path="/home" element={<Home />} />
      ) : (
        <Route path="/home" element={<Navigate to="/" replace />} />
      )}
    </Routes>
  );
}
