class Ici3Dn_identity:
    @classmethod
    def INPUT_TYPES(cls):
            return {"required": {					
					"Original_workflow": ("STRING",),
                    "ID": ("STRING",),
                    }
            }
    #RETURN_TYPES = ("MASK","FLOAT","STRING")
    #RETURN_NAMES = ("MASK","New pos","Debug")
    FUNCTION = "Ici3Dn_identity"
    OUTPUT_NODE = True
    CATEGORY = "Ici3Dn_ComFyIU"
		
    @classmethod
    def Ici3Dn_identity(self,Original_workflow, ID):
        	
        self.Original_workflow =Original_workflow
        self.ID
		