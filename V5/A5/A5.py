import redlab as rl

array = str(rl.cbVInScan(0,0,0,1000,7000,1))
print("Messreihe: " + array)
file = open("A5_7000.txt", "w+")
file.write(array)
file.close()