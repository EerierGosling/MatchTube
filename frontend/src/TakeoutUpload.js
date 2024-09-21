import React, { useState } from 'react';

const TakeoutUpload = () => {
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

        try {
            const response = await fetch('http://localhost:5001/upload', {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            setResponseMessage(data.message);
        } catch (error) {
            console.error('Error uploading file:', error);
            setResponseMessage('File upload failed.');
        }
    };

    return (
        <div>
            <h1>File Upload</h1>
            <form onSubmit={onFileUpload}>
                <input type="file" onChange={onFileChange} />
                <button type="submit">Upload</button>
            </form>
            {responseMessage && <p>{responseMessage}</p>}
        </div>
    );
};

export default TakeoutUpload;
