from rest_framework import status


STATUS = {
    "status": None,
    "message": None,
}

def too_many_requests():
    STATUS["status"] = status.HTTP_429_TOO_MANY_REQUESTS
    STATUS["message"] = "Reached max limit for the day."
    return (STATUS, STATUS["status"])

def unauthorized():
    STATUS["status"] = status.HTTP_401_UNAUTHORIZED
    STATUS["message"] = "User not logged in."
    return (STATUS, STATUS["status"])

def failure(message="Failed"):
    STATUS["status"] = status.HTTP_400_BAD_REQUEST
    STATUS["message"] = message
    return (STATUS, STATUS["status"])

def success(message=None):
    STATUS["status"] = status.HTTP_200_OK
    STATUS["message"] = message
    return (STATUS, STATUS["status"])

def user_detail(user, last_login):
    USER = {
        "id": user.pk,
        "last_login": last_login,
        "token": user.auth_token.key,
        "status": status.HTTP_200_OK
    }
    return (USER, STATUS["status"])
