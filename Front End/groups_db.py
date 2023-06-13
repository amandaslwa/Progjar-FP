class GroupsDB():
    groups_list=[{"group":"Group 1","group_id":"1"},
                {"group":"Group 2","group_id":"2"},
                {"group":"Group 3","group_id":"3"},
                ]

    # def read_gid(self,group_name:str):
    #     #print("Iniciando sesion.... ")
    #     for i in self.groups_list:
    #         if (i["group"]==group_name):
    #             return i["group_id"]
            
    def read_group(self):
        return GroupsDB.groups_list
    
    # def get_data(self):
    #     return GroupsDB.groups_list