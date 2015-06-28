# importing the full module 'random'
# import random
# using a direct import from random instead
from random import randint


leaveprogram = 0
while leaveprogram != "q":	
	print ("This is a dice rolling program")
	# raw_input waits for you to type enter (or anything else)
	raw_input("Press enter to roll ")
	number = randint(1,6)
	
	if number == 1:
		print("[------------- ]")
		print("[              ]")
		print("[              ]")
		print("[      o       ]")
		print("[              ]")
		print("[              ]")
		print("[------------- ]")
		print()
		
	if number == 2:
		print("[------------- ]")
		print("[              ]")
		print("[   o          ]")
		print("[              ]")
		print("[         o    ]")
		print("[              ]")
		print("[------------- ]")
	 	print()
		#print("Type 'q' to quit")
		#leaveprogram = input()
	if number == 3:
		print("[------------- ]")
		print("[              ]")
		print("[   o          ]")
		print("[      o       ]")
		print("[         o    ]")
		print("[              ]")
		print("[------------- ]")
		print()
		#print("Type 'q' to quit")
		#leaveprogram = input()
	if number == 4:
		print("[------------- ]")
		print("[              ]")
		print("[   o    o     ]")
		print("[              ]")
		print("[   o    o     ]")
		print("[              ]")
		print("[------------- ]")
		print()
		#print("Type 'q' to quit")
		#leaveprogram = input()
	if number == 5:
		print("[------------- ]")
		print("[              ]")
		print("[   o    o     ]")
		print("[      o       ]")
		print("[   o    o     ]")
		print("[              ]")
		print("[------------- ]")
	 	print()
		#print("Type 'q' to quit")
		#leaveprogram = input()
	if number == 6:
		print("[------------- ]")
		print("[              ]")
		print("[   o    o     ]")
		print("[   o    o     ]")
		print("[   o    o     ]")
		print("[              ]")
		print("[------------- ]")
		print()
		#print("Type 'q' to quit")
		#leaveprogram = input()

	leaveprogram = raw_input("Type 'q' to quit, or enter to resume")