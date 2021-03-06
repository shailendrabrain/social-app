import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter} from "react-router-dom";
import App from './App';
import * as serviceWorkerRegistration from './services/serviceWorkerRegistration';
import reportWebVitals from './services/reportWebVitals';
import axios from 'axios';


axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.headers.post['Content-Type'] = 'application/json';


ReactDOM.render(
    <React.StrictMode>
        <BrowserRouter>
            <App/>
        </BrowserRouter>
    </React.StrictMode>,
    document.getElementById('root')
);

serviceWorkerRegistration.unregister();
reportWebVitals();
