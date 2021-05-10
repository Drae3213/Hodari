'''
################################################
#  Program: Pod_members.py                     #
#  Author: Andrew                                #
#  Date: 2/23/2021                             #
#  Description: Program to be used by the      #
#               POD Leaders in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''
class Pods:
    # Class Constructor method is called when an Object is instantiated
    def __init__(self, pod_leader, pod_member):
       self.pod_leader = {}
       self.pod_member = {}
    # Class method to add a leader to the pod_leader dictionary       
    def add_leader(self, leader_to_add,cell_number):
        self.pod_leader[leader_to_add] = cell_number

    def add_member(self, name, cell):
        self.pod_member[name] = cell
        
    # Class method to print the pod_leader and cell numbers   
    def display_leaders(self):
      print('POD Leaders')      
      for leader, number in self.pod_leader.items():
        print(leader, number)

    def display_members(self):
        print("\n","POD Members")
        for member, number in self.pod_member.items():
             print(member, number)
             
pod = Pods("POD Leader", "POD Members");
pod.add_leader("Richard","(510) 228-5623")
pod.add_leader("Jacore","(845) 200-6250")
pod.add_leader("Gabriel","(510) 326-5834")
pod.add_leader("Aris","(510) 229-6359 ")
pod.add_leader("Andrew","(925) 727-4611")

pod.add_member("Glenn", "(510) 328-8290")
pod.add_member("Ronin", "(415) 910-3415")
pod.add_member("Malick", "(510) 405-8755")

pod.display_leaders()
pod.display_members()
