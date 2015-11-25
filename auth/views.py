from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.views.generic.base import TemplateView
from django.contrib.auth import logout


class LoginView(TemplateView):
    def user_login(request):
        context = RequestContext(request)
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('login/login.html', {'disabled':True})
            else:
                 return render_to_response('login/login.html', {'invalid':True})

        else:
            return render_to_response('login/login.html', {}, context)


    def user_logout(request):
        logout(request)
        return HttpResponseRedirect('/')