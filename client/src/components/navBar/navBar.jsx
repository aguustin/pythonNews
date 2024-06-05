
import './navBar.css'
import imageTitle from '../../assets/news.png';
import searchImg from '../../assets/search.png'
import { useContext } from 'react';
import UserContext from '../../context/usersContext';

const NavBar = () => {

    const {session} = useContext(UserContext)

    const searchNew = (e) => {
        e.preventDefault()
        const s = e.target.elements.search.values
    }
    
    return(
        <>
            <nav className='nav'>
                <img className='title-image' src={imageTitle} alt=""></img>
                <ul>
                    <li><a href="/home">Home</a></li>
                    <li><button>Cagories</button></li>
                    <li><a href="/dayNews">Day News</a></li>
                    {
                    session &&
                    session.userType == 1 
                    ?
                    <form className='form-search' onSubmit={(e) => searchNew(e)}>
                        <img src="" alt=""></img>
                        <input type="text" name="search"/>
                        <button type="submit"><img src={searchImg} alt=""></img></button>
                    </form>
                    :
                    <form className='form-search' onSubmit={(e) => searchNew(e)}>
                        <img src="" alt=""></img>
                        <input type="text" name="search"/>
                        <button type="submit"><img src={searchImg} alt=""></img></button>
                    </form>
                    }
                    
                    {
                    session &&
                    session.userType == 1 
                    ? 
                    <>
                        <li className='getin'><a href="/forms/uploadNew">Upload New</a></li>
                        <li className='signin'><a href="/forms/usersManage">Users Manage</a></li>
                    </>
                    : 
                    <>
                        <li className='getin'><a href="/forms/getIn">Get in</a></li>
                        <li className='signin'><a href="/forms/signIn">Sign In</a></li>
                    </>
                    }
                </ul>
            </nav>
        </>
    )
}

export default NavBar;