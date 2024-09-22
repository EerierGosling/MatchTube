import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Main from './pages/main'; 
import App from './App'
import reportWebVitals from './reportWebVitals';
import { RequiredAuthProvider, RedirectToLogin } from "@propelauth/react";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <RequiredAuthProvider
        authUrl={process.env.REACT_APP_AUTH_URL}
        // displayWhileLoading={<Loading />}
        displayIfLoggedOut={<RedirectToLogin />}>
        <App />
    </RequiredAuthProvider>,
    document.getElementById("root")
);

reportWebVitals();
