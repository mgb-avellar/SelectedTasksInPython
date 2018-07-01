#! /usr/bin/python

#############################################################################
#                                                                         ###
# Creating an inventory: classes of things, the items and their quantity. ###
#                                                                         ###
# Quantity is an integer and can be used for operations and math.         ###
#                                                                          ##
# Author: Dr. Marcio G B de Avellar - astrophysicist, learning python.     ##
#                                                                          ##
# Collaborator: Dr. Rodrigo A. de Souza - professional programmer, a       ##
#              friend and teacher. Also an astrophysicist.                 ##
#                                                                          ##
############################################################################# 


inventario = {}     # Creating an empty dictionary; the keys will be the classes of things

items_by_key = []   # Creating an empty list to be filled with items classified by class

print

while True:								# Loop for filling the classes
	
	class_name = raw_input('Class (type \done\ when finish): ')	# The class: for exemple, swords
	if class_name == 'done':					# Stop condition
		break
		
	else:
		
		items_by_key = []					# Filling the list of items and ...
									#  ... making it empty each iteration
		while True:						# Loop for filling the items

			item = raw_input('Item (type \done\ when finish): ')	# Specifying the item
			if item == 'done':				# Stop condition
				
				break
			try:						# Item must be a word, not a number
               			float(item)
               			print("Item must be a thing. Type a word, please. ")
               			continue
           		except ValueError:               			
               			pass
           		
			items_by_key.append(item)			# Appending the item to the list
	
			aux01 = int(1)					# Auxiliary variable to help testing if ...
									#  ... quantity is an integer.
			while True: 
				quantity = raw_input('Quantity: '.format(aux01))
           			try:					# Quantity must be an integer, not a string
               				int(quantity)					
            			except ValueError:
               				print("The quantity must be an integer. Say again, please?".format(aux01))
               				continue
				break				
          		
			items_by_key.append(int(quantity))		# Appending the quantity of the item to the list

		inventario[class_name] = items_by_key			# Putting the item the its quantity into ...
									#  ... the inventory

print 

print "You have:"

for index, key in enumerate(inventario):

    print index + 1, ")", key, inventario[key]
    
else:
    print
    print 'A fine selection of itens.'
    print

print inventario							# Printing your inventory

print
