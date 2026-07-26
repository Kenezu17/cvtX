import axios from 'axios';

const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:5173';
const apiKey = import.meta.env.VITE_API_KEY || '';

const APIURL = axios.create({
    baseURL,
});

APIURL.interceptors.request.use((config) => {
    if (!config.headers) {
        config.headers = {};
    }
    if (apiKey) {
        config.headers.Authorization = `Bearer ${apiKey}`;
    }
    return config;
});

export default APIURL;