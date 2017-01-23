import time
import sys
import random
from random import randint
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
print "Hello new Trainer!"
time.sleep(1.6)
print "I am your Kanto region Pokédex"
time.sleep(2.3)
print "I am a Pokédex, a Pokédex is a database of Pokémon."
time.sleep(3)
print "This  Pokédex is specific for Pokémon in the Kanto region."
time.sleep(3.5)
print "All Pokémon have an assigned number that corresponds to that certain Pokémon species"
time.sleep(4)
print "For example, Pikachu is the 25th entry in the Pokédex!"
time.sleep(3)
print "When you enter a Pokémon's # it will bring up all available information on that Pokémon"
time.sleep(5)
print "Please enter a number between 1 and 151 to learn about the Pokémon associated to that number."
time.sleep(0.5)
print "Enter 0 for a random Pokémon"

Bulbasaur = """0001 Bulbasaur
            Type: Grass | Poison
            The Seed Pokémon
            Bulbasaur can be seen napping in bright sunlight. There
            is a seed on its back. By soaking up the sun's rays, 
            the seed grows progressively larger.
            Evolves into Ivysaur."""
Ivysaur = """0002 Ivysaur
          Type: Grass | Poison
          The Seed Pokémon
          There is a bud on this Pokémon's back. To support its
          weight, Ivysaur's legs and trunk grow thick and strong. 
          If it starts spending more time lying in the sunlight, 
          it's a sign that the bud will bloom into a large flower soon.
          Evolves into Venasaur"""
Venasaur = """0003 Venasaur
           Type: Grass | Poison
           The Seed Pokémon
           There is a large flower on Venusaur's back. 
           The flower is said to take on vivid colors 
           if it gets plenty of nutrition and sunlight. 
           The flower's aroma soothes the emotions of people."""
Charmander = """0004 Charmander
             Type: Fire
             The Lizard Pokémon
             The flame that burns at the tip of its tail 
             is an indication of its emotions. The flame 
             wavers when Charmander is enjoying itself. 
             If the Pokémon becomes enraged, the flame burns fiercely.
             Evolves into Charmeleon"""
Charmeleon = """0005 Charmeleon
             Type: Fire
             The Flame Pokémon
             Charmeleon mercilessly destroys its foes using its 
             sharp claws. If it encounters a strong foe, it turns 
             aggressive. In this excited state, the flame at the tip
             of its tail flares with a bluish white color.
             Evolves into Charizard."""
Charizard = """0006 Charizard
            Type: Fire | Flying
            The Flame Pokémon
            Charizard flies around the sky in search of powerful 
            opponents. It breathes fire of such great heat that 
            it melts anything. However, it never turns its fiery 
            breath on any opponent weaker than itself."""
Squirtle = """0007 Squirtle
           Type: Water
           The Tiny Turtle Pokémon
           Squirtle's shell is not merely used for protection. 
           The shell's rounded shape and the grooves on its 
           surface help minimize resistance in water, 
           enabling this Pokémon to swim at high speeds.
           Evolves into Wartortle."""
Wartortle = """0008 Wartortle
            Type: Water
            The Turtle Pokémon
            Its tail is large and covered with a rich, 
            thick fur. The tail becomes increasingly deeper 
            in color as Wartortle ages. The scratches on its 
            shell are evidence of this Pokémon's toughness as a battler.
            Evolves into Blastoise."""
Blastoise = """0009 Blastoise
            Type: Water
            The Shellfish Pokémon
            Blastoise has water spouts that protrude from its 
            shell. The water spouts are very accurate. They can
            shoot bullets of water with enough accuracy to strike
            empty cans from a distance of over 160 feet."""
Caterpie = """0010 Caterpie
           Type: Bug
           The Worm Pokémon
           	Caterpie has a voracious appetite. It 
           	can devour leaves bigger than its body 
           	right before your eyes. From its antenna, 
           	this Pokémon releases a terrifically strong odor.
           	Evolves into Metapod."""
Metapod = """0011 Metapod
          Type: Bug
          The Cocoon Pokémon
          The shell covering this Pokémon’s body is as 
          hard as an iron slab. Metapod does not move 
          very much. It stays still because it is preparing
          its soft innards for evolution inside the hard shell.
          Evolves into Butterfree."""
Butterfree = """0012 Butterfree
             Type: Bug | Flying
             The Butterfly Pokémon
             Butterfree has a superior ability to search for 
             delicious honey from flowers. It can even
             search out, extract, and carry honey from flowers
             that are blooming over six miles from its nest."""
Weedle = """0013 Weedle
         Type: Bug
         The Hairy Bug Pokémon
         Weedle has an extremely acute sense of smell. 
         It is capable of distinguishing its favorite 
         kinds of leaves from those it dislikes just by 
         sniffing with its big red proboscis (nose).
         Evolves into Kakuna."""
Kakuna = """0014 Kakuna
         Type: Bug | Poison
         The Cocoon Pokémon
         Kakuna remains virtually immobile as it clings
         to a tree. However, on the inside, it is 
         extremely busy as it prepares for its coming 
         evolution. This is evident from how 
         hot the shell becomes to the touch.
         Evolves into Beedrill."""
