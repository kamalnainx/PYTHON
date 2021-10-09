# ui={"name":"thekamalnain","age":30,"city":"delhi"}
# print(ui)







# import json
# ui={"name":"thekamalnain","age":30,"city":"delhi"}
# print(ui)
# js1=json.dumps(ui)
# print(js1)











# import json as js
# js1=js.dumps({"name":"thekamalnain","age":30,"city":"delhi"})
# print(js1)












# import json as js
# print(js.dumps({"name":"thekamalnain","age":30,"city":"delhi"}))







# import json as js
# print(js.dumps({"name":"thekamalnain","age":30,"city":"delhi"}))
# print(js.dumps(["name","thekamalnain","age",30,"city","delhi"]),list)
# print(js.dumps(("name","thekamalnain","age",30,"city","delhi")),tuple)
# print(js.dumps("name:thekamalnain,age:30,city:delhi"),str)
# print(js.dumps(30),int)
# print(js.dumps(30.30),float)
# print(js.dumps(True),bool)
# print(js.dumps(False),bool)
# print(js.dumps(None))










# import json as j
# ui={"name":"kamalnainx","age":40,"married":True,"divorced":False,"pets":None,
#     "children":("anmol","anamika"),
#     "car":[
#         {"model":"BMW","kmpl":30},
#         {"model":"ford","kmpl":31},
#         ]
#     }
# print(ui)











# import json as j
# ui={"name":"kamalnainx","age":40,"married":True,"divorced":False,"pets":None,
#     "children":("anmol","anamika"),
#     "car":[
#         {"model":"BMW","kmpl":30},
#         {"model":"ford","kmpl":31},
#         ]
#     }
# print(ui)
# print(j.dumps(ui))
# print(j.dumps(ui,indent=4))










# import json as j
# ui={"name":"kamalnainx","age":40,"married":True,"divorced":False,"pets":None,
#     "children":("anmol","anamika"),
#     "car":[
#         {"model":"BMW","kmpl":30},
#         {"model":"ford","kmpl":31},
#         ]
#     }
# print(ui)
# print(j.dumps(ui))
# print(j.dumps(ui,indent=10))














# import json as j
# ui={"name":"kamalnainx","age":40,"married":True,"divorced":False,"pets":None,
#     "children":("anmol","anamika"),
#     "car":[
#         {"model":"BMW","kmpl":30},
#         {"model":"ford","kmpl":31},
#         ]
#     }
# print(ui)
# print(j.dumps(ui))
# print(j.dumps(ui,indent=10))
# print(j.dumps(ui,indent=5, separators=(":"," = ")))

















import json as j
ui={"name":"kamalnainx","age":40,"married":True,"divorced":False,"pets":None,
    "children":("anmol","anamika"),
    "car":[
        {"model":"BMW","kmpl":30},
        {"model":"ford","kmpl":31},
        ]
    }
print(ui)
print(j.dumps(ui))
print(j.dumps(ui,indent=10))
print(j.dumps(ui,indent=5, separators=(":"," = ")))
print(j.dumps(ui,indent=5, separators=(":"," = "), sort_keys=True))
print(j.dumps(ui,indent=5, separators=(":"," = "), sort_keys=False))
