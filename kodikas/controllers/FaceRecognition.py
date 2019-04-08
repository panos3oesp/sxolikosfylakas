import face_recognition
import cv2
import os
from models.personmodel import *
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

class FaceRecognition:
  def __init__(self,confManager):
    self.video_capture = cv2.VideoCapture(1)
    self.known_face_encodings = []
    self.known_face_names=[]
    self.confManager =  confManager
  def recognise(self):
    print("ciaos1")
    personModel=PersonModel(self.confManager.dbPath)
    persons = personModel.getAll()
    face_locations = []
    face_encodings = []
    face_names = []
    print("hi")
    camera = PiCamera()
    camera.resolution = (480, 320)
    for person in persons[1:2]:
      
      print("ciaos2")
      print("res"+os.path.sep+"faces"+os.path.sep+str(person[3]))
      image = face_recognition.load_image_file("res/faces/panos.png")
      print("ciaos3")
      encoding = face_recognition.face_encodings(image)[0]
      print("hi3")
      print("image"+person[3])
      self.known_face_encodings+=[encoding]
      self.known_face_names+=[str(person[1])+" "+(person[2])]

    self.process_this_frame = True
    
    while True:
      # Grab a single frame of video
      #ret, frame = self.video_capture.read()
      
      rawCapture = PiRGBArray(camera)
      time.sleep(0.1)
      camera.capture(rawCapture, format="bgr")
      frame = rawCapture.array
      
      print("get frame")
      # Resize frame of video to 1/4 size for faster face recognition processing
      small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
      
      print("resize frame")
      # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
      rgb_small_frame = small_frame [:, :, ::-1]
      print("convert colors")
      if self.process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:
          # See if the face is a match for the known face(s)
          matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
          name = "Unknown"
          print("testing encoding")
          if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
          face_names.append(name)

      self.process_this_frame = not self.process_this_frame

      # Display the results
      for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        print("printing rectangle")

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


      # Display the resulting image
      cv2.imshow('Video', frame)

      # Hit 'q' on the keyboard to quit!
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break


  # Release handle to the webcam
    self.video_capture.release()
    cv2.destroyAllWindows()

  def justEncode(self):
    personModel=PersonModel(self.confManager.dbPath)
    persons = personModel.getAll()
    face_locations = []
    face_encodings = []
    face_names = []
    print("hi")
    for person in persons:          
      print("res"+os.path.sep+"faces"+os.path.sep+str(person[3]))
      image = face_recognition.load_image_file("res/faces/panos.png")      
      encoding = face_recognition.face_encodings(image)[0]            
      self.known_face_encodings+=[encoding]
      self.known_face_names+=[str(person[1])+" "+(person[2])]
      print("Done "+ str(person[3]))
    print("general done")
    print(face_encodings)
    
