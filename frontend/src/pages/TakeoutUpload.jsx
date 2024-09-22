import React, { useState, useEffect } from 'react';
import PropelAuth from '../components/PropelAuth';
import {
    withAuthInfo,
    useRedirectFunctions,
    useLogoutFunction,
} from "@propelauth/react";

const TakeoutUpload = withAuthInfo((props) => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [responseMessage, setResponseMessage] = useState('');

    // Handle file selection
    const onFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    // Handle form submission and send file to backend
    const onFileUpload = async (event) => {
        event.preventDefault();
        if (!selectedFile) {
            alert('Please select a file before uploading.');
            return;
        }

        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('email', props.user.email)

        console.log(formData)

        const controller = new AbortController();
        const timeout = 500000;
        const timeoutId = setTimeout(() => controller.abort(), timeout);

        try {
            const response = await fetch('https://pennapps-project.onrender.com:5001/upload', {
                method: 'POST',
                body: formData,
                signal: controller.signal
            });
            
            if (!response.ok) {
                setResponseMessage("Upload Failed");
                console.error(response.message)
            }
            else {
                console.log("uploaded!")
            }
            
        } catch (error) {
            console.error('Error uploading file:', error);
            setResponseMessage('File upload failed.');
        }
    };

    return (
        <div className='flex-col min-h-screen w-full bg-cover bg-gradient-to-r from-tinderPink via-tinderRed to-tinderOrange flex justify-center items-center'> 
            <img 
                src="logo2.png" 
                className='w-3/4 md:w-1/3 mb-8'
            />
            <div className='bg-white rounded-2xl w-4/5 md:w-1/2 p-8 flex flex-col items-center justify-center'>

                <h1 className='text-2xl'>Upload to Get Started!</h1>
                <div className='flex flex-col justify-center items-center'>
                    <form onSubmit={onFileUpload} className='flex flex-col mt-5 items-center justify-center'>
                        <input 
                        type="file" 
                        onChange={onFileChange}
                        className='flex flex-col file:cursor-pointer file:transition file:ease-in-out file:hover:-translate-y-1 file:duration-300 file:border-none file:bg-gradient-to-r from-tinderPink via-tinderRed to-tinderOrange file:p-2 file:px-8 file:text-white md:text-xl file:mt-3 file:rounded-xl'/>
                        <button 
                            className="w-1/2 md:w-full transition ease-in-out hover:-translate-y-1 hover:scale-110 duration-300 bg-gradient-to-r mt-5 rounded-xl from-tinderPink via-tinderRed to-tinderOrange p-2 px-8 text-white md:text-xl"
                            type="submit"
                            >Upload
                        </button>
                    </form>
                </div>
                {responseMessage && <p>{responseMessage}</p>}
            </div>
            <div id='account' className='bg-white rounded-2xl w-4/5 md:w-1/2 p-8 flex flex-col items-center justify-center mt-5'>
                <PropelAuth />
            </div>
        </div>
    );
});

export default TakeoutUpload;
