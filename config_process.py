import yaml
from clash_merger import ClashMerger
from proxy_provider import ProxyProvider
from config_loader import ConfigLoader

class ConfigProcessor:

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.clash_merger: ClashMerger = None
        self.output_path = "output.yaml"

    def dump(self) -> str:
        return self.clash_merger.dump()

    def get_output_path(self) -> str:
        return self.output_path

    def process(self) -> None:

        list_providers = []

        for sub in self.config.get_subs():
            name = sub.get('name')
            url = sub.get('url')
            list_providers.append(ProxyProvider(name, url))
        
        self.clash_merger = ClashMerger(list_providers)
        self.clash_merger.merge()