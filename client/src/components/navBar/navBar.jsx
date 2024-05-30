
import './navBar.css'
import imageTitle from '../../assets/news.png';
import searchImg from '../../assets/search.png'

const NavBar = () => {

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
                    <form className='form-search' onSubmit={(e) => searchNew(e)}>
                        <img src="" alt=""></img>
                        <input type="text" name="search"/>
                        <button type="submit"><img src={searchImg} alt=""></img></button>
                    </form>
                </ul>
            </nav>
        </>
    )
}

export default NavBar;