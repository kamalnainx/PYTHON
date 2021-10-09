# json
# JAVASCRIPT object notation.






##import json
###python
##user11={"fname":"kamal","lname":"nain","height":6.1}
##print(type(user11))
##print(user11["fname"])
##
###json       
##user1='{"fname":"kamal","lname":"nain","height":6.1}'
##print(type(user1))
##print(user1)
##print(json.loads(user1))
##print(json.loads(user1)["fname"])
##loads()=this methed is use for move value json to python.














##import json
##user1='{"fname":"kamal","lname":"nain","height":6.1}'
##print(type(user1))
##print(user1)
##print(json.loads(user1))
##x=json.loads(user1)["fname"]
##print(x)
##y=json.loads(user1)

























##import json
##user1={"fname":"kamal","lname":"nain","height":6.1}
##print(type(user1))
##print(user1)
##
##
##x=json.dumps(user1)
##print(x)
##print(type(x))

##dumps()=this methed is use for move value python to json.




























##
##import json
##print(json.dumps({"fname":"kamal","lname":"nain","height":6.1}))
##print(json.dumps(["fname","kamal","lname","nain","height",6.1]))
##print(json.dumps(("fname","kamal","lname","nain","height",6.1)))
##print(json.dumps(None))
##print(json.dumps("fname"))
##print(json.dumps(6.1))
##print(json.dumps(6))
##print(json.dumps(True))



























##import json
##x={"full_name":{"fname":"kamal","lname":"nain"},
##   "height":6.1,
##   "married":True,
##   "children":("ram","sham"),
##   "pets":None,
##   "car":["BMW720","ford"]
##   }
##y=json.dumps(x)
##print(y)
