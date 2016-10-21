import cv2

class PeopleFinder():
    
    def __init__(self, cam, classifier):
        self.faceCascade = cv2.CascadeClassifier(classifier)
        self.video_capture = cv2.VideoCapture(cam)
        for i in range(30):
            ret, frame = self.video_capture.read()

    def get_people_number(self):
        for i in range(30):
            ret, frame = self.video_capture.read()
            if not ret:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.12,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
                )
        return len(faces)
