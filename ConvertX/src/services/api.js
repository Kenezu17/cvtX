import axios from 'axios';

const APIURL = axios.create({
    baseURL: import.meta.env.VITE_APIURL || 'http://localhost:5173',
});

export default APIURL;