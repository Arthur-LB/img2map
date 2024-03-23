import skimage as ski
import numpy as np
import matplotlib.pyplot as plt


def get_image_contours(image, level):
    """
    This function finds the contours of an image.
    :param image: The image to find the contours of.
    :param level: The level at which to find the contours.
    :return: The contours of the image.
    """
    return ski.measure.find_contours(
        image=image,
        level=level,
        fully_connected='high',
        positive_orientation=get_positive_orientation(image)
    )


def contour_to_polygon(contour, tolerance=0.1):
    """
    This function approximates a contour to a polygon.
    :param tolerance: The tolerance of the approximation.
    :param contour: The contour to approximate.
    :return: The approximated polygon.
    """
    return ski.measure.approximate_polygon(contour, tolerance)


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


def get_image_contours_polygons(contours, tolerance=0.1):
    """
    This function gets the polygons of the contours.
    :param tolerance: The tolerance of the approximation.
    :param contours: The contours to get the polygons of.
    :return: The polygons of the contours.
    """
    return [contour_to_polygon(contour, tolerance) for contour in contours]


def get_positive_orientation(image) -> str:
    """
    Compute the orientation of the image ("high" or "low")
    based on the given image.
    :param image: The image to get the positive orientation of.
    :return: The positive orientation of the image.
    """
    # Calculate the mean pixel intensity of the image
    mean_intensity = np.mean(image)

    # Determine orientation based on mean intensity
    if mean_intensity >= 0.5:
        return "high"
    else:
        return "low"


def main():
    """
    This is the main function.
    """
    # test and show the contour of image "./images/leaf.jpg"
    image = ski.io.imread("../tests/images/france.png", as_gray=True)
    html_map = image_to_html_map(image, 0.8, tolerance=0.1)
    print(html_map)

    with open("../tests/expected_results/france.html", "w") as file:
        file.write(html_map)

    print("The map has been saved to map.svg")


if __name__ == "__main__":
    main()
