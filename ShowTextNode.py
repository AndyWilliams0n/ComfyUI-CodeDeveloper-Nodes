class CodeDeveloperShowText:
    def __init__(self):
        self.type = "output"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {        
                "text": ("STRING", {
                    "forceInput": True
                }),     
            },
            "hidden": {},
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "display_text"
    OUTPUT_NODE = True
    CATEGORY = "code"
    
    def display_text(self, text):
        print("TEXT OUTPUT:")
        print(text)

        return {
            "ui": {
                "string": [text,]
            },
            "result": (text,)
        }
    
NODE_CLASS_MAPPINGS = {
    "CodeDeveloper_Display_Text": CodeDeveloperShowText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CodeDeveloper_Display_Text": "Display Text"
}


