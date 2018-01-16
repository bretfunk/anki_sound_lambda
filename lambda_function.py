from gtts import gTTS
import boto3

def lambda_handler(event, context):
    phrase = event["phrase"]
    language = event["language"]
    file_name = event["file_name"]
    create_file(phrase, language, file_name)

def create_file(phrase, language, file_name):
    tts = gTTS(text=phrase, lang=language)
    tts.save("/tmp/{}.mp3".format(file_name))
    upload_file(phrase, language, file_name)

def upload_file(phrase, language, file_name):
    bucket = 'elasticbeanstalk-us-west-2-747213477632'
    s3_client = boto3.client('s3')
    s3_client.upload_file("/tmp/{}.mp3".format(file_name), bucket, "{}/{}.mp3".format(language, file_name))
