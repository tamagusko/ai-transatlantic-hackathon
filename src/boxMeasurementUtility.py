from __future__ import annotations

import cv2
import imutils
import numpy as np
from imutils import contours
from imutils import perspective
# import json
# import pdb
# import matplotlib.pyplot as plt


def _midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def get_bbox_width_height_in_mm(image_width_height_pxl: tuple, distance_camera_object: float = 0, focal_length: float = 3.37):
    """
        compute the bounding box width and height that contains the object present in image.
        Assumption: the image only have one object

        :param image_width_height_pxl: the image width and height in pixels
        :param distance_camera_object: the distance object camera
        :param focal_length: the camera focal_length parameter
        :return: the bounding box width and height (width, height) in CM if training_phase is false in pixels else
        """
    assert distance_camera_object != 0 and focal_length != 0
    # x = 6.100 / 4224
    (width, height) = image_width_height_pxl
    height = (distance_camera_object * height) / (focal_length)
    width = (distance_camera_object * width) / (focal_length)
    return width, height


def get_bbox_width_height_pxl(image_mat):
    """
        compute the bounding box width and height that contains the object present in image.
        Assumption: the image only have one object

        :param image_mat: the matrix of the image
        :return: the bounding box width and height (width, height)  in pixels
        """

    # load the image, convert it to grayscale, and blur it slightly
    gray = image_mat  # cv2.cvtColor(image_mat, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=3)
    edged = cv2.erode(edged, None, iterations=2)

    # cv2.imshow("Image", edged)
    # cv2.waitKey(0)

    # find contours in the edge map
    cnts = cv2.findContours(
        edged.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    cnts = imutils.grab_contours(cnts)
    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable
    (cnts, _) = contours.sort_contours(cnts)

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 50:
            continue
        # compute the rotated bounding box of the contour
        orig = image_mat.copy()
        box = cv2.minAreaRect(c)
        # centroid = box[0]
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
        # print(centroid)
        # cv2.circle(orig, (int(centroid[0]), int(centroid[1])), 5, (255, 0, 0), -1)
        # cv2.imshow("test", orig)
        # cv2.waitKey()
        # pdb.set_trace()

        # print(tl, tr, br, bl)
        # print(xmin, xmax, ymin, ymax)
        # pdb.set_trace()
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
        return width, height, orig, (tltrX, tltrY, trbrX, trbrY), (tl, br)

# testing
# img_mat_view1 = cv2.imread("../data/images/image1_view1_.jpg")
# img_mat_view2 = cv2.imread("../data/images/image1_view2.jpg")

# pixelsPerCmMetric = np.load("../data/estimations/pixelsPerCMMetric_estimate.npy")

# print(pixelsPerCmMetric)

# result = get_bbox_width_height_pxl(img_mat_view1)
# print(result)
# _get_bbox_width_height(img_mat_view1, training_phase=False, pixelsPerCmMetric =pixelsPerCmMetric)
