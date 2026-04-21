"""
Type stubs for kaldi-native-fbank

# Copyright (c) 2025 (authors: Bangwen He)
"""

from typing import Dict, List, Mapping, Union
import numpy as np

class FbankOptions:
    """Filter bank feature extraction options."""

    def __init__(self) -> None: ...

    # Properties
    frame_opts: FrameExtractionOptions
    mel_opts: MelBanksOptions
    use_energy: bool
    energy_floor: float
    raw_energy: bool
    htk_compat: bool
    use_log_fbank: bool
    use_power: bool

    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, Union[Dict[str, Union[float, bool, str]], Dict[str, Union[int, float, bool, str]], bool, float]]: ...
    @staticmethod
    def from_dict(d: Mapping[str, Union[Mapping, bool, float]]) -> "FbankOptions": ...

class MfccOptions:
    """MFCC feature extraction options."""

    def __init__(self) -> None: ...

    # Properties
    frame_opts: FrameExtractionOptions
    mel_opts: MelBanksOptions
    num_ceps: int
    use_energy: bool
    energy_floor: float
    raw_energy: bool
    cepstral_lifter: float
    htk_compat: bool

    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, Union[Dict[str, Union[float, bool, str]], Dict[str, Union[int, float, bool, str]], int, bool, float]]: ...
    @staticmethod
    def from_dict(d: Mapping[str, Union[Mapping, int, bool, float]]) -> "MfccOptions": ...

class FrameExtractionOptions:
    """Frame extraction options for audio processing."""

    def __init__(self) -> None: ...

    # Properties
    samp_freq: float
    frame_shift_ms: float
    frame_length_ms: float
    dither: float
    preemph_coeff: float
    remove_dc_offset: bool
    window_type: str
    round_to_power_of_two: bool
    blackman_coeff: float
    snip_edges: bool

    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, Union[float, bool, str]]: ...
    @staticmethod
    def from_dict(d: Mapping[str, Union[float, bool, str]]) -> "FrameExtractionOptions": ...

class FeatureWindowFunction:
    """Feature window function for applying windowing to audio frames."""

    def __init__(self, opts: FrameExtractionOptions) -> None: ...

    def apply(self, wave: List[float]) -> List[float]: ...

    @property
    def window(self) -> List[float]: ...

class IStft:
    """Inverse Short-Time Fourier Transform."""

    def __init__(self, config: StftConfig) -> None: ...

    def compute(self, stft_result: StftResult) -> List[float]: ...
    def __call__(self, stft_result: StftResult) -> List[float]: ...

class MelBanksOptions:
    """Mel filter bank options."""

    def __init__(self) -> None: ...

    # Properties
    num_bins: int
    low_freq: float
    high_freq: float
    vtln_low: float
    vtln_high: float
    debug_mel: bool
    htk_mode: bool
    is_librosa: bool
    norm: str
    use_slaney_mel_scale: bool
    floor_to_int_bin: bool

    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, Union[int, float, bool, str]]: ...
    @staticmethod
    def from_dict(d: Mapping[str, Union[int, float, bool, str]]) -> "MelBanksOptions": ...

class MelBanks:
    """Mel filter bank for computing mel spectrograms."""

    def __init__(
        self,
        opts: MelBanksOptions = ...,
        frame_opts: FrameExtractionOptions = ...,
        vtln_warp_factor: float = 1.0
    ) -> None: ...

    @property
    def dim(self) -> int: ...

    def get_matrix(self) -> np.ndarray: ...
    def compute(self, fft_energies: np.ndarray) -> np.ndarray: ...

    @staticmethod
    def inverse_mel_scale(mel: float) -> float: ...

    @staticmethod
    def mel_scale(hz: float) -> float: ...

    @staticmethod
    def inverse_mel_scale_slaney(mel: float) -> float: ...

    @staticmethod
    def mel_scale_slaney(hz: float) -> float: ...

class RawAudioSamplesOptions:
    """Raw audio samples options."""

    def __init__(self) -> None: ...

    # Properties
    frame_opts: FrameExtractionOptions

    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, Dict[str, Union[float, bool, str]]]: ...
    @staticmethod
    def from_dict(d: Mapping[str, Mapping]) -> "RawAudioSamplesOptions": ...

