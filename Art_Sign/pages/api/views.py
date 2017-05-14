from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Art_Sign.pages.api.serializers import MembershipSerializer


@api_view(['POST'])
def NewMembershipView(request):
    serializer = MembershipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
