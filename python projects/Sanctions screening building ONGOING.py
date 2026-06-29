def get_data(prompt):
      return input(prompt)

def normalise(input_string):
    input_string = input_string.strip().lower().replace('-',' ')
    input_string = " ".join(input_string.split())
    return input_string


def create_review_breakdown(name, country, dob, PEP_status):
    return f'''=== SANCTIONS SCREENING SYSTEM ===
name: {name}
country: {country}
dob: {dob}
PEP Status: {PEP_status}
Status: PENDING REVIEW'''

def screen_customer(user_info,watchlist):
    normalised_user_name = normalise(user_info['name'])
    for person in watchlist:     
        if normalised_user_name == normalise(person['name']) and user_info['dob'] == person['dob']:
                return person

watchlist = [
    {"name": "Ali Hassan",       "dob": "22-10-1980", "country": "IR", "reason": "OFAC SDN — proliferation financing"},
    {"name": "John Kim",         "dob": "05-03-1975", "country": "KP", "reason": "OFAC SDN"},
    {"name": "Sara Petrov",      "dob": "14-07-1988", "country": "RU", "reason": "EU sanctions"},
    {"name": "Omar Khalid",      "dob": "30-01-1971", "country": "SY", "reason": "OFAC SDN — human rights abuses"},
    {"name": "Rhivo Mars",       "dob": "19-09-1983", "country": "BY", "reason": "EU sanctions"},
    {"name": "Hassan Al-Farsi",  "dob": "08-06-1969", "country": "IR", "reason": "OFAC SDN — sanctions evasion"},
    {"name": "Natalia Vorova",   "dob": "23-11-1991", "country": "RU", "reason": "UK OFSI — oligarch asset freeze"},
    {"name": "Chen Wei",         "dob": "11-04-1978", "country": "CN", "reason": "OFAC SDN"},
]
user_info_db = [{'name':'Aris Niamonitakis', 'dob':'23-11-2001'},
            {'name':'Ali Hassan', 'dob':'22-10-1980'},
            {'name':'Katya Sad', 'dob':'19-09-1983'}]

clear_count = 0
risk_count = 0
clear_list =[]
risk_list= []
for user in user_info_db:
    screened_results = screen_customer(user,watchlist)
    if screened_results:
         print(f'{user['name']} is blocked')
         risk_count += 1
         risk_list.append(user['name']) 
    else:
        print(f'{user['name']} is Cleared')
        clear_count += 1
        clear_list.append(user['name'])

print(f'{clear_count+risk_count} people screened\n{clear_count} people are clear, {risk_count} people are risky.\n Clear People are: {clear_list}\n Risky People are: {risk_list}')


