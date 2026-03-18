# V1
# Import the requests library to handle HTTP requests
# import requests 

# def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse)
#     # URL of the emotion analysis service 
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    
#     # Create a dictionary with the text to be analyzed
#     myobj = { "raw_document": { "text": text_to_analyse } }
    
#     # Set the headers required for the API request 
#     header =  {
#         "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
#     }

#     # Send a POST request to the API with the text and headers
#     response = requests.post(url, json = myobj, headers=header)

#     # Return the response text from the API    
#     return response.text

# V2
import requests 
import json

def emotion_detector(text_to_analyse): 
    # URL of the emotion analysis service 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format 
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion analysis service 
    header =  {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # Sending a POST request to the emotion analysis API 
    response = requests.post(url, json=myobj, headers=header)

    # Error handling incase of 404
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    
    # Extract the required set of emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

# V3
# import requests 
# import json

# def emotion_detector(text_to_analyse): 
#     # Define the URL for the emotion analysis API 
#     url = ''https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict''

#     # Create the payload with the text to be analyzed 
#     myobj = { "raw_document": { "text": text_to_analyse } }

#     # Set the headers with the required model ID for the API 
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-bert-workflow_lang_multi_stock"}

#     # Make a POST request to the API with the payload and headers 
#     response = requests.post(url, json=myobj, headers=header)

#     # Parse the response from the API 
#     formatted_response = json.loads(response.text)

#     # If the response status code is 200, extract the label and score from the response 
#     if response.status_code == 200: 
#         label = formatted_response['documentemotion']['label'] 
#         score = formatted_response['documentemotion']['score'] 
        
#     # If the response status code is 500, set label and score to None 
#     elif response.status_code == 500: 
#         label = None 
#         score = None

#     # Return the label and score in a dictionary 
#     return {'label': label, 'score': score}