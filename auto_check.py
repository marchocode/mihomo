import os
from config_loader import ConfigLoader

def token_check(token: str,config:ConfigLoader) -> None:
    
    sys_token = os.getenv('TOKEN')

    ## first
    if sys_token == token:
        return
    
    ## second
    if config.get_token() == token:
        return

    raise PermissionError("Invalid token")