from django.shortcuts import render

# Create your views here.
def main_url(request):
    """Main url"""

    return render(request, 'index.html')