import unittest
import test_type_checking, test_study_time, test_wiki_parsing

for test in (test_type_checking, test_study_time, test_wiki_parsing):
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(suite)