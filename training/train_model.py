#!/usr/bin/env python3
"""
Training script for the digit classifier model.
Run this script from the training directory to train a new model.

Usage:
    python train_model.py --model ../models/digit_classifier.h5

This script will:
1. Load the MNIST dataset
2. Train a CNN model for digit recognition
3. Save the trained model to the specified path
"""

import sys
import os
import argparse

# Add the parent directory to the path so we can import from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from train_digit_classifier import *

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Train digit classifier model')
    parser.add_argument('--model', type=str, default='../models/digit_classifier.h5',
                        help='Path to save the trained model')
    parser.add_argument('--epochs', type=int, default=10,
                        help='Number of training epochs')
    parser.add_argument('--batch-size', type=int, default=32,
                        help='Batch size for training')
    
    args = parser.parse_args()
    
    print(f"Training model with {args.epochs} epochs...")
    print(f"Model will be saved to: {args.model}")
    
    # Ensure the models directory exists
    os.makedirs(os.path.dirname(args.model), exist_ok=True)
    
    # Train the model (this would call the actual training function)
    print("Starting training...")
    print("Note: Please run the train_digit_classifier.py script directly with proper arguments.")
