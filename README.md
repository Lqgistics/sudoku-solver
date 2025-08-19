# Sudoku Solver with Computer Vision

An automated Sudoku solver that uses computer vision to extract puzzles from images and machine learning for digit recognition.

## Features

- **Image File Support**: Load Sudoku puzzles from image files (JPEG, PNG, BMP, TIFF)
- **Advanced Image Processing**: Automatic preprocessing with corner detection and perspective correction
- **Grid Extraction**: Automatic extraction of Sudoku grids from photographs
- **Cell Isolation**: Individual cell detection and isolation for digit recognition
- **Deep Learning OCR**: Trained neural network models for accurate digit recognition
- **Automatic Solving**: Fast backtracking algorithm for puzzle solving
- **GUI Interface**: User-friendly interface with image selection, hints and solving capabilities
- **Database Integration**: SQLite database for storing solutions and game states

## Technology Stack

- **Python 3.x**
- **TensorFlow/Keras** - Deep learning models
- **OpenCV** - Computer vision and image processing
- **NumPy** - Numerical computations
- **Tkinter** - GUI framework
- **SQLite** - Database management
- **Pillow** - Image manipulation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lqgistics/sudoku_solver.git
cd sudoku_solver
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main application:
```bash
python src/main.py
```

## Project Structure

```
sudoku-solver/
├── src/                          # Main application code
│   ├── main.py                   # Main application entry point
│   ├── sudoku_solver_v1.py       # Previous version implementation
│   └── sudoku_algorithm.py       # Core solving algorithms
├── models/                       # Trained neural network models
│   ├── digit_classifier.h5       # Digit recognition model
│   └── ocr_model.h5              # OCR processing model
├── data/                         # Sample data and databases
│   ├── answers.db                # SQLite database with solutions
│   └── sample_images/            # Test images
│       ├── test_sudoku.jpg       # Sample puzzle image
│       └── test_processed.png    # Processed image example
├── training/                     # Model training scripts
│   ├── train_digit_classifier.py # Main training script
│   └── model_training_experiments/
│       ├── training_experiment_1.py
│       └── training_experiment_2.py
├── tests/                        # Testing and validation
│   ├── model_performance_test.py # Model accuracy testing
│   ├── gui_test.py              # GUI functionality tests
│   ├── image_processing_test.py  # Computer vision tests
│   └── hough_lines_test.py      # Line detection tests
├── experiments/                  # Research and experiments
│   └── post_processing_experiments.py
└── docs/                        # Documentation
    └── original_readme.txt      # Original project notes
```

## Usage

### Basic Usage
1. Launch the application: `python src/main.py`


### Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)

### Alternative - Run from source directory
```bash
cd src
python main.py
```

### Training Custom Models
```bash
cd training
python train_digit_classifier.py --model ../models/new_model.h5
```

### Running Tests
```bash
cd tests
python model_performance_test.py
python gui_test.py
```

## How It Works

1. **Image Acquisition**: Load Sudoku puzzle image
2. **Preprocessing**: Apply Gaussian blur, thresholding, and noise reduction
3. **Grid Detection**: Use Hough line detection to find grid boundaries
4. **Perspective Correction**: Warp the image to get a top-down view
5. **Cell Extraction**: Divide the grid into 81 individual cells
6. **Digit Recognition**: Use trained CNN to recognize digits in each cell
7. **Puzzle Solving**: Apply backtracking algorithm to solve the puzzle
8. **Result Display**: Show the completed puzzle with highlighted solutions

## Model Performance

- **Digit Recognition Accuracy**: >95% on test dataset
- **Grid Detection Success Rate**: >90% on clear images
- **Average Solving Time**: <1 second for most puzzles

## Development History

This project represents the evolution of a Sudoku solver from initial experiments to a fully functional application:

- **V1-V2**: Initial computer vision experiments
- **V3-V4**: Model training and OCR development
- **V5 (Current)**: Complete application with GUI and database integration

## Contributing

This project was developed as part of an A-Level Computer Science project. Feel free to explore the code and suggest improvements!

## License

This project is open source and available under the MIT License.

## Contact

For questions or collaboration opportunities, please reach out through GitHub.
