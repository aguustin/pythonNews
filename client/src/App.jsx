import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import Home from './components/home/home'
import News from './components/news/news'
import NavBar from './components/navBar/navBar'
import Footer from './components/footer/footer'
import Forms from './components/forms/forms'
import { UserContextProvider } from './context/usersContext'
import UploadNewComp from './components/uploadNew/uploadNew'
import { NewContextProvider } from './context/productContext'


function App() {

  return (
    <>
     <BrowserRouter>
      <UserContextProvider>
        <NewContextProvider>
          <NavBar/>
            <Routes>
              <Route path='/home' element={<Home/>}></Route>
              <Route path='/new' element={<News/>}></Route>
              <Route path="/uploadNew" element={<UploadNewComp/>}></Route>
              <Route path='/forms/:formType' element={<Forms/>}></Route>
            </Routes>
          <Footer/>
        </NewContextProvider>
        </UserContextProvider>
     </BrowserRouter>
    </>
  )
}

export default App
