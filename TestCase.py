from unittest import TestCase
from stackit import stackit_core
__author__ = 'SWarren'


class Config():
    """ Main configuration object """
    def __init__(self):
        self.search = False
        self.stderr = False
        self.tag = False
        self.verbose = False

class TestStackIt(TestCase):
    def test_search_verbose(self):
        Term = 'People'
        self.assertIsInstance(Term,str)
        Result = stackit_core.search_verbose(Term)
        self.assertIsNone(Result)
        self.assertRaises(TypeError,stackit_core.search_verbose([]))
        self.assertRaises(TypeError,stackit_core.search_verbose(False))

    def test_print_full_question(self):
       questions = stackit_core.so.search_advanced(
        q="People",
        sort=stackit_core.Sort.Votes)
       Result = stackit_core.print_full_question(questions[0])
       self.assertIsNot(Result,list)
       self.assertRaises(TypeError,stackit_core.print_full_question(questions[0]))
       self.assertIsNone(Result)

    def test_print_question(self):
       questions = stackit_core.so.search_advanced(
        q="People",
        sort=stackit_core.Sort.Votes)
       Result = stackit_core.print_question(questions[0],1)
       self.assertIsNot(Result,list)
       self.assertRaises(TypeError,stackit_core.print_full_question(questions[0]))
       self.assertIsNone(Result)

    def test_get_term(self):

        self.assertIsInstance(stackit_core.Config().search, bool)
        self.assertIsInstance(stackit_core.Config().tag, bool)
        self.assertIsInstance(stackit_core.Config().stderr, bool)
        self.assertIsInstance(stackit_core.Config().verbose, bool)
        self.assertRaises(TypeError,stackit_core.get_term(stackit_core.Config()))
        self.assertIsNone(None,stackit_core.get_term(stackit_core.Config()))


    def test__search(self):
        config = stackit_core.Config()
        config.term = "help me with my chicken"
        self.assertIsInstance(config.search, bool)
        self.assertIsInstance(config.tag, bool)
        self.assertIsInstance(config.stderr, bool)
        self.assertIsInstance(config.verbose, bool)
        config.tag = ""




