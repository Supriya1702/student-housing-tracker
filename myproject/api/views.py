from rest_framework.response import Response
from rest_framework.decorators import api_view
from .users import DUMMY_USERS  # Import dummy users

@api_view(['GET'])
def get_users(request):
    return Response(DUMMY_USERS)
