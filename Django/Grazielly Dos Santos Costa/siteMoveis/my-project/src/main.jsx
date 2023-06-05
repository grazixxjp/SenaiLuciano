import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import Details from './pages/Details'
import Login from './pages/Login'
import Categories from './pages/Categories'
import Home from './pages/Home'
import Sign from './pages/Sign'
import Carrinho from './pages/Carrinho'
import './index.css'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const Rotas = createBrowserRouter([
  {
    path: "/Login",
    element: <Login/>,
  },
  {
    path: "/Home",
    element: <Home/>,
  },
  {
    path: "/Details",
    element: <Details/>,
  },
  {
    path: "/Categories",
    element : <Categories/>,
  },
  {
    path: "/Carrinho",
    element : <Carrinho/>,
  },
  {
    path: "/Sign",
    element : <Sign/>,
  }
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={Rotas}/>
  </React.StrictMode>
)
