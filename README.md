# processamento_de_imagem

```

#detector facial
detector = dlib.get_frontal_face_detector()

# pontos a serem preditos ( 68 pontos da face)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


img = cv2.imread("figs/silvio.jpg")

# grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# detectando landmarks
faces = detector(gray)
for face in faces:
    x1 = face.left() 
    y1 = face.top() 
    x2 = face.right() 
    y2 = face.bottom() 
    
    crop_img_face = img[y1:y1+y2, x1:x1+x2]
    
    # objeto landmark
    landmarks = predictor(image=gray, box=face)

    # Loop pontos
    for n in range(36, 48):
        pad=10
        
        xx = [landmarks.part(x).x for x in range(36,48)]
        yy = [landmarks.part(x).y for x in range(36,48)]
        maxx = max(xx)
        minx = min(xx)
        maxy = max(yy)
        miny = min(yy) 

        crop_img_eye = img[miny-pad:maxy+pad,minx-pad:maxx+pad]



```
