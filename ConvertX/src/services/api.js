import axios from 'axios';

const baseURL = import.meta.env.VITE_APIURL || (import.meta.env.DEV ? 'http://localhost:5173' : undefined);

if (!baseURL) {
  throw new Error(
    'VITE_APIURL is required in production. Set it in your deployment environment.'
  );
}

const APIURL = axios.create({
  baseURL,
});

export default APIURL;