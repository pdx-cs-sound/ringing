# ringing: IIR Filter Ringing Demo
Bart Massey 2022

This demo shows a difference between FIR and IIR filtering.

`ringing.py` generates an excitation signal by mixing three
one-second sine waves — 700Hz, 1000Hz and 1400Hz — and then
appending a one-second silence. This excitation is written
to `ringing-in.wav`.

The excitation is narrowly bandpass filtered at 1000Hz with
a 1023-point FIR windowed filter. The result is written to
`ringing-fir.wav`.

The excitation is then narrowly bandpass filtered at 1000Hz
with a 10-pole IIR filter. The result is written to
`ringing-iir.wav`.

Note that the FIR-filtered signal has a sharp start and stop
point, while the IIR-filtered signal "fades in" and "fades
out". This is because the IIR filter takes past history into
account: the filter "rings" with a decay time roughly
proportional to the filter gain at its peak frequency.

This is the price we pay for doing 100th the calculation.
