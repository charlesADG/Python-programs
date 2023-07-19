import random 

myDice = ["""[-------------]
[             ]
[      0      ]
[             ]
[-------------]""",
"""[-------------]
[      0      ]
[             ]
[      0      ]
[-------------]""",
"""[-------------]
[      0      ]
[      0      ]
[      0      ]
[-------------]""",
"""[-------------]
[    0   0    ]
[             ]
[    0   0    ]
[-------------]""",
"""[-------------]
[    0   0    ]
[      0      ]
[    0   0    ]
[-------------]""",
"""[-------------]
[    0   0    ]
[    0   0    ]
[    0   0    ]
[-------------]"""]

print("This is a Dice Rolling Simulator")

keepLooping = 'r'

while keepLooping.lower() == 'r':

  print(random.choice(myDice))

  rollAgain = input("Enter 'r' or 'R' to roll again: ")

  if rollAgain.lower() != 'r':
    break