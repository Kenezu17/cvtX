import axios from 'axios';

const APIURL = axios.create({
    baseURL: import.meta.env.VITE_APIURL || 'http://127.0.0.1:8000',
});

export default APIURL;