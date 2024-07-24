from .CodeDeveloperCreateText import CodeDeveloperCreateText
from .CodeDeveloperDisplayText import CodeDeveloperDisplayText

class OmniType(str):
    def __ne__(self, __value: object) -> bool:
        return False
    
OMNI = OmniType("*")

NODE_CLASS_MAPPINGS = {
    "CodeDeveloperCreateText": CodeDeveloperCreateText,
    "CodeDeveloperDisplayText": CodeDeveloperDisplayText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CodeDeveloperCreateText": "Create Text ♾️",
    "CodeDeveloperDisplayText": "Display Text ♾️"
}

WEB_DIRECTORY = "./web"
