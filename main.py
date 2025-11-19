temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no) ")

# 20 10 5



if(temp >= 20 and rain == "yes" ):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Don't forget your umbrella!")

elif(temp >=15):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
elif(temp >= 10):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
elif(temp > 5):
    print("Take a jacket with you")
elif(rain == "yes"):
    print("Don't forget your umbrella!")