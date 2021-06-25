from unittest import TestCase, skip

from tests.myfuncs import myadd


class TestMyAdd(TestCase):

    def setUp(self):
        self.myadd_dataset = [
            0, 0, 0,
            1, 2, 3,
            11, -5, 6,
            # 11, 5,  6,  # broken
        ]

    def test_myadd(self):
        for i in range(0, len(self.myadd_dataset), 3):
            a, b, c = self.myadd_dataset[i:i + 3]
            # assertEqual(EXPECTED, ACTUAL)
            # self.assertTrue(c == myadd(a, b))  # bad style
            self.assertEqual(c, myadd(a, b))     # good style

    @skip("Unimplemented")
    def test_myadd_complex(self):
        self.fail('Unimplemented test-case')
