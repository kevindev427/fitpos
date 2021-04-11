import cv2
import mediapipe as mp
import time
from imutils.video import VideoStream, WebcamVideoStream
import numpy as np

import argparse

def main_pose(cap):
  # if not (args.reps or args.duration):
  #   parser.error('No action requested, add --reps or --duration')
  #time.sleep(5)
  mp_drawing = mp.solutions.drawing_utils
  mp_pose = mp.solutions.pose

  #Upper body only (y/n)
  upper = True 

  #Setting up the parameters of the inference model
  with mp_pose.Pose(
      static_image_mode=False,
      upper_body_only=upper,
      smooth_landmarks=True,
      min_detection_confidence=0.9,
      min_tracking_confidence=0.9) as pose:
    
    stats = cv2.imread('white2.jpg') 

    while True:
      start = time.time()
      image = cap.read()
      # stats = cv2.imread('white2.jpg') 
      
      # Flip the image horizontally for a later selfie-view display, and convert the BGR image to RGB.
      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
      # To improve performance, optionally mark the image as not writeable to pass by reference.
      image.flags.writeable = False

      #Calling inference
      results = pose.process(image)

      # Draw the pose annotation on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      #Creating a uper_body_only yes/no state

      #Creating a list of dictionaries of the keypoints (x,y,z,visibility)
      if results.pose_landmarks:
        keypoints = []
        for data_point in results.pose_landmarks.landmark:
          keypoints.append({
            'X': data_point.x,
            'Y': data_point.y,
            'Z': data_point.z,
            'Visibility': data_point.visibility,
          })

        #Calling the shoulder press function that returns angles, deviations and stats image of every frame
        right_shoulder_angle, right_elbow_angle, right_deviation, left_shoulder_angle, left_elbow_angle, left_deviation, stats = shoulder_press(keypoints)

      #Error message if keypoints aren't visible
      else:
        image = cv2.putText(image, 'Upper body not visible', (5,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2, cv2.LINE_AA)

      #Different drawing functions for upper pose and non upper pose
      if upper==False:  
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
      elif upper==True:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.UPPER_BODY_POSE_CONNECTIONS)
      
      end = time.time()
      #print(1/(end-start))
      # if stats is not None:
      #   cv2.imshow('Stats', stats)
      image = cv2.putText(image, str(round((1/(end-start)),2)), (565,25), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2, cv2.LINE_AA)
      # cv2.imshow('MediaPipe Pose', image)
      # if cv2.waitKey(5) & 0xFF == 27:
      #   break
      
      return image