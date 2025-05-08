from onnxruntime import InferenceSession, get_available_providers
import numpy as np
from .paths import basepath
from os import listdir
from typing import List, Union
from .paths import basepath
from asyncio import Lock

__bp = basepath.joinpath("./store/voices")
__bps = [
    (
        __bp.joinpath(n),
        n.split(".")[0].split("_")[-1],
    )
    for n in list(
        filter(lambda x: x.endswith(".bin") and x.startswith("jf_"), listdir(__bp))
    )
]
stylemap = {n: np.fromfile(p, dtype=np.float32).reshape(-1, 1, 256) for (p, n) in __bps}
model = InferenceSession(basepath.joinpath("./store/model.onnx"))

speakers: List[str] = list(stylemap.keys())

__lock = Lock()


async def inference(tokens: List[int], speaker: str) -> Union[str, np.ndarray]:
    if speaker not in stylemap:
        return f"Speaker {speaker} not found, available speakers are: {', '.join(stylemap.keys())}"
    if len(tokens) > 510:
        return f"Token length is {len(tokens)}, please limit to 510 tokens."
    ref_s = stylemap[speaker][len(tokens)]
    tokens = [[0, *tokens, 0]]
    async with __lock:
        audio = model.run(
            None,
            dict(
                input_ids=tokens,
                style=ref_s,
                speed=np.array([1], dtype=np.float32),
            ),
        )[0]
    return audio[0]


def available_providers() -> List[str]:
    return get_available_providers()