Beedrill = """0015 Beedrill
           Type: Bug | Poison
           The Poison Bee Pokémon
           Beedrill is extremely territorial. 
           No one should ever approach its nest—this 
           is for their own safety. If angered, 
           they will attack in a furious swarm."""
Pidgey = """0016 Pidgey
         Type: Normal | Flying
         The Tiny Bird Pokémon
         Pidgey has an extremely sharp sense of direction. 
         It is capable of unerringly returning home 
         to its nest, however far it may be 
         removed from its familiar surroundings.
         Evolves into Pidgeotto."""
Pidgeotto ="""0017 Pidgeotto
           Type: Normal | Flying
           The Bird Pokémon
           Pidgeotto claims a large area as its own 
           territory. This Pokémon flies around, 
           patrolling its living space. If its territory 
           is violated, it shows no mercy in thoroughly 
           punishing the foe with its sharp claws.
           Evolves into Pidgeot."""
Pidgeot ="""0018 Pidgeot
         Type: Normal | Flying
         The Bird Pokémon
         This Pokémon has a dazzling plumage of
         beautifully glossy feathers. Many 
         Trainers are captivated by the striking 
         beauty of the feathers on its head, 
         compelling them to choose Pidgeot as their Pokémon."""
Rattata = """0019 Rattata
          Type: Normal 
          The Mouse Pokémon
          Rattata is cautious in the extreme. Even 
          while it is asleep, it constantly listens 
          by moving its ears around. It is not picky 
          about where it lives—it will make its nest anywhere.
          Evolves into Raticate."""
Raticate ="""0020 Raticate
          Type: Normal
          The Mouse Pokémon
          Raticate's sturdy fangs grow steadily. 
          To keep them ground down, it gnaws on rocks
          and logs. It may even chew on the walls of houses."""
Spearow ="""0021 Spearow
         Type: Normal | Flying
         The Tiny Bird Pokémon
         Spearow has a very loud cry that can be 
         heard over half a mile away. If its high, 
         keening cry is heard echoing all around, it 
         is a sign that they are warning each other of danger.
         Evolves into Fearow."""
Fearow ="""0022 Fearow
        Type: Normal | Flying
        The Beak Pokémon
        Fearow is recognized by its long neck and elongated
        beak. They are conveniently shaped for catching 
        prey in soil or water. It deftly moves 
        its long and skinny beak to pluck prey."""
Ekans ="""0023 Ekans
       Type: Poison
       The Snake Pokémon
       Ekans curls itself up in a spiral while it 
       rests. Assuming this position allows it to 
       quickly respond to a threat from any 
       direction with a glare from its upraised head.
       Evolves into Arbok."""
Arbok ="""0024 Arbok
       Type: Poison
       The Cobra Pokémon
       This Pokémon is terrifically strong in order 
       to constrict things with its body. It can even 
       flatten steel oil drums. Once Arbok wraps its 
       body around its foe, escaping its crunching embrace is impossible."""
Pikachu ="""0025 Pikachu
         Type: Electric
         The Mouse Pokémon
         Whenever Pikachu comes across something new,
         it blasts it with a jolt of electricity. 
         If you come across a blackened berry, it's 
         evidence that this Pokémon mistook the intensity of its charge.
         Evolves into Raichu."""
Raichu ="""0026 Raichu
        Type: Electric
        The Mouse Pokémon
        If the electrical sacs become excessively charged, 
        Raichu plants its tail in the ground and 
        discharges. Scorched patches of ground will
        be found near this Pokémon's nest."""
Sandshrew = """0027 Sandshrew
            Type: Ground
            The Mouse Pokemon
            Sandshrew's body is configured to absorb 
            water without waste, enabling it to survive
            in an arid desert. This Pokémon curls up to 
            protect itself from its enemies.
            Evolves into Sandslash."""
Sandslash = """0028 Sandslash
            Type: Ground
            The Mouse Pokémon
            Sandslash's body is covered by tough spikes, 
            which are hardened sections of its hide. 
            Once a year, the old spikes fall out, to 
            be replaced with new spikes that
            grow out from beneath the old ones."""
Nidoran_female = """0029 Nidoran♀
           Type: Poison
           The Poison Pin Pokémon
           Nidoran♀ has barbs that secrete a powerful
           poison. They are thought to have developed 
           as protection for this small-bodied Pokémon. 
           When enraged, it releases a horrible toxin from its horn.
           Evolves into Nidorina."""
Nidorina = """0030 Nidorina
           Type: Poison
           The Poison Pin Pokémon
           When Nidorina are with their friends or family, 
           they keep their barbs tucked away to prevent 
           hurting each other. This Pokémon appears to 
           become nervous if separated from the others.
           Evolves into Nidoqueen."""
Nidoqueen = """0031 Nidoqueen
            Type: Poison | Ground
            The Drill Pokémon
            Nidoqueen's body is encased in extremely hard 
            scales. It is adept at sending foes flying with
            harsh tackles. This Pokémon is at its strongest 
            when it is defending its young."""
