import json

user1 = {'id':1, 'name':'Hans', 'age':25, 'lang':'ger', 'hobbys':('Badminton', 'Tennis', 'Musik')}
user2 = {'id':2, 'name':'Peter', 'age':40, 'lang':'ger', 'hobbys':('Schwimmen', 'Technik')}
user = [user1, user2] # list of users

# we can keep the JSON-Data as a string or directly write it to a file
# convert userlist to json-string
jsonstring = json.dumps(user)
# write userlist to json-file
with open('data.json', 'w') as jsonfile:  # temporary open file (write only)
    json.dump(user, jsonfile )

# once saved we can load the data from string or file
# load python data from string
user_from_string = json.loads(jsonstring)
# load python object directly from file
with open('data.json', 'r') as jsonfile:  # temporary open file (read only)
    user_from_file = json.load(jsonfile)

# check same behavior as original object user
print(user[0]['name'])
print(user_from_string[0]['name'])
print(user_from_file[0]['name'])
