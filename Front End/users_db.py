class UsersDB():
    users_list=[{"user":"mario","password":"mario1"},
                {"user":"peach","password":"peach1"},
                {"user":"luigi","password":"luigi1"},
                {"user":"bowser","password":"bowser1"},
                {"user":"f","password":"f"},
                {"user":"a","password":"a"},
                ]

    def read_db(self,user_name:str,password:str):
        #print("Iniciando sesion.... ")
        for i in self.users_list:
            if (i["user"]==user_name and i["password"]==password):
                return True
        return False
    
  
    def write_db(self,user_name:str,password:str):
        #print("Creando usuario...")
        self.users_list.append({"user":user_name,"password":password})
        return True

    def read_user(self):
        return UsersDB.users_list
