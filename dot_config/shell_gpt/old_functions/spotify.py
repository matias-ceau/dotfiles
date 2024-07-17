import inspect
import os
from pathlib import Path
from typing import Any, Literal

from dotenv import load_dotenv
from pydantic import Field
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from instructor import OpenAISchema

# Load environment variables
load_dotenv(Path(__file__).parent.parent / ".sgptrc")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://localhost:3000"

SCOPES = [
    "user-read-playback-state",
    "user-modify-playback-state",
    "user-read-currently-playing",
    "app-remote-control",
    "streaming",
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-private",
    "playlist-modify-public",
    "user-follow-modify",
    "user-follow-read",
    "user-read-playback-position",
    "user-top-read",
    "user-read-recently-played",
    "user-library-modify",
    "user-library-read",
]

# Define the path for the token cache
CACHE_PATH = Path(__file__).parent.parent / ".cache"

# Function to get Spotify client with proper token handling
def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=" ".join(SCOPES),
        cache_path=CACHE_PATH
    )

    # Fetch the cached token
    token_info = auth_manager.get_cached_token()

    # Refresh the token if it has expired
    if not token_info or auth_manager.is_token_expired(token_info):
        token_info = auth_manager.refresh_access_token(token_info['refresh_token'])

    return Spotify(auth_manager=auth_manager)

spotify = get_spotify_client()

def get_spotify_methods():
    methods = []
    for method_name in dir(Spotify):
        method = getattr(spotify, method_name)

        if callable(method) and not method_name.startswith("_"):
            description = getattr(spotify, method_name).__doc__
            if isinstance(description, str):
                description = (
                    description[: description.index("\n")].strip()
                    if "\n" in description
                    else description
                )
                methods.append(
                    f"{method_name}{inspect.signature(getattr(spotify, method_name))}: {description}"
                )
    return methods

class Function(OpenAISchema):
    """Control spotify via api.
    Always pass function_call.name as 'spotify'.
    Pass function name to execute as function_call.arguments.method.
    Pass arguments as key value pairs in function_call.arguments.
    Never nest arguments deeper than function_call.arguments.
    Example:
    {
        'name': 'spotify',
        'arguments': {
            'method': 'search',
            'q': 'necro',
            'limit': 1,
            'type': 'artist',
        }
    }
    """

    method: Literal[*get_spotify_methods()] = Field(  # type: ignore
        ...,
        description="Method to call, return only the method name as method argument",
    )

    class Config:
        title = "spotify"

    @classmethod
    def execute(cls, *args, **kwargs) -> Any:
        arguments = kwargs.pop("arguments") if "arguments" in kwargs else kwargs
        method = arguments.pop("method")

        # Adjust the user_playlist_create method to use the correct user ID
        if method == 'user_playlist_create':
            user_id = spotify.me()['id']
            arguments['user'] = user_id
        
        try:
            result = getattr(spotify, method)(**arguments)
            return "Success" if result is None else str(result)
        except Exception as e:
            return str(e)
