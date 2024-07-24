class CodeDeveloperCreateText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "forceInput": False,
                }),
            }
        }

    RETURN_TYPES = ("STRING",)

    OUTPUT_NODE = True

    CATEGORY = "code"

    FUNCTION = "create_text"

    def create_text(self, text):
        return (text,)