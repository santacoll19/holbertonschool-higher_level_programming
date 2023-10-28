import unittest
import io
import unittest.mock
import json

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """ Test width conditions """

    def test_width(self):
        """ Test width"""
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.width, 2)

    def test_negative_width(self):
        """ Test negative width"""
        with self.assertRaises(ValueError):
            rec3 = Rectangle(-4, 1)

    def test_zero_width(self):
        """ Test zero width"""
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 5)

    def test_string_width(self):
        """ Test string width"""
        with self.assertRaises(TypeError):
            rec = Rectangle("2", 10)

    """ Test height conditions """

    def test_height(self):
        """ Test height"""
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.height, 4)

    def test_negative_height(self):
        """ Test negative height"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -2)

    def test_zero_height(self):
        """ Test zero height"""
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 0)

    def test_str_height(self):
        """ Test str height"""
        with self.assertRaises(TypeError):
            rec = Rectangle(35, "15")

    """ Test x conditions """

    def test_x(self):
        """ Test x"""
        rectangle = Rectangle(10, 2, 3, 5)
        self.assertEqual(rectangle.x, 3)

    def test_x_negative(self):
        """ Test x negative"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 5, -9)

    def test_x_zero(self):
        """ Test x zero"""
        rectangle = Rectangle(3, 2, 0, 1)
        self.assertEqual(rectangle.x, 0)

    def test_x_str(self):
        """ Test x str"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 5, "1")

    """ Test y conditions """

    def test_y(self):
        """ Test y"""
        rectangle = Rectangle(2, 3, 2, 2)
        self.assertEqual(rectangle.y, 2)

    def test_y_negative(self):
        """ Test y negative"""
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 2, 3, -1)

    def test_y_zero(self):
        """ Test y zero"""
        rectangle = Rectangle(3, 2, 1, 0)
        self.assertEqual(rectangle.y, 0)

    def test_y_str(self):
        """ Test y str"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 6, 2, "2")

    """ Test area """

    def test_area(self):
        """ Test area"""
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.area(), 9)

    def test_area_2(self):
        """ Test area"""
        rec = Rectangle(2, 10)
        self.assertEqual(rec.area(), 20)

    def test_area_3(self):
        """ Test area"""
        rec = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rec.area(), 56)

    """ Test display """
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, w, h, x, y, mock_stdout):
        """ Test display"""
        rec = Rectangle(w, h)
        rec.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        """ Test display"""
        self.assert_stdout("##\n##\n", 2, 2, 1, 1)
        self.assert_stdout("##\n##\n##\n", 2, 3, 2, 2)
        self.assert_stdout("###\n###\n", 3, 2, 1, 0)

    @unittest.expectedFailure
    def test_display_failure(self):
        """ Test display failure """
        self.assert_stdout(ValueError, 0, 0, 0, 0)

    """ Test __str__ """

    def test_str_method(self):
        """ Test __str__ method"""
        rec = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rec.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    """ Test update method """

    def test_update(self):
        """ Test update method"""
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(rec.id, 89)
        rec.update(89, 2)
        self.assertEqual(rec.width, 2)
        rec.update(89, 2, 3)
        self.assertEqual(rec.height, 3)
        rec.update(89, 2, 3, 4)
        self.assertEqual(rec.x, 4)
        rec.update(89, 2, 3, 4, 5)
        self.assertEqual(rec.y, 5)

    """  Test to_dictionary method """

    def test_to_dictionary(self):
        """ Test to_dictionary method"""
        rec = Rectangle(10, 2, 1, 9, 7)
        result = {'x': 1, 'y': 9, 'id': 7, 'height': 2, 'width': 10}
        self.assertDictEqual(rec.to_dictionary(), result)

    """ Test create method """

    def test_create(self):
        """ Test create method """
        r1 = Rectangle(3, 5, 1)
        r1_dic = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dic)
        self.assertNotEqual(r1, r2)

    """ Test save to file """

    def test_save_to_file_empty(self):
        """ Test save to file empty"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file_empty_2(self):
        """ Test save to file empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as fd:
            self.assertEqual('[]', fd.read())

    def save_to_file(self):
        """ Test save to file"""
        li_obj = []
        expe = []
        Rectangle.save_to_file(li_obj)
        with open("Rectangle.json") as fd:
            self.assertEqual(expe, fd.read())

    """ Test load from file """

    def test_load(self):
        """ Test load from file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        li_out = Rectangle.load_from_file()
        self.assertNotEqual(li_out[0], r1)


if __name__ == '__main__':
    unittest.main()
