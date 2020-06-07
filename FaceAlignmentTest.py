import sys
import dlib
import cv2
import openface
import glob
import os

predictor_model = "shape_predictor_68_face_landmarks.dat"

face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

faces_folder_path = sys.argv[1]

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))

    image = cv2.imread(f, cv2.IMREAD_COLOR)

    detected_faces = face_detector(image, 1)
    print("Number of faces detected: {}".format(len(detected_faces)))

    for i, face_rect in enumerate(detected_faces):
        print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(),
                                                                                 face_rect.right(), face_rect.bottom()))

        pose_landmarks = face_pose_predictor(image, face_rect)

        alignedFace = face_aligner.align(534, image, face_rect,
                                         landmarkIndices=openface.AlignDlib.INNER_EYES_AND_BOTTOM_LIP)

        cv2.imwrite(f + "{}.jpg".format(i), alignedFace)
