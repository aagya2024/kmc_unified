import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from './assets/kmc_logo.png';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoading(true);

    const formDetails = new URLSearchParams();
    formDetails.append('username', username);
    formDetails.append('password', password);

    try {
      const response = await fetch('http://localhost:8080/api/v1/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formDetails,
      });

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.access_token);
        navigate('/protected');
      } else {
        const errorData = await response.json();
        setError(errorData.detail || 'Access Denied: Invalid credentials');
      }
    } catch (error) {
      setError('Connection Error: Please ensure the server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <div style={{ textAlign: 'center', marginBottom: '30px' }}>
          <img
            src={logo}
            alt="KMC Logo"
            style={{ width: '120px', height: 'auto', marginBottom: '15px' }}
          />
          <h2 style={{ color: '#1a2b56', fontWeight: 800 }}>Unified Auth</h2>
          <p style={{ color: '#666', fontSize: '0.9rem' }}>Secure Portal for Kathmandu Citizens & Staff</p>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Username / Email / Phone</label>
            <input
              className="form-input"
              type="text"
              placeholder="Enter your identifier"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input
              className="form-input"
              type="password"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-primary btn-block" disabled={loading}>
            {loading ? 'Authenticating...' : 'Sign In'}
          </button>

          {error && (
            <div style={{ marginTop: '20px', padding: '10px', background: '#ffebee', color: '#d32f2f', borderRadius: '4px', fontSize: '0.85rem', textAlign: 'center' }}>
              {error}
            </div>
          )}
        </form>

        <div style={{ marginTop: '30px', textAlign: 'center', fontSize: '0.8rem', color: '#999' }}>
          By signing in, you agree to official KMC IT policies.
        </div>
      </div>
    </div>
  );
}

export default Login;
