# # `pip3 install assemblyai` (macOS)
# # `pip install assemblyai` (Windows)

# import assemblyai as aai

# aai.settings.api_key = "KEY-AssemblyAI"
# transcriber = aai.Transcriber()
# configuracoes = aai.TranscriptionConfig(
#     speaker_labels = True,
#     speaker_expected = 2,
#     language_code = 'pt'
#     )
# transcript = transcriber.transcribe("NEW-FILE.mp3",  config=configuracoes)
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")

# print(transcript.text)


import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "KEY-AssemblyAI"

##
def mp3_to_text()  #PRECISA TRANSFORMAR EM FUNÇÃO PARA CHAMAR NO AUTOMAI2


# URL of the file to transcribe
FILE_URL = "NEW-FILE.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

transcriber = aai.Transcriber()

configuracoes = aai.TranscriptionConfig(
    speaker_labels = True,
    speakers_expected = 2,
    language_code = 'pt'
    )
transcript = transcriber.transcribe(FILE_URL, config=configuracoes)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    for sentencia in transcript.utterances:
        print(f"{sentencia.speaker}: {sentencia.text}")
        print('\n')