Nidoran_male = """0032 Nidoran♂
           Type: Poison
           The Poison Pin Pokémon
           Nidoran♂ has developed muscles for moving its
           ears. Thanks to them, the ears can be freely 
           moved in any direction. Even the slightest sound 
           does not escape this Pokémon's notice.
           Evolves into Nidorino."""
Nidorino ="""0033 Nidorino
          Type: Poison
          The Poison Pin Pokémon
          Nidorino has a horn that is harder than a diamond. 
          If it senses a hostile presence, all the barbs 
          on its back bristle up at once, and it challenges
          the foe with all its might.
          Evolves into Nidoking."""
Nidoking ="""0034 Nidoking
          Type: Poison | Ground
          The Drill Pokémon
          Nidoking's thick tail packs enormously destructive
          power. With one swing, it can topple a metal 
          transmission tower. Once this Pokémon goes on 
          a rampage, there is no stopping it."""
Clefairy = """0035 Clefairy
           Type: Fairy
           The Fairy Pokémon
           On every night of a full moon, groups
           of this Pokémon come out to play. When
           dawn arrives, the tired Clefairy return 
           to their quiet mountain retreats and go
           to sleep nestled up against each other.
           Evolves into Clefable."""
Clefable = """0036 Clefable
           Type: Fairy
           The Fairy Pokémon
           Clefable moves by skipping lightly as if
           it were flying using its wings. Its bounc
           y step even lets it walk on water. It is 
           known to take strolls on lakes on quiet, moonlit nights."""
Vulpix ="""0037 Vulpix
        Type: Fire
        The Fox Pokémon
        At the time of its birth, Vulpix has one white
        tail. The tail separates into six if this 
        Pokémon receives plenty of love from its trainer. 
        The six tails become magnificently curled.	
        Evolves into Ninetales."""
Ninetales ="""0038 Ninetales
           Type: Fire
           The Fox Pokémon
           Ninetales casts a sinister light from its bright
           red eyes to gain total control over its foe's mind. 
           This Pokémon is said to live for one thousand years."""
Jigglypuff ="""0039 Jigglypuff
            Type: Normal | Fairy
            The Balloon Pokémon
            Jigglypuff's vocal cords can freely adjust 
            the wavelength of its voice. This Pokémon 
            uses this ability to sing at precisely the
            right wavelength to make its foes most drowsy.
            Evolves into Wigglytuff."""
Wigglytuff ="""0040 Wigglytuff
            Type: Normal | Fairy
            The Balloon Pokémon
            Wigglytuff has large, saucerlike eyes.
            The surfaces of its eyes are always covered
            with a thin layer of tears. If any dust gets 
            in this Pokémon's eyes, it is quickly washed away."""
Zubat = """0041 Zubat
        Type: Poison | Flying
        The Bat Pokémon
        Zubat remains quietly unmoving in a dark spot 
        during the bright daylight hours. It does so 
        because prolonged exposure to the sun causes 
        its body to become slightly burned.
        Evolves into Golbat."""
Golbat ="""0042 Golbat
        Type: Poison | Flying
        The Bat Pokémon
        Golbat loves to drink the blood of living things.
        It is particularly active in the pitch black 
        of night. This Pokémon flits around in the 
        night skies, seeking fresh blood."""
Oddish ="""0043 Oddish
        Type: Grass | Poison
        The Weed Pokémon
        During the daytime, Oddish buries itself 
        in soil to absorb nutrients from the ground 
        using its entire body. The more fertile the
        soil, the glossier its leaves become.
        Evolves into Gloom."""
Gloom ="""0044 Gloom
       Type: Grass | Poison
       The Weed Pokémon
       Gloom releases a foul fragrance from the 
       pistil of its flower. When faced with danger, 
       the stench worsens. If this Pokémon is feeling 
       calm and secure, it does not release its 
       usual stinky aroma.	
       Evolves into Vileplume."""
Vileplume ="""0045 Vileplume
           Type: Grass | Poison 
           The Flower Pokémon
           Vileplume's toxic pollen triggers atrocious 
           allergy attacks. That's why it is advisable 
           never to approach any attractive flowers in
           a jungle, however pretty they may be."""
Paras ="""0046 Paras
       Type: Bug | Grass
       The Mushroom Pokémon
       Paras has parasitic mushrooms growing on its 
       back called tochukaso. They grow large by 
       drawing nutrients from this Bug Pokémon host. 
       They are highly valued as a medicine for extending life.
       Evolves into Parasect."""
Parasect ="""0047 Parasect
          Type: Bug | Grass
          The Mushroom Pokémon
          Parasect is known to infest large trees 
          en masse and drain nutrients from the 
          lower trunk and roots. When an infested t
          ree dies, they move onto another tree all at once."""
Venonat ="""0048 Venonat
         Type: Bug | Poison
         The Insect Pokémon
         Venonat is said to have evolved with a coat
         of thin, stiff hair that covers its entire body
         for protection. It possesses large eyes that
         never fail to spot even miniscule prey.
         Evolves into Venomoth."""
Venomoth = """0049 Venomoth
           Type: Bug | Poison
           The Poison Moth Pokémon
           Venomoth is nocturnal—it is a Pokémon that only
           becomes active at night. Its favorite prey are 
           small insects that gather around streetlights, 
           attracted by the light in the darkness."""
