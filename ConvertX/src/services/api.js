import axios from 'axios';

const baseURL = import.meta.env.VITE_API_URL || '';
const apiKey = import.meta.env.VITE_API_KEY || '';

if (!apiKey) {
    console.warn('VITE_API_KEY is not set. Requests will be sent without Authorization header.');
}

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