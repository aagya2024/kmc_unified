import React from 'react';

const ReportPage = () => {
    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            minHeight: '70vh',
            padding: '40px'
        }}>
            <div style={{
                textAlign: 'center',
                maxWidth: '600px'
            }}>
                <div style={{
                    fontSize: '6rem',
                    marginBottom: '20px'
                }}>
                    🚧
                </div>
                
                <h1 style={{
                    color: '#1a2b56',
                    fontSize: '2.5rem',
                    marginBottom: '15px',
                    fontWeight: '700'
                }}>
                    Under Construction
                </h1>
                
                <p style={{
                    color: '#666',
                    fontSize: '1.2rem',
                    lineHeight: '1.6',
                    marginBottom: '30px'
                }}>
                    The Reports module is currently being developed. 
                    Please check back soon for analytics and reporting features.
                </p>
               
            </div>
        </div>
    );
};

export default ReportPage;