Diglett = """0050 Diglett
          Type: Ground
          The Mole Pokémon
          Diglett are raised in most farms. The reason is 
          simple—wherever this Pokémon burrows, the soil
          is left perfectly tilled for planting crops. 
          This soil is made ideal for growing delicious vegetables
          Evolves into Dugtrio."""
Dugtrio = """0051 Dugtrio
          Type: Ground
          The Mole Pokémon
          Dugtrio are actually triplets that emerged
          from one body. As a result, each triplet thinks
          exactly like the other two triplets. They work
          cooperatively to burrow endlessly."""
Meowth = """0052 Meowth
         Type: Normal
         The Scratch Cat Pokémon
         Meowth withdraws its sharp claws into its paws
         to slinkily sneak about without making any 
         incriminating footsteps. For some reason, this
         Pokémon loves shiny coins that glitter with light.
         Evolves into Persian."""
Persian = """0053 Persian
          Type: Normal
          The Classy Cat Pokémon
          Persian has six bold whiskers that give it a 
          look of toughness. The whiskers sense air 
          movements to determine what is in the Pokémon's 
          surrounding vicinity. It becomes docile if grabbed by the whiskers."""
Psyduck = """0054 Psyduck
          Type: Water
          The Duck Pokémon
          Psyduck uses a mysterious power. When it does so, 
          this Pokémon generates brain waves that are
          supposedly only seen in sleepers. This discovery 
          spurred controversy among scholars.
          Evolves into Golduck."""
Golduck = """0055 Golduck
          Type: Water
          The webbed flippers on its forelegs and hind 
          legs and the streamlined body of Golduck give 
          it frightening speed. The Pokémon is definitely
          much faster than even the most athletic swimmer."""
Mankey = """0056 Mankey          
         Type: Fighting
         The Pig Monkey Pokémon
         When Mankey starts shaking and its nasal breathing
         turns rough, it's a sure sign that it is becoming 
         angry. However, because it goes into a towering rage 
         almost instantly, it is impossible for anyone to flee its wrath.
         Evolves into Primeape."""
Primeape = """0057 Primeape
           Type: Fighting
           The Pig Monkey Pokémon
           When Primeape becomes furious, its blood circulation
           is boosted. In turn, its muscles are made even 
           stronger. However, it also becomes much less 
           intelligent at the same time."""
Growlithe = """0058 Growlithe
            Type: Fire
            The Puppy Pokémon
            Growlithe has a superb sense of smell. Once it 
            smells anything, this Pokémon won't forget the 
            scent, no matter what. It uses its advanced olfactory
            sense to determine the emotions of other living things.
            Evolves into Arcanine."""
Arcanine = """0059 Arcanine
           Type: Fire 
           The Legendary Pokémon
           Arcanine is known for its high speed. It is said 
           to be capable of running over 6,200 miles in a 
           single day and night. The fire that blazes wildly 
           within this Pokémon's body is its source of power."""
Poliwag = """0060 Poliwag
          Type: Water
          The Tadpole Pokémon
          Poliwag has a very thin skin. It is possible 
          to see the Pokémon's spiral innards right through
          the skin. Despite its thinness, however, the 
          skin is also very flexible. Even sharp fangs bounce right off it.
          Evolves into Poliwhirl."""
Poliwhirl = """0061 Poliwhirl
            Type: Water
            The Tadpole Pokémon
            The surface of Poliwhirl's body is always 
            wet and slick with an oily fluid. Because of 
            this greasy covering, it can easily slip and slide
            out of the clutches of any enemy in battle.
            Evolves into Poliwrath."""
Poliwrath = """0062 Poliwrath
            Type: Water | Fighting
            The Tadpole Pokémon
            Poliwrath's highly developed, brawny muscles
            never grow fatigued, however much it exercises.
            It is so tirelessly strong, this Pokémon can swim
            back and forth across the ocean without effort."""
Abra = """0063 Abra
       Type: Psychic
       The Psi Pokémon
       Abra sleeps for eighteen hours a day. However, 
       it can sense the presence of foes even while it is
       sleeping. In such a situation, this Pokémon 
       immediately teleports to safety.
       Evolves into Kadabra."""
Kadabra = """0064 Kadabra
          Type: Psychic
          The Psi Pokémon
          Kadabra emits a peculiar alpha wave if it 
          develops a headache. Only those people with a
          particularly strong psyche can hope to 
          become a trainer of this Pokémon.
          Evolves into Alakazam."""
Alakazam = """0065 Alakazam
           Type: Psychic
           The Psi Pokémon
           Alakazam's brain continually grows, making 
           its head far too heavy to support with its
           neck. This Pokémon holds its head up using
           its psychokinetic power instead."""
Machop = """0066 Machop
         Type: Fighting
         The Superpower Pokémon
         Machop's muscles are special—they never get 
         sore no matter how much they are used in 
         exercise. This Pokémon has sufficient 
         power to hurl a hundred adult humans.
         Evolves into Machoke."""
