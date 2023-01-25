#!/usr/bin/env python3

from PIL import Image
import turtle
import matplotlib.testing.compare as mpcompare
import unittest
import shapes
import tempfile
import os.path


class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename):
        ''' compares the current canvas to an expected filename.
        Returns None if and only if the files are identical'''
        TOLERANCE = 1.0 # somewhere between 0 and 255, higher is more lax.
        with tempfile.TemporaryDirectory() as tmp_dirname:
            actual_ps = os.path.join(tmp_dirname, 'canvas.ps')
            actual_png = os.path.join(tmp_dirname, 'canvas.png')
            canvas = turtle.getcanvas()
            canvas.postscript(file=actual_ps)
            with Image.open(actual_ps) as im:
                im.save(actual_png)
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)


    def setUp(self):
        turtle.reset()

    def test_circle(self):
        t = turtle.getturtle()
        shapes.draw_circle(t,20,20,20)
        t.hideturtle()
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/circle-20.png'))

    def test_circle_fail(self):
        # test that a badly sized circle fails to compare as equal
        t = turtle.getturtle()
        shapes.draw_circle(t,20,20,29)
        t.hideturtle()
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='testdata/circle-20.png'))



if __name__ == '__main__':
    unittest.main()
