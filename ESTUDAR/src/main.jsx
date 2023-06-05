import React from 'react'
import ReactDOM from 'react-dom/client'
import Login from './pages/login';
import './index.css'
import { BrowserRouter, createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from './pages/home';
import App from './App';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Login/>,
  },
  {
    path: "/home",
    element: <Home />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
        <BrowserRouter>
          <App />
        </BrowserRouter>
        {/* <RouterProvider router={router} /> */}
  </React.StrictMode>,
)
