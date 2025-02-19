import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './componenti/Card'
import Todolist from './componenti/Todolist'
import UserProfile from './componenti/UserProfile'

function alertClik(){
  alert("MA CIAOO!!")
}

function heandleChange(e){
  console.log(e.target.value)
}

function heandleSubmit(e){
  e.preventDefoult
  console.log(e)
}


function App() {
  const [count, setCount] = useState(0)
  const cities=[
    {id:1,
      name:"Tokyo",
      desc:"Hello there",
      imgUrl: "https://www.giapponepertutti.it/demo/wp-content/uploads/2024/07/Depositphotos_563013432_S.jpg",
      isVisitato:true
    }
  ]

/*<Card
      isVisitato = {true}
      titolo = "Tokyo"
      descrizione = "Hello there"
      image = "https://images.unsplash.com/photo-1732878796195-0479be305faf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxNDV8fHxlbnwwfHx8fHw%3D">
    </Card>
    <Card
    isVisitato = {true}
    titolo = "London"
    descrizione = "Good morning"
    image = "https://images.unsplash.com/photo-1733234976396-87cf34ae6038?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8" 
    ></Card>
    <Card 
    isVisitato = {true}
    titolo = "Heloooooooooo"
    descrizione ="hello"
    image = "https://plus.unsplash.com/premium_photo-1674489157120-9c386f7173d9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw2OHx8fGVufDB8fHx8fA%3D%3D" 
    >
    </Card>
    <Card
    isVisitato = {false}
    titolo = "?????????????????????"
    descrizione = "-------------------------"
    image = "https://images.unsplash.com/photo-1733036016861-0541eb76dac5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw3MHx8fGVufDB8fHx8fA%3D%3D"
    >
    </Card>*/

  return (
    <>
      <div>
        {cities.map((city) => (
            <Card key={city.id}
                  titolo = {city.name}
                  imgUrl = {city.imgUrl}
                  isVisitato={city.isVisitato}>
                  {city.descrizione}
            </Card>
            )
          )
        }

        {cities.filter((city) => city.isVisit).map((city) =>(
            <Card key={city.id}
                  titolo = {city.name}
                  imgUrl = {city.imgUrl}
                  isVisitato={city.isVisit}
                  descrizione={city.desc}>
            </Card>
            )
          )
        }
      </div>

        <Todolist></Todolist>

        <UserProfile></UserProfile>


      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={(alertClik)}>
          alert
        </button>
        <input type='text' onChange={heandleChange}/>
        <form onSubmit={heandleSubmit}>
          <button type='submit'>Cliccami!!!</button>
        </form>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
