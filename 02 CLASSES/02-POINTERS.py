#pointers
dict1={
  'value':11      
      }
dict2 = dict1 #means dict2 is completely dependent on dict1

print("Before value is updated: ")
print("dict1=", dict1)
print("dict2=", dict2)

dict1['value']=22

print("\nAfter value is updated: ")
print("dict1=", dict1)
print("dict2=", dict2)


#not pointers

num1=11
num2=num1 #these are not forever dependant and hence will be altered when num1 changes.
print('\nBefore value is updated: ')
print('num1 value is',num1)
print('num2 value is',num2) 
num1=22
print('\nAfter value is updated: ')
print('num1 value is',num1)
print('num2 value still is',num2)
