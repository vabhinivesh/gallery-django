from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import MultipleImage


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        for image in images:
            MultipleImage.objects.create(images=image)

    images = MultipleImage.objects.all().order_by('-id')
    p = Paginator(images, 12)
    page = request.GET.get('page', 1)


    try:
        imagesRes = p.page(page)
    except PageNotAnInteger:
        imagesRes = p.page(1)
    except EmptyPage:
        imagesRes = p.page(p.num_pages)

    return render(request, 'index.html', {'images': imagesRes})
