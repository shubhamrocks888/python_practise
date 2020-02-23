import json

people_string ='''
{
    "people" :[
    {"name":"John Smith",
    "phone":"615-555-7164",
    "emails":["johnsmith@usa.com","johnsmith@uk.com"],
    "has_license":false 
    },
    {"name":"Jane Doe",
    "phone":"560-111-7574",
    "emails":null, 
    "has_license":true  
    }
    ]
}
'''

# data = json.loads(people_string)      ---> convert json string or json object  into python dict ,indent doesn't work with json.loads
# print (data)

# o/p is:
# {'people': [{'name': 'John Smith', 'phone': '615-555-7164', 'emails': ['johnsmith@usa.com', 'johnsmith@uk.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-111-7574', 'emails': None, 'has_license': True}]}

# json      python
# true      True
#false      False
#null       None

# data = json.loads(people_string)

# for person in data['people']:
#     del person['phone']

# new_string = json.dumps(data)  ---> convert python dict into json string
# print (new_string)

# o/p is:
# {"people": [{"name": "John Smith", "emails": ["johnsmith@usa.com", "johnsmith@uk.com"], "has_license": false}, {"name": "Jane Doe", "emails": null, "has_license": true}]}

# data = json.loads(people_string)
#
# for person in data['people']:
#     del person['phone']
#
# new_string = json.dumps(data,indent=2)
# print (new_string)

# o/p is:
# {
#   "people": [
#     {
#       "name": "John Smith",
#       "emails": [
#         "johnsmith@usa.com",
#         "johnsmith@uk.com"
#       ],
#       "has_license": false
#     },
#     {
#       "name": "Jane Doe",
#       "emails": null,
#       "has_license": true
#     }
#   ]
# }

# data = json.loads(people_string)
#
# for person in data['people']:
#     del person['phone']
#
# new_string = json.dumps(data,indent=2,sort_keys=True)---> sort the keys alphabetically
# print (new_string)

# o/p is :
# {
#   "people": [
#     {
#       "emails": [
#         "johnsmith@usa.com",
#         "johnsmith@uk.com"
#       ],
#       "has_license": false,
#       "name": "John Smith"
#     },
#     {
#       "emails": null,
#       "has_license": true,
#       "name": "Jane Doe"
#     }
#   ]
# }
