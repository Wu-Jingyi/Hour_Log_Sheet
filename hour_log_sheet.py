from datetime import datetime
import csv
from sys import exit

def log_in(first_name, last_name, email, PIN):
	with open('roster.csv') as csvfile:
	     reader = csv.DictReader(csvfile)
	     for row in reader:
	     	if (row['first_name']==first_name and row['last_name']==last_name) and (row['email']==email and row['PIN']==PIN):
	         	return '%s_%s' % (first_name, last_name)
	         	break
	     else:
	     	return 'wrong'

class page(object):
	def __init__(self, Name):
		self.Name = Name

class enter_page(page):
		
	def enter(self):
		print "You can submit new form, view history, change profile, or quit. What would you do?"
		choice = raw_input("> ")
		if "new" in choice:
			submit_new_form(self.Name).enter()
		elif "change" in choice:
			change_profile(self.Name).enter()
		elif "history" in choice:
			view_history(self.Name).enter()
		elif "quit" in choice:
			exit(0)
		else:
			print "Wrong entry"
			enter_page(self.Name).enter()

class submit_new_form(page):

	def enter(self):
		print "We would like to ask a few questions."
		Mentee_Name = raw_input("What's the name of your mentee? ")
		Work_Type = raw_input("What's the type of your work? ")
		Hours = raw_input("How many hours did you work? ")
		Remarks = raw_input("Do you have any remarks? ")
		now = datetime.now()
		date = "%s, %s, %s" % (now.year, now.month, now.day)
		history=[]
		try:
			open('%s.csv' % str(self.Name), 'r').close()
		except IOError:
			open('%s.csv' % str(self.Name), 'w+')
		
		with open('%s.csv' % str(self.Name), 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				history.append(row)
		with open('%s.csv' % str(self.Name), 'w') as csvfile:
			fieldnames = ['Mentee_Name', 'Work_Type', 'Hours', 'Remarks']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for row in history:
				writer.writerow(row)
			writer.writerow({'Mentee_Name': '%s' % Mentee_Name, 'Work_Type': '%s' % Work_Type, 'Hours': '%s' % Hours, 'Remarks': '%s' % Remarks})
		print "entry submitted: Mentee_Name: %s, Work_Type: %s, Hours: %s, Remarks: %s" % (Mentee_Name, Work_Type, Hours, Remarks)
		enter_page(self.Name).enter()

class change_profile(page):
	def enter(self):
		print "What would you like to change? email address or PIN?"
		answer= raw_input("> ")
		if 'email' in answer:
			print "What's your old email address?"
			old_email = raw_input("> ")
			print "What's your new email address?"
			new_email = raw_input("> ")
			print "Repeat your new email address"
			new_email_again = raw_input("> ")
			roster=[]
			if new_email==new_email_again:
				with open("roster.csv") as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						if row['email']==old_email:
							row['email']=new_email
						roster.append(row)
				with open("roster.csv", "w") as csvfile:
					fieldnames = ['first_name', 'last_name', 'email', 'PIN', 'notification']
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					writer.writeheader()
					for row in roster:
						writer.writerow(row)
					print "You successfully changed your email address"
			else:
				print "Oops, try again"
				change_profile(self.Name).enter()
		if 'PIN' in answer:
			print "What's your old PIN?"
			old_PIN= raw_input("> ")
			print "What's your new PIN?"
			new_PIN= raw_input("> ")
			print "Repeat your new PIN"
			new_PIN_again = raw_input("> ")
			roster=[]
			if new_PIN==new_PIN_again:
				with open("roster.csv") as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:
						if row['PIN']==old_PIN:
							row['PIN']=new_PIN
						roster.append(row)
				with open("roster.csv", "w") as csvfile:
					fieldnames = ['first_name', 'last_name', 'email', 'PIN', 'notification']
					writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
					writer.writeheader()
					for row in roster:
						writer.writerow(row)
					print "You successfully changed your PIN"
			else:
				print "Oops, try again"
				change_profile(self.Name).enter()
		enter_page(self.Name).enter()

class view_history(page):
	def enter(self):
		try:
			open('%s.csv' % str(self.Name), 'r').close()
		except IOError:
			open('%s.csv' % str(self.Name), 'w+')
		with open('%s.csv' % str(self.Name), 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print row
		enter_page(self.Name).enter()

print "Welcome, is this your first time here?"
first_time = raw_input("> ")
if first_time == "yes":
	print "We would like you to enter some information about yourself."
	Registered_First_Name= raw_input("What's your first name? ")
	Registered_Last_Name= raw_input("What's your last name? ")
	Registered_Email= raw_input("What's your email? ")
	Registered_Notification = raw_input("Would you like to receive monthly notification? ")
	Registered_PIN = raw_input("What would you like your PIN to be? ")
	roster=[]
	try:
		open('roster.csv', 'r').close()
	except IOError:
		open('roster.csv', 'w+')
	with open('roster.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			roster.append(row)
	with open('roster.csv', 'w') as csvfile:
		fieldnames = ['first_name', 'last_name', 'email', 'PIN', 'notification']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for row in roster:
			writer.writerow(row)
		writer.writerow({'first_name': '%s' % Registered_First_Name, 'last_name': '%s' % Registered_Last_Name, 'email': '%s' % Registered_Email, 'PIN': '%s' % Registered_PIN, 'notification': '%s' % Registered_Notification})

print "We will transfer you to the log_in page"
log_in_first_name=raw_input("What's your first name? ")
log_in_last_name=raw_input("What's your last name? ")
log_in_email=raw_input("What's your email? ")
log_in_PIN=raw_input("What's your PIN ?")
access_key= log_in(log_in_first_name, log_in_last_name, log_in_email, log_in_PIN)
while access_key == 'wrong':
	print "Oops, wrong information. Please enter again."
	log_in_first_name=raw_input("What's your first name? ")
	log_in_last_name=raw_input("What's your last name? ")
	log_in_email=raw_input("What's your email? ")
	log_in_PIN=raw_input("What's your PIN ?")
	access_key = log_in(log_in_first_name, log_in_last_name, log_in_email, log_in_PIN)
else:
	enter_page(access_key).enter()