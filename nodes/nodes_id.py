
class Ici3Dn_identity:
    @classmethod
    def INPUT_TYPES(cls):
            return {"required": {					
					"Original_workflow": ("STRING",),
                    "ID": ("STRING",),
                    }
            }
   
    FUNCTION = "Ici3Dn_identity"
    OUTPUT_NODE = True
    CATEGORY = "Ici3Dn_ComFyIU"
    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("Original_workflow","ID")
    @classmethod
    def Ici3Dn_identity(self,Original_workflow, ID):
        	
        self.Original_workflow =Original_workflow
        self.ID=ID
        return (Original_workflow,ID)
        
		