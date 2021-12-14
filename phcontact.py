


phonecontacts=[{"viplist":[{"name":"Ajith","relation":"Close-friend","phone-number":9598979235,"Email-id":"ajith123@gmail.com","DOB":"09/01/1998"},
                           {"name":"kaviya","relation":"Close-friend","phone-number":9598979521,"Email-id":"kaviya@gmail.com","DOB":"20/12/2002"},
                           {"name":"preethika","relation":"Close-friend","phone-number":9598889235,"Email-id":"preethika789@gmail.com","DOB":"15/11/1999"},
                            {"name":"Aswetha","relation":"Close-friend","phone-number":7418529631,"Email-id":"aswetha121@gmail.com","DOB":"24/02/2003"},
                            {"name":"Sneha","relation":"Close-friend","phone-number":9876543218,"Email-id":"snehaa2407@gmail.com","DOB":"24/06/2001"},
                            {"name":"Maha","relation":"Close-friend","phone-number":9876543217,"Email-id":"maha217@gmail.com","DOB":"7/07/2001"},
                            {"name":"Rajkumar","relation":"Close-friend","phone-number":9876543220,"Email-id":"rajkumar220@gmail.com","DOB":"17/07/1889"},
                            {"name":"Swetha","relation":"Close-friend","phone-number":9876543222,"Email-id":"swetharajkumar222@gmail.com","DOB":"7/04/2004"},
                            {"name":"Jiji","relation":"Close-friend","phone-number":9876543221,"Email-id":"jijirajkumar221@gmail.com","DOB":"17/07/1890"},
                            {"name":"Karthick","relation":"Close-friend","phone-number":9876543223,"Email-id":"jijirajkumar221@gmail.com","DOB":"24/10/2000"},
                            {"name":"Praveenkumar","relation":"Close-friend","phone-number":9876543225,"Email-id":"praveenkumar225@gmail.com","DOB":"08/09/2004"},
                            {"name":"Deepak","relation":"Close-friend","phone-number":9876553210,"Email-id":"deepak210@gmail.com","DOB":"04/05/2006"},
                            {"name":"Suriyaprakash","relation":"Close-friend","phone-number":7010206775,"Email-id":"suriyaprakash@gmail.com","DOB":"05/06/2001"},
                            {"name":"Mani","relation":"Close-friend","phone-number":7790877087,"Email-id":"manikandan087@gmail.com","DOB":"06/07/2002"},
                            {"name":"Aishu","relation":"Close-friend","phone-number":7709864532,"Email-id":"gayathri532@gmail.com","DOB":"07/08/2006"},
                            {"name":"Sruthi","relation":"Close-friend","phone-number":8809864421,"Email-id":"sruthi421@gmail.com","DOB":"18/12/2002"},
                            {"name":"Guruvishnu","relation":"Close-friend","phone-number":7784574196,"Email-id":"guru245@gmail.com","DOB":"30/09/2012"},
                            {"name":"Akash","relation":"Close-friend","phone-number":9875421784,"Email-id":"akash784@gmail.com","DOB":"31/07/2000"},
                            {"name":"Dinesh","relation":"Close-friend","phone-number":9874891784,"Email-id":"dinesh459@gmail.com","DOB":"07/07/2013"},
                            {"name":"Geetha","relation":"Close-friend","phone-number":9875421521,"Email-id":"geetha521@gmail.com","DOB":"12/03/1898"},
                            {"name":"Aysha","relation":"Close-friend","phone-number":8956412544,"Email-id":"aysha544@gmail.com","DOB":"09/05/1999"},
                            {"name":"Bathara","relation":"Close-friend","phone-number":7418529521,"Email-id":"bathra521@gmail.com","DOB":"02/02/2000"},
                            {"name":"Abi","relation":"Close-friend","phone-number":7894561232,"Email-id":"abi232@gmail.com","DOB":"31/12/1888"},
                            {"name":"Ranjan","relation":"Close-friend","phone-number":8876543210,"Email-id":"ranjan2100@gmail.com","DOB":"06/07/2005"}]}]



for i in phonecontacts:

    for j,k in i.items():
        print(j,k)


class phonedetails:

    def detail(name:str)->list:
        if isinstance(name,str)==False:
            raise TypeError("invalid type")

        if len(phone-number)<10:
            raise ValueError("not a valid number")
        
    
                            
