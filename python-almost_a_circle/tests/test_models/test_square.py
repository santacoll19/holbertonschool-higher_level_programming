from models.square import Square
import unittest


class TestSquare(unittest.TestCase):

    """ Checker preference """

    def test_checker(self):
        """ Test checker """
        with self.assertRaises(ValueError):
            sqr = Square(0)

    """ Testing size """

    def test_size(self):
        """ Test size """
        sqr = Square(1, 2)
        self.assertEqual(sqr.size, 1)

    """ Testing width """

    def test_width(self):
        """ Test width """
        sqr = Square(1, 2, 3)
        self.assertEqual(sqr.width, 1)

    """ Testing a str as argument """

    def test_str_1_arg(self):
        """ Test str"""
        with self.assertRaises(TypeError):
            sqr = Square("1")

    def test_str_2_arg(self):
        """ Test str"""
        with self.assertRaises(TypeError):
            sqr = Square(1, "2")

    def test_str_3_arg(self):
        """ Test str"""
        with self.assertRaises(TypeError):
            sqr = Square(1, 2, "3")

    """ Testing Negative Arguments """

    def test_neg_arg_1(self):
        """ Test negative argument"""
        with self.assertRaises(ValueError):
            sqr = Square(-1)

    def test_neg_arg_2(self):
        """ test negative argument"""
        with self.assertRaises(ValueError):
            sqr = Square(1, -2)

    def test_neg_arg_3(self):
        """ test negative argument"""
        with self.assertRaises(ValueError):
            sqr = Square(1, 2, -3)

    """ Testing to_dictionary method """

    def test_to_dic(self):
        """ test to dictionary"""
        sqr = Square(10, 2, 1, 6)
        result = {'id': 6, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(sqr.to_dictionary(), result)

    """ Testing update method """

    def test_update(self):
        """ Test update method"""
        sqr = Square(5)
        sqr.update(10)
        self.assertEqual(sqr.id, 10)
        sqr.update(1, 2)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.width, 2)
        sqr.update(1, 2, 3)
        self.assertEqual(sqr.x, 3)
        sqr.update(1, 2, 3, 4)
        self.assertEqual(sqr.y, 4)

    """ Testing create method """

    def test_create(self):
        """ Test create method """
        sqr1 = Square(2)
        sqr1_dic = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dic)
        self.assertNotEqual(sqr1, sqr2)

    """ Testing to save to file """

    def test_save_to_file_empty(self):
        """ Test save to file empty"""
        Square.save_to_file(None)
        with open("Square.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file_empty_2(self):
        """ Test save to file empty"""
        Square.save_to_file([])
        with open("Square.json") as fd:
            self.assertEqual('[]', fd.read())

    """ Test load from file """

    def test_load_file(self):
        """ test load from file"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        li_sqr_out = Square.load_from_file()
        self.assertNotEqual(li_sqr_out[0], s1)


if __name__ == '__main__':
    unittest.main()
