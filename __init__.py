import importlib.util
import glob
import os
import sys
from .ici3dn import init, get_ext_dir
#from .nodes.nodes import *
#from .nodes.showText import *

#from .nodes.loopback import *


#NODE_CLASS_MAPPINGS = { 
#	"Ici3Dn Build Mask":Ici3Dn_Mask,
#    "Ici3Dn identity":Ici3Dn_Identity,
#    "Ici3Dn ShowText":Ici3Dn_ShowText,
#    "Ici3Dn ViewText":Ici3Dn_ViewText,
#    "ShowText test":ShowText
  
#}

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

if init():
    py = get_ext_dir("py")
    files = glob.glob(os.path.join(py, "*.py"), recursive=False)
    for file in files:
        name = os.path.splitext(file)[0]
        spec = importlib.util.spec_from_file_location(name, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        if hasattr(module, "NODE_CLASS_MAPPINGS") and getattr(module, "NODE_CLASS_MAPPINGS") is not None:
            NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
            if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS") and getattr(module, "NODE_DISPLAY_NAME_MAPPINGS") is not None:
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
               
    print(f"Ici3Dn : {NODE_DISPLAY_NAME_MAPPINGS}")
    
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

    
print("\033[ComfyUI_Ici3Dn_Nodes: \033[92mLoaded\033[0m")
