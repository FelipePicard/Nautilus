# find the clown-fish in the anemone
# make the color segmentation of the fish
# display the original video and the filtered one

import cv2

cap = cv2.VideoCapture('nemo.mp4')


while(True):
    ret,frame=cap.read()

    # #Converting the frames to HSV, because with this color
    # #space also shows us the value (or intensity) of each
    # #color, making it easier for us to find nemo's orange color
    nemo = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #defining the color limits for our mask
    # got them from this website https://realpython.com/python-opencv-color-spaces/
    Lorange = (1, 190, 200)
    Dorange = (18, 255, 255)
    Lwhite = (0, 0, 200)
    Dwhite = (145, 60, 255)
    orange_mask = cv2.inRange(nemo, Lorange, Dorange)
    white_mask = cv2.inRange(nemo, Lwhite, Dwhite)

    final_mask = orange_mask + white_mask

    #applying the mask to our video feed to get only the masked colors
    findingnemo = cv2.bitwise_and(frame, frame, mask = final_mask)

    #displaying the original and the filtered video feeds
    cv2.imshow("Filtered", findingnemo)
    cv2.imshow("Original", frame)

    #break the loop if we press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when we leave the loop, stop the capture and close all windows
cap.release()
cv2.destroyAllWindows()