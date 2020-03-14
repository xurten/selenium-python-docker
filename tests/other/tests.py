from unittest import TestCase


class FileTests(TestCase):

    def setUp(self):
        pass

    @staticmethod
    def tests_check_file():
        file = open('results.txt', 'w+')
        file.write('Some text')
        file.close()
        print("file pass")
        pass

    def tearDown(self):
        pass
