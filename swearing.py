import pyaudio, os, wave, time, random
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_FILE = os.path.join(TOP_DIR, "final_swear_words/common.res")
DETECT_Fuck = os.path.join(TOP_DIR, "final_swear_words/fuck.wav")
#DETECT_Fuck = os.path.join(TOP_DIR, "fuck.mp3")
fuck=DETECT_Fuck

DETECT_FuckYou = os.path.join(TOP_DIR, "final_swear_words/fuckyou.wav")
#DETECT_FuckYou = os.path.join(TOP_DIR, "fuckyou.mp3")
fuckyou=DETECT_FuckYou

DETECT_Mother = os.path.join(TOP_DIR, "final_swear_words/mother_fuckers.wav")
mother=DETECT_Mother

DETECT_Fucking_prick = os.path.join(TOP_DIR, "final_swear_words/fucking_prick.wav")
fucking_prick=DETECT_Fucking_prick

DETECT_Holy_shit = os.path.join(TOP_DIR, "final_swear_words/holy_shit.wav")
holy_shit=DETECT_Holy_shit

DETECT_Bastard = os.path.join(TOP_DIR, "final_swear_words/bastard.wav")
bastard=DETECT_Bastard

DETECT_Horse_fucker = os.path.join(TOP_DIR, "final_swear_words/horse_fucker.wav")
horse_fucker=DETECT_Horse_fucker

DETECT_Shitface = os.path.join(TOP_DIR, "final_swear_words/shitface.wav")
shitface=DETECT_Shitface

DETECT_Wanker = os.path.join(TOP_DIR, "final_swear_words/wankers.wav")
wanker=DETECT_Wanker

#def play_audio_file(fname=DETECT_DING):
def play_audio_file():
    """Simple callback function to play a wave file. By default it plays
    a Ding sound.

    :param str fname: wave file name
    :return: None
    """
    swearWords = [fuck, fuckyou, fucking_prick, mother, holy_shit, horse_fucker, shitface, wanker]
    randomly = random.choice(swearWords)
    print randomly

    ding_wav = wave.open(randomly, 'rb')
    ding_data = ding_wav.readframes(ding_wav.getnframes())
    audio = pyaudio.PyAudio()
    stream_out = audio.open(
        format=audio.get_format_from_width(ding_wav.getsampwidth()),
        channels=ding_wav.getnchannels(),
        rate=ding_wav.getframerate(), input=False, output=True)
    stream_out.start_stream()
    stream_out.write(ding_data)
    time.sleep(0.2)
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()
