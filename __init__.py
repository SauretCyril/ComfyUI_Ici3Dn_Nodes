from .nodes.nodes import *
from .nodes.showText import *

#from .nodes.loopback import *


NODE_CLASS_MAPPINGS = { 
	"Ici3Dn Build Mask":Ici3Dn_Mask,
    "Ici3Dn identity":Ici3Dn_Identity,
    "Ici3Dn ShowText":Ici3Dn_ShowText,
    "Ici3Dn ViewText":Ici3Dn_ViewText,
    "ShowText test":ShowText
  
    }


    
print("\033[ComfyUI_Ici3Dn_Nodes: \033[92mLoaded\033[0m")
