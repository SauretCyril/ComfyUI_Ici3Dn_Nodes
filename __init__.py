from .nodes.nodes import *
from .nodes.nodes_id import *
#from .nodes.loopback import *


NODE_CLASS_MAPPINGS = { 
	"Ici3Dn Build Mask":Ici3Dn_Mask,
    "Ici3Dn identity":Ici3Dn_identity}
    
print("\033[ComfyUI_Ici3Dn_Nodes: \033[92mLoaded\033[0m")
