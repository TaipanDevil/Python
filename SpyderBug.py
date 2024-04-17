# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:10:57 2019

@author: azeng
"""
#foo()
#import pdb; pdb.set_trace()
#bar()
MPCastPhrases = {
    "Cleese": "It's not pining, it's passed on! This parrot is no more!\
    It has ceased to be! It's expired and gone to meet its maker! This\
    is a late parrot! It's a stiff! Bereft of life, it rests in peace!\
    If you hadn't nailed it to the perch, it would be pushing up the\
    daisies! It's rung down the curtain and joined the choir invisible.\
    This is an ex-parrot!",
    "Palin": "Bally Jerry pranged his kite right in the how's-your-father;\
    hairy blighter, dicky-birded, feathered back on his sammy, took a waspy,\
    flipped over on his Betty Harpers and caught his can in the Bertie.",
    "Jones": "Spam! Spam! Spam! Spam! Spam! Spam!",
    "Idle": "Nobody expects the Spanish Inquisition!",
    "Gilliam": "What... is the air-speed velocity of an unladen swallow?",
    "Chapman": "We are no longer the knights who say Ni! We are now the\
    knights who say ekki-ekki-ekki-pitang-zoom-boing!"
}

# (1) Inspect Variables with program paused.
print('\nMonty Python Cast')
print('-----------------')
for CastMember in MPCastPhrases.keys():
    print(CastMember + ' ', end="")
# (2) Step through code a line at a time
print('\n\nFamous Lines')
print('------------')
for Line in MPCastPhrases.values():
    print(Line + "\n")

# (3) Modify a command
# Fun with strings
# Cleese's Speech Backwards!
breakpoint()
Line = MPCastPhrases['Cleese']
Line = Line[0:2:]
print(Line + "\n")

# (4) Modify a variable in memory.

# (5) Trigger a breakpoint.
# Oops, Palin and Idle sayings accidentally swapped
# Let's fix that with the standard swap algorithm
print(MPCastPhrases["Idle"] + "\n")
Temp = MPCastPhrases["Palin"]
MPCastPhrases["Palin"] = MPCastPhrases["Idle"]
MPCastPhrases["Idle"] = Temp
print(MPCastPhrases["Idle"] + "\n")
