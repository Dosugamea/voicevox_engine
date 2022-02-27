import json
from logging import getLogger
from typing import Any, Dict, List

import numpy as np
from pyopenjtalk import tts
from scipy.signal import resample

DUMMY_TEXT = "これはダミーのテキストです"


def initialize(path: str, use_gpu: bool, *args: List[Any]) -> None:
    pass


def yukarin_s_forward(length: int, **kwargs: Dict[str, Any]) -> np.ndarray:
    logger = getLogger("uvicorn")  # FastAPI / Uvicorn 内からの利用のため
    logger.info(
        "Sorry, yukarin_s_forward() is a mock. Return values are incorrect.",
    )
    return np.ones(length) / 5


def yukarin_sa_forward(length: int, **kwargs: Dict[str, Any]) -> np.ndarray:
    logger = getLogger("uvicorn")  # FastAPI / Uvicorn 内からの利用のため
    logger.info(
        "Sorry, yukarin_sa_forward() is a mock. Return values are incorrect.",
    )
    return np.ones((1, length)) * 5


def decode_forward(length: int, **kwargs: Dict[str, Any]) -> np.ndarray:
    """
    合成音声の波形データをNumPy配列で返します。ただし、常に固定の文言を読み上げます（DUMMY_TEXT）
    参照→SynthesisEngine のdocstring [Mock]

    Parameters
    ----------
    length : int
        フレームの長さ

    Returns
    -------
    wave : np.ndarray
        音声合成した波形データ

    Note
    -------
        ここで行う音声合成では、調声（ピッチ等）を反映しない
        また、入力内容によらず常に固定の文言を読み上げる

        # pyopenjtalk.tts()の出力仕様
        dtype=np.float64, 16 bit, mono 48000 Hz

        # resampleの説明
        非モックdecode_forwardと合わせるために、出力を24kHzに変換した。
    """
    logger = getLogger("uvicorn")  # FastAPI / Uvicorn 内からの利用のため
    logger.info(
        "Sorry, decode_forward() is a mock. Return values are incorrect.",
    )
    wave, sr = tts(DUMMY_TEXT)
    wave = resample(
        wave.astype("int16"),
        24000 * len(wave) // 48000,
    )
    return wave


def metas() -> str:
    return json.dumps(
        [
            {
                "name": "つくよみちゃん",
                "styles": [
                    {"name": "れいせい", "id": 0},
                    {"name": "おしとやか", "id": 5},
                    {"name": "げんき", "id": 6},
                ],
                "speaker_uuid": "3c37646f-3881-5374-2a83-149267990abc",
                "version": "3.0.0",
            },
            {
                "name": "MANA",
                "styles": [
                    {"name": "のーまる", "id": 1},
                ],
                "speaker_uuid": "292ea286-3d5f-f1cc-157c-66462a6a9d08",
                "version": "3.0.0",
            },
            {
                "name": "おふとんP",
                "styles": [
                    {"name": "のーまる", "id": 2},
                ],
                "speaker_uuid": "a60ebf6c-626a-7ce6-5d69-c92bf2a1a1d0",
                "version": "3.0.0",
            },
            {
                "name": "ディアちゃん",
                "styles": [
                    {"name": "のーまる", "id": 3},
                ],
                "speaker_uuid": "b28bb401-bc43-c9c7-77e4-77a2bbb4b283",
                "version": "3.0.0",
            },
            {
                "name": "アルマちゃん",
                "styles": [
                    {"name": "のーまる", "id": 4},
                ],
                "speaker_uuid": "c97966b1-d80c-04f5-aba5-d30a92843b59",
                "version": "3.0.0",
            },
        ]
    )