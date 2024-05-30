import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import Home from './components/home/home'
import News from './components/news/news'
import NavBar from './components/navBar/navBar'
import Footer from './components/footer/footer'

function App() {

  return (
    <>
     <BrowserRouter>
        <NavBar/>
        <Routes>
          <Route path='/home' element={<Home/>}></Route>
          <Route path='/new' element={<News/>}></Route>
        </Routes>
        <Footer/>
     </BrowserRouter>
    </>
  )
}

export default App
