from django.shortcuts import render

def about_view(request):
    return render(request, 'about/about.html')  # Ensure you have a template called about.html
