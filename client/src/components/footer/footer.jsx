import './footer.css';
import gmailImg from '../../assets/gmail.png';
import linkedinImg from '../../assets/linkedin.png'
import githubImg from '../../assets/github.png'
import portfolioImg from '../../assets/portfolio.png'

const Footer = () => {
    return(
        <>
            <section className='footer'>
                <div className='footer-child-container'>
                    <div className='footer-child'>
                        <li>
                            <a href="agustin.molee@gmail.com"><img src={gmailImg} alt=""></img></a>
                            <label>Gmail</label>
                        </li>
                        <li>
                            <a href="https://www.linkedin.com/in/agust%C3%ADn-mol%C3%A9-barolo-b042141b1/"><img src={linkedinImg} alt=""></img></a>
                            <label>LinkedIn</label>
                        </li>
                    </div>
                    <div className='footer-child'>
                        <li>
                            <a href="https://github.com/aguustin"><img src={githubImg} alt=""></img></a>
                            <label>Github</label>
                        </li>
                        <li>
                            <a href="https://mysecportfolio.000webhostapp.com/"><img src={portfolioImg} alt=""></img></a>
                            <label>Porfolio url</label>
                        </li>
                    </div>
                </div>
            </section>
        </>
    )
}

export default Footer