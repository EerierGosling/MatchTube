import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import Main from "./pages/main";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { RequiredAuthProvider, RedirectToLogin } from "@propelauth/react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <RequiredAuthProvider
        authUrl="https://258796592.propelauthtest.com"
        // displayWhileLoading={<Loading />}
        displayIfLoggedOut={<RedirectToLogin />}>
        <Router>
            <Routes>
                <Route path="/" element={<App />} />
                <Route path="/main" element={<Main />} />
            </Routes>
        </Router>
    </RequiredAuthProvider>,
    document.getElementById("root")
);

reportWebVitals();
