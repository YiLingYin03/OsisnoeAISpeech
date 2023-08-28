import os
import azure.cognitiveservices.speech as speechsdk

def azure_text_to_speech(text, accent):

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                           region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = accent

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    result = speech_synthesizer.speak_text(text)

    speech_synthesizer.stop_speaking()

def azure_text_to_speech_file(text, accent):

    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                           region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(filename="temp/outputfile.wav")
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name = accent

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    result = speech_synthesizer.speak_text(text)

    speech_synthesizer.stop_speaking()
