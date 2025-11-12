#!/usr/bin/env python3
"""
Face Dataset Creation Application
==================================
This application allows users to create a face dataset by:
1. Entering their name
2. Taking 1 front photo and 11 additional photos
3. Saving all photos with proper labels in a dataset directory
"""

import cv2
import os
import sys
from datetime import datetime


class FaceDatasetCreator:
    """Class to handle face dataset creation"""
    
    def __init__(self):
        self.dataset_dir = "dataset"
        self.person_name = ""
        self.person_dir = ""
        
    def setup_directories(self):
        """Create necessary directories for the dataset"""
        if not os.path.exists(self.dataset_dir):
            os.makedirs(self.dataset_dir)
            print(f"✓ Created dataset directory: {self.dataset_dir}")
        
        # Create person-specific directory
        self.person_dir = os.path.join(self.dataset_dir, self.person_name)
        if not os.path.exists(self.person_dir):
            os.makedirs(self.person_dir)
            print(f"✓ Created directory for {self.person_name}: {self.person_dir}")
        else:
            print(f"⚠ Warning: Directory for {self.person_name} already exists")
            response = input("Continue anyway? (y/n): ")
            if response.lower() != 'y':
                print("Exiting...")
                sys.exit(0)
    
    def get_person_name(self):
        """Request and validate person's name"""
        while True:
            name = input("\nEnter the person's name: ").strip()
            if name:
                self.person_name = name.replace(" ", "_")
                print(f"✓ Name set to: {self.person_name}")
                return
            else:
                print("❌ Name cannot be empty. Please try again.")
    
    def capture_photos(self):
        """Capture 12 photos: 1 front photo + 11 additional photos"""
        print("\n" + "="*60)
        print("PHOTO CAPTURE INSTRUCTIONS")
        print("="*60)
        print("You will take 12 photos:")
        print("  - Photo 1: Front face photo (looking directly at camera)")
        print("  - Photos 2-12: Additional photos (different angles/expressions)")
        print("\nControls:")
        print("  - Press SPACE to capture photo")
        print("  - Press ESC to cancel and exit")
        print("="*60)
        
        input("\nPress ENTER to start capturing photos...")
        
        # Initialize camera
        camera = cv2.VideoCapture(0)
        
        if not camera.isOpened():
            print("❌ Error: Could not open camera")
            print("Please check if:")
            print("  1. A camera is connected to your computer")
            print("  2. No other application is using the camera")
            print("  3. You have granted camera permissions")
            sys.exit(1)
        
        print("✓ Camera initialized successfully")
        
        # Set camera properties for better quality
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        photo_count = 0
        total_photos = 12
        
        while photo_count < total_photos:
            ret, frame = camera.read()
            
            if not ret:
                print("❌ Error: Could not read frame from camera")
                break
            
            # Display current photo number and instructions
            photo_type = "FRONT PHOTO" if photo_count == 0 else f"PHOTO {photo_count + 1}/{total_photos}"
            instruction = "Look directly at camera" if photo_count == 0 else "Different angle/expression"
            
            # Add text overlay
            display_frame = frame.copy()
            cv2.putText(display_frame, photo_type, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(display_frame, instruction, (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.putText(display_frame, "SPACE: Capture | ESC: Exit", (10, 90), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
            
            # Show progress bar
            progress_width = int((photo_count / total_photos) * 620)
            cv2.rectangle(display_frame, (10, 450), (630, 470), (50, 50, 50), -1)
            cv2.rectangle(display_frame, (10, 450), (10 + progress_width, 470), (0, 255, 0), -1)
            progress_text = f"{photo_count}/{total_photos} photos captured"
            cv2.putText(display_frame, progress_text, (210, 465), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            cv2.imshow('Face Dataset Creator', display_frame)
            
            key = cv2.waitKey(1) & 0xFF
            
            # Space key to capture
            if key == 32:  # SPACE key
                # Generate filename with label
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                if photo_count == 0:
                    label = "front"
                    filename = f"{self.person_name}_{label}_{timestamp}.jpg"
                else:
                    label = f"photo_{photo_count + 1:02d}"
                    filename = f"{self.person_name}_{label}_{timestamp}.jpg"
                
                filepath = os.path.join(self.person_dir, filename)
                
                # Save the photo
                cv2.imwrite(filepath, frame)
                photo_count += 1
                
                print(f"✓ Photo {photo_count}/{total_photos} saved: {filename}")
                
                # Brief pause to show feedback
                feedback_frame = display_frame.copy()
                cv2.putText(feedback_frame, "CAPTURED!", (220, 240), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
                cv2.imshow('Face Dataset Creator', feedback_frame)
                cv2.waitKey(500)  # Show for 500ms
                
            # ESC key to exit
            elif key == 27:  # ESC key
                print("\n⚠ Cancelled by user")
                camera.release()
                cv2.destroyAllWindows()
                sys.exit(0)
        
        camera.release()
        cv2.destroyAllWindows()
        
        print(f"\n✓ Successfully captured all {total_photos} photos!")
        return photo_count
    
    def create_dataset_info(self, photo_count):
        """Create a metadata file with dataset information"""
        info_file = os.path.join(self.person_dir, "dataset_info.txt")
        
        with open(info_file, 'w') as f:
            f.write(f"Face Dataset Information\n")
            f.write(f"=" * 50 + "\n")
            f.write(f"Person Name: {self.person_name}\n")
            f.write(f"Total Photos: {photo_count}\n")
            f.write(f"Creation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Directory: {self.person_dir}\n")
            f.write(f"\nPhoto Breakdown:\n")
            f.write(f"  - 1 front photo (direct face)\n")
            f.write(f"  - {photo_count - 1} additional photos (various angles)\n")
        
        print(f"✓ Dataset info saved: {info_file}")
    
    def run(self):
        """Main execution flow"""
        print("\n" + "="*60)
        print("FACE DATASET CREATOR")
        print("="*60)
        print("This application will help you create a face dataset")
        print("by capturing 12 photos with proper labels.")
        print("="*60)
        
        # Step 1: Get person's name
        self.get_person_name()
        
        # Step 2: Setup directories
        self.setup_directories()
        
        # Step 3: Capture photos
        photo_count = self.capture_photos()
        
        # Step 4: Create dataset info file
        self.create_dataset_info(photo_count)
        
        # Summary
        print("\n" + "="*60)
        print("DATASET CREATION COMPLETE!")
        print("="*60)
        print(f"Person: {self.person_name}")
        print(f"Photos saved: {photo_count}")
        print(f"Location: {self.person_dir}")
        print("="*60)
        print("\n✓ Your face dataset has been successfully created!")


def main():
    """Entry point of the application"""
    try:
        creator = FaceDatasetCreator()
        creator.run()
    except KeyboardInterrupt:
        print("\n\n⚠ Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
