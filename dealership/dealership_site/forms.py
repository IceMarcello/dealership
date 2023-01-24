from django import forms
import calculation
from forex_python.converter import CurrencyRates
from .models import Post, Image


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "price",
            "odo",
            "capacity",
            "power",
            "year",
            "fuel",
            "date_posted",
            "status",
            "content",
            "mainimage",
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )
    class Meta:
        model = Image
        fields = ("image",)


