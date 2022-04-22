from __future__ import annotations

import json

import cv2
import imutils
import numpy as np
from imutils import contours
from imutils import perspective


def _midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def _get_bbox_width_height(
    image_mat, training_phase, pixelsPerCmMetric: float = 0,
    distance_camera_object: float = 0,
    use_focal: bool = False, focal_length: int = 0,
):
    """
        compute the bounding box width and height that contains the object present in image.
        Assumption: the image only have one object

        :param image_mat: the matrix of the image
        :param training_phase: true if we want to use the result to estimate the focal_length/pixelsPerCmMetric
        :param pixelsPerCmMetric: the pixels per CM ratio
        :param distance_camera_object: the distance object camera
        :param use_focal: true if we want to use the focal_length to reconstructs the real distance
        :param focal_length: the camera (estimated) focal_length parameter
        :return: the bounding box width and height (width, height) in CM if training_phase is false in pixels else
        """
    if use_focal:
        assert distance_camera_object != 0 and focal_length != 0
    else:
        pixelsPerCmMetric != 0

    # load the image, convert it to grayscale, and blur it slightly
    gray = cv2.cvtColor(image_mat, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # find contours in the edge map
    cnts = cv2.findContours(
        gray.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    cnts = imutils.grab_contours(cnts)
    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable
    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric_pass = None

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 100:
            continue
        # compute the rotated bounding box of the contour
        orig = image_mat.copy()
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype='int')
        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)
        cv2.drawContours(orig, [box.astype('int')], -1, (0, 255, 0), 2)

        # unpack the ordered bounding box, then compute the midpoint
        # between the top-left and top-right coordinates, followed by
        # the midpoint between bottom-left and bottom-right coordinates
        (tl, tr, br, bl) = box
        width1 = np.linalg.norm(tl - tr)
        width2 = np.linalg.norm(bl - br)
        height1 = np.linalg.norm(tl - bl)
        height2 = np.linalg.norm(tr - br)

        (tltrX, tltrY) = _midpoint(tl, tr)

        (trbrX, trbrY) = _midpoint(tr, br)

        # np.linalg.norm(top_center - button_center)
        width = width1 if width1 >= width2 else width2
        # np.linalg.norm(left_center - right_center)
        height = height1 if height1 >= height2 else height2

        if training_phase:
            return width, height

        if pixelsPerMetric_pass is None:
            print(training_phase)
            pixelsPerMetric_pass = 1

            # compute the size of the object
            if use_focal:
                width = (distance_camera_object * width / focal_length)
                height = (distance_camera_object * height / focal_length)

            else:
                width = width / pixelsPerCmMetric
                height = height / pixelsPerCmMetric

            # draw the object sizes on the image
            # cv2.putText(orig, "{:.1f}cm".format(width),
            #          (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
            #           0.65, (255, 255, 255), 2)
            # cv2.putText(orig, "{:.1f}cm".format(height),
            #          (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
            #           0.65, (255, 255, 255), 2)
            # show the output image
            # cv2.imshow("Image", orig)
            # cv2.waitKey(0)
            return width, height


# focal length finder function
def _compute_focal_length(measured_distance, real_width, image_width):
    focal = (image_width * measured_distance) / real_width
    return np.mean(focal)


def focal_length_and_pixelsPerCM(filename='../data/images/object_distances.json', image_path='../data/images', storage_path='../data/estimations') -> float:
    """
    compute an estimation of the focal_length and the number of pixels per centimeter of the camera based of measured values

    :param filename: a JSON file that contains Lengths of a set of objects in real world.
    :param image_path: the directory containing the corresponding images
    :param storage_path: the directory where to store the estimations
    :return: an estimate of the focal_length of the camera and pixelsPerCM ratio.
    """
    f = open(filename)
    data = json.load(f)

    image_measures = []
    real_measures = []
    distances_camera_objects = []
    # Iterating through the json
    # list
    for image in data:
        view1 = data[image]['view1']
        real_width = view1['width']
        real_height1 = view1['height']
        distance1 = view1['distance']
        real_measures.append(real_width)
        real_measures.append(real_height1)
        distances_camera_objects.append(distance1)
        distances_camera_objects.append(distance1)
        img_view1 = cv2.imread(
            image_path + '/' + image +
            '_view1.jpg', cv2.IMREAD_COLOR,
        )
        img_width, img_height1 = _get_bbox_width_height(
            img_view1, training_phase=True,
        )
        image_measures.append(img_width)
        image_measures.append(img_height1)
        view2 = data[image]['view2']
        real_height2 = view2['height']
        real_depth = view2['depth']
        distance2 = view1['distance']
        real_measures.append(real_height2)
        real_measures.append(real_depth)
        distances_camera_objects.append(distance2)
        distances_camera_objects.append(distance2)
        img_view2 = cv2.imread(
            image_path + '/' + image +
            '_view2.jpg', cv2.IMREAD_COLOR,
        )
        img_height2, img_depth = _get_bbox_width_height(
            img_view2, training_phase=True,
        )
        image_measures.append(img_height2)
        image_measures.append(img_depth)
    # Closing file
    f.close()
    focal_length = _compute_focal_length(
        np.array(distances_camera_objects), np.array(real_measures),
        np.array(image_measures),
    )
    pixelsPerMetric = np.mean(
        np.array(image_measures) / np.array(real_measures),
    )
    for i in range(len(distances_camera_objects)):
        test_result = (
            distances_camera_objects[i] * image_measures[i]
        ) / focal_length
        # print(test_result, real_measures[i])

    np.save(storage_path + '/focal_length_estimate', focal_length)
    np.save(storage_path + '/pixelsPerCMMetric_estimate', pixelsPerMetric)
    return focal_length, pixelsPerMetric


def compute_dimension_of_object(
    img_mat_view1: np.array, img_mat_view2: np.array, pixelsPerCmMetric: float = 0,
    distance_camera_object: float = 0,
    use_focal: bool = False, focal_length: int = 0,
):
    """
        compute an estimation of the dimension (width ,height,depth) of the object present in image.
        Assumption: the image only have one object

        :param img_mat_view1: the matrix of the image filmed in one side
        :param img_mat_view2: the matrix of the image filmed in another side (not parallel to the first view)
        :param pixelsPerCmMetric: the pixels per CM ratio
        :param distance_camera_object: the distance object camera
        :param use_focal: true if we want to use the focal_length to reconstructs the real distance
        :param focal_length: the camera (estimated) focal_length parameter
        :return: the bounding box width and height (width, height) in CM if training_phase is false in pixels else
        """
    width1, height1 = _get_bbox_width_height(
        img_mat_view1, training_phase=False, pixelsPerCmMetric=pixelsPerCmMetric,
        distance_camera_object=distance_camera_object,
        use_focal=use_focal, focal_length=focal_length,
    )

    width2, height2 = _get_bbox_width_height(
        img_mat_view2, training_phase=False, pixelsPerCmMetric=pixelsPerCmMetric,
        distance_camera_object=distance_camera_object,
        use_focal=use_focal, focal_length=focal_length,
    )

    result = [width1, width2, height1, height2]
    result.sort()
    print(result)
    return result[-3:]


focal_length, pixelsPerCM = focal_length_and_pixelsPerCM()


# testing
img_mat_view1 = cv2.imread('../data/images/image1_view1.jpg')
img_mat_view2 = cv2.imread('../data/images/image1_view2.jpg')

pixelsPerCmMetric = np.load(
    '../data/estimations/pixelsPerCMMetric_estimate.npy',
)

result = compute_dimension_of_object(
    img_mat_view1, img_mat_view2, pixelsPerCmMetric,
)
print(result)
