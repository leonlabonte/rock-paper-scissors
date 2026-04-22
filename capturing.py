import cv2

# start camera
cap = cv2.VideoCapture(1)
ret, frame = cap.read()
height, width = frame.shape[:2]

# set new height and width
mid_width = width // 2
mid_height = height // 2
new_h_w = 256

print('Press r to start/end capturing rock-pictures')
print('Press p to start/end capturing paper-pictures')
print('Press s to start/end capturing scissors-pictures')
print('Press q to quit')

r_idx = 0
p_idx = 0
s_idx = 0

# start camera feed
while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    # crop frame
    frame = frame[mid_height-new_h_w//2:mid_height+new_h_w//2,
                  mid_width-new_h_w//2:mid_width+new_h_w//2]

    # rock
    if cv2.waitKey(1) & 0xFF == ord('r'):
            cv2.imshow('frame', frame)
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'data/rock_{r_idx}.jpg', frame)
            r_idx += 1
    
    # elif cv2.waitKey(1) & 0xFF == ord('p'):
    #     cv2.imwrite('data/paper.jpg', frame)
    # elif cv2.waitKey(1) & 0xFF == ord('s'):
    #     cv2.imwrite('data/scissors.jpg', frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break