import numpy as np
import scipy.signal as ss
import scipy.io.wavfile as wav

sample_rate = 48000

def sine(f, t):
    ts = np.linspace(0, t, num=sample_rate, endpoint=False, dtype = np.float32)
    return np.sin(2 * np.pi * f * ts)


tones = 0.5 * (1/3) * (sine(700, 1) + sine(1000, 1) + sine(1400, 1))
silence = np.zeros(sample_rate, dtype = np.float32)
exc = np.append(tones, silence)
wav.write("ringing-in.wav", sample_rate, exc)

fir = ss.firwin(
    1023,
    cutoff = [999, 1001],
    pass_zero = False,
    scale = True,
    fs = sample_rate,
)
ffir = ss.convolve(
    fir,
    exc,
)
wav.write("ringing-fir.wav", sample_rate, ffir)

iir = ss.iirfilter(
    10,
    [990, 1010],
    btype = 'bandpass',
    output = 'sos',
    fs = sample_rate,
)
fiir = ss.sosfilt(
    iir,
    exc,
)
wav.write("ringing-iir.wav", sample_rate, fiir)
