import unittest
#from parser import Parser

#class ParserTestCase(unittest.TestCase):

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)


class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)


#class FailureMessageTest(unittest.TestCase):

    #def test_fail(self):
        #self.assertTrue(False, 'failure message goes here')

#class OutcomesTest(unittest.TestCase):

    #def test_pass(self):
        #self.assertTrue(True)

    #def test_fail(self):
        #self.assertTrue(False)

    #def test_error(self):
        #raise RuntimeError('Test error!')

#class InequalityTest(unittest.TestCase):

    #def testEqual(self):
        #self.assertNotEqual(1, 3-2)

    #def testNotEqual(self):
        #self.assertEqual(2, 3-2)

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))
        
class ExceptionTest(unittest.TestCase):
    
    def test_trap_locally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')
    
    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')



class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('in test()')
        self.assertEqual(self.fixture, range(1, 10))




if __name__ == '__main__':
    unittest.main()