'''phonecontacts'''


facebook=[{"GroupFriends":[{"name":"sneha","groupname":"friendsworld","Groupcount":25},
                           {"name":"kaviya","groupname":"friendsworld","Groupcount":25},
                           {"name":"ramya","groupname":"friendsworld","Groupcount":25},
                           {"name":"sneha","groupname":"friendsworld","Groupcount":25},
                           {"name":"abi","groupname":"friendsworld","Groupcount":25},
                           {"name":"vishnu","groupname":"friendsworld","Groupcount":25},
                           {"name":"vimala","groupname":"friendsworld","Groupcount":25},
                           {"name":"sara","groupname":"friendsworld","Groupcount":25},
                           {"name":"riya","groupname":"friendsworld","Groupcount":25},
                           {"name":"mubu","groupname":"friendsworld","Groupcount":25},
                           {"name":"vino","groupname":"friendsworld","Groupcount":25},
                           {"name":"ammu","groupname":"friendsworld","Groupcount":25},
                           {"name":"abisha","groupname":"friendsworld","Groupcount":25},
                           {"name":"jayanthi","groupname":"friendsworld","Groupcount":25},
                           {"name":"abi","groupname":"friendsworld","Groupcount":25},
                           {"name":"aarthi","groupname":"friendsworld","Groupcount":25},
                           {"name":"aarish","groupname":"friendsworld","Groupcount":25},
                           {"name":"aara","groupname":"friendsworld","Groupcount":25},
                           {"name":"keerthana","groupname":"friendsworld","Groupcount":25},
                           {"name":"venky","groupname":"friendsworld","Groupcount":25},
                           {"name":"suriya","groupname":"friendsworld","Groupcount":25},
                           {"name":"shalu","groupname":"friendsworld","Groupcount":25},
                           {"name":"manoj","groupname":"friendsworld","Groupcount":25},
                           {"name":"swetha","groupname":"friendsworld","Groupcount":"25"},
                           {"name":"jv","groupname":"friendsworld","Groupcount":25}]}]


for i in facebook:
    for j,k in i.items():
        print(j,k)


Facebook1=[{"CommonFriends":[{"name":"praveen","mutualfriend":"karthi","relation":"closefriend"},
                             {"name":"lakshman","mutualfriend":"prugu","relation":"brother"},
                             {"name":"sam","mutualfriend":"vishnu","relation":"friend"},
                             {"name":"sathish","mutualfriend":"prince","relation":"friend"},
                             {"name":"diana","mutualfriend":"kavya","relation":"sister"},
                             {"name":"abi","mutualfriend":"priju","relation":"sister"},
                             {"name":"krithi","mutualfriend":"sneha","relation":"friend"},
                             {"name":"arunpriya","mutualfriend":"shalini","relation":"friend"},
                             {"name":"sivan","mutualfriend":"melkis","relation":"friend"},
                             {"name":"boo","mutualfriend":"rajesh","relation":"closefriend"},
                             {"name":"balaji","mutualfriend":"vino","relation":"closefriend"},
                             {"name":"santham","mutualfriend":"vichu","relation":"brother"},
                             {"name":"akash","mutualfriend":"vineeth","relation":"friend"},
                             {"name":"sanjay","mutualfriend":"adhi","relation":"friend"},
                             {"name":"surya","mutualfriend":"dharshan","relation":"brother"},
                             {"name":"ramesh","mutualfriend":"selva","relation":"cousin"},
                             {"name":"selva","mutualfriend":"sathish","relation":"cousin"},
                             {"name":"gopi","mutualfriend":"bala","relation":"brother"},
                             {"name":"krithika","mutualfriend":"mahesh","relation":"sister"},
                             {"name":"babu","mutualfriend":"mohan","relation":"brother"},
                             {"name":"preethika","mutualfriend":"aswetha","relation":"friend"},
                             {"name":"bathraa","mutualfriend":"varatha","relation":"friend"},
                             {"name":"mukesh","mutualfriend":"avinash","relation":"friend"},
                             {"name":"abilash","mutualfriend":"anbu","relation":"friend"},
                             {"name":"baby","mutualfriend":"jayanthi","relation":"friend"}]}]


for i in Facebook1:
    if isinstance("name",str):
        continue
    else:
        raise TypeError("InvalidName")

    if isinstance("Groupcount",int):
        continue
    else:
        raise TypeError ("InvalidNumber")
    for j,k in i.items():
        print(j,k)
facebook.txt
Displaying facebook.txt.
