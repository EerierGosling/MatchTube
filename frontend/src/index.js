import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Main from './pages/main'; 
import App from './App'
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <Routes>
      <Route path="/" element={<App />} />     
      <Route path="/main" element={<Main />} /> 
    </Routes>
</Router>
);

reportWebVitals();