Machoke = """0067 Machoke
          Type: Fighting
          The Superpower Pokémon
          Machoke's thoroughly toned muscles possess
          the hardness of steel. This Pokémon has so 
          much strength, it can easily hold aloft a 
          sumo wrestler on just one finger.
          Evolves into Machamp."""
Machamp = """0068 Machamp
          Type: Fighting
          The Superpower Pokémon
          Machamp has the power to hurl anything aside.
          However, trying to do any work requiring care 
          and dexterity causes its arms to get tangled.
          This Pokémon tends to leap into action before it thinks."""
Bellsprout = """0069 Bellsprout
             Type: Grass | Poison
             The Flower Pokemon
             Bellsprout's thin and flexible body lets it bend
             and sway to avoid any attack, however strong it 
             may be. From its mouth, this Pokémon spits a 
             corrosive fluid that melts even iron.
             Evolves into Weepingbell."""
Weepingbell = """0070 Weepingbell
              Type: Grass | Poison
              The Flycatcher Pokémon
              Weepinbell has a large hook on its rear end. 
              At night, the Pokémon hooks on to a tree branch 
              and goes to sleep. If it moves around in its 
              sleep, it may wake up to find itself on the ground.
              Evolves into Victreebel."""
Victreebel = """0071 Victreebel
             Type: Grass | Poison
             The Flycatcher Pokémon
             Victreebel has a long vine that extends from 
             its head. This vine is waved and flicked about as 
             if it were an animal to attract prey. When an 
             unsuspecting prey draws near, this Pokémon swallows it whole."""
Tentacool = """0072 Tentacool
            Type: Water | Poison
            The Jellyfish Pokémon
            Tentacool's body is largely composed of water.
            If it is removed from the sea, it dries up like 
            parchment. If this Pokémon happens to become 
            dehydrated, put it back into the sea.
            Evolves into Tentacruel."""
Tentacruel = """0073 Tentacruel
             Type: Water | Poison
             The Jellyfish Pokémon
             Tentacruel has large red orbs on its head.
             The orbs glow before lashing the vicinity with
             a harsh ultrasonic blast. This Pokémon's outburst
             creates rough waves around it."""
Geodude = """0074 Geodude
          Type: Rock | Ground
          The Rock Pokémon
          The longer a Geodude lives, the more its edges
          are chipped and worn away, making it more rounded in
          appearance. However, this Pokémon's heart will remain
          hard, craggy, and rough always.
          Evolves into Graveler."""
Graveler = """0075 Graveler
           Type: Rock | Ground
           The Rock Pokémon
           Graveler grows by feeding on rocks. Apparently, 
           it prefers to eat rocks that are covered in moss. 
           This Pokémon eats its way through a
           ton of rocks on a daily basis.
           Evolves into Golem."""
Golem = """0076 Golem
        Type: Rock | Ground
        The Megaton Pokémon
        Golem live up on mountains. If there is a large 
        earthquake, these Pokémon will come rolling down
        off the mountains en masse to the foothills below."""
Ponyta = """0077 Ponyta
         Type: Fire
         The Fire Horse Pokémon
         Ponyta is very weak at birth. It can barely 
         stand up. This Pokémon becomes stronger by 
         stumbling and falling to keep up with its parent.
         Evolves into Rapidash."""
Rapidash = """0078 Rapidash
           Type: Fire 
           The Fire Horse Pokémon
           Rapidash usually can be seen casually cantering
           in the fields and plains. However, when this 
           Pokémon turns serious, its fiery manes flare and 
           blaze as it gallops its way up to 150 mph."""
Slowpoke = """0079
           Type: Water | Psychic
           The Dopey Pokémon
           Slowpoke uses its tail to catch prey by 
           dipping it in water at the side of a river. 
           However, this Pokémon often forgets what it's 
           doing and often spends entire days just loafing at water's edge.
           Evolves into Slowbro."""
Slowbro = """0080 Slowbro
          Type: Water | Psychic
          The Hermit Crab Pokémon
          Slowbro's tail has a Shellder firmly attached 
          with a bite. As a result, the tail can't be used 
          for fishing anymore. This causes Slowbro to grudgingly
          swim and catch prey instead."""
Magnemite = """0081 Magnemite
            Type: Electric | Steel
            The Magnet Pokémon
            Magnemite attaches itself to power lines to feed
            on electricity. If your house has a power outage, 
            check your circuit breakers. You may find a 
            large number of this Pokémon clinging to the breaker box.
            Evolves into Magneton."""
Magneton = """0082 Magneton
           Type: Electric | Steel
           The Magnet Pokémon
           Magneton emits a powerful magnetic force that is
           fatal to mechanical devices. As a result, large 
           cities sound sirens to warn citizens of 
           large-scale outbreaks of this Pokémon."""
Farfetchd = """0083 Farfetch'd
            Type: Normal | Flying
            The Wild Duck Pokémon
            Farfetch'd is always seen with a stalk from 
            a plant of some sort. Apparently, there are 
            good stalks and bad stalks. This Pokémon has 
            been known to fight with others over stalks."""
