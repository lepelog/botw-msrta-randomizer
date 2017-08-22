from django import forms

class SettingsForm(forms.Form):
    
    blood_moon=forms.BooleanField(label='Blood Moon Shrine', initial=False, required=False)
    gyro=forms.BooleanField(label='Apparatus Shrines', initial=True, required=False)
    blessing=forms.BooleanField(label='Blessing Shrines', initial=True, required=False)
    camera=forms.BooleanField(label='Camera Shrines', initial=True, required=False)
    CHOICES=[(0,'no'),(1,'maybe'),(2,'yes')]
    medoh = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Medoh', empty_value=-1, coerce=int, initial=1)
    naboris = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Naboris', empty_value=-1, coerce=int, initial=1)
    ruta = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Ruta', empty_value=-1, coerce=int, initial=1)
    rudania = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='Include Vah Rudania', empty_value=-1, coerce=int, initial=1)
