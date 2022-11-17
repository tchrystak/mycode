#!/usr/bin/env python3
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


char_name= input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n").capitalize()   
                                                                                                          # by adding those methods to end of input, it will capitalize or lower
                                                                                                          # the string that input returns, right at the source!
char_stat= input("What statistic do you want to know about? (real name, powers, archenemy)\n").lower()



#print(f"{char_name}'s {char_stat} is: {marvelchars[char_name].lower()[char_stat].title()}")
print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")
