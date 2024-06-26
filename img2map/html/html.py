from img2map.core import *


def polygon_to_html_area(polygon):
    """
    This function converts a polygon to an HTML area.
    :param polygon: The polygon to convert.
    :return: The HTML area.
    """
    base_str = '<area shape="poly" alt="html area" coords="'
    coords_str = ""
    for point in polygon:
        coords_str += f"{int(point[1])},{int(point[0])},"
    coords_str = coords_str[:-1]
    return base_str + coords_str + '"/>'


def polygons_to_html_map(polygons):
    """
    This function converts polygons to an HTML map.
    :param polygons: The polygons to convert.
    :return: The HTML map.
    """
    base_str = '<map name="map">\n'
    for i, polygon in enumerate(polygons):
        area_str = polygon_to_html_area(polygon)
        base_str += f"\t{area_str}\n"
    return base_str + "</map>"


def contours_to_html_map(contours, tolerance=0.1):
    """
    This function converts contours to an HTML map.
    :param tolerance: The tolerance of the approximation.
    :param contours: The contours to convert.
    :return: The HTML map.
    """
    polygons = [contour_to_polygon(contour, tolerance) for contour in contours]
    return polygons_to_html_map(polygons)


def image_to_html_map(image, level, tolerance=0.1):
    """
    This function converts an image to an HTML map.
    :param tolerance: The tolerance of the approximation.
    :param image: The image to convert.
    :param level: The level at which to find the contours.
    :return: The HTML map.
    """
    contours = get_image_contours(image, level)
    return contours_to_html_map(contours, tolerance)
