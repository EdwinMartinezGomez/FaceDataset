"""
Test script for Face Dataset Application
Tests the core functionality without requiring a camera
"""

import unittest
import os
import shutil
import sys
from unittest.mock import Mock, patch, MagicMock
import numpy as np


# Add the parent directory to the path to import the app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from face_dataset_app import FaceDatasetApp


class TestFaceDatasetApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.app = FaceDatasetApp()
        self.test_dataset_path = "test_dataset"
        self.app.dataset_path = self.test_dataset_path
        
    def tearDown(self):
        """Clean up test dataset directory"""
        if os.path.exists(self.test_dataset_path):
            shutil.rmtree(self.test_dataset_path)
    
    def test_initialization(self):
        """Test that the app initializes correctly"""
        self.assertIsNone(self.app.name)
        self.assertEqual(self.app.total_photos, 12)
        self.assertEqual(self.app.photos_taken, 0)
        self.assertFalse(self.app.front_face_captured)
        self.assertIsNotNone(self.app.face_cascade)
    
    @patch('builtins.input', return_value='TestPerson')
    def test_get_name_valid(self, mock_input):
        """Test getting a valid name"""
        result = self.app.get_name()
        self.assertTrue(result)
        self.assertEqual(self.app.name, 'TestPerson')
    
    @patch('builtins.input', side_effect=['', '   ', 'ValidName'])
    def test_get_name_with_retries(self, mock_input):
        """Test that empty names are rejected"""
        result = self.app.get_name()
        self.assertTrue(result)
        self.assertEqual(self.app.name, 'ValidName')
        # Should have been called 3 times due to 2 invalid inputs
        self.assertEqual(mock_input.call_count, 3)
    
    def test_create_person_directory(self):
        """Test directory creation"""
        self.app.name = "TestPerson"
        person_path = self.app.create_person_directory()
        
        expected_path = os.path.join(self.test_dataset_path, "TestPerson")
        self.assertEqual(person_path, expected_path)
        self.assertTrue(os.path.exists(person_path))
        self.assertTrue(os.path.isdir(person_path))
    
    def test_detect_front_face_with_face(self):
        """Test face detection with a face present"""
        # Create a dummy frame with appropriate shape
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Mock the face_cascade object itself
        mock_cascade = Mock()
        mock_cascade.detectMultiScale = Mock(return_value=np.array([[100, 100, 200, 200]]))
        original_cascade = self.app.face_cascade
        self.app.face_cascade = mock_cascade
        
        try:
            has_face, faces = self.app.detect_front_face(frame)
            self.assertTrue(has_face)
            self.assertEqual(len(faces), 1)
        finally:
            self.app.face_cascade = original_cascade
    
    def test_detect_front_face_no_face(self):
        """Test face detection with no face present"""
        # Create a dummy frame
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Mock the face_cascade object itself
        mock_cascade = Mock()
        mock_cascade.detectMultiScale = Mock(return_value=np.array([]))
        original_cascade = self.app.face_cascade
        self.app.face_cascade = mock_cascade
        
        try:
            has_face, faces = self.app.detect_front_face(frame)
            self.assertFalse(has_face)
            self.assertEqual(len(faces), 0)
        finally:
            self.app.face_cascade = original_cascade
    
    def test_photos_taken_counter(self):
        """Test that photo counter increments correctly"""
        self.assertEqual(self.app.photos_taken, 0)
        self.app.photos_taken += 1
        self.assertEqual(self.app.photos_taken, 1)
        self.app.photos_taken += 1
        self.assertEqual(self.app.photos_taken, 2)
    
    def test_front_face_flag(self):
        """Test front face captured flag"""
        self.assertFalse(self.app.front_face_captured)
        self.app.front_face_captured = True
        self.assertTrue(self.app.front_face_captured)
    
    def test_dataset_path_configuration(self):
        """Test that dataset path can be configured"""
        custom_path = "custom_dataset"
        self.app.dataset_path = custom_path
        self.assertEqual(self.app.dataset_path, custom_path)


class TestFaceDatasetAppIntegration(unittest.TestCase):
    """Integration tests for the full workflow"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_dataset_path = "test_dataset_integration"
        
    def tearDown(self):
        """Clean up test dataset directory"""
        if os.path.exists(self.test_dataset_path):
            shutil.rmtree(self.test_dataset_path)
    
    @patch('builtins.input', return_value='IntegrationTest')
    def test_name_and_directory_creation_flow(self, mock_input):
        """Test the complete flow of name input and directory creation"""
        app = FaceDatasetApp()
        app.dataset_path = self.test_dataset_path
        
        # Get name
        result = app.get_name()
        self.assertTrue(result)
        
        # Create directory
        person_path = app.create_person_directory()
        expected_path = os.path.join(self.test_dataset_path, "IntegrationTest")
        
        self.assertEqual(person_path, expected_path)
        self.assertTrue(os.path.exists(person_path))


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
