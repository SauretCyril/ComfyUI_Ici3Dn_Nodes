import importlib.util
import glob
import os
import sys
from .ici3dn import init, get_ext_dir
from .nodes.nodes import *
from .nodes.showText import *

#from .nodes.loopback import *


#NODE_CLASS_MAPPINGS = { 
#	"Ici3Dn Build Mask":Ici3Dn_Mask,
#    "Ici3Dn identity":Ici3Dn_Identity,
#    "Ici3Dn ShowText":Ici3Dn_ShowText,
#    "Ici3Dn ViewText":Ici3Dn_ViewText,
#    "ShowText test":ShowText
  
#}


NODE_CLASS_MAPPINGS = {
    "ShowText25": ShowText25,
    "Ici3Dn identity":Ici3Dn_Identity
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText25": "Show Text 25",
    "Ici3Dn identity":"Ici3Dn identity"
}

init()

    
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

    
print("\033[ComfyUI_Ici3Dn_Nodes: \033[92mLoaded\033[0m")
