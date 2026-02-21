import cv2

def main():
    # 0 is usually the standard webcam. if it won't work, try 1 or 2
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Fehler: Kamera konnte nicht geöffnet werden.")
        return

    print("Live-View gestartet. Drücke 'q' zum Beenden.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # get image height and width
        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2

        # --- show crosshair ---
        color = (0, 255, 0)  # green (BGR format)
        thickness = 1

        # horizontal line
        cv2.line(frame, (center_x - 40, center_y), (center_x + 40, center_y), color, thickness)
        # vertical line
        cv2.line(frame, (center_x, center_y - 40), (center_x, center_y + 40), color, thickness)
        # circle
        cv2.circle(frame, (center_x, center_y), 15, color, thickness)
        # pint in the middle
        cv2.circle(frame, (center_x, center_y), 1, color, -1)

        # show frame
        cv2.imshow('CNC XY-Nullpunkt Ausrichtung', frame)

        # press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
