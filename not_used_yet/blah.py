import random
import json

with open('test_data.txt', 'r') as fo:
    raw_data = fo.read().split('\n')

split_data = []
data_set = []
i = 0

while i < len(raw_data):
    if not raw_data[i]:
        if data_set:
            split_data.append(data_set)
        data_set = []
    else:
        data_set.append(raw_data[i])
        
    i += 1

    
    
test_users = []
for user_data in split_data:
    test_user = {}
    
    test_user['first_name'] = user_data[0].split(' ')[0]
    test_user['last_name'] = user_data[0].split(' ')[1]
    test_user['email'] = user_data[5].rstrip().lstrip()
    test_user['street_address'] = user_data[2]
    test_user['city'] = user_data[3]
    test_user['state'] = 'TX'
    test_user['zip_code'] = user_data[4]

    test_user['phone_number'] = user_data[1].replace('-', '')

    test_user['bio'] = 'Some bio'
    test_user['rating'] = random.choice(['A', 'B', 'C', 'D', 'E'])

    rand_coach = [False]
    if test_user['rating'] == 'A':
        rand_coach.append(True)
    test_user['is_coach'] = random.choice(rand_coach)

    test_users.append(test_user)

dump_str = '    {}\n' * (len(test_users) - 30)

dump_str = '''test_users = [

'''

dump_users_strs = []

for test_user in test_users:
    


    inner_data = json.dumps(test_user).rstrip('}').lstrip('{')

    inner_data = ',\n'.join(['        ' + data.rstrip().lstrip() for data in inner_data.split(',')]) + ','

    inner_data = '    {\n' + inner_data + '\n    },\n'
    dump_str += inner_data

print(dump_str + ']')

with open('dumps.py', 'w') as fo:
    fo.write(dump_str + ']')







