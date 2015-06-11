__author__ = 'shawn.wang'

dict1 = {'what': 1, "does": 2, "fox": 3, 'say': 1}
dict2 = {2: 1, 8: 2, 4: 3, 6: 1}
print dict1.get("what1")
# dict1["what1"] # will give the error message but dict1.get("what1") print out None
print dict1.get("what") == dict1['what']
dict2[2] = 0
print dict2[2]