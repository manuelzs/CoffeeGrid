from django.shortcuts import render_to_response

def dashboard(request):
    rsp_dict = {}
    rsp_dict['user'] = request.user
    return render_to_response('dashboard.html',rsp_dict)
