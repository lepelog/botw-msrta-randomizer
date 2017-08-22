class BeastShrine:
    """
    Superclass for both beasts and shrines
    """
    def __init__(self, id, name, orbs, region):
        self.id=id
        self.name=name
        self.orbs=orbs
        self.region=region
    
    
class Beast(BeastShrine):
    def __init__(self, id, name, region):
        super().__init__(id, name, 4, region)
        
    def __repr__(self):
        return 'Beast(id={}, name={!r}, region={!r})'\
            .format(self.id, self.name, self.region)

class Shrine(BeastShrine):
    def __init__(self, id, name, trial, quest, blessing, tos, beast, region):
        super().__init__(id, name, 1, region)
        self.trial=trial
        self.quest=quest
        self.blessing=blessing
        self.tos=tos
        self.beast=beast
    def __repr__(self):
        return 'Shrine(id={}, name={!r}, trial={!r}, quest={!r}, blessing={}, tos={!r}, beast={!r}, region={!r})'\
            .format(self.id, self.name, self.trial, self.quest, self.blessing, self.tos, self.beast, self.region)
            
#Copied and modified from https://github.com/rekyuu/msrta_gen/blob/master/lib/msrta_gen/definitions.ex
beasts=[
Beast(
    id=0,
    name='Vah Medoh',
    region='Tabantha'
),
Beast(
    id=1,
    name='Vah Naboris',
    region='Wasteland'
),
Beast(
    id=2,
    name='Vah Ruta',
    region='Lanayru'
),
Beast(
    id=3,
    name='Vah Rudania',
    region='Eldin'
)
]

