from django import forms
from form_utils.forms import BetterForm

class SettingsForm(BetterForm):
    
    blood_moon=forms.BooleanField(label='Blood Moon Shrine', initial=False, required=False)
    gyro=forms.BooleanField(label='Apparatus Shrines', initial=True, required=False)
    blessing=forms.BooleanField(label='Blessing Shrines', initial=True, required=False)
    camera=forms.BooleanField(label='Camera Shrines', initial=True, required=False)
    CHOICES=[(0,'no'),(1,'maybe'),(2,'yes')]
    medoh = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Medoh', empty_value=-1, coerce=int, initial=1)
    naboris = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Naboris', empty_value=-1, coerce=int, initial=1)
    ruta = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Ruta', empty_value=-1, coerce=int, initial=1)
    rudania = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Rudania', empty_value=-1, coerce=int, initial=1)
    minortos = forms.BooleanField(label='minor', initial=True, required=False)
    modesttos = forms.BooleanField(label='modest', initial=True, required=False)
    majortos = forms.BooleanField(label='major', initial=True, required=False)
    
    dueling_peaks=forms.BooleanField(label='Dueling Peaks', initial=True, required=False)
    gerudo=forms.BooleanField(label='Gerudo', initial=True, required=False)
    hebra=forms.BooleanField(label='Hebra', initial=True, required=False)
    lake=forms.BooleanField(label='Lake', initial=True, required=False)
    woodland=forms.BooleanField(label='Woodland', initial=True, required=False)
    ridgeland=forms.BooleanField(label='Ridgeland', initial=True, required=False)
    tabantha=forms.BooleanField(label='Tabantha', initial=True, required=False)
    hateno=forms.BooleanField(label='Hateno', initial=True, required=False)
    eldin=forms.BooleanField(label='Eldin', initial=True, required=False)
    akkala=forms.BooleanField(label='Akkala', initial=True, required=False)
    central=forms.BooleanField(label='Central', initial=True, required=False)
    lanayru=forms.BooleanField(label='Lanayru', initial=True, required=False)
    faron=forms.BooleanField(label='Faron', initial=True, required=False)
    wasteland=forms.BooleanField(label='Wasteland', initial=True, required=False)
    
    class Meta:
        fieldsets = [('Include specific Shrines', {'fields': ['blood_moon','gyro','blessing','camera']}),
                     ('Divine Beasts', {'fields': ['medoh', 'naboris', 'ruta','rudania'],
                                   'classes': []}),
                     ('Include Tests of Strength', {'fields':['minortos','modesttos','majortos'], 'classes':['tos']}),
                     ('Include Regions', {'fields':['akkala', 'central', 'dueling_peaks', 'eldin', 'faron', 'gerudo', 'hateno', 'hebra', 'lake', 'lanayru', 'ridgeland', 'tabantha', 'wasteland', 'woodland']})]
        row_attrs = {}

