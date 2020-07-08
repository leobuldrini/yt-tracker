import json
import numpy
import pandas as pd
import main

#main.createJSON()

file = "inutilismo.json"
with open(file, 'r') as f:
    data = json.load(f)

channel_id, stats = data.popitem()
print(channel_id)
channel_stats = stats['channel_statistics']
video_stats = stats['dados_do_video']
print(channel_stats["viewCount"])

sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True)
stats = []
for vid in sorted_vids:
    video_id = vid[0]
    title = vid[1]["title"]
    views = vid[1]["viewCount"]
    likes = vid[1]["likeCount"]
    dislikes = vid[1]["dislikeCount"]
    comments = vid[1]["commentCount"]
    date = vid[1]["publishedAt"]
    stats.append([video_id, title, views, likes, dislikes, comments, date])

df = pd.DataFrame(data=stats, columns=['ID', 'Title', 'Views', 'Likes', 'Dislikes', 'Comments', 'Published at'])
print(df.head(10))