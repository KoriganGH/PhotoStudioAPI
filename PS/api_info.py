from drf_yasg import openapi

api_info = openapi.Info(
    title='Your API Title',
    default_version='1.0.0',
    description='Your API Description',
    terms_of_service='https://www.example.com/terms/',
    contact=openapi.Contact(email='contact@example.com'),
    license=openapi.License(name='Your License'),
)