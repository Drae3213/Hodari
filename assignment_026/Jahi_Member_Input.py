'''
#######################################
#                                                   #
#  Program: Member input        #
#  Author: Andrew Lubega        #
#  Date    2/23/2021                    #
#  The Hidden Genius Project  #
#  OAK8 Cohort                         #
#                                                 #
#######################################
'''

class Pod:
    # Class variable
    member = {}
    # Class Constructor method is called when an Object is instantiated
    def __init__(self, leader, cell):
        Pod.member[leader] = cell
        
    # Method to add member and number to member dictionary
    def add_member(self, name , cell):
        Pod.member[name] = cell
        
    # Class method to print the pod_leader and cell numbers   
    def display_members(self):
        print('\n')
        for Pod.member, number in Pod.member.items():
            print(Pod.member, number)
            
#  Prompt for the Pod Leader name and number
leader = input('Who is the leader? ')
cell = input('What is the leaders cell number? ')

# Initialize the Pod Dictionary with the leader's name and number
pod = Pod(leader,cell)
pod.add_member(leader,cell)

amount = int(input("How many members would you like to add? "))

for i in range(0, amount):
    member = input("Who is the member?: ")
    cell = input("What os their phone #?: ")
    pod.add_member(member, cell)

pod.display_members()

"""
isStopped =False

while(isStopped == False):
    member =input("Who is the member?: ")
    if (member != "stop"):
        cell = input("What is their number?: ")
        pod.add_member(member, cell)
    else:
        isStopped = True
"""
