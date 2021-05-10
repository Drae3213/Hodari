'''
***********************************************
*  Program: telephone book            *
* Author: Andrew Lubega                       *
* Date: 1/28/2021                             *
* The Hidden Genius Project                   *
* Cohort: OAK8(THE BEST ONE!!!!!!!!!)         *
***********************************************
'''

import pickle

# 1. Leader Numbers
leader = {}
leader["Jacore:"] = "(845) 200-6250"
leader["Andrew:"] = "(925) 727-4611"
leader["Gabriel:"] = "(510) 613-6288"
leader["Aris:"] = "(510) 229-6359"
leader["Richard:"] = "(510) 228-5623"

# 2. create/open pod_nbrs.pkl file
pod_file = open("pod_nbrs.pkl", "wb")

# 3. Write POD Leader number to a file
pickle.dump(leader,pod_file)

# 4. Member Numbers
member = {}
member["Andrew:"] = "(925) 727-4611"
member["Glenn:"] = "(510) 328-8290"
member["Mallick:"] = "(510) 409-8755"
member["Ronin:"] = "(415) 910-3415"

# 5. Write Member numbers to pod_file
pickle.dump(member,pod_file)

# 6. Close pode_file
pod_file.close()

# 7. Open pod.file
pod_file = open("pod_nbrs.pkl", "rb")

# 8. Leader numbers
print("Leaders: ")
for key, value in leader.items():
    print(key, value)

print("\n")

# 9. Print POD members
print("Members:")
for key, value in member.items():
    print(key, value)

print("\n")

# 10. Close pod_file
pod_file.close()
