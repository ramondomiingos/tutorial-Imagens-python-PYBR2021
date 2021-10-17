import  cv2
import numpy as np
def web_cam_capture():
    web_cam = cv2.VideoCapture(0)
    if web_cam.isOpened():
        #print("conectou!")
        #print(web_cam.read());
        validacao, frame = web_cam.read()
        while validacao:
            validacao, frame = web_cam.read()
            cv2.imshow('minha web cam', cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY ) )
            largura, altura, _ = frame.shape
            imagem_preta = np.zeros((largura, altura), dtype='uint8')
            (B,G,R) = cv2.split(frame)
            R = cv2.merge([imagem_preta,imagem_preta,R])
            G = cv2.merge([imagem_preta,G, imagem_preta])
            B = cv2.merge([B,imagem_preta,imagem_preta])
            cv2.imshow('minha web cam', G )
            key = cv2.waitKey(5)
            if key == 27: #ESC
                break
        # cv2.imwrite("meu_exemplo.jpg", R)
    web_cam.release()
    cv2.destroyAllWindows()