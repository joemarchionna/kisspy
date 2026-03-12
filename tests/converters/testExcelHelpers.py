from kissut import LoggingTestCase
import kisspy.converters.excelHelpers as excelHelpers


class TestExcelHelpers(LoggingTestCase):
    def testToExcel01(self):
        c = excelHelpers.toExcelCol(1)
        self.assertEqual("A", c)

    def testToExcel02(self):
        c = excelHelpers.toExcelCol(26)
        self.assertEqual("Z", c)

    def testToExcel03(self):
        c = excelHelpers.toExcelCol(27)
        self.assertEqual("AA", c)

    def testToExcel04(self):
        c = excelHelpers.toExcelCol(53)
        self.assertEqual("BA", c)

    def testFromExcel01(self):
        c = excelHelpers.fromExcelCol("A")
        self.assertEqual(1, c)

    def testFromExcel02(self):
        c = excelHelpers.fromExcelCol("Y")
        self.assertEqual(25, c)

    def testFromExcel03(self):
        c = excelHelpers.fromExcelCol("AB")
        self.assertEqual(28, c)

    def testFromExcel04(self):
        c = excelHelpers.fromExcelCol("BB")
        self.assertEqual(54, c)
