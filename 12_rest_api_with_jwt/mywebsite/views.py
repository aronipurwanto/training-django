from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data.get('access')
        refresh_token = response.data.get('refresh')

        if access_token and refresh_token:
            # Decode the access token to get expiration time
            # (Assuming you are using the default JWT settings)
            from rest_framework_simplejwt.tokens import AccessToken
            access_token_obj = AccessToken(access_token)
            expired_at = datetime.fromtimestamp(access_token_obj['exp'])
            issued_at = datetime.fromtimestamp(access_token_obj['iat'])

            return Response({
                'statusCode': status.HTTP_200_OK,
                'message': 'Token berhasil dibuat.',
                'data': {
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'expired_at': expired_at,
                    'issued_at': issued_at
                }
            })
        else:
            return response  # Jika gagal, kembalikan response default

class MyTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data.get('access')

        if access_token:
            # Decode the access token to get expiration time
            from rest_framework_simplejwt.tokens import AccessToken
            access_token_obj = AccessToken(access_token)
            expired_at = datetime.fromtimestamp(access_token_obj['exp'])
            issued_at = datetime.fromtimestamp(access_token_obj['iat'])

            return Response({
                'statusCode': status.HTTP_200_OK,
                'message': 'Token berhasil di-refresh.',
                'data': {
                    'access_token': access_token,
                    'expired_at': expired_at,
                    'issued_at': issued_at
                }
            })
        else:
            return response  # Jika gagal, kembalikan response default