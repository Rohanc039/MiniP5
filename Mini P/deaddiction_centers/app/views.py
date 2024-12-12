
from django.shortcuts import render
from .models import DeAddictionCenter


def homepg(request):
    return render(request,"app/homepg.html")




def center_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        centers = DeAddictionCenter.objects.filter(state__icontains=query)  # Case-insensitive search
    else:
        centers = DeAddictionCenter.objects.all()
    return render(request, 'app/center_list.html', {'centers': centers, 'query': query})
