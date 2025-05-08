from .preprocess import g2p
from .inference import inference, available_providers, speakers
from .conv import rate, pcm_to_wav

default_speaker = speakers[0]


async def tts(
    text: str,
    speaker: str = default_speaker,
    with_wav: bool = True,
    force_tokenize: bool = False,
):
    restokens = g2p(text, force_tokenize=force_tokenize)
    if type(restokens) == str:
        return restokens
    res = await inference(restokens, speaker)
    if with_wav and type(res) != str:
        return pcm_to_wav(res)
    else:
        return res


__all__ = [
    "tts",
    "get_speakers",
    "available_providers",
    "default_speaker",
    "rate",
    "pcm_to_wav",
    "g2p",
]
