import random
import string
from django.shortcuts import render

def password_generator(request):
    # Default values for the form
    password_length = int(request.GET.get('length', 12))  # Default length is 12
    include_uppercase = request.GET.get('uppercase')  # If not checked, this will be None
    include_numbers = request.GET.get('numbers')  # If not checked, this will be None
    include_special = request.GET.get('special')  # If not checked, this will be None

    # Base characters (lowercase letters only)
    characters = list(string.ascii_lowercase)

    # Add additional character sets based on user selection
    if include_uppercase:  # Include uppercase letters if checked
        characters.extend(list(string.ascii_uppercase))
    if include_numbers:  # Include numbers if checked
        characters.extend(list(string.digits))
    if include_special:  # Include special symbols if checked
        characters.extend(list(string.punctuation))

    # Generate random password
    password = ''.join(random.choices(characters, k=password_length))

    return render(request, 'polls/password.html', {'password': password})
