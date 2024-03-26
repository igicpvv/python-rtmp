from ffmpeg_streaming import Formats, input


video = input(f'lives/sample.flv')
dash = video.dash(Formats.h264())
dash.auto_generate_representations()
dash.output('lives/dash.mpd')