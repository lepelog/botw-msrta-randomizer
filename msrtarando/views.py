from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
import random
from .chooser import Settings, Chooser
# Create your views here.
def run(request):
    settings=request.GET.get('settings',None)
    seed=request.GET.get('seed',-1)
    error=False
    try:
        seed=int(seed)
    except NumberFormatException:
        error=True
        seed=random.getrandbits(32)
    if seed<0:
        error=True
        seed=random.getrandbits(32)
    if settings==None:
        error=True
        settings=Settings()
    else:
        try:
            settings=Settings.from_setting_str(settings)
        except:
            settings=Settings()
            error=True
    if error:
        return HttpResponseRedirect('run?seed={}&settings={}'.format(seed,settings.to_setting_str()))
    route=Chooser(seed, settings).get_route()
    if route==None:
        return HttpResponseBadRequest('Not enough orbs to finish a run!')
    return render(request, 'run.html', {'run':route})
