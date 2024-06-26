from img2map.core import *


def polygon_to_polygon_svg(polygon):
    """
    This function converts a polygon to an SVG polygon.
    :param polygon: The polygon to convert.
    :return: The SVG polygon.
    """
    base_str = '<polygon points="'
    coords_str = ""
    for point in polygon:
        coords_str += f"{int(point[1])},{int(point[0])} "
    coords_str = coords_str[:-1]
    return base_str + coords_str + '"/>'


def polygons_to_svg(polygons, **svg_group_attrs):
    """
    This function converts polygons to an SVG group.
    :param polygons: The polygons to convert.
    :param svg_group_attrs: The attributes of the SVG group.
    :return: The SVG group.
    """
    group_attrs_str = " ".join([f'{key.replace("_", "-")}="{value}"' for key, value in svg_group_attrs.items()])
    base_str = f'\t<g {group_attrs_str}>\n'
    for i, polygon in enumerate(polygons):
        polygon_str = polygon_to_polygon_svg(polygon)
        base_str += f"\t\t{polygon_str}\n"
    return base_str + "\t</g>"


def contours_to_svg(contours, tolerance=0.1, **svg_group_attrs):
    """
    This function converts contours to an SVG group.
    :param tolerance: The tolerance of the approximation.
    :param contours: The contours to convert.
    :param svg_group_attrs: The attributes of the SVG group.
    :return: The SVG group.
    """
    polygons = [contour_to_polygon(contour, tolerance) for contour in contours]
    return polygons_to_svg(polygons, **svg_group_attrs)


def image_to_svg(image, level, tolerance=0.1, **svg_group_attrs):
    """
    This function converts an image to an SVG.
    :param tolerance: The tolerance of the approximation.
    :param image: The image to convert.
    :param level: The level at which to find the contours.
    :param svg_group_attrs: Other attributes used for the SVG group.
    :return: The SVG.
    """
    contours = get_image_contours(image, level)
    base_str = (f'<svg '
                f'xmlns="http://www.w3.org/2000/svg" '
                f'viewBox="{"0 0 " + str(image.shape[1]) + " " + str(image.shape[0])}"'
                f'>\n'
                )
    end_str = "\n</svg>"
    svg_group_str = contours_to_svg(contours, tolerance, **svg_group_attrs)
    return base_str + svg_group_str + end_str

