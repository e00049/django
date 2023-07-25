import os
import jwt
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        # Generate and send verification email
        token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        verify_url = os.environ.get('FRONTEND_URL') + f'/verify-email?token={token}'
        self.send_verification_email(user.email, verify_url)

    def send_verification_email(self, email, verify_url):
        message = Mail(
            from_email='noreply@example.com',  # Replace with your email address
            to_emails=email,
            subject='Verify Your Email',
            html_content=f'Hi,<br><br>Please click the link below to verify your email:<br><br><a href="{verify_url}">{verify_url}</a>'
        )

        try:
            sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')  # Replace with your SendGrid API key
            response = sg.send(message)
            print(response.status_code)
        except Exception as e:
            print(str(e))

class VerifyEmailView(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
