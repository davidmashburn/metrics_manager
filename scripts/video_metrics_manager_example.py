from metrics_manager.video_metrics_manager import *

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

# Sample file to analyze:
f = os.path.expanduser('~/sciencecasts-_total_eclipse_of_the_moon.mp4')

if not os.path.exists(f):
    print('File not available, downloading to ' + f)
    url = 'http://www.nasa.gov/downloadable/videos/sciencecasts-_total_eclipse_of_the_moon.mp4'
    urlretrieve(url, f)
    print('Finished downloading')

metrics_definitions = [
    #Metadata metrics:
    [VIDEO_FPS, Metric, METADATA],
    [VIDEO_NUM_FRAMES, Metric, METADATA],
    [VIDEO_SAMPLING_INTERVAL, Metric, METADATA],
    [AUDIO_FPS, Metric, METADATA],
    [AUDIO_NUM_SAMPLES, Metric, METADATA],
    [AUDIO_SAMPLING_INTERVAL, Metric, METADATA],
    
    #Other metrics:
    [AUDIO_TRACE, TimeMetric, AUDIO, identity, ag(AUDIO_SAMPLING_INTERVAL)],
]

mm = VideoMetricsManager(f, NpyStorageInterface(), metrics_definitions,
                         metrics_dict={})
mm.get_metrics([VIDEO_NUM_FRAMES,
                VIDEO_FPS,
                VIDEO_SAMPLING_INTERVAL,
                AUDIO_NUM_SAMPLES,
                AUDIO_FPS,
                AUDIO_SAMPLING_INTERVAL,
                AUDIO_TRACE,
               ],
              #force_resave=True,
)

# Prove it worked by plotting the audio from the video :)
import plt
plt.ioff()
plt.plot(mm.get_metrics([AUDIO_TRACE])[AUDIO_TRACE].data)
plt.show()
