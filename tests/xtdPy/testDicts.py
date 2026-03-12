from kisspy.xtdPy.dicts import getValueOfPath, setValueOfPath
from kissut import LoggingTestCase

d = {
    "name": {"first": "fred", "last": "johnson"},
    "address": {"street": "44 holly pl", "city": "monroe", "state": "ct"},
    "meta": {"age": 38, "favoriteNumber": 99, "lotteryWins": 0},
}


class TestDicts(LoggingTestCase):
    def test_a_none(self):
        resp = getValueOfPath(d, "address/province")
        self.assertIsNone(resp)

    def test_b_def(self):
        resp = getValueOfPath(d, "address/province", defaultValue="")
        self.assertEqual(resp, "")

    def test_c_def(self):
        resp = getValueOfPath(d, "address/province", defaultValue="NY")
        self.assertEqual(resp, "NY")

    def test_d_def0(self):
        resp = getValueOfPath(d, "meta/province", defaultValue=0)
        self.assertEqual(resp, 0)

    def test_e_val(self):
        resp = getValueOfPath(d, "address/state", defaultValue="NY")
        self.assertEqual(resp, "ct")

    def test_f_val(self):
        resp = getValueOfPath(d, "meta/lotteryWins", -1)
        self.assertEqual(0, resp)

    def test_s_0(self):
        d = {}
        resp = setValueOfPath(d, "a/b/c", "hello")
        self.logger.debug("d: {}".format(d))
        self.assertTrue(resp)
        self.assertTrue(d)

    def test_s_1(self):
        d = {"a": {"b": []}}
        resp = setValueOfPath(d, "a/b/c", "hello")
        self.logger.debug("d: {}".format(d))
        self.assertFalse(resp)
