from kissut import LoggingTestCase
import kisspy.converters.numericConverter as numCnvtr


class TestNumericConverter(LoggingTestCase):
    def test_a_toFloat(self):
        c = numCnvtr.toNumeric("4.24")
        self.assertIsInstance(c, float)

    def test_b_toInt(self):
        c = numCnvtr.toNumeric("40")
        self.assertIsInstance(c, int)

    def test_c_none(self):
        c = numCnvtr.toNumeric("cat")
        self.assertIsNone(c)

    def test_d_none(self):
        c = numCnvtr.toNumeric("cat", onFail=numCnvtr.returnTxt)
        self.assertEqual("cat", c)

    def test_e_valErr(self):
        self.assertRaises(ValueError, numCnvtr.toNumeric, "dog", numCnvtr.raiseValExc)
