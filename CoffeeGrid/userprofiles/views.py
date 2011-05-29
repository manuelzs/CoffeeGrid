# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

def profile(request, username):
    puser = get_object_or_404(User, username=username)
    response_dict = {}
    user = request.user
    response_dict['profile_user'] = puser
    
    return render_to_response('userprofile.html', response_dict)