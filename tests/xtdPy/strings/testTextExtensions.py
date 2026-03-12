from kissut import LoggingTestCase
from kisspy.xtdPy.strings.textExtensions import replaceChars, cleanAndNormalize


class TestTextExtensions(LoggingTestCase):
    def test_a_replace(self):
        s = "Example(of)No[Spaces]In/String"
        r = replaceChars(s, "()[]/", " ")
        self.assertNotEqual(s, r)
        self.assertEqual(r, "Example of No Spaces In String")

    def test_b_replace(self):
        s = "Example(of)No[Spaces]In/String"
        r = replaceChars(s, "()[]/", "")
        self.assertNotEqual(s, r)
        self.assertEqual(r, "ExampleofNoSpacesInString")

    def test_c_clean(self):
        s = "my [file]"
        r = cleanAndNormalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual(r, "my_file")

    def test_d_clean(self):
        s = "<this is> my [file]"
        r = cleanAndNormalize(s)
        self.assertNotEqual(s, r)
        self.assertEqual(r, "this_is_my_file")
