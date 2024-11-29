from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Jenkins CI/CD! 🚀")
