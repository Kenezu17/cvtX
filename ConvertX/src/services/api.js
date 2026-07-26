import axios from 'axios';

const APIURL = axios.create({
    baseURL: import.meta.env.VITE_APIURL || 'https://cvtx.onrender.com',
});

export default APIURL;