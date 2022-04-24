#!/usr/bin/env python3
"""
(c) Jovial Silatsa Tchatchum 2022
        mbonnoujovial@gmail.com
"""

import depthai as dai
from src.calc import HostSpatialsCalc

import numpy as np
import math
import matplotlib.pyplot as plt
import boxMeasurementUtility as bm
import keyboard
import pdb


class Dimensions:
    """
    This class help to compute the dimension (in meter) of an object with the following  process:
    - takes the image of the object directly from the camera
    - compute the bounding box ( in pixels ) of the object present on the image
    - compute the distance (object - camera) by applying the "Calculate spatial coordinates on the host"
        (https://github.com/luxonis/depthai-experiments/tree/master/gen2-calc-spatials-on-host) of depthai
    - convert the dimension of computed bounding box from pixels to meter using the distance (object - camera)
        and the focal length of the color camera

    the function compute_width_height follows all these steps and  return the dimension
    of the object present on the current image
    """

    def __init__(self):
        self._pipeline = dai.Pipeline()

        # Define sources and outputs
        self._camRgb = self._pipeline.create(dai.node.ColorCamera)
        self._monoLeft = self._pipeline.create(dai.node.MonoCamera)
        self._monoRight = self._pipeline.create(dai.node.MonoCamera)
        self._stereo = self._pipeline.create(dai.node.StereoDepth)

        # Properties
        self._monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        self._monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
        self._monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        self._monoRight.setBoardSocket(dai.CameraBoardSocket.RIGHT)

        self._camRgb.setPreviewSize(416, 416)
        self._camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
        self._camRgb.setInterleaved(False)
        self._camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

        self._stereo.initialConfig.setConfidenceThreshold(170)
        # stereo.setLeftRightCheckThreshold(5)
        self._stereo.setLeftRightCheck(True)
        self._stereo.setExtendedDisparity(True)
        self._stereo.setSubpixel(False)

        # Linking
        self._monoLeft.out.link(self._stereo.left)
        self._monoRight.out.link(self._stereo.right)

        self._xoutDepth = self._pipeline.create(dai.node.XLinkOut)
        self._xoutRgb = self._pipeline.create(dai.node.XLinkOut)
        # xoutMonoRight = pipeline.create(dai.node.XLinkOut)

        self._xoutRgb.setStreamName("rgb")
        self._xoutDepth.setStreamName("depth")
        # xoutMonoRight.setStreamName("mono")

        self._stereo.depth.link(self._xoutDepth.input)
        self._camRgb.preview.link(self._xoutRgb.input)
        # monoRight.out.link(xoutMonoRight.input)

        self._xoutDepth = self._pipeline.create(dai.node.XLinkOut)
        self._xoutDepth.setStreamName("disp")
        self._stereo.disparity.link(self._xoutDepth.input)

    def compute_width_height(self, focal_length=3.37, return_mat=False):
        """
        compute the dimension (in meter) of the object present on the current image took by the camera
        :param focal_length: the focal length of the camera
        :param return_mat: True if the matrix of the current image must be returned
        :return: the dimension in meter on optionally the matrix of the image
        """
        # Connect to device and start pipeline
        with dai.Device(self._pipeline) as device:
            # Output queue will be used to get rgb frames and the depth frames from the outputs defined above
            previewQueue = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
            depthQueue = device.getOutputQueue(name="depth")
            dispQ = device.getOutputQueue(name="disp")
            # monoQ = device.getOutputQueue(name="mono")

            hostSpatials = HostSpatialsCalc(device)
            # y = 200
            # x = 300
            step = 3
            delta = 5
            hostSpatials.setDeltaRoi(delta)
            hostSpatials.setLowerThreshold(20)

            print("Use WASD keys to move ROI.\nUse 'r' and 'f' to change ROI size.")

            # while True:

            frame = previewQueue.get().getCvFrame()
            # monoFrame = monoQ.get().getCvFrame()
            depthFrame = depthQueue.get().getFrame()
            width, height, orig, (tltrX, tltrY, trbrX, trbrY), (topLeft, bottomRight) = bm.get_bbox_width_height_pxl(
                frame)

            # color = (255, 0, 0)
            # image = cv2.rectangle(frame, (int(tltrX-width/2), int(tltrY-height/2)), (int(trbrX-width/2), int(trbrY-height/2)), color, 2)
            # print((xmin, ymin, xmax, ymax))
            # plt.imshow(image)
            # plt.show()
            # pdb.set_trace()
            # Calculate spatial coordiantes from depth frame
            spatials, centroid = hostSpatials.calc_spatials(depthFrame,
                                                            [int(topLeft[0]), int(topLeft[1]), int(bottomRight[0]),
                                                             int(bottomRight[1])])  # centroid == x/y in our case

            Z = spatials['z']
            # pdb.set_trace()
            if not math.isnan(Z):
                # print(Z)
                width, height = bm.get_bbox_width_height_in_mm((width, height), Z, focal_length)

                # draw the object sizes on the image
                # cv2.putText(orig, "{:.1f}cm".format(width/1000),
                #              (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                #               0.65, (255, 255, 255), 2)
                # cv2.putText(orig, "{:.1f}cm".format(height/1000),
                #              (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                #               0.65, (255, 255, 255), 2)

                # Show the frame
                # cv2.imshow("depth", orig)
                # cv2.waitKey()
            if return_mat:
                return width / 1000, height / 1000, frame
            return width / 1000, height / 1000


def boxMeasurement():
    """
    apply the box measurement commended by the space keyboard
    usage:
    - press the "space" one time to take the width and height of the object
    - change the position/view-side of the object
    - press "space" again to take the width/height and depth of the object
    :return: the dimension (width, height, depth) after the space is pressed 2 times
    """
    dimension_list = []
    dimensions = Dimensions()
    view1 = 1
    while True:
        print("press space to compute the next dimension")
        # key = cv2.waitKey(0  )
        keyboard.wait(" ")
        width, height = dimensions.compute_width_height()
        dimension_list.append(width)
        dimension_list.append(height)

        if view1 == 1:
            view1 = 2
        elif view1 == 2:
            break
    dimension_list.sort()
    return dimension_list[:3]


dim = boxMeasurement()

print(dim)
