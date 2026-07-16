import axios, { create } from 'axios'
import { useEffect } from 'react';

const APIURL = axios.create({
    baseURL: import.meta.env.VITE_APIURL,
});


export default APIURL;