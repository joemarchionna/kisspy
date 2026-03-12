from kissut import LoggingTestCase
from kisspy.xtdPy.strings.textNormalizer import TextNormalizer


class TestTextNormalizer(LoggingTestCase):
    def testNoSpaces1(self):
        s = "Example(of)No[Spaces]In/String"
        r = TextNormalizer().normalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual("Example (of) No [Spaces] In/String", r)

    def testNoSpaces2(self):
        s = "Example(of)No[Spaces]In/(a)String"
        r = TextNormalizer().normalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual("Example (of) No [Spaces] In/(a) String", r)

    def testTooManySpaces1(self):
        s = "Example ( of ) No [ Spaces   ] In   /        String"
        r = TextNormalizer().normalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual("Example (of) No [Spaces] In/String", r)

    def testNonAscii1(self):
        s = "Example(of)Greek β In String"
        r = TextNormalizer().normalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual("Example (of) Greek b In String", r)

    def testClosingParenthesis(self):
        s = "Example(of)Greek β In String (duh)"
        r = TextNormalizer().normalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual("Example (of) Greek b In String (duh)", r)
