import random
from .nice_shrines import beasts, shrines, BeastShrine
from collections import defaultdict
import base64

class Chooser:
    
    def __init__(self,seed,settings):
        self.seed=seed
        self.settings=settings
        
    def get_route(self):
        """
        Returns a route for the seed and the settings
        Returns:
            list of tuple (region, list with shrinebeasts)
            None if there are not enough available orbs in the settings
        """
        self.rand=random.Random(self.seed)
        orbcount=0
        
        #Special shrine ids
        #(stolen heilroom, fragmented monument, guardian slideshow)
        camera_ids={39,17,70}
        #Apparatus
        gyro_ids={3,6,22,45,52}
        #Apply settings:
        def shrinefilter(shrine):
            #Filter by region
            return ((shrine.region in self.settings.allowed_regions)
            #Filter blessing
            and (self.settings.blessing or not shrine.blessing)
            #Filter tos
            and (shrine.tos==None or shrine.tos in self.settings.tos)
            #Filter camera
            and (self.settings.camera or not shrine.id in camera_ids)
            #Filter gyro
            and (self.settings.gyro or not shrine.id in gyro_ids)
            #Filter blood moon
            and (self.settings.blood_moon or not shrine.id == 83)
            #Filter medoh shrine
            and (self.settings.medoh != 0 or not shrine.id == 93)
            #Filter naboris shrine
            and (self.settings.naboris != 0 or not shrine.id == 103))
        
        shrines_remaining=list(filter(shrinefilter, shrines))
        
        beasts_remaining=[]
        choosen=[]
        if self.settings.medoh==1:
            beasts_remaining.append(beasts[0])
        elif self.settings.medoh==2:
            choosen.append(beasts[0])
            orbcount+=4
        
        if self.settings.naboris==1:
            beasts_remaining.append(beasts[1])
        elif self.settings.naboris==2:
            choosen.append(beasts[1])
            orbcount+=4
        
        if self.settings.ruta==1:
            beasts_remaining.append(beasts[2])
        elif self.settings.ruta==2:
            choosen.append(beasts[2])
            orbcount+=4
        
        if self.settings.rudania==1:
            beasts_remaining.append(beasts[3])
        elif self.settings.rudania==2:
            choosen.append(beasts[3])
            orbcount+=4
       
        #Test if we have enough orbs to finish
        if 36>(len(shrines_remaining)+len(beasts_remaining)*4+len(choosen)*4):
            return None
        while True:
            while orbcount<36:
                if orbcount<=32:
                    num=self.rand.randrange(0, len(beasts_remaining)*4+len(shrines_remaining))
                    if num<len(beasts_remaining)*4:
                        #divine beast selected
                        selected=beasts_remaining[num//4]
                        choosen.append(selected)
                        beasts_remaining.remove(selected)
                        orbcount+=4
                    else:
                        #shrine selected
                        selected=shrines_remaining[num-len(beasts_remaining)*4]
                        choosen.append(selected)
                        shrines_remaining.remove(selected)
                        orbcount+=1
                elif len(shrines_remaining)==0:
                    #This should not happen
                    return None
                else:
                    num=self.rand.randrange(0, len(shrines_remaining))
                    #shrine selected
                    selected=shrines_remaining[num]
                    choosen.append(selected)
                    shrines_remaining.remove(selected)
                    orbcount+=1
            #Check for shrines that depend on divine beasts
            #Undefeated Champ
            if not 1 in (beast.id for beast in choosen if beast.orbs==4):
                for shrine in choosen:
                    if shrine.id==103:
                        choosen.remove(shrine)
                        orbcount-=1
            
            #Recital at Warbler's Nest
            if not 0 in (beast.id for beast in choosen if beast.orbs==4):
                for shrine in choosen:
                    if shrine.id==93:
                        choosen.remove(shrine)
                        orbcount-=1
            
            if orbcount==36:
                break
                        
        
        #Group by region
        grouped_choosen=defaultdict(list)
        for chos in choosen: grouped_choosen['Divine Beast'].append(chos) if chos.orbs==4 else grouped_choosen[chos.region].append(chos)
        #Add the heros sword
        grouped_choosen['Woodland'].append(BeastShrine(-1, "The Hero's Sword", 4, "Woodland"))
        grouped_choosen=sorted(grouped_choosen.items(),key=lambda kv: '0' if kv[0]=='Divine Beast' else kv[0])
        return grouped_choosen

class Settings:
    all_regions=['Dueling Peaks', 'Gerudo', 'Hebra', 'Lake', 'Woodland', 'Ridgeland', 'Tabantha', 'Hateno', 'Eldin', 'Akkala', 'Central', 'Lanayru', 'Faron', 'Wasteland']
    tests_of_strength=['minor','modest','major']
    def __init__(self, allowed_regions=all_regions, blood_moon=False, tos=tests_of_strength, gyro=True, camera=True, blessing=True, medoh=1, naboris=1, ruta=1, rudania=1):
        """
        Construct the settings for an awesome MSRTA-Rando!
        Params:
            allowed_regions (set): Set including all allowed regions
            blood_moon (bool): Wether or no include the blood moon shrine
            tos (set): all selected tos-variants, minor, modest and/or major
            gyro (bool): Include shrines requiring gyro-control
            camera (bool): Include shrines requiring the camera
            blessing (bool): Include blessing shrines
            medoh (int): 0=excluded, 1=pickable (random), 2=included
            naboris (int): same as medoh
            ruta (int): same as medoh
            rudania (int): same as medoh
        """
        self.allowed_regions=allowed_regions
        self.blood_moon=blood_moon
        self.tos=tos
        self.gyro=gyro
        self.camera=camera
        self.blessing=blessing
        self.medoh=medoh
        self.naboris=naboris
        self.ruta=ruta
        self.rudania=rudania
    
    def to_display_dict(self):
        special=[]
        if self.blood_moon: special.append('Blood Moon Shrine')
        if self.gyro: special.append('Apparatus Shrines')
        if self.blessing: special.append('Blessing Shrines')
        if self.camera: special.append('Camera Shrines')
        dbchoices=['no', 'maybe', 'yes']
        return {'regions': ', '.join(sorted(self.allowed_regions)), 'tos': ', '.join(self.tos), 'special_shrines': ', '.join(special),
          'medoh': dbchoices[self.medoh], 'naboris': dbchoices[self.naboris], 'ruta': dbchoices[self.ruta], 'rudania': dbchoices[self.rudania]}
    
    def to_setting_str(self):
        """
        Serialization
        """
        binaryopts = tuple(True if region in self.allowed_regions else False for region in self.all_regions)+(self.blood_moon, self.gyro, self.camera, self.blessing, 'minor' in self.tos, 'modest' in self.tos, 'major' in self.tos)
        base=1
        erg=b''
        current=0
        for opt in binaryopts:
            if base>128:
                erg+=bytes((current,))
                current=0
                base=1
            if opt:
                current+=base
            base*=2
        erg+=bytes((current,))
        erg+=bytes((self.medoh+self.naboris*0b100+self.ruta*0b10000+self.rudania*0b1000000,))
        return base64.urlsafe_b64encode(erg).decode('ascii').strip('=')
       
    @staticmethod    
    def from_setting_str(string):
        """
        Deserialization
        """
        string+='='*((4-len(string)%4)%4)
        settings=Settings()
        decoded=base64.urlsafe_b64decode(string.encode('ascii'))
        binaryopts=decoded[0:-1]
        beastopts=decoded[-1]
        settings.medoh=beastopts&0b11
        settings.naboris=(beastopts&0b1100)>>2
        settings.ruta=(beastopts&0b110000)>>4
        settings.rudania=(beastopts&0b11000000)>>6
        
        current=0
        base=1
        boollist=[]
        while current<len(binaryopts):
            boollist.append((binaryopts[current]&base)!=0)
            base*=2
            if base>128:
                base=1
                current+=1
        regionopts=boollist[0:len(Settings.all_regions)]
        otheropts=boollist[len(Settings.all_regions):len(Settings.all_regions)+4]
        tosopts=boollist[len(Settings.all_regions)+4:len(Settings.all_regions)+4+len(Settings.tests_of_strength)]
        settings.blood_moon=otheropts[0]
        settings.gyro=otheropts[1]
        settings.camera=otheropts[2]
        settings.blessing=otheropts[3]
        settings.allowed_regions=[]
        for i,region in enumerate(regionopts):
            if region:
                settings.allowed_regions.append(Settings.all_regions[i])
        settings.tos=[]
        for i, tos in enumerate(tosopts):
            if tos:
                settings.tos.append(Settings.tests_of_strength[i])
        return settings
        

def print_grouped_choosen(choosen):
    for k,v in choosen:
        if k=='Divine Beast':
            print('Divine Beast')
        else:
            print("\nRegion: "+k)
        for shrinebeast in v:
            if shrinebeast.orbs==4:
                print('-Divine Beast {}'.format(shrinebeast.name))
            elif shrinebeast.quest==None:
                print('-{} - {}'.format(shrinebeast.trial, shrinebeast.name))
            else:
                print('-{} - {} - {}'.format(shrinebeast.trial, shrinebeast.name, shrinebeast.quest))

#if __name__=='__main__':
#    import sys
#    if len(sys.argv)==2:
#        seed=int(sys.argv[1])
#    else:
#        seed=random.getrandbits(32)
#    print_grouped_choosen(Chooser(seed,Settings()).get_route())

#class Settings:
#    def __init__(self):
