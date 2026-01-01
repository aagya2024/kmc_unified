// src/api.js
import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL, // change to your backend URL
    withCredentials: true, // send cookies for auth/session
    headers: {
        "Content-Type": "application/json",
    },
});

// add interceptors for auth tokens
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("token"); // if you store JWT
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default api;
