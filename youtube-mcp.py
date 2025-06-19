from youtube_transcript_api import YouTubeTranscriptApi as yta
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP
import time
from typing import List, Dict
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = os.getenv('YOUTUBE_API_SERVICE_NAME', 'youtube')
YOUTUBE_API_VERSION = os.getenv('YOUTUBE_API_VERSION', 'v3')

mcp = FastMCP("youtube-mcp")

@mcp.tool()
def search_youtube_videos(query: str, max_results: int=5) -> List[str]:
    """
    Searches YouTube for videos that match a given query and returns a list of video IDs.

    Parameters:
        query (str): The search term to query on YouTube.
        max_results: Maximum number of results to retrieve (default: 5)

    Returns:
        list: A list of YouTube video IDs that match the search query.
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        q=query,
        part='id',
        type='video',
        maxResults=max_results
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
    return video_ids



@mcp.tool()
def get_transcript_from_video_ids(video_ids: List[str]) -> Dict[str, str]:
    """
    Retrieves the transcript text for a list of YouTube video IDs.

    Parameters:
        video_ids (list): A list of YouTube video IDs as individual strings (e.g., ["id1", "id2"]).

    Returns:
        dict: A dictionary where keys are video IDs and values are the corresponding transcript text.
            If a transcript is unavailable, the value will contain an error message.
    """
    video_transcripts = {}
    for video_id in video_ids:
        try:
            transcript_list = yta.list_transcripts(video_id)
            for tr in transcript_list:
                data = tr.fetch()
                break
            text = ' '.join([seg.text for seg in data])
            video_transcripts[video_id] = text
        except Exception as e:
            video_transcripts[video_id] = f"No transcript available for this video. {e}"
        time.sleep(0.5)  # API rate limits
    return video_transcripts


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')