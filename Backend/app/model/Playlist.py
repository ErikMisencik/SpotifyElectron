import json
from dataclasses import dataclass
from typing import List

from app.model.model_schema import SpotifyElectronModel


@dataclass
class Playlist(SpotifyElectronModel):
    name: str
    photo: str
    description: str
    upload_date: str
    owner: str
    song_names: List[str]

    def add_songs(self, songs: List[str]) -> None:
        self.song_names.extend(songs)

    def get_json(self) -> str:
        json.dumps(self.__dict__)
        playlist_json = json.dumps(self.__dict__)
        return playlist_json
