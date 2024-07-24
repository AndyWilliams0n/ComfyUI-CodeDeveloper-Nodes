class CodeDeveloperDisplayText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "forceInput": True,
                }),
            }
        }

    RETURN_TYPES = ("STRING",)

    OUTPUT_NODE = True

    CATEGORY = "code"

    FUNCTION = "display_text"

    def display_text(self, text):
        return {
            "ui": {
                "string": [text,]
            },
            "result": (text,)
        }
