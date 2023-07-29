# Speech-Recognition-Microsoft-Azure
 This Python program uses Azure Cognitive Services Speech SDK to detect if a user's pronunciation matches a given text. It transcribes the user's speech from an audio file and compares it with the provided text to determine if the pronunciation is correct. The program also includes a graphical user interface (GUI) built with tkinter for ease of use.

## Features

- Speech-to-Text Transcription: Converts user's speech from an audio file into written text using Azure Speech Services.
- Pronunciation Comparison: Compares the recognized text with the given text to evaluate pronunciation correctness.
- Case-Insensitive Comparison: Pronunciation comparison is case-insensitive to accommodate variations in speech.
- Graphical User Interface (GUI): Provides an intuitive GUI powered by tkinter for a seamless user experience.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Azure Speech Services Account: Sign up for a free account [here](https://azure.microsoft.com/en-us/free/cognitive-services/).

### Installation

1. Clone the repository:
`git clone https://github.com/your-username/pronunciation-detection.git`
cd 'Speech Project'

### Install the required packages:
`pip install -r requirements.txt`

#### Configuration
- Replace "YOUR_SPEECH_SERVICES_API_KEY" and "YOUR_SPEECH_SERVICES_REGION" with your actual API key and region in pronunciation_detection.py.
- Provide the path to the audio file containing the user's speech in the audio_file_path variable in pronunciation_detection.py.

Usage
Run the Speech_Project.py script to detect the pronunciation correctness:
`python Speech_Project.py`


## Acknowledgments
This project uses Azure Cognitive Services to perform speech-to-text transcription
