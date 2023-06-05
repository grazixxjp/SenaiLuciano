import { useState } from 'react'
import './App.css'
import Categories from './pages/Categories'
import Details from './pages/Details'
import Home from './pages/Home'
import { Router } from 'react-router-dom'


function App() {
  const [dados, setDados] = useState(() => {
    const info = JSON.parse(localStorage.getItem('dados'))
    return info
  })

  const [logado, setLogado] = useState(false)

  const [contador, setContador] = useState(0)
  const [valorTotal, setValorTotal] = useState(0)

  const navigate = useNavigate()

  useEffect(() => {
      console.log("use effect trigger")
      setDados(() => {
          const info = JSON.parse(localStorage.getItem('dados'))
          return info
      })
  }, [logado])

  useEffect(() => {
    let total = valorTotal + (5 * contador)
    setValorTotal(total)
}, [contador])

  const logar = (login, senha) => {

    axios.post('http://127.0.0.1:8080/auth/jwt/create',{
      username: login,
      password: senha
    }).then((res) => {
      console.log(res);
    })

    localStorage.setItem("dados", JSON.stringify({login: login, senha: senha }))
    setLogado(true)
    navigate('/home')
}
const deslogar = () => {
  //3 etapas
  //1 - limpar localstorage
  localStorage.clear()
  //2 - alterar o state setLogado
  setLogado(false)
  //3 - redirecionar para o login
  navigate('/')
}

return ( 
  <div>
      {contador} <button onClick={() => setContador(contador +1)}>+</button>
      <h2>Valor Total {valorTotal}</h2>
      <NavBar
       nome={dados && dados.login}  deslogar={deslogar}
       />
      <Routes>
          <Route path="/" element={<Login logar={logar} />} />
          <Route path="/home" element={<Home />} />
          <Route path="*" component={() => <h1>Page not found</h1>} />
      </Routes>
      {/* <Login/> */}
  </div>
);
}

export default App