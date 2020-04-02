#Author : Vibhav Aggarwal

import numpy as np

class_ids = {'Kindergarten - 2nd' : 0, '3rd to 5th' : 1, '6th to 10th' : 2, '11th and 12th (engineering)' : 3, '11th and 12th (medical)' : 4, '11th and 12th (arts or commerce)' : 5, 'College Applications for foreign universities' : 6}

class Mentor :
	def __init__(self, name, email, contacts, class_list, hours, mentees) :
		self.name = name
		self.email = email
		self.contacts = contacts		# contacts is a list for ex: ['Email', 'WhatsApp']
		self.class_list = class_list	# class_list is a list of integers. All classes/subjects have been assigned a unique id
		self.hours = hours
		self.mentees = mentees			# no of mentees assigned currently

class Student :
	def __init__(self, name, contact, class_id) :
		self.name = name
		self.email = email
		self.contact = contact				# contact is a list for ex: ['Email', 'WhatsApp']
		self.class_id = class_id			# class_id is an integer

def convToList (classes) :			# classes is a string. For ex : "3rd to 5th, 6th to 10th, 11th and 12th (engineering)"
	final_list = []
	for sub in classes.split(", ") :
		final_list.append(class_ids[sub])
	return final_list

mentors = []						# list of Mentor objects
students = []						# list of Student objects
mentorOf = np.load('pairs.npy', allow_pickle='TRUE').item()		# A dictionary. Maps student's index in "students" list to that of mentor's in "mentors" list
mentorOf_new = {}

# insert code to read mentor spreadsheet and populate mentors list (initially set mentees = 0)
# insert code to read student spreadsheet and populate students list

for i in range(len(students)) :
	if i not in mentorOf :
		assignable_mentors = []			# a list to store indices of assignable mentors
		for j in range(len(mentors)) :
			men = mentors[j]
			stud = students[i]
			if stud.class_id in men.class_list and stud.contact in men.contacts :
				assignable_mentors.append(j)

		# assignable_mentors list is ready. No we need to select the mentor having least value of mentees/hours
		min_ratio = 1000
		mentor_index = -1
		for ind in assignable_mentors :
			men = mentors[ind]
			if men.mentees/men.hours < min_ratio :
				min_ratio = men.mentees/men.hours
				mentor_index = ind
		mentorOf[i] = mentor_index
		mentorOf_new[i] = mentor_index

# insert code to read from mentorOf_new dictionary and append the value to mentor-pairing sheet

np.save('pairs.npy', mentorOf) 

