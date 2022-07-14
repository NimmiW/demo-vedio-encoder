import ffmpeg
import sys
sys.path.append('ffmpeg')

out_file = 'out.mp4'
in_file = 'in_3.mp4'

def get_data(in_file):
    try:
        probe = ffmpeg.probe(in_file)
    except ffmpeg.Error as e:
        print(e)
        sys.exit(1)
        
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print('No video stream found', file=sys.stderr)
        sys.exit(1)

    width = int(video_stream['width'])
    height = int(video_stream['height'])
    num_frames = int(video_stream['nb_frames'])
    print('width: {}'.format(width))
    print('height: {}'.format(height))
    print('num_frames: {}'.format(num_frames))
    
def flip_vertically(in_file, out_file):
    input = ffmpeg.input(in_file)
    audio = input.audio#.filter("aecho", 0.8, 0.9, 1000, 0.3)
    video = input.video.vflip()

    out = ffmpeg.output(audio, video, out_file)
    out.overwrite_output().run()
    
    
    
    
print(get_data(in_file))
flip_vertically(in_file, out_file)