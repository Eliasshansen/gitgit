import random
print("\n-:gissa talet\n")
print("Gissa på ett tal och vinn en anka du har tre försök.\n")

slumptal = random.randint(1,3)
#print(slumptal)

#print(slumptal)

vinst = False 
i=1 #antal gånger frågan ställs, används i loop

while i < 4:
    gissatalet = input("skriv talet")
    # print("gissatalet="+gissatalet)
    # print("slumptalet=" + str(slumptal))
    i = i + 1

    if slumptal == int(gissatalet):
        print("yipppie!\n")
        vinst = True
      
        break





if vinst==False:
    print ("tyvärr, Bot")