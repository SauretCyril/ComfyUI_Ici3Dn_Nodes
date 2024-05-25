class Ici3Dn_test:
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
		FUNCTION = "Ici3Dn_test"
		OUTPUT_NODE = True
		CATEGORY = "Ici3Dn_ComFyIU"
		@classmethod
		#def Ici_BuildMask(self,imgWidth,imgHeight,Force, MaskWidth, MaskTransi,MaskPosiX):
		def Ici3Dn_test(self,destination,Force, MaskWidth, Feath_L,Feath_R,MaskPosiX):	
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
