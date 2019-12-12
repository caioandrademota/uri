l1 = ['vertebrado', 'invertebrado']
l2 = ['ave', 'mamifero', 'inseto', 'anelideo']
l3 = ['carnivoro', 'herbivoro', 'onivoro', 'hematofago']
l4 = ['aguia', 'pomba', 'homem', 'vaca', 'pulga',
      'lagarta', 'sanguessuga', 'minhoca']
a1 = input()
a2 = input()
a3 = input()

if a1 == l1[0] and a2 == l2[0] and a3 == l3[0]:
    print(l4[0])
if a1 == l1[0] and a2 == l2[0] and a3 == l3[2]:
    print(l4[1])
if a1 == l1[0] and a2 == l2[1] and a3 == l3[2]:
    print(l4[2])
if a1 == l1[0] and a2 == l2[1] and a3 == l3[1]:
    print(l4[3])
if a1 == l1[1] and a2 == l2[2] and a3 == l3[3]:
    print(l4[4])
if a1 == l1[1] and a2 == l2[2] and a3 == l3[1]:
    print(l4[5])
if a1 == l1[1] and a2 == l2[3] and a3 == l3[3]:
    print(l4[6])
if a1 == l1[1] and a2 == l2[3] and a3 == l3[2]:
    print(l4[7])
