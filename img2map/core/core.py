import skimage as ski
import numpy as np


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