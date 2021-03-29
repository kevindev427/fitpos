import math
import numpy as np
import cv2

#Angle using arctan2
def angle(a,b,c):
    ba = a - b
    bc = c - b
    angle = math.atan2(bc[1], bc[0]) - math.atan2(ba[1], ba[0])
    if (angle < 0):
        angle += 2 * math.pi
    angle_in_deg = (angle*180)/math.pi
    return angle_in_deg
      
#Used for calculating angle between 3 specified keypoints 
def keypoint_angle(keypoints,a,b,c):
    a1 = keypoints[a]['X']*100,keypoints[a]['Y']*100
    b1 = keypoints[b]['X']*100,keypoints[b]['Y']*100
    c1 = keypoints[c]['X']*100,keypoints[c]['Y']*100
    a2,b2,c2 = np.array(list(a1)), np.array(list(b1)), np.array(list(c1))
    angle1 = angle(a2,b2,c2)
    return(angle1,a2,b2,c2)

def ohp_posture_right(right_deviation, flag_right_correct, flag_right_wrong, stats):

    if right_deviation<10:
      stats = cv2.putText(stats, 'Right deviation: '+ str(round(right_deviation,2)), (5,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
      flag_right_correct += 1
      if flag_right_correct>0 and flag_right_correct<=20:
        stats = cv2.putText(stats, 'Fix your right hand form!', (5,185), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)
      elif flag_right_correct>20:
        flag_right_wrong = 0
        stats = cv2.putText(stats, 'Your right hand form is perfect', (5,185), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

    else:
      stats = cv2.putText(stats, 'Right deviation: '+ str(round(right_deviation,2)), (5,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA)
      flag_right_wrong += 1
      if flag_right_wrong>0 and flag_right_wrong<=15:
        stats = cv2.putText(stats, 'Your right hand form is perfect', (5,185), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)
      elif flag_right_wrong>15:
        flag_right_correct = 0
        stats = cv2.putText(stats, 'Fix your right hand form!', (5,185), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)

    return(right_deviation, flag_right_correct, flag_right_wrong, stats)

def ohp_posture_left(left_deviation, flag_left_correct, flag_left_wrong, stats):

    if left_deviation<10:
      stats = cv2.putText(stats, 'Left deviation: '+ str(round(left_deviation,2)), (5,155), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA) 
      flag_left_correct += 1
      if flag_left_correct>0 and flag_left_correct<=20:
        stats = cv2.putText(stats, 'Fix your left hand form!', (5,205), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)
      elif flag_left_correct>20:
        flag_left_wrong = 0
        stats = cv2.putText(stats, 'Your left hand form is perfect', (5,205), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

    else:
      stats = cv2.putText(stats, 'Left deviation: '+ str(round(left_deviation,2)), (5,155), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA) 
      flag_left_wrong+=1
      if flag_left_wrong>0 and flag_left_wrong<=15:
        stats = cv2.putText(stats, 'Your left hand form is perfect', (5,205), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)
      elif flag_left_wrong>15:
        flag_left_correct  = 0
        stats = cv2.putText(stats, 'Fix your left hand form!', (5,205), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA)

    return(left_deviation, flag_left_correct, flag_left_wrong, stats)
