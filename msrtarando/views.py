from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
import random
from .chooser import Settings, Chooser
from .forms import SettingsForm
# Create your views here.
def run(request):
    settings=request.GET.get('settings',None)
    seed=request.GET.get('seed',-1)
    error=False
    try:
        seed=int(seed)
    except ValueError:
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

def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            #TODO regions
            settings=Settings(blood_moon=cd['blood_moon'], camera=cd['camera'], gyro=cd['camera'], blessing=cd['blessing'],
              medoh=cd['medoh'], naboris=cd['naboris'], ruta=cd['ruta'], rudania=cd['rudania'])
            return HttpResponseRedirect('run?seed={}&settings={}'.format(random.getrandbits(32),settings.to_setting_str()))
    else:
        form = SettingsForm()
    return render(request, 'settings.html', {'form':form})

def index(request):
    return HttpResponseRedirect('settings')
