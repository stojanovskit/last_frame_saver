import cv2
import os
import time

def get_last_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames in {video_path}: {total_frames}")
    if total_frames == 0:
        print(f"Error: Video {video_path} has no frames.")
        cap.release()
        return None
    
    # Set the position to the last frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
    ret, frame = cap.read()
    cap.release()
    if not ret or frame is None:
        print(f"Error: Could not read the last frame from {video_path}")
        return None
    return frame

def save_frame(frame, output_path):
    cv2.imwrite(output_path, frame)

def get_frame_near_end(video_path, offset=10):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames in {video_path}: {total_frames}")
    frame_to_capture = max(total_frames - offset, 0)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_capture)
    ret, frame = cap.read()
    cap.release()
    if not ret or frame is None:
        print(f"Error: Could not read the near end frame from {video_path}")
        return None
    return frame

def main(folder_path):
    processed_videos = set()

    while True:
        # Scan for new video files
        for filename in os.listdir(folder_path):
            if filename.endswith(('.mp4', '.avi', '.mov')) and filename not in processed_videos:
                video_path = os.path.join(folder_path, filename)
                print(f"Processing video: {filename}")

                # Get the last frame
                last_frame = get_last_frame(video_path)
                if last_frame is not None:
                    last_frame_path = os.path.join(folder_path, f"{filename}_last_frame.jpg")
                    save_frame(last_frame, last_frame_path)
                    print(f"Saved last frame to: {last_frame_path}")

                    # Ask user if the photo is clear
                    while True:
                        user_input = input("Is the photo clear? (1: Yes, 2: No, 0: Exit): ")
                        if user_input == '1':
                            processed_videos.add(filename)
                            break
                        elif user_input == '2':
                            # Get a frame near the end
                            near_end_frame = get_frame_near_end(video_path)
                            if near_end_frame is not None:
                                near_end_frame_path = os.path.join(folder_path, f"{filename}_near_end_frame.jpg")
                                save_frame(near_end_frame, near_end_frame_path)
                                print(f"Saved near end frame to: {near_end_frame_path}")
                        elif user_input == '0':
                            print("Exiting...")
                            return
                        else:
                            print("Invalid input. Please enter 1, 2, or 0.")

        time.sleep(5)  # Wait before scanning again

if __name__ == "__main__":
    folder_to_watch = r"E:\Downloads\videonew"  # Change this to your folder path
    main(folder_to_watch)
