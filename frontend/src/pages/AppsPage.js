import React from 'react';

const AppsPage = () => {
    const kmcLogo = 'https://kathmandu.gov.np/wp-content/themes/kmc-theme/images/kmc-logo.png';
     
    const apps = [
        {
            id: 1,
            name: 'eSifarish System',
            description: 'Online Recommendation Service',
            logo: kmcLogo,
            link: 'https://esifarish.kathmandu.gov.np/login',
            color: '#1a2b56'
        },
        {
            id: 2,
            name: 'eOffice System',
            description: 'Electronic Office Management',
            logo: kmcLogo,
            link: 'https://eoffice.kathmandu.gov.np/eoadmin',
            color: '#d32f2f'
        },
        {
            id: 3,
            name: 'निशुल्क उपचार सहजिकरण सेवा',
            description: 'Free Healthcare Facilitation Service',
            logo: kmcLogo,
            link: 'http://freehealth.kathmandu.gov.np/',
            color: '#2196F3'
        },
        {
            id: 4,
            name: 'फोहरमैला व्यवस्थापन प्रणाली',
            description: 'Waste Management System',
            logo: kmcLogo,
            link: 'https://clean.kathmandu.gov.np/',
            color: '#FF9800'
        },
        {
            id: 5,
            name: 'डाटा कलेक्सन प्रणाली',
            description: 'Data Collection System',
            logo: kmcLogo,
            link: 'https://datacollection.kathmandu.gov.np/',
            color: '#9C27B0'
        },
        {
            id: 6,
            name: 'विद्युतीय नक्शा पास प्रणाली',
            description: 'Electronic Building Permit System',
            logo: kmcLogo,
            link: 'http://ebps.kathmandu.gov.np/',
            color: '#F44336'
        },
        {
            id: 7,
            name: 'बिपद् सूचना ब्यवस्थापन प्रणाली',
            description: 'Disaster Information Management System',
            logo: kmcLogo,
            link: 'https://bipadportal.gov.np/',
            color: '#E91E63'
        },
        {
            id: 8,
            name: 'सहकारी व्यवस्थापन प्रणाली',
            description: 'Cooperative Management System',
            logo: kmcLogo,
            link: 'https://copomis.gov.np/',
            color: '#673AB7'
        },
        {
            id: 9,
            name: 'महानगर विद्युतीय खबरपत्रिका',
            description: 'Metro Digital Newsletter',
            logo: kmcLogo,
            link: 'http://metronews.kathmandu.gov.np/',
            color: '#3F51B5'
        },
        {
            id: 10,
            name: 'बोलपत्र आवहन प्रणाली',
            description: 'Public Procurement System',
            logo: kmcLogo,
            link: 'https://bolpatra.gov.np/egp/',
            color: '#009688'
        },
        {
            id: 11,
            name: 'घटना दर्ता नागरिक सेवा',
            description: 'Incident Registration Citizen Service',
            logo: kmcLogo,
            link: 'https://public.donidcr.gov.np/',
            color: '#795548'
        },
        {
            id: 12,
            name: 'राजश्व भुक्तानी प्रणाली',
            description: 'Revenue Payment System',
            logo: kmcLogo,
            link: 'http://eservice.kathmandu.gov.np/',
            color: '#607D8B'
        }
    ];

    const handleAppClick = (app) => {
        if (app.link) {
            window.open(app.link, '_blank');
        }
    };

    return (
        <div style={{ padding: '30px' }}>
            <div style={{ marginBottom: '30px' }}>
                <h2 style={{ color: '#1a2b56', fontSize: '2rem', marginBottom: '10px' }}>
                    KMC WebApps
                </h2>
                <p style={{ color: '#666', fontSize: '1rem' }}>
                    Access all KMC integration web-applications from one place
                </p>
            </div>

            <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
                gap: '20px',
                marginTop: '20px'
            }}>
                {apps.map((app) => (
                    <div
                        key={app.id}
                        onClick={() => handleAppClick(app)}
                        style={{
                            background: '#fff',
                            borderRadius: '12px',
                            padding: '25px',
                            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                            cursor: 'pointer',
                            transition: 'all 0.3s ease',
                            border: '2px solid transparent'
                        }}
                        onMouseEnter={(e) => {
                            e.currentTarget.style.transform = 'translateY(-5px)';
                            e.currentTarget.style.boxShadow = '0 8px 16px rgba(0,0,0,0.15)';
                            e.currentTarget.style.borderColor = app.color;
                        }}
                        onMouseLeave={(e) => {
                            e.currentTarget.style.transform = 'translateY(0)';
                            e.currentTarget.style.boxShadow = '0 2px 8px rgba(0,0,0,0.1)';
                            e.currentTarget.style.borderColor = 'transparent';
                        }}
                    >
                        <div style={{
                            width: '60px',
                            height: '60px',
                            borderRadius: '12px',
                            background: '#fff',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            fontSize: '2rem',
                            marginBottom: '15px',
                            padding: '10px',
                            border: '1px solid #eee'
                        }}>
                            <img 
                                src={app.logo} 
                                alt={app.name}
                                style={{
                                    width: '100%',
                                    height: '100%',
                                    objectFit: 'contain'
                                }}
                            />
                        </div>

                        <h3 style={{
                            color: '#1a2b56',
                            fontSize: '1.1rem',
                            marginBottom: '8px',
                            fontWeight: '600',
                            lineHeight: '1.4'
                        }}>
                            {app.name}
                        </h3>

                        <p style={{
                            color: '#666',
                            fontSize: '0.85rem',
                            lineHeight: '1.5',
                            marginBottom: '15px'
                        }}>
                            {app.description}
                        </p>

                        <div style={{
                            display: 'flex',
                            alignItems: 'center',
                            color: app.color,
                            fontSize: '0.85rem',
                            fontWeight: '600'
                        }}>
                            <span>Open</span>
                            <span style={{ marginLeft: '5px' }}>→</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default AppsPage;
