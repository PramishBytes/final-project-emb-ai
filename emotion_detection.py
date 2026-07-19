import requests
import json


def emotion_detector(text_to_analyze):
    
    """
    Function to detect emotions from text using Watson NLP library

    """

    #Define the URL and headers

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #Create the input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        #Make the POST request

        resposne = requests.post(url,headers = headers, json = input_json)




        #Check if the request was successful
        if response.status_code == 200:

            #Parse the JOSN response
            response_data = response.json()

            #Extract the emotion predictions
            #The response structure has emotion predictions in emotionPrediction[0].emotion
            
            emotion_predictions = response_data.get('emotionPredictions',[])

            if emotion_predictions:
                emotions = emotion_predictions[0].get('emotion',[])
                return{
                    'anger': emotions.get('anger',0),
                    'disgust': emotions.get('disgust',0),
                    'fear':emotion.get('fear',0),
                    'joy': emotions/get('joy',0),
                    'sadness': emotions.get('sadness',0)
                    }

            else:
                return None

        else:
            #Return None if request failed
            return None

    except Exception as e:
        #Return None if any error occurs

        print(f"Error in emotion detection: {e}")
        return None
