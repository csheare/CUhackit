from halo import Halo
import time


print("Would you like to install CUhackit?(y/n)")
response = input()
if(response == "y"):
	print("Downloading Organizers!")
	spinner = Halo(text='Downloading:', spinner='dots')
	spinner.start()

	organizers = ["Courtney Shearer", "Madision Maddox", "Peter Sterck", "Patrick Gorospe", "Natalie DellaMaria", "Angelo Carrabba", "Ayush Petigara", "Charlie Gallentine", "Carley Shue","Ethan Bensman","Jacovia Cherry","Kevin","Max Harley","Nikki Wyman","Sloan Nietart", "Chris Lampert" ]

	for person in organizers:
		time.sleep(.2);
		print(str(person))
	
	spinner.stop()

	print("Downloading Components")
	spinner = Halo(text='Downloading:', spinner='dots')
	spinner.start()
	
	components = ["Watt Center","Makerspace", "Immersive Space", "Food Trucks","Mentors", "Sessions", "Dance Party", "HYPE"]
	for c in components:
                time.sleep(.2);
                print(str(c))

	spinner.stop()
else:
	print("Yeah, I don't like fun hackathons either...")
