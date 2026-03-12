import unidecode
import logging
import re

SPACE_BEFORE = r"(["
SPACE_AFTER = r")];,"
NO_SPACE_BEFORE = r")]/\-;,"
NO_SPACE_AFTER = r"([/\-"

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


def _createSeq(chars: str, addSpace: bool, before: bool):
    d = {}
    for c in chars:
        if addSpace:
            d[c] = " {}".format(c) if before else "{} ".format(c)
        else:
            k = " {}".format(c) if before else "{} ".format(c)
            d[k] = c
    return d


def _removeKeys(s: str, sequence: dict):
    for k in sequence.keys():
        s = s.replace(str(k), sequence[k])
    return s


def _normalize(txt: str, preferredSeq: dict, removeSeq: dict, toAscii: bool, removeUnprintable: bool, preserveMultispace: bool) -> str:
    if removeUnprintable:
        txt = "".join(c for c in txt if c.isprintable())
    if toAscii:
        txt = unidecode.unidecode(txt)
    txt = _removeKeys(txt, preferredSeq)
    if not preserveMultispace:
        txt = re.sub(r"\s+", " ", txt)
    txt = _removeKeys(txt, removeSeq)
    return txt.strip()


def normalizeTxt(
    txt: str,
    spaceBefore: str = SPACE_BEFORE,
    spaceAfter: str = SPACE_AFTER,
    noSpaceBefore: str = NO_SPACE_BEFORE,
    noSpaceAfter: str = NO_SPACE_AFTER,
    toAscii: bool = True,
    removeUnprintable: bool = True,
    preserveMultispace: bool = False,
) -> str:
    """
    normalizes string s;\n
    'β-NS' --> 'b-NS'\n
    'Some Text(Example)For Display' --> 'Some Text (Example) For Display'
    """
    preferredSequences = _createSeq(spaceBefore, True, True)
    preferredSequences.update(_createSeq(spaceAfter, True, False))
    removeSequences = _createSeq(noSpaceBefore, False, True)
    removeSequences.update(_createSeq(noSpaceAfter, False, False))
    ns = _normalize(txt, preferredSequences, removeSequences, toAscii, removeUnprintable, preserveMultispace)
    _logger.debug("Text '{}' Normalized To '{}'".format(txt, ns))
    return ns


class TextNormalizer(object):
    """provides an object that persists the settings and log debug statements if needed"""

    def __init__(
        self,
        spaceBefore: str = SPACE_BEFORE,
        spaceAfter: str = SPACE_AFTER,
        noSpaceBefore: str = NO_SPACE_BEFORE,
        noSpaceAfter: str = NO_SPACE_AFTER,
        toAscii: bool = True,
        removeUnprintable: bool = True,
        preserveMultispace: bool = False,
    ) -> None:
        self.toAscii = toAscii
        self.removeUnprintable = removeUnprintable
        self.preserveMultiSpace = preserveMultispace
        self.preferredSequences = _createSeq(spaceBefore, True, True)
        self.preferredSequences.update(_createSeq(spaceAfter, True, False))
        self.removeSequences = _createSeq(noSpaceBefore, False, True)
        self.removeSequences.update(_createSeq(noSpaceAfter, False, False))

    def normalize(self, s: str):
        """
        normalizes string s;\n
        'β-NS' --> 'b-NS'\n
        'Some Text(Example)For Display' --> 'Some Text (Example) For Display'
        """
        ns = _normalize(
            s,
            self.preferredSequences,
            self.removeSequences,
            self.toAscii,
            self.removeUnprintable,
            self.preserveMultiSpace,
        )
        _logger.debug("Text '{}' Normalized To '{}'".format(s, ns))
        return ns