Doduo = """0084 Doduo
        Type: Normal | Flying
        The Twin Bird Pokémon
        Doduo's two heads never sleep at the same 
        time. Its two heads take turns sleeping, so 
        one head can always keep watch for 
        enemies while the other one sleeps.
        Evolves into Dodrio."""
Dodrio = """0085 Dodrio
         Type: Normal | Flying
         The Triple Bird Pokémon
         Watch out if Dodrio's three heads are looking 
         in three separate directions. It's a sure 
         sign that it is on its guard. Don't go near 
         this Pokémon if it's being wary-it may decide to peck you."""
Seel = """0086 Seel
       Type: Water
       The Sea Lion Pokémon
       Seel hunts for prey in the frigid sea underneath 
       sheets of ice. When it needs to breathe, it punches 
       a hole through the ice with the sharply 
       protruding section of its head.
       Evolves into Dewgong."""
Dewgong = """0087 Dewgong
          Type: Water | Ice 
          The Sea Lion Pokémon
          Dewgong loves to snooze on bitterly cold ice. 
          The sight of this Pokémon sleeping on a glacier 
          was mistakenly thought to be a mermaid 
          by a mariner long ago."""
Grimer = """0088 Grimer
         Type: Poison
         The Sludge Pokémon
         Grimer's sludgy and rubbery body can be forced 
         through any opening, however small it may be. This 
         Pokémon enters sewer pipes to drink filthy wastewater.
         Evolves into Muk."""
Muk = """0089 Muk
      Type: Poison
      The Sludge Pokémon
      From Muk's body seeps a foul fluid that gives 
      off a nose-bendingly horrible stench. Just one 
      drop of this Pokémon's body fluid can turn 
      a pool stagnant and rancid."""
Shellder = """0090 Shellder
           Type: Water
           The Bivalve Pokémon
           At night, this Pokémon uses its broad tongue 
           to burrow a hole in the seafloor sand and then
           sleep in it. While it is sleeping, Shellder 
           closes its shell, but leaves its tongue hanging out.
           Evolves into Cloyster."""
Cloyster = """0091 Cloyster
           Type: Water | Ice
           The Bivalve Pokémon
           Cloyster is capable of swimming in the sea. 
           It does so by swallowing water, then jetting 
           it out toward the rear. This Pokémon shoots 
           spikes from its shell using the same system."""
Gastly = """0092 Gastly
         Type: Ghost | Poison
         The Gas Pokémon
         Gastly is largely composed of gaseous matter. 
         When exposed to a strong wind, the gaseous body
         quickly dwindles away. Groups of this Pokémon 
         cluster under the eaves of houses to escape the ravages of wind.
         Evolves into Haunter."""
Haunter = """0093 Haunter
          Type: Ghost | Poison
          The Gas Pokémon
          Haunter is a dangerous Pokémon. If one beckons
          you while floating in darkness, you must never
          approach it. This Pokémon will try to lick you 
          with its tongue and steal your life away.
          Evolves into Gengar."""
Gengar = """0094 Gengar 
         Type: Ghost | Poison
         The Shadow Pokémon
         Sometimes, on a dark night, your shadow thrown
         by a streetlight will suddenly and startlingly
         overtake you. It is actually a Gengar running 
         past you, pretending to be your shadow."""
Onix = """0095 Onix
       Type: Rock | Ground
       The Rock Snake Pokémon
       Onix has a magnet in its brain. It acts as a 
       compass so that this Pokémon does not lose direction 
       while it is tunneling. As it grows older, its body
       becomes increasingly rounder and smoother."""
Drowzee = """0096 Drowzee
          Type: Psychic
          The Hypnosis Pokémon
          If your nose becomes itchy while you are 
          sleeping, it's a sure sign that one of these
          Pokémon is standing above your pillow and trying
          to eat you dream through your nostrils.
          Evolves into Hypno."""
Hypno = """0097 Hypno 
        Type: Psychic
        The Hypnosis Pokémon
        Hypno holds a pendulum in its hand. The arcing movement 
        and glitter of the pendulum lull the foe into a deep 
        state of hypnosis. While this Pokémon searches for 
        prey, it polishes the pendulum."""
Krabby = """0098 Krabby 
         Type: Water
         The River Crab Pokémon
         Krabby live on beaches, burrowed inside holes dug 
         into the sand. On sandy beaches with little in the way
         of food, these Pokémon can be seen squabbling 
         with each other over territory.
         Evolves into Kingler."""
Kingler = """0099 Kingler
          Type: Water
          The Pincer Pokémon
          Kingler has an enormous, oversized claw. It waves 
          this huge claw in the air to communicate with
          others. However, because the claw is so heavy, 
          the Pokémon quickly tires."""
Voltorb = """0100 Voltorb
          Type: Electric
          The Ball Pokémon
          Voltorb was first sighted at a company that 
          manufactures Poké Balls. The link between that 
          sighting and the fact that this Pokémon looks 
          very similar to a Poké Ball remains a mystery.
          Evolves into Electrode."""
Electrode = """0101 Electrode
            Type: Electric
            The Ball Pokémon
            Electrode eats electricity in the atmosphere. 
            On days when lightning strikes, you can see this 
            Pokémon exploding all over the place 
            from eating too much electricity."""
