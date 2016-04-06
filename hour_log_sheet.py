from datetime import datetime
from sys import argv
script, filename = argv
roster=open(filename, "w+")
new_roster={}
history={}

#I'm hoping to create a database for each of the name in roster,
def log_in():
	log_in_name = raw_input("What's your name?")
	log_in_email = raw_input("What's your email?")
	log_in_PIN = raw_input("What's your PIN?")
# what I want to do here is to append every single line to the dictionary new_roster, with names as keys, and emails and PINs as values.
	for line in roster.readlines():
		li= [line.strip().split(' ')]
		print li
		new_roster[li[0]+'_'+li[1]]= [li[3],li[2]]# I'm trying to make new_roster look like this: Jingyi_Wu: XXX@gmail.com, 1234
	print new_roster
	log_name = log_in_name.strip().split(' ')
	stock_name = log_name[0]+'_'+log_name[1]
	if new_roster[stock_name][0] == log_in_email and new_roster[log_in_name][1] == log_in_PIN:
			enter_page(stock_name).enter()
		
class page(object):
	def __init__(self, Name):
		self.Name = Name

class enter_page(page):
		
	def enter(self):
		print "You can submit new form, view history and change profile. What would you do?"
		choice = raw_input("> ")
		if "new" in choice:
			submit_new_form(stock_name).enter()
		elif "change" in choice:
			change_profile(stock_name).enter()
		elif "history" in choice:
			view_history(stock_name).enter()
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
		history = open(stock_name+'_history','w+')
		history.write('%r %r %r %r %r') % (date, Mentee_Name, Work_Type, hour, Remarks) #I'm trying to store history in a file
		enter_page(stock_name).enter()

class change_profile(page):
	def enter(self):
		print "What would you like to change? email address or PIN?
		answer= raw_input("> ")
		if email in answer:
			print "What's your old email address?"
			old_email= raw_input("> ")
			print "What's your new email address?"
			new_email= raw_input("> ")
			print "Repeat your new email address"
			new_email_again = raw_input("> ")
			if new_roster[stock_name][0]=old_email and new_email=new_email_again:
				print "Changing email address"
				new_roster[stock_name][0]=new_email
			else:
				print "Oops, try again"
				enter(self)
		if PIN in answer:
			print "What's your old PIN?"
			old_PIN= raw_input("> ")
			print "What's your new PIN?"
			new_PIN= raw_input("> ")
			print "Repeat your new PIN"
			new_PIN_again = raw_input("> ")
			if new_roster[stock_name][1]=old_PIN and new_PIN=new_PIN_again:
				print "Changing PIN"
				new_roster[stock_name][1]=new_PIN
			else:
				print "Oops, try again"
				enter(self)
		enter_page(stock_name).enter()

class view_history(page):
	def enter(self):
		history = open(stock_name+'_history','w+')
		print history.read()

print "Welcome, is this your first time here?"
first_time = raw_input("> ")
if first_time == "yes":
	print "We would like you to enter some information about yourself."
	Name= raw_input("What's your name? First and then Last? ")
	Email= raw_input("What's your email? ")
	Notification = raw_input("Would you like to receive monthly notification? ")
	PIN = raw_input("What would you like your PIN to be? ")
	roster.write("%r %r %r %r \n" %(Name, PIN, Email, Notification))
	print "We will transfer you to the log_in page"
	log_in()
else:
	print "We will transfer you to the log_in page"
	log_in()
	
history.close()
roster.close()