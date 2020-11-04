from mtcnn import MTCNN
import cv2
import tensorflow as tf


tf.get_logger().setLevel('INFO')


# img = cv2.cvtColor(cv2.imread("2.jpg"), cv2.COLOR_BGR2RGB)
# detector = MTCNN()
# detector.detect_faces(img)
# print(tf.version)