import cv2

# start camera
cap = cv2.VideoCapture(1)
ret, frame = cap.read()
height, width = frame.shape[:2]

# set new height and width
mid_width = width // 2
mid_height = height // 2
new_h_w = 256

print('Press r to capture a rock picture')
print('Press p to capture a paper picture')
print('Press s to capture a scissors picture')
print('Press q to quit')

r_idx = 0
p_idx = 0
s_idx = 0

# start camera feed
while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    # crop frame to 256x256 px
    frame = frame[mid_height-new_h_w//2:mid_height+new_h_w//2,
                  mid_width-new_h_w//2:mid_width+new_h_w//2]

    cv2.imshow('frame', frame)

    # rock
    if cv2.waitKey(1) & 0xFF == ord('r'):
            # cv2.imshow('frame', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'data/rock_{r_idx}.jpg', gray)
            print(f'rock_{r_idx}.jpg saved')
            r_idx += 1
    
    # paper
    elif cv2.waitKey(1) & 0xFF == ord('p'):
            # cv2.imshow('frame', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'data/paper_{p_idx}.jpg', gray)
            print(f'paper_{p_idx}.jpg saved')
            p_idx += 1
    
    # scissors
    elif cv2.waitKey(1) & 0xFF == ord('s'):
            # cv2.imshow('frame', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'data/scissors_{s_idx}.jpg', gray)
            print(f'scissors_{s_idx}.jpg saved')
            s_idx += 1

    # quit
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

    else:
        continue

cap.release()
cv2.destroyAllWindows()