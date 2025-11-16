import yaml

class ConfigLoader:

    def __init__(self, path: str):
        self.path = path
        self.config = {}
        self.token = None
        self.subs = []

    def load(self) -> None:
        
        with open(self.path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        mihomo = self.config.get('mihomo', {})
        self.token = mihomo.get('token', "")
        self.subs = mihomo.get('subs', [])

    def get_token(self) -> str:
        return self.token
    
    def get_subs(self) -> list:
        return self.subs