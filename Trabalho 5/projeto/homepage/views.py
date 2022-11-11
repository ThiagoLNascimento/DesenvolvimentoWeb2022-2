from django.shortcuts import render
from homepage.models import Banner, CardFront, Carousel

def homepage(request):
    carousel = Carousel.objects.all()
    banner = Banner.objects.all()
    cardFront = CardFront.objects.all()
    return render(request, 'homepage/', { 'carousel': carousel, 'banner':banner, 'cards':cardFront })