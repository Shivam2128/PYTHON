marks = {
    'harry':100,
    'shivam':89,
    "anurag":56,
}

# print(marks.items()) #item () function
# print(marks.keys()) #keys() function
# print(marks.values())
# marks.update({'shivam':99})/
print(marks) 
# print(marks.get('shivam'))
# print(marks['shivam'])

marks.pop('harry', 100)
print(marks)
