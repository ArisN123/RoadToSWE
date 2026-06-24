# #EX 1
# Method chain drill
# Take the string " MR. AHMED AL-RASHID " and write a chain that produces "ahmed al rashid" — no spaces at edges, no hyphens, no "mr.", all lowercase.
#  You'll need to chain at least 4 methods.

name = " MR. AHMED AL-RASHID "
def normalise(string):
    string = string.lower().replace('.','').replace('-',' ').replace('mr','').strip()
    return string

print(normalise(name))