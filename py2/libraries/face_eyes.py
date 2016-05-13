import cv2
ff = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'
ef = '/usr/share/opencv/haarcascades/haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(ff)
eye_cascade = cv2.CascadeClassifier(ef)

def detect_faces(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(faces == ()):
        return 0
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imwrite(img_path, img)
    return len(faces)
    
    
def detect_eyes(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    if(eyes == ()):
        return 0
    for(x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imwrite(img_path, img)
    return len(eyes)


def main(args):
    if(len(sys.argv) != 2):
        print('Image Path Needed.')
    else:
        img_path = sys.argv[1]
        try:
            n = detect_faces(img_path)
            if(n == 0):
                print('No faces detected.')
            else:
                print('Found {} face{}.'.format(n, ('s' if n > 1 else '')))
            n = detect_eyes(img_path)
            if(n == 0):
                print('No eyes detected.')
            else:
                print('Found {} eye{}.'.format(n, ('s' if n > 1 else '')))
        except Exception as e:
            print('Exception thrown:\n', e) 
                
if(__name__ == '__main__'):
    import sys
    print('argv len= ', len(sys.argv))
    main(sys.argv)
