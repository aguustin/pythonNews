import { useContext, useState } from 'react'
import './uploadNew.css'
import NewContext from '../../context/productContext';
import UserContext from '../../context/usersContext';

const UploadNewComp = () => {

    const {session} = useContext(UserContext)
    const {uploadNewContext} = useContext(NewContext)
    const [categories, setCategories] = useState([])
    const [users, setUsers] = useState([])

    const handleCategories = (e) => {
        const selectedOptions = Array.from(e.target.selectedOptions, (x) => x.value)
        setCategories([...categories, selectedOptions[0]])
    }

    const handleUsers = (e) => {
        const selectedOptions = Array.from(e.target.selectedOptions, (x) => x.value)
        setUsers([...users, selectedOptions[0]])
    }

    console.log(users, " ", categories)
    const uploadNew = async (e) => {
        const formData = new FormData();
        e.preventDefault()
        formData.append("users", JSON.stringify(users))
        formData.append("categories", JSON.stringify(categories))
        formData.append("title", e.target.elements.title.value)
        formData.append("subtitle", e.target.elements.subtitle.value)
        formData.append("imageTitle", e.target.elements.imageTitle.files[0])
        formData.append("firstParagraph", e.target.elements.firstParagraph.value)
        formData.append("firstImage", e.target.elements.firstImage.files[0])
        formData.append("secondParagraph", e.target.elements.secondParagraph.value)
        formData.append("secondImage", e.target.elements.secondImage.files[0])
        formData.append("thirdParagraph", e.target.elements.thirdParagraph.value)
        formData.append("thirdImage", e.target.elements.secondImage.files[0])
        
        await uploadNewContext(formData)
    }


    return(
        <>
            <div className='upload-new-container'>
                <form className='upload-new-form' onSubmit={(e) => uploadNew(e)}>
                    <select name="category" multiple onChange={handleCategories}>
                        <option value="Deportes">Deportes</option>
                        <option value="Politica">Politica</option>
                    </select>
                    <select name="writers" multiple onChange={handleUsers}>
                        <option value="agustin@gmail.com">Agustin</option>
                        <option value="juan@gmail.com">Juan</option>
                    </select>
                    <div>
                        <div>
                            <input type="text" className='title-subtitle' name="title" placeholder='Notice title'></input>
                            <input type="file" name="imageTitle"></input>
                        </div>
                        <div>
                            <input type="text" className='title-subtitle' name="subtitle" placeholder='Notice subtitle'></input>
                            <input type="file" name="firstImage"></input>
                        </div>
                    </div>
                    <textarea name="firstParagraph" cols={79} rows={30}></textarea>
                    <input type="file" name="secondImage"></input>
                    <textarea name="secondParagraph" cols={79} rows={30}></textarea>
                    <input type="file" name="thirdImage"></input>
                    <textarea name="thirdParagraph" cols={79} rows={30}></textarea>
                    <button type='submit'>Upload New</button>
                </form>
            </div>
        </>
    )
}

export default UploadNewComp