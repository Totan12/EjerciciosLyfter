print("Hola" + "World") #HolaWorld
print("Hola" + 8) #TypeError: can only concatenate str (not "int") to str
print(8 + "Hola") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([1,2,3,4,5] + [6,7,8,9,10]) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Hola" + [6,7,8,9,10]) # TypeError: can only concatenate str (not "list") to str
print(3.14 + 5) # 8.14 
print(True + False) #1
print(True + True)#2 ===> El True actúa como "1" y el False como "0"