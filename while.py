# x=10
# y=0
# while y<= 10:
#     print(y)
#     y+=1


# for i in range(1,11):
#     if i %2 ==0:
#         print(i)

# total_weight =0

# weights= [100,200,234,387, 666, 333]        
# for index, weight in enumerate(weights):
#     print(index, weight)
#     weight=weights[index]
#     total_weight += weight

# print(f"Average weight is {total_weight/len(weights)}")

# groceries =["milk", "eggs", "bread"]        

# for item in groceries:
#     print(len(item))
import random
score = 0
gameover = False
while not gameover:
    score +=random.randint(1,10)
    print(score)
    if score <50:
       continue
    if score > 100:
        gameover=True
        break
    
    print("Close to winning")
print("You won")