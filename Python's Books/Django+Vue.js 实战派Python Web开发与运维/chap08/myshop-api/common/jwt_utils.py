def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "token": token,
        'id': user.id,
        'username': user.username,
        'email':user.email,
        #'is_active':user.is_active,
    }