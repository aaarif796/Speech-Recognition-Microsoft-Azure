import os
import time
import azure.cognitiveservices.speech as speechsdk
#from azure.cognitiveservices.translate import TranslatorTextClient
from msrest.authentication import CognitiveServicesCredentials


def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription="20cadcfcdf464c47ab17c319cc146e96", region="centralindia")
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    #speech_config.set_property(property_id=speechsdk.PropertyId.SpeechServiceConnection_LanguageIdMode, value='Continuous')
    #speechsdk.recognizer.start_continuous_recognition()
    #speechsdk.recognizer.stop_continuous_recognition()
    print("Speak the following sentence to check prounciation")
    file_path = "text.txt"


    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
            speech_recognition_result = speech_recognizer.recognize_once_async().get()
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Recognized: {}".format(speech_recognition_result.text))
                s2=speech_recognition_result.text
                print_unmatched_words(line, s2)
        
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

def print_unmatched_words(sentence, reference_words):
    words_in_sentence = sentence.lower().replace('?','').replace('.','').replace(',','').split()
    reference_words_lower = reference_words.lower().replace('?','').replace('.','').replace(',','').split()

    # Find the unmatched words
    unmatched_words = [word for word in words_in_sentence if word not in reference_words_lower]
    if len(unmatched_words)==0:
        print('You Spoke Correctly')
    # Print the unmatched words
    else:
        print("Misspelled Words or missing words")
        for word in unmatched_words:
            print(word)
    print()

recognize_from_microphone()