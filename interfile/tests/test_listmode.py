
# interfile - Interfile read and write 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 

import unittest
from .. import listmode

class TestLoadLibraries(unittest.TestCase): 
    """Sequence of tests to verify that the C libraries are loaded correctly. """ 
    def setUp(self):
        pass

    def test_library_listmode_iface(self): 
        """If this test passes, the library listmode_iface has been built and wrapped successfully. """
        self.assertTrue(listmode.test_library_listmode_iface()) 

    def test_petlink32_info(self): 
        """Test if petlink32_info works. """ 
        pass 


if __name__=="__main__": 
    unittest.main() 

