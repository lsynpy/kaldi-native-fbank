#!/usr/bin/env python3
#
# Copyright (c)  2025  Xiaomi Corporation (authors: Fangjun Kuang)


import kaldi_native_fbank as knf
import pytest
import torch


def test_stft_config():
    config = knf.StftConfig(
        n_fft=512,
        hop_length=128,
        win_length=512,
        window_type="povey",
        center=True,
        pad_mode="reflect",
        normalized=False,
    )
    print(config)


def _test_stft_impl(n_fft, normalized, window_type="", center=False):
    hop_length = n_fft // 4
    win_length = n_fft

    window = None

    if window_type == "hann":
        window = torch.hann_window(win_length)
    elif window_type == "hann2":
        window = torch.hann_window(win_length).pow(0.5)

    samples = torch.rand(50000)
    config = knf.StftConfig(
        n_fft=n_fft,
        hop_length=hop_length,
        win_length=n_fft,
        window_type=window_type,
        center=center,
        pad_mode="reflect",
        normalized=normalized,
        window=window.tolist() if window is not None else [],
    )
    torch_result = torch.stft(
        samples,
        n_fft=n_fft,
        hop_length=hop_length,
        center=center,
        return_complex=False,
        normalized=normalized,
        window=window,
    )
    # y.shape: (n_fft/2+1, num_frames, 2)

    stft = knf.Stft(config)
    k = stft(samples.tolist())
    knf_result = torch.tensor([k.real, k.imag]).reshape(2, k.num_frames, -1)
    # now knf_result is (2, num_frames, n_fft/2+1)

    knf_result = knf_result.permute(2, 1, 0)

    assert torch.allclose(torch_result, knf_result, atol=1e-3), (
        torch_result,
        knf_result,
        torch_result.shape,
        knf_result.shape,
    )
    print(f"Passed: n_fft={n_fft}, normalized={normalized}, window_type={window_type}")


@pytest.mark.parametrize("n_fft", [6, 10, 400, 1000, 8, 64, 128, 256, 512, 1024, 2048, 4096])
@pytest.mark.parametrize("normalized", [True, False])
@pytest.mark.parametrize("window_type", ["", "hann", "hann2"])
@pytest.mark.parametrize("center", [True, False])
def test_stft(n_fft, normalized, window_type, center):
    torch.manual_seed(20250308)
    _test_stft_impl(
        n_fft=n_fft,
        normalized=normalized,
        window_type=window_type,
        center=center,
    )
