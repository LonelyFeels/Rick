import os
import urllib.request
import json


class ServerStatus:
    def __init__(self) -> None:
        response = urllib.request.urlopen("https://api.mcsrvstat.us/1/148.251.236.239:25565")
        data = json.load(response)
        self.online: bool = data['debug']['ping']
        # If not online skip this
        if self.online:
            self.motd: str = data['motd']['clean'][0].strip()
            self.version: int = data['version']
            self.online_players: int = data['players']['online']    
            self.max_players: int = data['players']['max']
            self.players_list: str = '\n'.join(data['players']['list'])