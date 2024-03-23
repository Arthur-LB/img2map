import os
import unittest
import numpy as np
import skimage as ski
from img2map import get_image_contours, contour_to_polygon, polygon_to_html_area, polygons_to_html_map, \
    contours_to_html_map, image_to_html_map, polygon_to_polygon_svg, polygons_to_svg, contours_to_svg, image_to_svg, \
    get_image_contours_polygons, get_positive_orientation

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestImageProcessing(unittest.TestCase):
    """
    This class tests the image processing functions.
    It tests simple and complex images.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        leaf_iamge_path = os.path.join(THIS_DIR, "images/leaf.jpg")
        self.leaf_image = ski.io.imread(leaf_iamge_path, as_gray=True)  # Simple image unevenly filled

        france_image_path = os.path.join(THIS_DIR, "images/france.png")
        self.france = ski.io.imread(france_image_path, as_gray=True)  # Complex image with multiple contours

        true_france_html_map_path = os.path.join(THIS_DIR, "expected_results/france.html")
        with open(true_france_html_map_path, "r") as file:
            self.true_france_html_map = file.read()

        true_france_svg_path = os.path.join(THIS_DIR, "expected_results/france.svg")
        with open(true_france_svg_path, "r") as file:
            self.true_france_svg = file.read()

        true_leaf_html_map_path = os.path.join(THIS_DIR, "expected_results/leaf.html")
        with open(true_leaf_html_map_path, "r") as file:
            self.true_leaf_html_map = file.read()

        true_leaf_svg_path = os.path.join(THIS_DIR, "expected_results/leaf.svg")
        with open(true_leaf_svg_path, "r") as file:
            self.true_leaf_svg = file.read()

        self.level = 0.8

    def test_get_image_contours(self):
        """
        Test the get_image_contours function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        self.assertTrue(len(leaf_contours) > 0)

        france_contours = get_image_contours(self.france, self.level)
        self.assertTrue(len(france_contours) > 0)

    def test_contour_to_polygon(self):
        """
        Test the contour_to_polygon function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_polygon = contour_to_polygon(leaf_contours[0])
        self.assertTrue(len(leaf_polygon) > 0)

        france_contours = get_image_contours(self.france, self.level)
        france_polygon = contour_to_polygon(france_contours[0])
        self.assertTrue(len(france_polygon) > 0)

    def test_polygon_to_html_area(self):
        """
        Test the polygon_to_html_area function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_polygon = contour_to_polygon(leaf_contours[0])
        leaf_html_area = polygon_to_html_area(leaf_polygon)
        self.assertTrue(len(leaf_html_area) > 0)

        france_contours = get_image_contours(self.france, self.level)
        france_polygon = contour_to_polygon(france_contours[0])
        france_html_area = polygon_to_html_area(france_polygon)
        self.assertTrue(len(france_html_area) > 0)

    def test_polygons_to_html_map(self):
        """
        Test the polygons_to_html_map function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_polygons = get_image_contours_polygons(leaf_contours)
        leaf_html_map = polygons_to_html_map(leaf_polygons)
        self.assertEqual(leaf_html_map, self.true_leaf_html_map)

        france_contours = get_image_contours(self.france, self.level)
        france_polygons = get_image_contours_polygons(france_contours)
        france_html_map = polygons_to_html_map(france_polygons)
        self.assertEqual(france_html_map, self.true_france_html_map)

    def test_contours_to_html_map(self):
        """
        Test the contours_to_html_map function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_html_map = contours_to_html_map(leaf_contours)
        self.assertEqual(leaf_html_map, self.true_leaf_html_map)

        france_contours = get_image_contours(self.france, self.level)
        france_html_map = contours_to_html_map(france_contours)
        self.assertEqual(france_html_map, self.true_france_html_map)

    def test_image_to_html_map(self):
        """
        Test the image_to_html_map function.
        """
        leaf_html_map = image_to_html_map(self.leaf_image, self.level)
        self.assertEqual(leaf_html_map, self.true_leaf_html_map)

        france_html_map = image_to_html_map(self.france, self.level)
        self.assertEqual(france_html_map, self.true_france_html_map)

    def test_polygon_to_polygon_svg(self):
        """
        Test the polygon_to_polygon_svg function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_polygon = contour_to_polygon(leaf_contours[0])
        leaf_polygon_svg = polygon_to_polygon_svg(leaf_polygon)
        self.assertTrue(len(leaf_polygon_svg) > 0)

        france_contours = get_image_contours(self.france, self.level)
        france_polygon = contour_to_polygon(france_contours[0])
        france_polygon_svg = polygon_to_polygon_svg(france_polygon)
        self.assertTrue(len(france_polygon_svg) > 0)

    def test_polygons_to_svg(self):
        """
        Test the polygons_to_svg function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_polygons = get_image_contours_polygons(leaf_contours)
        leaf_svg = polygons_to_svg(leaf_polygons)
        self.assertTrue(len(leaf_svg) > 0)

        france_contours = get_image_contours(self.france, self.level)
        france_polygons = get_image_contours_polygons(france_contours)
        france_svg = polygons_to_svg(france_polygons)
        self.assertTrue(len(france_svg) > 0)

    def test_contours_to_svg(self):
        """
        Test the contours_to_svg function.
        """
        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_svg = contours_to_svg(leaf_contours)
        self.assertTrue(len(leaf_svg) > 0)

        france_contours = get_image_contours(self.france, self.level)
        france_svg = contours_to_svg(france_contours)
        self.assertTrue(len(france_svg) > 0)

    def test_image_to_svg(self):
        """
        Test the image_to_svg function.
        """
        leaf_svg = image_to_svg(self.leaf_image, self.level, fill="#01567d", stroke="#fff", stroke_width=".5")
        self.assertEqual(leaf_svg, self.true_leaf_svg)

        france_svg = image_to_svg(self.france, self.level, fill="#01567d", stroke="#fff", stroke_width=".5")
        self.assertEqual(france_svg, self.true_france_svg)

    def test_get_positive_orientation(self):
        """
        Test the get_positive_orientation function.
        """

        leaf_contours = get_image_contours(self.leaf_image, self.level)
        leaf_polygon = contour_to_polygon(leaf_contours[0])
        leaf_orientation = get_positive_orientation(leaf_polygon)
        self.assertEqual(leaf_orientation, "high")

        france_contours = get_image_contours(self.france, self.level)
        france_polygon = contour_to_polygon(france_contours[0])
        france_orientation = get_positive_orientation(france_polygon)
        self.assertEqual(france_orientation, "high")


if __name__ == '__main__':
    unittest.main()