shrines=[
Shrine(
    id=0,
    name='Tutsuwa Nima',
    trial='A Major Test of Strength',
    quest='The Spring of Power',
    blessing=False,
    tos='major',
    beast=None,
    region='Akkala'
),
Shrine(
    id=1,
    name='Dah Hesho',
    trial='A Minor Test of Strength',
    quest=None,
    blessing=False,
    tos='minor',
    beast=None,
    region='Akkala'
),
Shrine(
    id=2,
    name="Ke'nai Shakah",
    trial='A Modest Test of Strength',
    quest=None,
    blessing=False,
    tos='modest',
    beast=None,
    region='Akkala'
),
Shrine(
    id=3,
    name='Katosa Aug',
    trial='Katosa Aug Apparatus',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Akkala'
),
Shrine(
    id=4,
    name='Ritaag Zumo',
    trial="Ritaag Zumo's Blessing",
    quest='Into the Vortex',
    blessing=True,
    tos=None,
    beast=None,
    region='Akkala'
),
Shrine(
    id=5,
    name="Tu Ka'loh",
    trial="Tu Ka'loh's Blessing",
    quest='Trial of the Labyrinth',
    blessing=True,
    tos=None,
    beast=None,
    region='Akkala'
),
Shrine(
    id=6,
    name='Ze Kasho',
    trial='Ze Kasho Apparatus',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Akkala'
),
Shrine(
    id=7,
    name='Zuna Kai',
    trial="Zuna Kai's Blessing",
    quest="The Skull's Eye",
    blessing=True,
    tos=None,
    beast=None,
    region='Akkala'
),
Shrine(
    id=8,
    name="Saas Ko'sah",
    trial='A Major Test of Strength',
    quest=None,
    blessing=False,
    tos='major',
    beast=None,
    region='Central'
),
Shrine(
    id=9,
    name='Katah Chuki',
    trial='A Minor Test of Strength',
    quest=None,
    blessing=False,
    tos='minor',
    beast=None,
    region='Central'
),
Shrine(
    id=10,
    name='Noya Neha',
    trial='A Minor Test of Strength',
    quest=None,
    blessing=False,
    tos='minor',
    beast=None,
    region='Central'
),
Shrine(
    id=11,
    name='Namika Ozz',
    trial='A Modest Test of Strength',
    quest=None,
    blessing=False,
    tos='modest',
    beast=None,
    region='Central'
),
Shrine(
    id=12,
    name='Wahgo Katta',
    trial='Metal Connections',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Central'
),
Shrine(
    id=13,
    name='Rota Ooh',
    trial='Passing of the Gates',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Central'
),
Shrine(
    id=14,
    name='Kaya Wan',
    trial='Shields from Water',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Central'
),
Shrine(
    id=15,
    name="Kaam Ya'tak",
    trial='Test of Power',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Central'
),
Shrine(
    id=16,
    name='Hila Rao',
    trial='Drifting',
    quest='Watch Out for the Flowers',
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=17,
    name='Lakna Rokee',
    trial="Lakna Rokee's Blessing",
    quest='The Stolen Heirloom',
    blessing=True,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=18,
    name="Ta'loh Naeg",
    trial="Ta'loh Naeg's Teaching",
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=19,
    name='Ha Dahamar',
    trial='The Water Guides',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=20,
    name='Bosh Kala',
    trial='The Wind Guides You',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=21,
    name='Ree Dahee',
    trial='Timing is Critical',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=22,
    name='Toto Sah',
    trial='Toto Sah Apparatus',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=23,
    name='Shee Vaneer',
    trial='Twin Memories',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=24,
    name='Shee Venath',
    trial='Twin Memories',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Dueling Peaks'
),
Shrine(
    id=25,
    name='Qua Raym',
    trial='A Balanced Approach',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=26,
    name='Shora Hah',
    trial='Blue Flame',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=27,
    name='Gorae Torr',
    trial="Gorae Torr's Blessing",
    quest='The Gut Check Challenge',
    blessing=True,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=28,
    name='Kayra Mah',
    trial='Greedy Hill',
    quest="A Brother's Roast",
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=29,
    name="Mo'a Keet",
    trial='Metal Makes a Path',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=30,
    name='Tah Muhl',
    trial='Passing the Flame',
    quest='A Landscape of a Stable',
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=31,
    name='Sah Dahaj',
    trial='Power of Fire',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=32,
    name='Daqa Koh',
    trial='Stalled Flight',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Eldin'
),
Shrine(
    id=33,
    name="Shae Mo'sah",
    trial='Swinging Flames',
    quest=False,
    blessing=False,
    tos=False,
    beast=False,
    region='Eldin'
),
Shrine(
    id=34,
    name='Muwo Jeem',
    trial='A Modest Test of Strength',
    quest=None,
    blessing=False,
    tos='modest',
    beast=None,
    region='Faron'
),
Shrine(
    id=35,
    name='Yah Rin',
    trial='A Weighty Decision',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=36,
    name='Korgu Chideh',
    trial="Korgu Chideh's Blessing",
    quest='Stranded on Eventide',
    blessing=True,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=37,
    name='Shai Utoh',
    trial='Halt the Tilt',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=38,
    name='Shoda Sah',
    trial='Impeccable Timing',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=39,
    name='Kah Yah',
    trial='Quick Thinking',
    quest='A Fragmented Monument',
    blessing=False,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=40,
    name='Qukah Nata',
    trial="Qukah Nata's Blessing",
    quest='A Song of Storms',
    blessing=True,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=41,
    name='Tawa Jinn',
    trial="Tawa Jinn's Blessing",
    quest='The Three Giant Brothers',
    blessing=True,
    tos=None,
    beast=None,
    region='Faron'
),
Shrine(
    id=42,
    name='Kema Kosassa',
    trial='A Major Test of Strength',
    quest=None,
    blessing=False,
    tos='major',
    beast=None,
    region='Gerudo'
),
Shrine(
    id=43,
    name='Dah Kaso',
    trial='A Minor Test of Strength',
    quest=None,
    blessing=False,
    tos='minor',
    beast=None,
    region='Gerudo'
),
Shrine(
    id=44,
    name='Sasa Kai',
    trial='A Modest Test of Strength',
    quest='Sign of the Shadow',
    blessing=False,
    tos='modest',
    beast=None,
    region='Gerudo'
),
Shrine(
    id=45,
    name='Joloo Nah',
    trial='Joloo Nah Apparatus',
    quest='Test of Will',
    blessing=False,
    tos=None,
    beast=None,
    region='Gerudo'
),
Shrine(
    id=46,
    name='Keeha Yoog',
    trial="Keeha Yoog's Blessing",
    quest='Cliffside Etchings',
    blessing=True,
    tos=None,
    beast=None,
    region='Gerudo'
),
Shrine(
    id=47,
    name='Kuh Takkar',
    trial='Melting Ice Hazard',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Gerudo'
),
Shrine(
    id=48,
    name='Sho Dantu',
    trial='Two Bombs',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Gerudo'
),
Shrine(
    id=49,
    name='Chaas Qeta',
    trial='A Major Test of Strength',
    quest=None,
    blessing=False,
    tos='major',
    beast=None,
    region='Hateno'
),
Shrine(
    id=50,
    name='Mezza Lo',
    trial='Ancient Trifecta',
    quest='The Crowned Beast',
    blessing=False,
    tos=None,
    beast=None,
    region='Hateno'
),
Shrine(
    id=51,
    name="Jitan Sa'mi",
    trial="Jitan Sa'mi's Blessing",
    quest='The Spring of Wisdom',
    blessing=True,
    tos=None,
    beast=None,
    region='Hateno'
),
Shrine(
    id=52,
    name='Myahm Agana',
    trial='Myahm Agana Apparatus',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hateno'
),
Shrine(
    id=53,
    name="Tahno O'ah",
    trial="Tahno O'ah's Blessing",
    quest='Secret of the Cedars',
    blessing=True,
    tos=None,
    beast=None,
    region='Hateno'
),
Shrine(
    id=54,
    name="Dow Na'eh",
    trial='Three Boxes',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hateno'
),
Shrine(
    id=55,
    name='Kam Urog',
    trial='Trial of Passage',
    quest='The Cursed Statue',
    blessing=False,
    tos=None,
    beast=None,
    region='Hateno'
),
Shrine(
    id=56,
    name='Goma Asaagh',
    trial='A Major Test of Strength',
    quest=None,
    blessing=False,
    tos='major',
    beast=None,
    region='Hebra'
),
Shrine(
    id=57,
    name='Hia Miu',
    trial='A Major Test of Strength',
    quest=None,
    blessing=False,
    tos='major',
    beast=None,
    region='Hebra'
),
Shrine(
    id=58,
    name='Mozo Shenno',
    trial='A Major Test of Strength',
    quest='The Bird in the Mountains',
    blessing=False,
    tos='major',
    beast=None,
    region='Hebra'
),
Shrine(
    id=59,
    name='Dunba Taag',
    trial='Build and Release',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=60,
    name='Rin Oyaa',
    trial='Directing the Wind',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=61,
    name='Lanno Kooh',
    trial="Lanno Kooh's Blessing",
    quest=None,
    blessing=True,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=62,
    name='Rok Uwog',
    trial='Power of Reach',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=63,
    name='Qaza Tokki',
    trial="Qaza Tokki's Blessing",
    quest='Trial on the Cliff',
    blessing=True,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=64,
    name='Shada Naw',
    trial='Red Giveaway',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=65,
    name='Sha Gehma',
    trial='Shift and Lock',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=66,
    name='Maka Rah',
    trial='Steady Thy Heart',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=67,
    name="Gee Ha'rah",
    trial='Tandem',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=68,
    name='To Quomo',
    trial="To Quomo's Blessing",
    quest=None,
    blessing=True,
    tos=None,
    beast=None,
    region='Hebra'
),
Shrine(
    id=69,
    name='Pumaag Nitae',
    trial='A Minor Test of Strength',
    quest=None,
    blessing=False,
    tos='minor',
    beast=None,
    region='Lake'
),
Shrine(
    id=70,
    name='Shoqa Tatone',
    trial='A Modest Test of Strength',
    quest='Guardian Slideshow',
    blessing=False,
    tos='modest',
    beast=None,
    region='Lake'
),
Shrine(
    id=71,
    name='Ishto Soh',
    trial="Bravery's Grasp",
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lake'
),
Shrine(
    id=72,
    name="Ka'o Makagh",
    trial='Metal Doors Open the Way',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lake'
),
Shrine(
    id=73,
    name='Shae Katha',
    trial="Shae Katha's Blessing",
    quest="The Serpent's Jaws",
    blessing=True,
    tos=None,
    beast=None,
    region='Lake'
),
Shrine(
    id=74,
    name='Ya Naga',
    trial='Shatter the Heavens',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lake'
),
Shrine(
    id=75,
    name='Soh Kofi',
    trial='A Minor Test of Strength',
    quest=None,
    blessing=False,
    tos='minor',
    beast=None,
    region='Lanayru'
),
Shrine(
    id=76,
    name='Dagah Keek',
    trial="Dagah Keek's Blessing",
    quest='The Ceremonial Song',
    blessing=True,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=77,
    name='Kah Mael',
    trial='Drop and Rise',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=78,
    name='Rucco Maag',
    trial='Five Flames',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=79,
    name="Ne'ez Yohma",
    trial='Pushing Power',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=80,
    name='Shai Yota',
    trial="Shai Yota's Blessing",
    quest='Master of the Wind',
    blessing=True,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=81,
    name='Sheh Rata',
    trial='Speed of Light',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=82,
    name='Daka Tuss',
    trial='Sunken Scoop',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Lanayru'
),
Shrine(
    id=83,
    name='Mijah Rokee',
    trial='A Modest Test of Strength',
    quest='Under a Red Moon',
    blessing=False,
    tos='modest',
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=84,
    name='Shae Loya',
    trial='Aim for the Moment',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=85,
    name='Toh Yahsa',
    trial='Buried Secrets',
    quest='Trial of Thunder',
    blessing=False,
    tos=None,
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=86,
    name="Maag No'rah",
    trial="Maag No'rah's Blessing",
    quest=None,
    blessing=True,
    tos=None,
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=87,
    name='Sheem Dagoze',
    trial='Moving in Parallel',
    quest='The Two Rings',
    blessing=False,
    tos=None,
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=88,
    name='Mogg Latan',
    trial='Synced Swing',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=89,
    name='Zalta Wa',
    trial='Two Orbs to Guide You',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Ridgeland'
),
Shrine(
    id=90,
    name="Tena Ko'sah",
    trial='A Major Test of Strength',
    quest=None,
    blessing=False,
    tos='major',
    beast=None,
    region='Tabantha'
),
Shrine(
    id=91,
    name='Bareeda Naag',
    trial='Cannon',
    quest='The Ancient Rito Song',
    blessing=False,
    tos=None,
    beast=None,
    region='Tabantha'
),
Shrine(
    id=92,
    name='Sha Warvo',
    trial='Path of Hidden Winds',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Tabantha'
),
Shrine(
    id=93,
    name='Voo Lota',
    trial='The Winding Route',
    quest="Recital at Warbler's Nest",
    blessing=False,
    tos=None,
    beast='medoh',
    region='Tabantha'
),
Shrine(
    id=94,
    name='Kah Okeo',
    trial='Wind Guide',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Tabantha'
),
Shrine(
    id=95,
    name="Akh Va'quot",
    trial='Windmills',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Tabantha'
),
Shrine(
    id=96,
    name='Kema Zoos',
    trial='A Delayed Puzzle',
    quest='The Silent Swordswomen',
    blessing=False,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=97,
    name='Dila Maag',
    trial="Dila Maag's Blessing",
    quest='The Desert Labyrinth',
    blessing=True,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=98,
    name='Dako Tah',
    trial='Electric Path',
    quest='The Eye of the Sandstorm',
    blessing=False,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=99,
    name="Korsh O'hu",
    trial="Korsh O'hu's Blessing",
    quest='The Seven Heroines',
    blessing=True,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=100,
    name='Misae Suma',
    trial="Misae Suma's Blessing",
    quest='The Perfect Drink',
    blessing=True,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=101,
    name='Jee Noh',
    trial='On the Move',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=102,
    name='Kay Noh',
    trial='Power of Electricity',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=103,
    name='Raqa Zunzo',
    trial="Raqa Zunzo's Blessing",
    quest='The Undefeated Champ',
    blessing=True,
    tos=None,
    beast='naboris',
    region='Wasteland'
),
Shrine(
    id=104,
    name='Suma Sahma',
    trial="Suma Sahma's Blessing",
    quest='Secret of the Snowy Peaks',
    blessing=True,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=105,
    name='Hawa Koth',
    trial='The Current Solution',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=106,
    name='Daqo Chisay',
    trial='The Whole Picture',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=107,
    name='Tho Kayu',
    trial="Tho Kayu's Blessing",
    quest=None,
    blessing=True,
    tos=None,
    beast=None,
    region='Wasteland'
),
Shrine(
    id=108,
    name='Daag Chokah',
    trial="Daag Chokah's Blessing",
    quest='The Lost Pilgrimage',
    blessing=True,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=109,
    name='Monya Toma',
    trial='Drawing Parabolas',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=110,
    name='Keo Ruug',
    trial='Fateful Stars',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=111,
    name='Ketoh Wawai',
    trial="Ketoh Wawai's Blessing",
    quest='Shrouded Shrine',
    blessing=True,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=112,
    name='Kuhn Sidajj',
    trial="Kuh Sidajj's Blessing",
    quest='Trial of Second Sight',
    blessing=True,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=113,
    name='Maag Halan',
    trial="Maag Halan's Blessing",
    quest='The Test of Wood',
    blessing=True,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=114,
    name='Rona Kachta',
    trial="Rona Kachta's Blessing",
    quest=None,
    blessing=True,
    tos=None,
    beast=None,
    region='Woodland'
),
Shrine(
    id=115,
    name='Mirro Shaz',
    trial='Tempered Power',
    quest=None,
    blessing=False,
    tos=None,
    beast=None,
    region='Woodland'
)
]
