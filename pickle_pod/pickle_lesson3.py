'''
***********************************************
*  Program: pickle_lesson2.py                 !
* Author: Glenn Ivory                         *
* Date: 1/27/2021                             *
* The Hidden Genius Project                   *
* Cohort: OAK8(THE BEST ONE!!!!!!!!!)         *
***********************************************
'''
instructor = {}

jacore_leader = {}
instructor['Baba'] = jacore_leader

andrew_leader = {}
instructor['Hodari'] = andrew_leader

richard_leader = {}
instructor['Paris'] = richard_leader

gabriel_leader = {}
instructor['Akeem'] = gabriel_leader

aris_leader = {}
instructor['David'] = aris_leader





jacore_members = {}
jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'
jacore_leader['Jacore'] = jacore_members



andrew_members = {}
andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'
andrew_leader['Andrew'] = andrew_members




richard_members = {}
richard_members['Richard Kamau'] = '(510)228-5623'
richard_members['Matthew Dudley'] = '(510)816-2411'
richard_members['Kymari Rhodes'] = '(510)575-1982'
richard_members['Josiah Johnson'] = '(510)860-5112'
richard_leader['Richard'] = richard_members




gabriel_members = {}
gabriel_members['Gabriel Reader'] = '(510)326-5834'
gabriel_members['Emanual Torbor'] = '(510)934-4133'
gabriel_members['David Brickely'] = '(510)631-6288'
gabriel_members['Myles Wilkerson'] = '(510)500-7266'
gabriel_leader['Gabriel'] = gabriel_members



aris_members = {}
aris_members['Aris Carter'] = '(510)229-6359'
aris_members['Milan Kral'] = '(510)816-3232 '
aris_members['Maurice Richardson'] = '(510)424-7789'
aris_members['Zyion Williams'] = '(510)480-5785'
aris_members['Hyab Isayas'] = '(510)612-3737'
aris_leader['Aris'] =  aris_members




#print(instructor)

for instructor, pod_leader in instructor.items():
  print('The Instructor:',instructor)
  
  for pod_leader, pod_members in pod_leader.items():
    print("pod_leader:", pod_leader)
    
    for pod_members, phone_number in pod_members.items():
      print(pod_members,phone_number);
      
  print("\n")
