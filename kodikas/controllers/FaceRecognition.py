# κλαση υπεύθυνη για την αναγνώριση προσώπου
# έχει βασιστεί στον κώδικα που δίνεται στο 
# https://github.com/ageitgey/face_recognition

import face_recognition
import cv2
import os
from models.personmodel import *
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import pickle


class FaceRecognition:
  def __init__(self,confManager,mediaHelper):
    self.video_capture = cv2.VideoCapture(1)  #πάρε την on board camera και οχι την usb
    self.known_face_encodings = [] # εδώ κρατάει τα πρόσωπα που υπάρχουν στη βάση αναλυμένα 
    self.known_face_names=[] # εδώ κρατάει τα πρόσωπα που υπάρχουν στη βάση όσον αφόρα τα ονόματά τους
    self.known_face_names_greeklish=[] # το ίδιο αλλά σε greeklish γιατι δεν υποστηρίζει η python στο video rendering ελληνικών
    self.confManager =  confManager
    self.mediaHelper = mediaHelper
  #κάνε την ανάλυση των προσώπων και αποθήκευσέ τα σε αρχείο.
  #αυτό έγινε γιατι το raspberry αδυνατούσε να το κάνει realtime.
  def faceAnalysis(self):
    personModel=PersonModel(self.confManager.dbPath)  #φτιάξε το personmodel instance από τη βάση που βρίσκεται στο ταδε μονοπάτι
    persons = personModel.getAll() #πάρε όλα τα άτομα από τη βδ
    face_encodings = []  #όλα τα πρόσωπα
    for person in persons: # για κάθε άτομο από τη βάση 
      image = face_recognition.load_image_file("res/faces/"+str(person[3]))  #σήκωσε  τις εικόνες τους
      encoding = face_recognition.face_encodings(image)[0] # φτιαξε το encoding καθε εικόνας
      self.known_face_encodings+=[encoding] #βάλε το σε λίστα
    with open('res/dataset_faces.dat', 'wb') as f:  #άνοιξε το αρχείο
       pickle.dump(self.known_face_encodings, f) # πέταξε τη λιστα στο αρχειο dump ;-)
   
  #function που κάνει την αναγνώριση    
  def recognise(self,sendMailForUnknown=False):    
    personModel=PersonModel(self.confManager.dbPath) #φτιαξε instance από το personModel
    persons = personModel.getAll() #πάρε όλα τα άτομα
    face_locations = [] #συγκρατεί τις θέσεις των ατομων στην κάθε εικόνα
    face_encodings = [] # οι αναλύσεις των προσώπων
    face_names = [] #τα ονόματα 
    
    camera = PiCamera() #ξεκίνα την κάμερα
    camera.resolution = (1024, 768)
    for person in persons:
      print("res"+os.path.sep+"faces"+os.path.sep+str(person[3]))              
      self.known_face_names+=[str(person[1])+" "+str(person[2])]
      self.known_face_names_greeklish +=[str(person[6])]

    with open('res/dataset_faces.dat', 'rb') as f:
      self.known_face_encodings = pickle.load(f)
    self.process_this_frame = True
    t_end = time.time() + 60 * 1
    while time.time() < t_end:
      # Grab a single frame of video
      #ret, frame = self.video_capture.read()
      
      rawCapture = PiRGBArray(camera)
      time.sleep(0.1)
      camera.capture(rawCapture, format="bgr")
      frame = rawCapture.array
      
      
      # Resize frame of video to 1/4 size for faster face recognition processing
      small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
      
      
      # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
      rgb_small_frame = small_frame [:, :, ::-1]
      
      if self.process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        
        for face_encoding in face_encodings:
          
          # See if the face is a match for the known face(s)
          matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
        
          name = "Unknown"
          
          if True in matches:
            
            first_match_index = matches.index(True)
            greekName = self.known_face_names[first_match_index]
            name = self.known_face_names_greeklish[first_match_index]
            self.mediaHelper.playStringAsSound("Γεια σου, "+greekName)
            print(greekName)
          face_names.append(name)
          if(sendMailForUnknown  and (name=="Unknown"   or str(person[4]=="0"))):
            self.mediaHelper.playStringAsSound("Συναγερμός! Προσοχή, Προσοχή! Συναγερμός! Προσοχή, Προσοχή! Συναγερμός! Συναγερμός! Συναγερμός! Προσοχή, Προσοχή!")
            

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
    
