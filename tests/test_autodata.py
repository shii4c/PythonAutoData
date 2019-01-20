import unittest
import autodata

class TestAutoData(unittest.TestCase):
    def test_autodict(self):
        d = autodata.autodict()
        d["key1"]["key1-1"] = 1
        d["key1"]["key1-2"] = 2
        d["key2"]["key2-1"] = 3
        d["key3"] += 1
        d["key4"] += 1
        d["key4"] += 1

        self.assertEqual(1, d["key1"]["key1-1"])
        self.assertEqual(2, d["key1"]["key1-2"])
        self.assertEqual(3, d["key2"]["key2-1"])
        self.assertEqual(1, d["key3"])
        self.assertEqual(2, d["key4"])
        self.assertTrue(autodata.defined(d["key1"]))
        self.assertFalse(autodata.defined(d["key5"]))
        self.assertFalse(autodata.defined(d["key5"]["key5-1"]))
        keylist = " ".join(sorted(d.keys()))
        self.assertEqual("key1 key2 key3 key4", keylist)

    def test_autolist(self):
        a = autodata.autolist()
        a[3] = 1
        self.assertEqual(4, len(a))
        self.assertEqual(1, a[3])
        self.assertFalse(autodata.defined(a[2]))
        a[0][0].append(2)
        a[0][0][1] = 3
        self.assertEqual(2, a[0][0][0])
        self.assertEqual(3, a[0][0][1])

        list1 = [1,2,3]
        a[1] += list1
        a[1][3] = 4
        self.assertEqual([1,2,3,4], a[1])
        self.assertEqual([1,2,3], list1)

if __name__ == '__main__':
    unittest.main()
