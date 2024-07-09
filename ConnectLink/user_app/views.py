from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from user_app.serializers import UserSerializer, LoginSerializer

from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return Response({
            'access': str(refresh.access_token),
            'user': user_data,
        },status.HTTP_200_OK,
)


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Get the logged-in user
        logged_in_user = self.request.user

        # Exclude the logged-in user from the queryset
        queryset = User.objects.exclude(pk=logged_in_user.pk)
        
        return queryset


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        user_id = self.kwargs.get('pk')  # 'pk' is the default name for primary key in DRF
        return User.objects.get(pk=user_id)
    
    
    
    
    


