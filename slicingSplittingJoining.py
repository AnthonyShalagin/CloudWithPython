
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]

sentence = "The quick brown fox jumped over the lazy dog"

print(sentence[0]) #T
print(sentence[4]) #q

print(colors[1]) #Orange
print(colors[-2]) #Blue

#slice 					[inclusive, exclusive] 
print(colors[1:4]) # [Orange, Yellow, Green]
print(colors[::2]) #start at the beginning, go the end, take every other color

print(colors[0:4:2]) # [Red, yellow]

#change the array of strings
colors[0] = 'new color'
print(colors[0])