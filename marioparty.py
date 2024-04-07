def mario_number(level):
     if level == 1:
          return 1
     elif level % 10 == 0:
          return 0
     else:
          return mario_number(level // 10) + mario_number(level // 100)
          
print("10101 = 1\n" + str(mario_number(10101)) + "\n")
print("11101 = 2\n" + str(mario_number(11101)) + "\n")
print("100101 = 0\n" + str(mario_number(100101)) + "\n")