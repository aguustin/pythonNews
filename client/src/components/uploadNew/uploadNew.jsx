import { useState } from 'react'
import './uploadNew.css'

const UploadNewComp = () => {

    const [categories, setCategories] = useState();
    const [users, setUsers] = useState();

    const uploadNew = (e) => {
        const formData = new FormData()
        formData.append("title", e.target.elements.title.value)
        formData.append("subtitle", e.target.elements.subtitle.value)
        formData.append("imageTitle", e.target.elements.imageTitle.files[0])
        formData.append("firstParagraph", e.target.elements.firstParagraph.value)
        formData.append("firstImage", e.target.elements.firstImage.files[0])
        formData.append("secondParagraph", e.target.elements.secondParagraph.value)
        formData.append("secondImage", e.target.elements.secondImage.files[0])
        formData.append("thirdParagraph", e.target.elements.thirdParagraph.value)
        formData.append("thirdImage", e.target.elements.secondImage.files[0])

        uploadNewContext(formData)
    }


    return(
        <>
            <div className='upload-new-container'>
                <form className='upload-new-form' onSubmit={() => uploadNew()}>
                    <select name="category">
                        <option value="categoria A" onChange={setCategories([...categories, e.target.value])}>categoria A</option>
                        <option value="categoria B" onChange={setCategories([...categories, e.target.value])}>categoria B</option>
                        <option value="categoria C" onChange={setCategories([...categories, e.target.value])}>categoria C</option>
                        <option value="categoria D" onChange={setCategories([...categories, e.target.value])}>categoria D</option>
                        <option value="categoria E" onChange={setCategories([...categories, e.target.value])}>categoria E</option>
                    </select>
                    <select name="writers">
                        <option value="usuario A" onChange={setUsers([...users, e.target.value])}>usuario A</option>
                        <option value="usuario B" onChange={setUsers([...users, e.target.value])}>usuario B</option>
                        <option value="usuario C" onChange={setUsers([...users, e.target.value])}>usuario C</option>
                        <option value="usuario D" onChange={setUsers([...users, e.target.value])}>usuario D</option>
                        <option value="usuario E" onChange={setUsers([...users, e.target.value])}>usuario E</option>
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