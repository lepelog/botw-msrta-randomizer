from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
import random
from .chooser import Settings, Chooser
from .forms import SettingsForm

REGION_CONVERTION_FIELD=['akkala', 'central', 'dueling_peaks', 'eldin', 'faron', 'gerudo', 'hateno', 'hebra', 'lake', 'lanayru', 'ridgeland', 'tabantha', 'wasteland', 'woodland']
REGION_CONVERTION_SETTINGS=['Akkala', 'Central', 'Dueling Peaks', 'Eldin', 'Faron', 'Gerudo', 'Hateno', 'Hebra', 'Lake', 'Lanayru', 'Ridgeland', 'Tabantha', 'Wasteland', 'Woodland']
# helper
def get_chooser_or_response(request, strict=False):
    """
    get the route and fills illegal params with defaults if strict is false, otherwise
    fails with status codes. Only if all params were correct a Chooser-object is returned
    Returns:
        Chooser or HttpResponse subclass
    """
    setting_str=request.GET.get('settings',None)
    seed=request.GET.get('seed',-1)
    error = False
    try:
        seed=int(seed)
    except ValueError:
        if strict:
            return HttpResponseBadRequest("Bad seed given (not a number)")
        else:
            error=True
            seed=random.getrandbits(32)
    if seed<0:
        if strict:
            return HttpResponseBadRequest("Bad seed given (below 0)")
        else:
            error=True
            seed=random.getrandbits(32)
    if setting_str==None:
        if strict:
            return HttpResponseBadRequest("No settings given")
        else:
            error=True
            settings=Settings()
    else:
        try:
            settings=Settings.from_setting_str(setting_str)
        except:
            if strict:
                return HttpResponseBadRequest("Bad settings")
            else:
                settings=Settings()
                error=True
    if error:
        return HttpResponseRedirect('run?seed={}&settings={}'.format(seed,settings.to_setting_str()))
    return Chooser(seed, settings)

# Create your views here.
def run(request):
    resp = get_chooser_or_response(request)
    if type(resp) == Chooser:
        route=resp.get_grouped_route()
    else:
        return resp
    if route==None:
        return HttpResponseBadRequest('Not enough orbs to finish a run!')
    params = resp.settings.to_display_dict()
    #used for the next run
    newseed = random.getrandbits(32)
    params.update({'run': route, 'setting_str':resp.settings.to_setting_str(), 'seed':resp.seed, 'newseed':newseed})
    return render(request, 'run.html', params)

def card(request):
    resp = get_chooser_or_response(request, strict=True)
    if type(resp) == Chooser:
        route=resp.get_route()
    else:
        return resp
    if route==None:
        return HttpResponseBadRequest('Not enough orbs to finish a run!')
    
    route = sorted(route, key=
        lambda beast_shrine: ('0' if beast_shrine.orbs == 4 else beast_shrine.region) + beast_shrine.name)
    table_run = list()
    i = 0
    while i < len(route):
        if (i % 3) == 0:
            curr_row = list()
            table_run.append(curr_row)
        curr_row.append(route[i])
        i+=1
    return render(request, 'card.html', {'run':table_run})


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
    resp = get_chooser_or_response(request, strict=True)
    if type(resp) == Chooser:
        route=resp.get_route()
    else:
        return resp
    if route==None:
        return HttpResponseBadRequest('Not enough orbs to finish a run!')
    
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