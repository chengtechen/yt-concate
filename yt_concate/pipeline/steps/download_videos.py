from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download:', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exist(yt):
                print(f'found existing video file fot {url}, skipping')
                continue

            print('downloading', url)
            try:
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
            except KeyError:
                print('Error when download video for ', url)
                continue
            except:
                print('Error when download video for ', url)
                continue

        return data

