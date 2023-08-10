# 1 import
from youtube_transcript_api import YouTubeTranscriptApi as yta
import convert_format as convert

# 2 get youtube video id
# https://www.youtube.com/watch?v=Cj1AB3XCSTo
vid_id = 'Cj1AB3XCSTo'
data = yta.get_transcript(vid_id,languages=['pt','en'], preserve_formatting=True)
# 3 logic
import json


# with open("episodio_168.txt", 'w', encoding='utf8') as file:
#   json.dump(data,file,indent=4)
transcript = ''

for i,value in enumerate(data):
  script_format = convert.calculate_and_format_times(value['start'],value['duration'])
  transcript += f"{i+1}\n{script_format}\n{value['text']}\n\n"


# Example usage
# api_time = "17.66 --> 10.789"
# formatted_subtitle = convert_and_format_time(api_time)
# print(formatted_subtitle)

# 4 outuput to file
file = open("episodio_168.srt", 'w', encoding='utf8')
file.write(transcript)
file.close()

# 17.66 --> 10.789
# 1
# 00:02:16,612 --> 00:02:19,376
# Senator, we're making
# our final approach into Coruscant.