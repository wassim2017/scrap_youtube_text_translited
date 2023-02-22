"""
    This Script of scrap text from youtube video with translite text as file
    author: FOUAD ATTIG 2023
    Country: ALGERIA

    lib install:
        pip install -r req.text

"""
from youtube_transcript_api import YouTubeTranscriptApi
import os
os.system("cls")



def get_id_video(url):
    """This Function of get id from url youtube video

    Args:
        url (string): this a valid url youtube video.

    Returns:
        string,None: return string If the video is working else None.
    """
    try:
        if "&" in url:
            id = url.split('=')[1].split('&')[0]
        else:
            id = url.split('=')[1]
        return id
    except:
        return None

def scrap_text_video_youtube(id_video,lang_find=['ar', 'en',"fr"],translite_to="fr",show_file=True):
    """This Function of scrap text from youtube video

    Args:
        id_video (string): id youtube video or id.
        lang_find (list, optional): this lang find to current video. Defaults to ['ar', 'en',"fr"].
        translite_to (str, optional): this lang want to translite text from video. Defaults to "ar".
        show_file (bool, optional): this option of explore folder working. Defaults to True.
    """
    data =None
    try:
        data = YouTubeTranscriptApi.get_transcript(video_id=id_video)#languages=['ar', 'en',"fr"]
        transcript_list = YouTubeTranscriptApi.list_transcripts(id_video)
        transcript = transcript_list.find_transcript(lang_find)
        translated_transcript = transcript.translate(translite_to)
        file_name= f'output/video_{str(id)}/orgin_text.txt'
        file_tra= f'output/video_{str(id)}/transit_text.txt'
        for i in data:
            with open(file_name,"a+",encoding="utf8") as f:
                f.write(i['text']+"\n")
        for c in translated_transcript.fetch():
            # print(c['text']+"\n")
            with open(file_tra,"a+",encoding="utf8") as f:
                f.write(c['text']+"\n")

        
        if show_file:
            if os.path.exists(f'output/video_{str(id)}'):
                start_folder = os.path.join('output',f'video_{str(id)}')
                print(start_folder)
                os.system(f'start {str(start_folder)}')
        exit(0)

    except Exception as ex:
        if "Subtitles are disabled for this video" in str(ex):
            print(f'[-] This video id("{id_video}") has no subtitles.. (-_-)\n\t\tPLEASE TRY AGAIN..')
        else:
            print(f'[-] ERROR:\n{str(ex)}.')
        exit(0)


if __name__ == '__main__':
    if not os.path.exists('output'):
        os.system("mkdir output")
    id = str(input("Enter link video youtube or video id: "))
    if 'https' in id:
        id = get_id_video(id)
        if id:
            if not os.path.exists(f'output/video_{str(id)}'):
                os.system(f'mkdir "output/video_{str(id)}"')
            scrap_text_video_youtube(id)
        else:
            print('[ERROR]: video not valid tyr again ..')





