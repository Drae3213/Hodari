'''
***********************************************
*  Program: pickle.lesson2_staff.py                 *
* Author: Andrew Lubega                       *
* Date: 1/28/2021                             *
* The Hidden Genius Project                   *
* Cohort: OAK8(THE BEST ONE!!!!!!!!!)         *
***********************************************
'''



#1 Initialize an empty dictionary variable, name it all_pod_members
pod_leaders = {}
instructor_pod = {}

#2 Initialize a file variable to write data to, name it pod_file, that will
# open a file named hgp_pods that you will write data to the file. 


#3  Initialize empty dictionary variables, name it as such;
jacore_members = {}
andrew_members = {}
gabriel_members = {}
aris_members = {}
richard_members = {}

#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard

#5 Add the names and telephone numbers of each member POD

jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'

andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'

gabriel_members["Emmanuel Torbor"] = "(510) 934-4133"
gabriel_members["David Brickley"] = "(510) 631-6288 "
gabriel_members["Myles Wilkerson"] = "(510) 500-7266"
gabriel_members["Gabriel Reader"] = "(510) 326-5834"

aris_members["Aris Carter"] = "(510) 229-6359 "
aris_members["Zyion Williiams"] ="(510) 480-5785 "
aris_members["Milan Kral"] = "(510) 816-3232 "
aris_members["Hyab Isayas"] = "(510) 612-3737 "
aris_members["Maurice Richardson"] = "(510) 424-7789 "

richard_members["Richard Kamau"] = "(510) 228-5623 "
richard_members["Mathew Dudley"] = "(510) 816-2411 "
richard_members["Kymari Rhodes"] = "(510) 816-2411 "

#6 Add all the PODS to the all_pod_members dictionary

pod_leaders['Jacore'] =  jacore_members
pod_leaders['Andrew'] = andrew_members
pod_leaders['Gabriel'] = gabriel_members
pod_leaders['Aris'] = aris_members
pod_leaders['Richard'] = richard_members

instructor_pod["Akeem"] = pod_leaders["Jacore"]
instructor_pod["Baba"] =  pod_leaders["Andrew"]
instructor_pod["Hodari"] =  pod_leaders["Gabriel"]
instructor_pod["David"] =  pod_leaders["Aris"]
instructor_pod["Paris"] =  pod_leaders["Richard"]

#7 Dump all the 

#8 Open the pod_file to read data


#9 Print all the Pod leaders and POD membership
for instructor_pod, pod_leaders in instructor_pod.items():
  print("POD Instructor: ", instructor_pod)
  print("POD Leader",str(list(pod_leaders.keys())[0]))
  for pod_leaders, pod_members in pod_leaders.items():
    print( pod_leaders, pod_members)
  print("\n")
      
  



