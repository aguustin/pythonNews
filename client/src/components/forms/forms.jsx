import { useParams, useNavigate } from 'react-router-dom';
import './forms.css';
import { getInRequest, signInRequest } from '../../api/userRequests';
import { useContext } from 'react';
import UserContext from '../../context/usersContext';

const Forms = () => {

    const {getInContext} = useContext(UserContext)
    const {formType} = useParams();
    const navigate = useNavigate();

    const signIn = (e) => {
        e.preventDefault()

        const data = {
            mail: e.target.elements.mail.value,
            username: e.target.elements.username.value,
            lastname: e.target.elements.lastname.value,
            password: e.target.elements.password.value,
            confirmPassword: e.target.elements.confirmPassword.value
        }
        console.log(data)

        signInRequest(data)
    }
    
    const getIn = async (e) => {
        e.preventDefault()
   
        const data = {
            mail: e.target.elements.mail.value,
            password: e.target.elements.password.value
        }
        await getInContext(data);
    }

    return(
        <>
        <div className='forms'>
            {formType === 'getIn' ?
                <form className='form-container' onSubmit={(e) => getIn(e)}>
                    <div>
                        <h3>Get In</h3>
                    </div>
                    <div className='form-group'>
                        <label>Mail</label>
                        <input type="text" name="mail"></input>
                    </div>
                    <div className='form-group'>
                        <label>Password</label>
                        <input type="password" name="password"></input>
                    </div>
                    <div className='button-container'>
                        <button type='submit'>Get in</button>
                    </div>
                </form> 
            :
                <form className='form-container' onSubmit={(e) => signIn(e)}>
                    <h3>Sign In</h3>
                    <div className='form-group'>
                        <label>Mail</label>
                        <input type="text" name="mail"></input>
                    </div>
                    <div className='form-group'>
                        <label>Username</label>
                        <input type="text" name="username"></input>
                    </div>
                    <div className='form-group'>
                        <label>Lastname</label>
                        <input type="text" name="lastname"></input>
                    </div>
                    <div className='form-group'>
                        <label>Password</label>
                        <input type="password" name="password"></input>
                    </div>
                    <div className='form-group'>
                        <label>Confirm Password</label>
                        <input type="password" name="confirmPassword"></input>
                    </div>
                    <div className='button-container'>
                        <button type='submit'>Sign in</button>
                    </div>
                </form>
            }
        </div>
        </>
    )
}

export default Forms;