const [endereco, setEndereco ] = useState('')
const [cep, setCEP] = useState('')
const [logradouro, setLogradouro] = useState('')
const [bairro, setBairro] = useState('')

const cep(){
    return (
        <>
              <input type='text' className='border-2 border-blue-400 rounded-md outline-none' placeholder='cep' maxLength={8} onChange={(e) => setCEP(e.target.value)} value={cep}></input>
           
    
              <input type='text' className='border-2 border-blue-400 rounded-md outline-none' placeholder='logradouro' onChange={(e) => setLogradouro(e.target.value)} value={logradouro}></input>
            
    
              <input type='text' className='border-2 border-blue-400 rounded-md outline-none' placeholder='bairro'  onChange={(e) => setBairro(e.target.value)} value={bairro}></input>
           
          </>
      );
}