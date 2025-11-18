from datetime import datetime

def check_access(user, resource):
    # Check subscription level
    if user.subscription_level == 'premium':
        return True
    if resource.access_level == 'basic' and user.subscription_level == 'basic':
        pass  # continue checks
    else:
        return False

    # Check available hours
    now = datetime.now().strftime("%H:%M")
    start, end = resource.available_hours.split('-')
    if not (start <= now <= end):
        return False

    # Check account status
    if user.account_status != 'active':
        return False

    return True
