from django.forms import ModelForm
from .models import Wishlist

class WishlistForm(ModelForm):
    class Meta:
        model=Wishlist
        fields=['movie_name']