// src/contexts/AuthContext.jsx
import { createContext, useState, useEffect } from "react";
import api from "@/utils/APIHelper";
import { useToast } from "./ToastContext";

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const { showSuccess, showError, showInfo } = useToast();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  //load user safely from localStorage on visiting website
  useEffect(() => {
    const savedUser = localStorage.getItem("user");
    if (savedUser) {
      try {
        setUser(JSON.parse(savedUser));
      } catch (err) {
        console.error("Invalid user in localStorage, clearing:", err);
        localStorage.removeItem("user");
      }
    }
    setLoading(false);
  }, []);

  // Login
  const login = async (emailOrPhone, password) => {
    try {
      const res = await api.post("/login", { emailOrPhone, password });

      // axios automatically gives you parsed JSON
      const data = res.data;

      // store user + token
      localStorage.setItem("token", data.token);
      localStorage.setItem("user", JSON.stringify(data.user));
      setUser(data.user);

      // return success and message from backend
      return { success: true, message: data.message };
    } catch (err) {
      const message =
        err.response?.data?.message ||
        "Something went wrong. Please try again.";

      return { success: false, message };
    }
  };
  // Logout
  const logout = async () => {
    try {
      await api.post("/logout");
    } catch (error) {
      // ignore backend error for now
    }
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    setUser(null);
    showSuccess("Logged out successfully!");
  };

  // Check auth
  //   const checkAuth = async () => {
  //     const token = localStorage.getItem("token");
  //     const userString = localStorage.getItem("user");

  //     if (!token || !userString) {
  //       showInfo("No token found. Please login.");
  //       return false;
  //     }

  //     let userObj;
  //     try {
  //       userObj = JSON.parse(userString);
  //     } catch (err) {
  //       console.error("Invalid stored user JSON, clearing:", err);
  //       localStorage.removeItem("user");
  //       return false;
  //     }

  //     try {
  //       const { data } = await api.get(`/user/${userObj._id}`);
  //       setUser(data.user);
  //       return true;
  //     } catch (err) {
  //       showError("Authentication failed, please login again.");
  //       logout();
  //       return false;
  //     }
  //   };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
