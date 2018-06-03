import unittest
import detectQR

class ModuleTest(unittest.TestCase):
    def testjson(self):
        image_name = '1527589403.6_1.jpg';

        detectQRTest.detectQR(image_name)

        self.assertEqual(detectQRTest.detectQR(image_name),1)

unittest.main()