class OnlineRawAudioSamples:
    """Online raw audio samples extractor."""

    def __init__(self, opts: RawAudioSamplesOptions) -> None: ...

    @property
    def dim(self) -> int: ...

    @property
    def frame_shift_in_seconds(self) -> float: ...

    @property
    def num_frames_ready(self) -> int: ...

    def is_last_frame(self, frame: int) -> bool: ...
    def get_frame(self, frame: int) -> np.ndarray: ...
    def accept_waveform(self, sampling_rate: float, waveform: List[float]) -> None: ...
    def input_finished(self) -> None: ...
    def pop(self, n: int) -> None: ...

class WhisperFeatureOptions:
    """Whisper feature extraction options."""

    def __init__(self) -> None: ...

    # Properties
    frame_opts: FrameExtractionOptions
    dim: int

    def __str__(self) -> str: ...
    def as_dict(self) -> Dict[str, Union[Dict[str, Union[float, bool, str]], int]]: ...
    @staticmethod
    def from_dict(d: Mapping[str, Union[Mapping, int]]) -> "WhisperFeatureOptions": ...

class OnlineFbank:
    """Online filter bank feature extractor."""

    def __init__(self, opts: FbankOptions) -> None: ...

    @property
    def dim(self) -> int: ...

    @property
    def frame_shift_in_seconds(self) -> float: ...

    @property
    def num_frames_ready(self) -> int: ...

    def is_last_frame(self, frame: int) -> bool: ...
    def get_frame(self, frame: int) -> np.ndarray: ...
    def accept_waveform(self, sampling_rate: float, waveform: List[float]) -> None: ...
    def input_finished(self) -> None: ...
    def pop(self, n: int) -> None: ...

class OnlineMfcc:
    """Online MFCC feature extractor."""

    def __init__(self, opts: MfccOptions) -> None: ...

    @property
    def dim(self) -> int: ...

    @property
    def frame_shift_in_seconds(self) -> float: ...

    @property
    def num_frames_ready(self) -> int: ...

    def is_last_frame(self, frame: int) -> bool: ...
    def get_frame(self, frame: int) -> np.ndarray: ...
    def accept_waveform(self, sampling_rate: float, waveform: List[float]) -> None: ...
    def input_finished(self) -> None: ...
    def pop(self, n: int) -> None: ...

class OnlineWhisperFbank:
    """Online Whisper filter bank feature extractor."""

    def __init__(self, opts: WhisperFeatureOptions) -> None: ...

    @property
    def dim(self) -> int: ...

    @property
    def frame_shift_in_seconds(self) -> float: ...

    @property
    def num_frames_ready(self) -> int: ...

    def is_last_frame(self, frame: int) -> bool: ...
    def get_frame(self, frame: int) -> np.ndarray: ...
    def accept_waveform(self, sampling_rate: float, waveform: List[float]) -> None: ...
    def input_finished(self) -> None: ...
    def pop(self, n: int) -> None: ...

class Rfft:
    """Real-valued Fast Fourier Transform."""

    def __init__(self, n: int, inverse: bool = False) -> None: ...

    def compute(self, d: List[float]) -> List[float]: ...

class StftConfig:
    """STFT configuration parameters."""

    def __init__(
        self,
        n_fft: int,
        hop_length: int,
        win_length: int,
        window_type: str = "",
        center: bool = True,
        pad_mode: str = "reflect",
        normalized: bool = False,
        window: List[float] = []
    ) -> None: ...

    # Properties
    n_fft: int
    hop_length: int
    win_length: int
    window_type: str
    center: bool
    pad_mode: str
    normalized: bool

    def __str__(self) -> str: ...

class StftResult:
    """STFT computation result containing real and imaginary parts."""

    def __init__(self, real: List[float], imag: List[float], num_frames: int) -> None: ...

    @property
    def real(self) -> List[float]: ...

    @property
    def imag(self) -> List[float]: ...

    @property
    def num_frames(self) -> int: ...

class Stft:
    """Short-Time Fourier Transform."""

    def __init__(self, config: StftConfig) -> None: ...

    def compute(self, input: List[float]) -> StftResult: ...
    def __call__(self, input: List[float]) -> StftResult: ...
