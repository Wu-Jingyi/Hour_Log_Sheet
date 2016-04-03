from datetime import datetime
from sys import argv
script, filename = argv
roster=open(filename, "w+")
new_roster={}
history={}


def log_in():
	log_in_name = raw_input("What's your name?")
	log_in_email = raw_input("What's your email?")
	log_in_PIN = raw_input("What's your PIN?")
	read = roster.readlines()
# what I want to do here is to
	for l in read:
		split= l.split(", ")
		new_roster[split[0]] = [split[2], split[1]]
	if new_roster[log_in_name][0] == log_in_email and new_roster[log_in_name][1] == log_in_PIN:
			enter_page(log_in_name).enter()
		
class page(object):
	def __init__(self, Name):
		self.Name = Name

class enter_page(page):
		
	def enter(self):
		print "You can submit new form, view history and change profile. What would you do?"
		choice = raw_input("> ")
		if "new" in choice:
			submit_new_form(Name).enter()
		elif "change" in choice:
			change_profile(Name).enter()
		elif "history" in choice:
			view_history(Name).enter()
		else:
			print "Wrong entry"
			enter()

class submit_new_form(page):
	def enter(self):
		print "We would like to ask a few questions."
		Mentee_Name = raw_input("What's the name of your mentee? ")
		Work_Type = raw_input("What's the type of your work? ")
		Hours = raw_input("How many hours did you work? ")
		Remarks = raw_input("Do you have any remarks? ")
		now = datetime.now()
		date = "%s, %s, %s" % (now.year, now.month, now.day)
		hour = float(hours)
		history[Name].append([date, Mentee_Name, Work_Type, hour, Remarks])
		enter_page(Name).enter()

class change_profile(page):
	def enter(self):
		pass

class view_history(page):
	def enter(self):
		pass

print "Welcome, is this your first time here?"
first_time = raw_input("> ")
if first_time == "yes":
	print "We would like you to enter some information about yourself."
	Name= raw_input("What's your name? ")
	Email= raw_input("What's your email? ")
	Notification = raw_input("Would you like to receive monthly notification? ")
	PIN = raw_input("What would you like your PIN to be? ")
	roster.write("%r, %r, %r, %r \n" %(Name, PIN, Email, Notification))
	log_in()
else:
	print "We will transfer you to the log_in page"
	log_in()
	
roster.close()