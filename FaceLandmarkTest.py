import sys
import os
import dlib
import glob

if len(sys.argv) != 3:
    print(
        "Give the path to the trained shape predictor model as the first "
        "argument and then the directory containing the facial images.\n"
        "For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./face_landmark_detection.py shape_predictor_68_face_landmarks.dat ../examples/faces\n"
        "You can download a trained facial shape predictor from:\n"
        "    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
    exit()

predictor_path = sys.argv[1]
faces_folder_path = sys.argv[2]

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

win = dlib.image_window()

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))

    img = dlib.load_rgb_image(f)

    win.clear_overlay()
    win.set_image(img)

    dets = detector(img, 1)

    print("Number of faces detected: {}".format(len(dets)))

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))

        shape = predictor(img, d)

        print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                  shape.part(1)))

        for j in range(68):
            x, y = shape.part(j).x, shape.part(j).y
            win.add_overlay_circle(dlib.point(x, y), 1, dlib.rgb_pixel(0, 0, 255))

        win.add_overlay(shape)

    win.add_overlay(dets)

    dlib.hit_enter_to_continue()