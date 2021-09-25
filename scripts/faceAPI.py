from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from config import FKEY, ENDPOINT


def detect(path):


    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(FKEY))

    image_file = open(path, 'rb')

    response_detection = face_client.face.detect_with_stream(
        image_file,
        detection_model= 'detection_01',
        recognition_model='recognition_04',
        return_face_attributes=['age', 'emotion'],
    )     

    if response_detection:

        for face in response_detection:
            age = face.face_attributes.age
            emotions = face.face_attributes.emotion
            neutral = '{0:.0f}%'.format(emotions.neutral * 100)
            happiness = '{0:.0f}%'.format(emotions.happiness * 100)
            surprise = '{0:.0f}%'.format(emotions.surprise * 100)
            anger = '{0:.0f}%'.format(emotions.anger* 100)


    
        stats = 'Estimated Age: '+str(age)+'\nNeutral: '+str(neutral)+'\nHappiness: '+str(happiness)+'\nSurprise: '+str(surprise)+'\nAnger: '+str(anger)

        return stats        
