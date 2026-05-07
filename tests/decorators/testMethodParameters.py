from kissut import LoggingTestCase
from kisspy.decorators.methodParameters import parametersNotNone, parametersHaveTruthyValue, parameterLimit


@parametersNotNone(["a", "b"])
def _add(a, b) -> int:
    return a + b


@parametersHaveTruthyValue(["a", "b"])
def _concat(a, b) -> str:
    return a + b


@parameterLimit("b", 0, 10)
def _limited(a, b) -> int:
    return a + b


class TestMethodParameters(LoggingTestCase):
    def test_a_success(self):
        self.assertEqual(10, _add(4, 6))

    def test_a_fail(self):
        self.assertRaises(ValueError, _add, 4, None)

    def test_b_success(self):
        self.assertEqual("st", _concat("s", "t"))

    def test_b_fail(self):
        self.assertRaises(ValueError, _concat, "s", None)

    def test_c_ok(self):
        self.assertEqual(13, _limited(6, 7))

    def test_c_mxModified(self):
        self.assertEqual(24, _limited(14, 22))

    def test_c_mnModified(self):
        self.assertEqual(4, _limited(4, -4))