Exeggcute = """0102 Exeggcute
            Type: Grass | Psychic
            The Egg Pokémon
            This Pokémon consists of six eggs that form a 
            closely knit cluster. The six eggs attract each 
            other and spin around. When cracks increasingly 
            appear on the eggs, Exeggcute is close to evolution.
            Evolves into Exeggutor."""
Exeggutor = """0103 Exeggutor
            Type: Grass | Psychic
            The Coconut Pokémon
            Exeggutor originally came from the tropics. 
            Its heads steadily grow larger from exposure to 
            strong sunlight. It is said that when the heads
            fall off, they group together to form Exeggcute."""
Cubone = """0104 Cubone
         Type: Ground
         The Lonely Pokémon
         Cubone pines for the mother it will never see again. 
         Seeing a likeness of its mother in the full moon, 
         it cries. The stains on the skull the Pokémon wears
         are made by the tears it sheds.
         Evolves into Marowak."""
Marowak = """0105 Marowak
          Type: Ground
          The Bone Keeper Pokémon
          Marowak is the evolved form of a Cubone that has 
          overcome its sadness at the loss of its mother 
          and grown tough. This Pokémon's tempered and 
          hardened spirit is not easily broken."""












         
         
def print_userpoke_details(userpoke):
  
    
  
    if userpoke == 1:
        print(Bulbasaur)
    elif userpoke == 2:
        print(Ivysaur)
    elif userpoke == 3:
        print(Venasaur)
    elif userpoke == 4:
        print(Charmander)
    elif userpoke == 5:
        print(Charmeleon)
    elif userpoke == 6:
        print(Charizard)
    elif userpoke == 7:
        print(Squirtle)
    elif userpoke == 8:
        print(Wartortle)
    elif userpoke == 9:
        print(Blastoise)    
    elif userpoke == 10:
        print(Caterpie)    
    elif userpoke == 11:
        print(Metapod)    
    elif userpoke == 12:
        print(Butterfree)    
    elif userpoke == 13:
        print(Weedle)    
    elif userpoke == 14:
        print(Kakuna)    
    elif userpoke == 15:
        print(Beedrill)
    elif userpoke == 16:
        print(Pidgey)    
    elif userpoke == 17:
        print(Pidgeotto)    
    elif userpoke == 18:
        print(Pidgeot)    
    elif userpoke == 19:
        print(Rattata)    
    elif userpoke == 20:
        print(Raticate)    
    elif userpoke == 21:
        print(Spearow)      
    elif userpoke == 22:
        print(Fearow)
    elif userpoke == 23:
        print(Ekans)    
    elif userpoke == 24:
        print(Arbok)    
    elif userpoke == 25:
        print(Pikachu)    
    elif userpoke == 26:
        print(Raichu)    
    elif userpoke == 27:
        print(Sandshrew)    
    elif userpoke == 28:
        print(Sandslash)      
    elif userpoke == 29:
        print(Nidoran_female)
    elif userpoke == 30:
        print(Nidorina)    
    elif userpoke == 31:
        print(Nidoqueen)    
    elif userpoke == 32:
        print(Nidoran_male)    
    elif userpoke == 33:
        print(Nidorino)    
    elif userpoke == 34:
        print(Nidoking)    
    elif userpoke == 35:
        print(Clefairy)      
    elif userpoke == 36:
        print(Clefable)
    elif userpoke == 37:
        print(Vulpix)    
    elif userpoke == 38:
        print(Ninetales)    
    elif userpoke == 39:
        print(Jigglypuff)    
    elif userpoke == 40:
        print(Wigglytuff)    
    elif userpoke == 41:
        print(Zubat)    
    elif userpoke == 42:
        print(Golbat)      
    elif userpoke == 43:
        print(Oddish)
    elif userpoke == 44:
        print(Gloom)    
    elif userpoke == 45:
        print(Vileplume)    
    elif userpoke == 46:
        print(Paras)    
    elif userpoke == 47:
        print(Parasect)    
    elif userpoke == 48:
        print(Venonat)    
    elif userpoke == 49:
        print(Venomoth)      
    elif userpoke == 50:
        print(Diglett)
    elif userpoke == 51:
        print(Dugtrio)    
    elif userpoke == 52:
        print(Meowth)    
    elif userpoke == 53:
        print(Persian)    
    elif userpoke == 54:
        print(Psyduck)    
    elif userpoke == 55:
        print(Golduck)    
    elif userpoke == 56:
        print(Mankey)      
    elif userpoke == 57:
        print(Primeape)
    elif userpoke == 58:
        print(Growlithe)    
    elif userpoke == 59:
        print(Arcanine)    
    elif userpoke == 60:
        print(Poliwag)    
    elif userpoke == 61:
        print(Poliwhirl)    
    elif userpoke == 62:
        print(Poliwrath)    
    elif userpoke == 63:
        print(Abra)      
    elif userpoke == 64:
        print(Kadabra)    
    elif userpoke == 65:
        print(Alakazam)      
    elif userpoke == 66:
        print(Machop)
    elif userpoke == 67:
        print(Machoke)    
    elif userpoke == 68:
        print(Machamp)    
    elif userpoke == 69:
        print(Bellsprout)    
    elif userpoke == 70:
        print(Weepingbell)    
    elif userpoke == 71:
        print(Victreebel)    
    elif userpoke == 72:
        print(Tentacool)          
    elif userpoke == 73:
        print(Tentacruel)    
    elif userpoke == 74:
        print(Geodude)      
    elif userpoke == 75:
        print(Graveler)
    elif userpoke == 76:
        print(Golem)    
    elif userpoke == 77:
        print(Ponyta)    
    elif userpoke == 78:
        print(Rapidash)    
    elif userpoke == 79:
        print(Slowpoke)    
    elif userpoke == 80:
        print(Slowbro)    
    elif userpoke == 81:
        print(Magnemite)          
    elif userpoke == 82:
        print(Magneton)    
    elif userpoke == 83:
        print(Farfetchd)      
    elif userpoke == 84:
        print(Doduo)
    elif userpoke == 85:
        print(Dodrio)    
    elif userpoke == 86:
        print(Seel)    
    elif userpoke == 87:
        print(Dewgong)    
    elif userpoke == 88:
        print(Grimer)    
    elif userpoke == 89:
        print(Muk)    
    elif userpoke == 90:
        print(Shellder)          
    elif userpoke == 91:
        print(Cloyster)    
    elif userpoke == 92:
        print(Gastly)      
    elif userpoke == 93:
        print(Haunter)
    elif userpoke == 94:
        print(Gengar)    
    elif userpoke == 95:
        print(Onix)    
    elif userpoke == 96:
        print(Drowzee)    
    elif userpoke == 97:
        print(Hypno)    
    elif userpoke == 98:
        print(Krabby)    
    elif userpoke == 99:
        print(Kingler)      
    elif userpoke == 100:
        print(Voltorb)    
    elif userpoke == 101:
        print(Electrode)      
    elif userpoke == 102:
        print(Exeggcute)
    elif userpoke == 103:
        print(Exeggutor)    
    elif userpoke == 104:
        print(Cubone)    
    elif userpoke == 105:
        print(Marowak)    
    elif userpoke == 106:
        print(Hitmonlee)    
    elif userpoke == 107:
        print(Hitmochan)    
    elif userpoke == 108:
        print(Lickitung)          
    elif userpoke == 109:
        print(Koffing)    
    elif userpoke == 110:
        print(Weezing)      
    elif userpoke == 111:
        print(Rhyhorn)
    elif userpoke == 112:
        print(Rhydon)    
    elif userpoke == 113:
        print(Chansey)    
    elif userpoke == 114:
        print(Tangela)    
    elif userpoke == 115:
        print(Kangaskan)    
    elif userpoke == 116:
        print(Horsea)    
    elif userpoke == 117:
        print(Seadra)          
    elif userpoke == 118:
        print(Goldeen)    
    elif userpoke == 119:
        print(Seaking)      
    elif userpoke == 120:
        print(Staryu)
    elif userpoke == 121:
        print(Starmie)    
    elif userpoke == 122:
        print(Mr_Mime)    
    elif userpoke == 123:
        print(Scyther)    
    elif userpoke == 124:
        print(Jynx)    
    elif userpoke == 125:
        print(Electabuzz)    
    elif userpoke == 126:
        print(Magmar)    
    elif userpoke == 127:
        print(Pinsir)    
    elif userpoke == 128:
        print(Tauros)      
    elif userpoke == 129:
        print(Magikarp)
    elif userpoke == 130:
        print(Gyrados)    
    elif userpoke == 131:
        print(Lapras)    
    elif userpoke == 132:
        print(Ditto)    
    elif userpoke == 133:
        print(Eevee)    
    elif userpoke == 134:
        print(Vaporeon)    
    elif userpoke == 135:
        print(Jolteon)      
    elif userpoke == 136:
        print(Flareon)    
    elif userpoke == 137:
        print(Porygon)      
    elif userpoke == 138:
        print(Omanyte)
    elif userpoke == 139:
        print(Omastar)    
    elif userpoke == 140:
        print(Kabuto)    
    elif userpoke == 141:
        print(Kabutops)    
    elif userpoke == 142:
        print(Aerodactyl)    
    elif userpoke == 143:
        print(Snorlax)    
    elif userpoke == 144:
        print(Articuno)          
    elif userpoke == 145:
        print(Zapdos)    
    elif userpoke == 146:
        print(Moltres)      
    elif userpoke == 147:
        print(Dratini)
    elif userpoke == 148:
        print(Dragonair)    
    elif userpoke == 149:
        print(Dragonite)    
    elif userpoke == 150:
        print(Mewtwo)    
    elif userpoke == 151:
        print(Mew)    
    elif userpoke >= 152:
        print "Please Enter Valid Numbers 1-151"
  

while True:
    try:
        userpoke = int(raw_input("Enter Pokémon#: "))
        if userpoke == 0:
            userpoke = random.randint(1,151)
        elif userpoke == 999:
            sys.exit(0)
    except ValueError:
        print("Sorry, I didn't understand that, Please try again")
        continue
    else:
        print_userpoke_details(userpoke)
sys.exit(0)
