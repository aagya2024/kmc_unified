import logo from '../assets/kmc_logo.png';

const Navbar = ({ user, onLogout }) => {
    return (
        <nav className="navbar">
            <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
                <img src={logo} alt="KMC Logo" style={{ height: '45px', width: 'auto' }} />
                <h2 style={{ fontSize: '1.2rem', color: '#1a2b56', margin: 0 }}>Unified Services Portal</h2>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
                <div style={{ textAlign: 'right' }}>
                    <div style={{ fontWeight: 'bold', fontSize: '0.9rem' }}>{user?.username}</div>
                    <div style={{ fontSize: '0.75rem', color: '#666', textTransform: 'uppercase' }}>{user?.role?.replace('_', ' ')}</div>
                </div>
                <button onClick={onLogout} className="btn btn-primary" style={{ padding: '8px 16px', fontSize: '0.85rem' }}>
                    Logout
                </button>
            </div>
        </nav>
    );
};

export default Navbar;
