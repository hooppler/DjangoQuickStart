from django.shortcuts import render
from form_app.forms import TestForm
from form_app.models import TestModel
from django.http import HttpResponseRedirect

def form_app_view(request):
    if request.method == 'POST':
        print('SSSS')
        form = TestForm(request.POST)
        if form.is_valid():
            attribute1 = form.cleaned_data['attribute1']
            attribute2 = form.cleaned_data['attribute2']
            p = TestModel(attribute1=attribute1, attribute2=attribute2)
            p.save()
            #return HttpResponseRedirect('//')
    else:
        form = TestForm()
    
    tests = TestModel.objects.all()
    return render(request, 'form_app/form.html', {'form': form, 'tests': tests})
