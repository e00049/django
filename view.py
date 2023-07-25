def fetch_values(request):

    all_objects      = YourTable.objects.all() 	    # Retrieve all objects from the table

    filtered_objects = YourTable.objects.filter(phone_number = 7358220899)     # Retrieve objects based on a condition

    single_object    = YourTable.objects.get(id=some_id)     # Retrieve a single object

    profile          = YourTable.object.create(user = user, phone_number = phone_number)  - Create an object

    delete_user      = YourTable.objects.get(id=1).delete()

    update           = YourTable.objects.filter(phone_number=phone_number).update(otp=str(random.randint(100000, 999999)))
    
    
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username      = serializer.validated_data['username']
        email         = serializer.validated_data['email']
        mobile_number = serializer.validated_data['mobile_number']

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email already exists'}, status=400)

        if User.objects.filter(mobile_number=mobile_number).exists():
            return Response({'message': 'Mobile number already exists'}, status=400)            

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users      = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    request.user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, uid):
    try:
        user = User.objects.get(unique_number=uid)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
            
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'User deleted successfully'})

    otp             = models.CharField(max_length=6, null=True, blank=True)
    expiration_time = models.DateTimeField(auto_now=True)
    expiration_time = timezone.now() + timezone.timedelta(minutes=5)
    
    
# from rest_framework import generics
# from .models import User
# from .serializers import UserSerializer

# class UserCreateAPIView(generics.CreateAPIView):
#     queryset         = User.objects.all()
#     serializer_class = UserSerializer

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from myapp.models import User
# from myapp.serializers import UserSerializer
# from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def sign_in(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         response_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#         return Response(response_data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        url      = (f"https://2factor.in/API/V1/{settings.TWO_FACTOR_API_KEY}/SMS/{mobile_number}/AUTOGEN2/:OTP1")
        payload  = {}
        headers  = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        otp_user  = (json.loads(response.text))['OTP']
        User.objects.filter(mobile_number=mobile_number).update(otp_user)

            payload = [ key : value, key : value ]
            for key, value in payload.items():
                print(f"{key}: {value}")        
                print("I am here in for loop ...")
