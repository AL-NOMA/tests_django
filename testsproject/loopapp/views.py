from django.shortcuts import render

# Create your views here.

def forloop(request):
    template_name = 'loopapp/home.html'
    my_list = range(6, 15)
    context = {'my_list': my_list}
    return render(request, template_name, context)
