from misaki import ja
import json
from typing import Dict, List, Union
from .paths import basepath

__tokens: Dict[str, int] = json.load(
    open(basepath.joinpath("./store/tokens.json"), "r", encoding="utf-8")
)
__g2pcls = ja.JAG2P()


def g2p(text: str, force_tokenize: bool = False) -> Union[List[int], str]:
    if len(text) > 510 * 3 and not force_tokenize:
        return f"Text length is {len(text)}, I think its too long that may exceed 510 tokens. Long text takes a long time to preprocess, if you want to force it, set force_tokenize=True"
    phonemes, __unused = __g2pcls(text)
    return list(
        filter(lambda i: i is not None, map(lambda p: __tokens.get(p), phonemes))
    )
