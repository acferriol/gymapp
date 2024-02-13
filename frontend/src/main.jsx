import React from 'react'
import ReactDOM from 'react-dom/client'
import {App} from './App.jsx'
import './index.css'
import { BrowserRouter } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import  store  from "./store/store.js";
import { Provider } from "react-redux";

ReactDOM.createRoot(document.getElementById('root')).render(
  <>
  <Provider store={store}>
    <BrowserRouter>
      <App/>
    </BrowserRouter>
    <ToastContainer />
  </Provider>
  </>
)
