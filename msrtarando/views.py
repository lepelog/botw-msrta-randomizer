from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
import random
from .chooser import Settings, Chooser
from .forms import SettingsForm

REGION_CONVERTION_FIELD=['akkala', 'central', 'dueling_peaks', 'eldin', 'faron', 'gerudo', 'hateno', 'hebra', 'lake', 'lanayru', 'ridgeland', 'tabantha', 'wasteland', 'woodland']
REGION_CONVERTION_SETTINGS=['Akkala', 'Central', 'Dueling Peaks', 'Eldin', 'Faron', 'Gerudo', 'Hateno', 'Hebra', 'Lake', 'Lanayru', 'Ridgeland', 'Tabantha', 'Wasteland', 'Woodland']

# Create your views here.
def run(request):
    setting_str=request.GET.get('settings',None)
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
    if setting_str==None:
        error=True
        settings=Settings()
    else:
        try:
            settings=Settings.from_setting_str(setting_str)
        except:
            settings=Settings()
            error=True
    if error:
        return HttpResponseRedirect('run?seed={}&settings={}'.format(seed,settings.to_setting_str()))
    route=Chooser(seed, settings).get_grouped_route()
    if route==None:
        return HttpResponseBadRequest('Not enough orbs to finish a run!')
    params=settings.to_display_dict()
    params.update({'run': route, 'setting_str':setting_str, 'seed':seed})
    return render(request, 'run.html', params)

def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            settings=Settings(blood_moon=cd['blood_moon'], camera=cd['camera'], gyro=cd['camera'], blessing=cd['blessing'],
              medoh=cd['medoh'], naboris=cd['naboris'], ruta=cd['ruta'], rudania=cd['rudania'], tos=[], allowed_regions=[])
            if cd['minortos']: settings.tos.append('minor')
            if cd['modesttos']: settings.tos.append('modest')
            if cd['majortos']: settings.tos.append('major')
            
            for i, region in enumerate(REGION_CONVERTION_FIELD):
                if cd[region]:
                    settings.allowed_regions.append(REGION_CONVERTION_SETTINGS[i])
            
            return HttpResponseRedirect('run?seed={}&settings={}'.format(random.getrandbits(32),settings.to_setting_str()))
    else:
        form = SettingsForm()
    return render(request, 'settings.html', {'form':form})

def index(request):
    return HttpResponseRedirect('settings')

def map(request):
    setting_str=request.GET.get('settings',None)
    seed=request.GET.get('seed',-1)
    try:
        seed=int(seed)
    except ValueError:
        return HttpResponseBadRequest("Bad seed given (not a number)")
    if seed<0:
        return HttpResponseBadRequest("Bad seed given (below 0)")
    if setting_str==None:
        return HttpResponseBadRequest("No settings given")
    else:
        try:
            settings=Settings.from_setting_str(setting_str)
        except:
            return HttpResponseBadRequest("Bad settings")
    route=Chooser(seed, settings).get_route()
    if route==None:
        return HttpResponseBadRequest('Not enough orbs to finish a run!')
    #Test for the divine beasts:
    naboris_chosen=False
    medoh_chosen=False
    ruta_chosen=False
    rudania_chosen=False
    for shrine in route:
        if shrine.orbs == 4:
            if shrine.name == "Vah Medoh": medoh_chosen=True
            if shrine.name == "Vah Naboris": naboris_chosen=True
            if shrine.name == "Vah Ruta": ruta_chosen=True
            if shrine.name == "Vah Rudania": rudania_chosen=True
            
    return render(request, 'map.html', {'locations':route, 'naboris_chosen':naboris_chosen, 'medoh_chosen':medoh_chosen,
                                        'ruta_chosen':ruta_chosen,'rudania_chosen':rudania_chosen})
