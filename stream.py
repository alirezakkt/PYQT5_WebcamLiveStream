import sys
import cv2

from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi


class Life2coding(QDialog) :
    def __init__(self) :
        super(Life2coding,self).__init__()
        loadUi('2_web.ui',self)
        self.image = None
        self.startButton.clicked.connect(self.start_webcam)
        self.stopButton.clicked.connect(self.stop_webcam)


    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)

        self.timer = Qtimer(self)
        self.timer.timeout.conect(self.update_frame)
        self.timer.star(5)
             
    def update_frame(self) :
        ret.self.image = self.capture.read()
        self.image = cv2.flip(self.image,1)
        self.displayImage(self.image,1)
        


    def stop_webcam(self):
        
        self.timer.stop()

    def displayImage(self,img,window=1):
        pass


if __name__=='__main__':
    app = QApplication(sys.argv)
    window=Life2coding()
    window.setWindowTitle("nadanestegari")
    window.show()
    sys.exit(app.exec_())