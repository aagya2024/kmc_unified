
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import DashboardContent from './pages/DashboardContent';

function Protected() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const checkAuth = async () => {
            const token = localStorage.getItem('token');
            if (!token) {
                navigate('/');
                return;
            }

            try {
                const response = await fetch('http://localhost:8080/api/v1/auth/verify', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    const userData = await response.json();
                    setUser(userData);
                } else {
                    localStorage.removeItem('token');
                    navigate('/');
                }
            } catch (error) {
                localStorage.removeItem('token');
                navigate('/');
            } finally {
                setLoading(false);
            }
        };

        checkAuth();
    }, [navigate]);

    const handleLogout = () => {
        localStorage.removeItem('token');
        navigate('/');
    };

    if (loading) {
        return (
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: '#f4f7f6' }}>
                <p style={{ color: '#1a2b56', fontWeight: 'bold' }}>Loading Secure Session...</p>
            </div>
        );
    }

    return (
        <div className="app-container">
            <Sidebar role={user?.role} />
            <div className="main-content">
                <Navbar user={user} onLogout={handleLogout} />
                <div style={{ flex: 1, overflowY: 'auto' }}>
                    <DashboardContent user={user} />
                </div>
            </div>
        </div>
    );
}

export default Protected;