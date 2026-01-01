
import React from 'react';

const Sidebar = ({ role }) => {
    const links = {
        super_admin: [
            { name: 'Dashboard', path: '/protected' },
            { name: 'Department Mgt', path: '/depts' },
            { name: 'Ward Admins', path: '/wards' },
            { name: 'System Logs', path: '/logs' },
        ],
        department_admin: [
            { name: 'Dashboard', path: '/protected' },
            { name: 'Dept Users', path: '/dept-users' },
            { name: 'Statistics', path: '/stats' },
        ],
        ward_admin: [
            { name: 'Dashboard', path: '/protected' },
            { name: 'Ward Services', path: '/ward-services' },
            { name: 'Report Status', path: '/reports' },
        ],
        user: [
            { name: 'Home', path: '/protected' },
            { name: 'My Services', path: '/services' },
            { name: 'Profile', path: '/profile' },
        ]
    };

    const activeLinks = links[role] || links.user;

    return (
        <aside className="sidebar">
            <div style={{ padding: '0 25px 20px 25px', marginBottom: '10px', borderBottom: '1px solid rgba(255,255,255,0.1)' }}>
                <h4 style={{ fontSize: '0.8rem', opacity: 0.6, textTransform: 'uppercase', letterSpacing: '1px' }}>Menu</h4>
            </div>
            {activeLinks.map((link, idx) => (
                <a key={idx} href="#" className="nav-link" onClick={(e) => e.preventDefault()}>
                    {link.name}
                </a>
            ))}
        </aside>
    );
};

export default Sidebar;
