from fastapi import Depends, HTTPException, status

def super_admin_only():
    # Simple demo check (you can extend to JWT)
    is_super_admin = True  

    if not is_super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Super Admin access required"
        )
