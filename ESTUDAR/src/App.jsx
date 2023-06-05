import { Route, Routes, useNavigate } from "react-router-dom";
import NavBar from "./components/navbar";
import Login from "./pages/login";
import Home from "./pages/home";
import { useEffect, useState } from "react";

function App() {

    const [dados, setDados] = useState(() => {
        const info = JSON.parse(localStorage.getItem('dados'))
        return info
    })

    // const dados = JSON.parse(localStorage.getItem("dados"))
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

    //redux + saga > 2 pastas, 1 redux - states , 1 saga - consultas na api
    useEffect(() => {
        let total = valorTotal + (5 * contador)
        setValorTotal(total)
    }, [contador])

    //passar uma função para o component via props
    //utilizar essa função (passando parâmetros)
    //executar a lógica no app

   const logar = (login, senha) => {
        //requisição POST enviando login e senha
        //caso login seja efetuado, retornará 2 tokens
        //access token - 5min
        //refresh token - 24h

        //se os 2 tokens expirarem, oq fazer?
        //redirecionar o usuário para a tela de login
        //e fazer o login novamente

        //{ chaves }
        // [colchetes]
        // (parentêses)
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
            </Routes>
            {/* <Login/> */}
        </div>
     );
}

// próxima aula
// import { matchRoutes, useLocation } from "react-router-dom"

// const routes = [{ path: "/members/:id" }]

// const useCurrentPath = () => {
//   const location = useLocation()
//   const [{ route }] = matchRoutes(routes, location)

//   return route.path
// }
export default App;