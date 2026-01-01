
import React from 'react';

const DashboardContent = ({ user }) => {
    const renderSuperAdmin = () => (
        <div className="dashboard-grid">
            <div className="card">
                <h3 className="card-title">Infrastructure Overview</h3>
                <p>Manage KMC high-level services and department allocations.</p>
                <div style={{ marginTop: '15px' }}>
                    <span className="badge badge-blue">12 Departments</span>
                    <span className="badge badge-red" style={{ marginLeft: '10px' }}>32 Wards</span>
                </div>
            </div>
            <div className="card">
                <h3 className="card-title">Admin Management</h3>
                <p>Provision new Department and Ward administrators.</p>
                <button className="btn btn-primary" style={{ marginTop: '15px', width: '100%' }}>Manage Admins</button>
            </div>
            <div className="card red">
                <h3 className="card-title">System Health</h3>
                <p>All authentication services are active and running.</p>
                <div style={{ color: 'green', fontWeight: 'bold' }}>● Operational</div>
            </div>
        </div>
    );

    const renderDeptAdmin = () => (
        <div className="dashboard-grid">
            <div className="card">
                <h3 className="card-title">Department: {user.department_id || 'Health & Sanitation'}</h3>
                <p>Managing services for your specific department.</p>
            </div>
            <div className="card">
                <h3 className="card-title">User Analytics</h3>
                <p>Active users within your department: 452</p>
            </div>
        </div>
    );

    const renderWardAdmin = () => (
        <div className="dashboard-grid">
            <div className="card">
                <h3 className="card-title">Ward No: {user.ward_id || '04'}</h3>
                <p>Local ward service coordination.</p>
            </div>
            <div className="card">
                <h3 className="card-title">Local Requests</h3>
                <p>Pending registrations: 12</p>
                <button className="btn btn-primary" style={{ marginTop: '10px' }}>Review Requests</button>
            </div>
        </div>
    );

    const renderUser = () => (
        <div className="dashboard-grid">
            <div className="card">
                <h3 className="card-title">My Services</h3>
                <p>Access your certificates, licenses, and KMC official forms.</p>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '15px' }}>
                    <button className="btn btn-primary btn-block">e-Governance Services</button>
                    <button className="btn btn-primary btn-block" style={{ background: '#4a4a4a' }}>Tax Payments</button>
                </div>
            </div>
            <div className="card">
                <h3 className="card-title">Notifications</h3>
                <p>You have no new notifications.</p>
            </div>
        </div>
    );

    const getDashboard = () => {
        switch (user.role) {
            case 'super_admin': return renderSuperAdmin();
            case 'department_admin': return renderDeptAdmin();
            case 'ward_admin': return renderWardAdmin();
            default: return renderUser();
        }
    };

    return (
        <main style={{ padding: '30px' }}>
            <header style={{ marginBottom: '30px' }}>
                <h1 style={{ color: '#1a2b56', fontSize: '1.75rem' }}>Welcome, {user.username}</h1>
                <p style={{ color: '#666' }}>
                    Role: <span className="badge badge-blue">{user.role?.replace('_', ' ')}</span>
                </p>
            </header>
            {getDashboard()}
        </main>
    );
};

export default DashboardContent;
