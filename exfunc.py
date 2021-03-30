import numpy as np
import math
import cv2
from basics import *

NOSE = 0
LEFT_EYE_INNER = 1
LEFT_EYE = 2
LEFT_EYE_OUTER = 3
RIGHT_EYE_INNER = 4
RIGHT_EYE = 5
RIGHT_EYE_OUTER = 6
LEFT_EAR = 7
RIGHT_EAR = 8
MOUTH_LEFT = 9
MOUTH_RIGHT = 10
LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12
LEFT_ELBOW = 13
RIGHT_ELBOW = 14
LEFT_WRIST = 15
RIGHT_WRIST = 16
LEFT_PINKY = 17
RIGHT_PINKY = 18
LEFT_INDEX = 19
RIGHT_INDEX = 20
LEFT_THUMB = 21
RIGHT_THUMB = 22
LEFT_HIP = 23
RIGHT_HIP = 24
LEFT_KNEE = 25
RIGHT_KNEE = 26
LEFT_ANKLE = 27
RIGHT_ANKLE = 28
LEFT_HEEL = 29
RIGHT_HEEL = 30
LEFT_FOOT_INDEX = 31
RIGHT_FOOT_INDEX = 32

#Global flag declarations 
flag_right_correct = 0
flag_right_wrong = 0
flag_left_correct = 0
flag_left_wrong = 0

#For counting reps
def count_reps(right_deviation, left_deviation, right_shoulder_angle, left_shoulder_angle, reps, rep_flag):
    if right_deviation < 10 and left_deviation < 10:
        if right_shoulder_angle < 90 and left_shoulder_angle < 90 and rep_flag == 0:
            rep_flag = 1
        elif right_shoulder_angle > 170 and left_shoulder_angle > 170 and rep_flag == 1:
            rep_flag = 0
            reps += 1
    return reps, rep_flag

def shoulder_press(keypoints, reps, rep_flag):
    global flag_right_correct
    global flag_right_wrong
    global flag_left_correct 
    global flag_left_wrong

    #Right hand angle and deviation calculation
    right_shoulder_angle, x, y, z = keypoint_angle(keypoints, LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP)
    right_elbow_angle, x, y, z = keypoint_angle(keypoints, LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST)
    right_deviation = abs(right_shoulder_angle - right_elbow_angle)

    #Left hand angle and deviation calculation
    left_shoulder_angle, x, y, z = keypoint_angle(keypoints, RIGHT_HIP, RIGHT_SHOULDER, RIGHT_ELBOW)
    left_elbow_angle, x, y, z = keypoint_angle(keypoints, RIGHT_WRIST, RIGHT_ELBOW, RIGHT_SHOULDER)
    left_deviation = abs(left_shoulder_angle - left_elbow_angle)

    #Rep counter
    reps, rep_flag = count_reps(right_deviation, left_deviation, right_shoulder_angle, left_shoulder_angle, reps, rep_flag)

    #Blank white image to display stats
    stats = cv2.imread('white2.jpg') 

    stats = cv2.putText(stats, 'Stats', (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)
    stats = cv2.putText(stats, 'Angle at right shoulder : '+ str(round(right_shoulder_angle,2)), (5,35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)    
    stats = cv2.putText(stats, 'Angle at right elbow : '+ str(round(right_elbow_angle,2)), (5,55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)
    
    #Evaluating the posture for the right hand using a function
    right_deviation, flag_right_correct, flag_right_wrong, stats = ohp_posture_right(right_deviation, flag_right_correct, flag_right_wrong, stats)
    
    stats = cv2.putText(stats, 'Angle at left shoulder : '+ str(round(left_shoulder_angle,2)), (5,115), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)    
    stats = cv2.putText(stats, 'Angle at left elbow : '+ str(round(left_elbow_angle,2)), (5,135), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA) 
   
    #Evaluating the posture for the left hand using a function
    left_deviation, flag_left_correct, flag_left_wrong, stats = ohp_posture_left(left_deviation, flag_left_correct, flag_left_wrong, stats)

    return(right_shoulder_angle, right_elbow_angle, right_deviation, left_shoulder_angle, left_elbow_angle, left_deviation, reps, rep_flag, stats)
