from .ShowTextNode import CodeDeveloperShowText

class OmniType(str):
    """A special string type that acts as a wildcard for universal input/output. 
       It always evaluates as equal in comparisons."""
    def __ne__(self, __value: object) -> bool:
        return False
    
OMNI = OmniType("*")


NODE_CLASS_MAPPINGS = {
    "CodeDeveloper_Display_Text": CodeDeveloperShowText,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CodeDeveloper_Display_Text": "Display Text ♾️",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
