from .nodes.nodes import *
from .nodes.loopback import *


NODE_CLASS_MAPPINGS = { 
	"Ici3Dn Build Mask":Ici3Dn_Mask,
    "ici3Dn identity":ici3Dn_identity}
    
print("\033[ComfyUI_Ici3Dn_Nodes: \033[92mLoaded\033[0m")
