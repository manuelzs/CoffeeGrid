# Create your views here.
from django.shortcuts import render_to_response

def profile(request, username):
    return render_to_response('userprofile.html')