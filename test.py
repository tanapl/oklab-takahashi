import time

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect emotion in the current frame
    # FER returns a list of dictionaries with emotions and scores
    # We'll pick the top emotion from the first face detected
    detections = detector.detect_emotions(frame)
    if detections:
        # Consider only the first face for simplicity
        first_face = detections[0]
        emotions = first_face["emotions"]
        # Find the emotion with the highest score
        dominant_emotion = max(emotions, key=emotions.get)
    else:
        dominant_emotion = "neutral"  # fallback if no face detected

    # Map emotion to PNG
    avatar_file = emotion_to_file.get(dominant_emotion, "neutral.png")
    
    # Load the chosen avatar PNG
    avatar_image = cv2.imread(avatar_file, cv2.IMREAD_UNCHANGED)
    # Resize the avatar if you want
    avatar_image = cv2.resize(avatar_image, (300, 300))
    
    # Display the avatar in a window
    cv2.imshow("Avatar", avatar_image)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(0.1)  # small delay to reduce CPU usage

cap.release()
cv2.destroyAllWindows()