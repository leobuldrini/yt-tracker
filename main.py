from youtube_statistics import YTstats

#266103494904-qqf6q5h7am12let79mrm1ong26cm1rns.apps.googleusercontent.com

API_KEY = "AIzaSyA5OpjLeWdzFpCHcP6Vbs5Ae6mjIKkm8Rc"
channel_id = "UCK-rDvDp1O1uxxwLUHgt1gQ"

def createJSON():
    yt = YTstats(API_KEY, channel_id)
    yt.get_channel_statistics()
    yt.get_channel_video_data()
    yt.dump()

