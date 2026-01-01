from fastapi import HTTPException, status

def super_admin_only():
    # Demo logic (replace with JWT later)
    is_super_admin = True

    if not is_super_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Super Admin access only"
        )
