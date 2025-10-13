# from django import forms

# from .models import Comment

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ["post"]
#         labels = {
#             "user_name": "Your Name",
#             "user_email": "Your Email",
#             "text": "Your Comment"
#         }  
        
        
from django import forms

from .models import Comment
from .models import Contact

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # Note: If your Contact model doesn't have a 'post' field, 
        # consider using 'fields = ["user_name", "user_email", "phone_number"]' 
        # instead of 'exclude = ["post"]'.
        exclude = ["post"] 
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            # CORRECTED: The key must match the model field name (e.g., 'phone_number').
            "phone_number": "Your Phone" 
        }