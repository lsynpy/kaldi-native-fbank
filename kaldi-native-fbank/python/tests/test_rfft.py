#!/usr/bin/env python3
#
# Copyright (c)  2021-2023  Xiaomi Corporation (authors: Fangjun Kuang)


import pytest
import torch

import kaldi_native_fbank as knf


@pytest.mark.parametrize("N", [4, 6, 8, 10, 16, 32, 64, 128, 512, 1024, 1000])
def test_rfft(N):
    torch.manual_seed(20250528)
    t = torch.rand(N)
    r = torch.fft.rfft(t)
    assert len(r) == N // 2 + 1, (len(r), N // 2 + 1)

    real = r.real
    imag = r.imag

    k = t.tolist()
    rfft = knf.Rfft(N)

    p = rfft.compute(k)

    assert abs(p[0] - real[0]) < 1e-3, (p[0], real[0])
    assert imag[0] == 0, imag[0]

    assert abs(p[1] - real[-1]) < 1e-3, (p[1], real[-1])
    assert imag[-1] == 0, imag[-1]

    for i in range(1, N // 2):
        assert abs(p[2 * i] - real[i]) < 1e-1, (p[2 * i], real[i])
        # Note: the imaginary part is multiplied by negative 1
        assert abs(p[2 * i + 1] - imag[i]) < 1e-1, (p[2 * i + 1], imag[i])
