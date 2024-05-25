import numpy as np
import torch
import math
import folder_paths
import os
from PIL import Image, ImageDraw, ImageFont
from comfy_extras.nodes_mask import MaskComposite, SolidMask,FeatherMask
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0) 
 
Ici3Dn_data_Conf="G:\\GenezIA_Working_G\\WorkSpace_Python\\PyRun_Comfyui_Data\\nodes"		

class Ici3Dn_Mask:
		#"imgWidth": ("INT", {"default": 524}),	
		#"imgHeight": ("INT", {"default": 524}),
		@classmethod
		def INPUT_TYPES(cls):
 
			return {"required": {					
					"destination": ("MASK",),
                    "Force": ("FLOAT", {"default": 1.00, "min": 0, "max": 1.00}),
					"MaskWidth": ("FLOAT", {"default": 0.25, "min": 0, "max": 1.00}),
					"Feath_L": ("FLOAT", {"default": 0, "min": 0, "max": 1.00}),
                    "Feath_R": ("FLOAT", {"default": 0.25, "min": 0, "max": 1.00}),
					"MaskPosiX": ("FLOAT", {"default": 0.00, "min": 0.00, "max": 1.00}),
                    }
                }
		
		RETURN_TYPES = ("MASK","FLOAT","STRING")
		RETURN_NAMES = ("MASK","New pos","Debug")
		FUNCTION = "Ici3Dn_BuildMask"
		OUTPUT_NODE = True
		CATEGORY = "Ici3Dn_ComFyIU"
		@classmethod
		#def Ici_BuildMask(self,imgWidth,imgHeight,Force, MaskWidth, MaskTransi,MaskPosiX):
		def Ici3Dn_BuildMask(self,destination,Force, MaskWidth, Feath_L,Feath_R,MaskPosiX):	
			pxForce=Force
			#Mask0 = SolidMask().solid(0, imgWidth, imgHeight)[0]
			
			
			mask_size = destination.size()
			mask_width = int(mask_size[2])
			mask_height = int(mask_size[1])
		
			pxWidth=int(mask_width*MaskWidth)
			pxFeather_R=(mask_width*Feath_R)
			pxFeather_L=(mask_width*Feath_L)
			
			Int_pxFeather_R= math.ceil(pxFeather_R)
			Int_pxFeather_L= math.ceil(pxFeather_L)
			
			pxPosition=math.ceil(mask_width*MaskPosiX)	
			
			mask1 = SolidMask().solid(pxForce, pxWidth, mask_height)[0]
			FeatMask = FeatherMask().feather(mask1, Int_pxFeather_L, 0, Int_pxFeather_R, 0)[0]
			
			FinalMask = MaskComposite().combine(destination,FeatMask,pxPosition,0,"add")[0]
			NewPosi=(pxPosition+pxWidth)/mask_width
			
			debugText = "Width: "+ str(pxWidth) + "| Feather Right:" + str(Int_pxFeather_R)+ "| Feather Left:" + str(Int_pxFeather_L)
			
			return (FinalMask,pxWidth,NewPosi,debugText)        

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False
 
class Ici3Dn_Identity:
    def __init__(self, ):
        pass
	
    @classmethod
    def INPUT_TYPES(s):
       
        return {
            "required": {
                "In": {"anything": (AnyType("*"), )},
                "ID": ("STRING", {"multiline": False}),
                "Originale": ("STRING", {"multiline": False}),
            }
        }

    #RETURN_TYPES = ("STRING","STRING")
    RETURN_TYPES=()
    RETURN_NAMES= ()
    FUNCTION = "run"

    CATEGORY = "Ici3Dn_ComFyIU"   
    
    def run(self, In, ID,Originale):
        
        file=(f"{Ici3Dn_data_Conf}\\{ID}.json")
        
        #file= os.path.joint(self.data_Conf,f"{ID}.json")
        isConfFil="False"
        if os.path.exists(file):
            isConfFil="True"
         
        return str(In),{"ui": {"text": "why not"}, "result": isConfFil}   
    
class Ici3Dn_ShowText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
        }
   
    #INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "utils"

    def notify(self, text):
        result=text
        
        return {"ui": {"text": text}, "result": result}
 
