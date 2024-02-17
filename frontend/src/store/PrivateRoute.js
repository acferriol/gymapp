import React from "react";
import { useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";

const PrivateRoute = ({ children }) => {
  const navigate = useNavigate();
  const { isLogin } = useSelector((state) => state.user);
  return isLogin ? children : navigate('/');
};

export default PrivateRoute;
