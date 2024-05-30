import './footer.css';
import gmailImg from '../../assets/gmail.png';
import linkedinImg from '../../assets/linkedin.png'
import githubImg from '../../assets/github.png'
import portfolioImg from '../../assets/portfolio.png'

const Footer = () => {
    return(
        <>
            <section className='footer'>
                <div>
                    <li>
                        <img src={gmailImg} alt=""></img>
                        <label>agustin.molee@gmail.com</label>
                    </li>
                    <li>
                        <a href=""><img src={linkedinImg} alt=""></img></a>
                        <label>https://www.linkedin.com/in/agust%C3%ADn-mol%C3%A9-barolo-b042141b1/</label>
                    </li>
                    <li>
                        <a href=""><img src={githubImg} alt=""></img></a>
                        <label>https://github.com/aguustin</label>
                    </li>
                    <li>
                        <a href=""><img src={portfolioImg} alt=""></img></a>
                        <labe>https://mysecportfolio.000webhostapp.com/</labe>
                    </li>
                </div>
            </section>
        </>
    )
}

export default Footer