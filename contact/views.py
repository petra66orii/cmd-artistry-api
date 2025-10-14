from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def contact_form(request):
    """
    Handles submission of the contact form and sends an email.
    """
    data = request.data
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Basic validation
    if not all([name, email, message]):
        return Response(
            {'error': 'Missing data. Please fill out all fields.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    subject = f"New Contact Form Submission from {name}"
    email_message = f"""
    You have a new message from your website contact form:

    Name: {name}
    Email: {email}

    Message:
    {message}
    """
    recipient_list = [settings.EMAIL_HOST_USER]

    try:
        send_mail(subject, email_message, settings.EMAIL_HOST_USER, recipient_list)
        return Response({'success': 'Email sent successfully!'}, status=status.HTTP_200_OK)
    except Exception as e:
        # Log the error for debugging
        print(e)
        return Response(
            {'error': 'An error occurred while sending the email.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )