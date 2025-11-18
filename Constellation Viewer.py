
def Orion ():
   print("NAME: Orion")
   print("ASCII:")
   print("        .      *    .         *")
   print("    *        ⭐           *       .")
   print("         .       ⭐  ⭐      .")
   print("    .        ⭐  ⭐  ⭐         *")
   print("         *      ⭐  ⭐  ⭐    .")
   print("    .            ⭐              .")
   print("         *    ⭐     ⭐      *")
   print("              ⭐         ⭐")
   print("    .      *          .      *")
   print("📚 Scientific Information:")
   print("\nINFO: Orion is one of the most famous constellations, containing the red supergiant Betelgeuse and the blue star Rigel. Best visible in winter. The Orion Nebula (M42) is about 1,344 light-years away, a stellar nursery. - NASA\n")

def UrsaMajor ():
    print("NAME: Ursa Major")
    print("ASCII:")
    print("    *        *")
    print("     ⭐────⭐     *")
    print("       │    │")
    print("    .  ⭐    ⭐──⭐     .")
    print("        │         ⭐")
    print("    *   ⭐──────⭐   *")
    print("           │")
    print("    .      *     .    *")
    print("📚 Scientific Information:")
    print("\nINFO: Contains the Big Dipper, used for navigation for thousands of years. Its stars point to the North Star. Known as 'The Great Bear'. - IAU\n")

def Cassiopeia () :
    print("NAME: Cassiopeia")
    print("ASCII:")
    print("         ⭐")
    print("        ╱  ╲")
    print("    .  ⭐    ⭐   *")
    print("       │      │")
    print("       ⭐      ⭐    .")
    print("         *      .")
    print("📚 Scientific Information:")
    print("\nINFO: Forms a W or M shape depending on its position in the sky. Near the North Celestial Pole, visible all year in the northern hemisphere. Contains the Heart Nebula (IC 1805). - NASA\n")

def Scorpius ():
    print("NAME: Scorpius")
    print("ASCII:")
    print("       ⭐")
    print("    .  │ ╲  *")
    print("       ⭐──⭐")
    print("    *  │    ╲  .")
    print("       ⭐     ⭐")
    print("         ╲     │")
    print("    .     ⭐──⭐  *")
    print("            │")
    print("         *  ⭐  .")
    print("📚 Scientific Information:")
    print("\nINFO: Contains the red supergiant Antares, rivaling Mars in color. One of the oldest known constellations, mentioned in Babylonian texts 5,000 years ago. Best seen in summer in the northern hemisphere. - NASA\n")

def Leo ():
    print("NAME: Leo")
    print("ASCII:")
    print("    *    ⭐──⭐    .")
    print("        ╱      ╲")
    print("       ⭐        ⭐  *")
    print("    .  │          ╲")
    print("       ⭐    ⭐──⭐──⭐")
    print("         *    .    *")
    print("📚 Scientific Information:")
    print("\nINFO: Leo contains the bright star Regulus, shining about 360 times more than the Sun. One of the zodiac constellations. Best seen in spring. - IAU\n")

def Cygnus () :
    print("NAME: Cygnus")
    print("ASCII:")
    print("         ⭐")
    print("         │  *")
    print("    .    │")
    print("    ⭐──⭐──⭐    *")
    print("         │")
    print("    *    │   .")
    print("         ⭐")
    print("         │")
    print("      .  ⭐   *")
    print("📚 Scientific Information:")
    print("\nINFO: Known as the Northern Cross, flying along the Milky Way. Deneb is its brightest star. Contains the first discovered black hole Cygnus X-1. - IAU\n")

def Taurus ():
    print("NAME: Taurus")
    print("ASCII:")
    print("    .    ⭐   ⭐    *")
    print("          ╲ ╱")
    print("       *   ⭐   .")
    print("          ╱ ╲")
    print("    .   ⭐   ⭐  *")
    print("         │ │")
    print("    *    ⭐⭐    .")
    print("📚 Scientific Information:")
    print("\nINFO: Contains the Pleiades cluster and the orange star Aldebaran. Home to Crab Nebula (M1), remnant of a supernova in 1054. One of the zodiac constellations. - IAU\n")      
        
def  Crux():
    print("NAME: Crux")
    print("ASCII:")
    print("         ⭐  *")
    print("         │")
    print("    .  ⭐─┼─⭐")
    print("         │    .")
    print("    *    ⭐")
    print("           *    .")
    print("📚 Scientific Information:")
    print("\nINFO: Smallest constellation but the most famous in the southern hemisphere. Used for navigation, points south. Contains the Coal Sack Nebula. Symbol on Australia, New Zealand, and Brazil flags. - IAU\n")

def Pegasus():
    print("NAME: Pegasus")
    print("ASCII:")
    print("    ⭐────────⭐")
    print("    │    *    │")
    print("    │    .    │  *")
    print("    ⭐────────⭐")
    print("       ╲    ╱")
    print("    .   ⭐⭐   *")
    print("📚 Scientific Information:")
    print("\nINFO: Known as the Northern Cross, flying along the Milky Way. Deneb is its brightest star. Contains the first discovered black hole Cygnus X-1. - IAU\n")
        
def Andromeda() :
    print("NAME: Andromeda")
    print("ASCII:")
    print("    *      ⭐    .")
    print("          ╱  ╲")
    print("    .    ⭐    ⭐  *")
    print("        ╱        ╲")
    print("       ⭐          ⭐")
    print("    *    .     *     .")
    print("📚 Scientific Information:")
    print("\nINFO: Contains the Andromeda Galaxy (M31), the nearest major spiral galaxy to the Milky Way, 2.5 million light-years away. Will collide with Milky Way in ~4 billion years. - NASA\n")
    
def main():
    print("\n" + "="*60)
    print("✨ Welcome to the Constellation Viewer ✨")
    print("   Explore the stars and constellations")
    print("="*60 + "\n")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's explore some constellations.\n")

    constellations = {
        "orion": Orion,
        "ursa major": UrsaMajor,
        "cassiopeia": Cassiopeia,
        "scorpius": Scorpius,
        "leo": Leo,
        "cygnus": Cygnus,
        "taurus": Taurus,
        "crux": Crux,
        "pegasus": Pegasus,
        "andromeda": Andromeda
    }

    while True:
        print("You can choose from the following constellations:")
        for c in constellations:
            print("-", c.title())
        print("─"*60)
        choice = input("\nWhich constellation would you like to see? ").strip().lower()

        if choice in constellations:
            constellations[choice]()
        else:
            print("Sorry, that constellation is not in the list. Please try again.\n")
            continue
        print("─"*60)
        again = input("Do you want to view another constellation? (yes/no): ").strip().lower()
        if again != "yes":
            print(f"\nThank you for exploring the stars with us, {name} Goodbye!")
            break

# Run the program
main()