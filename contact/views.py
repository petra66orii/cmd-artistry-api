from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


@api_view(['POST'])
def contact_form(request):
    """
    Handles submission of the contact form and sends an email.
    """
    data = request.data
    name = data.get('name')
    email = data.get('email')
    
    subject = data.get('subject')
    service = data.get('service', 'Not specified') # Gets the service, or a default
    message = data.get('message')

    if not all([name, email, subject, message]):
        return Response(
            {'error': 'Missing data. Please fill out all required fields.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    email_subject = f"New Contact Form Submission: {subject}"
    
    email_message = f"""
    You have a new message from your website contact form:

    Name: {name}
    Email: {email}
    Service: {service}
    Subject: {subject}

    Message:
    {message}
    """
    recipient_list = [settings.EMAIL_HOST_USER]

    try:
        send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, recipient_list)
        return Response({'success': 'Email sent successfully!'}, status=status.HTTP_200_OK)
    except Exception as e:
        # Log the error for debugging
        print(e)
        return Response(
            {'error': 'An error occurred while sending the email.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@ensure_csrf_cookie
def get_csrf_token(request):
    """
    A view to send the CSRF token cookie to the frontend.
    """
    return JsonResponse({"message": "CSRF cookie set."})