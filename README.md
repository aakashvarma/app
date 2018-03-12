# Rant it

This repository is the Natural Language Processing (NLP) part of the application.

### Libraries used:
Numpy, nltk, flask

### Description of the flask app:
The flask application returnd an API in JSON format. This flask application gets input data from another API ("http://letsrant.azurewebsites.net/api/values")

### API sample:

{
  "data": [
    {
      "coordinates": null, 
      "issue": "null", 
      "place": "Vellore", 
      "sentneg": "0.2222222222222222", 
      "sentpos": "0.5555555555555556", 
      "tweetid": 972616540976644096
    }, 
    {
      "coordinates": {
        "Latitude": 12.9698532, 
        "Longitude": 79.1555099
      }, 
      "issue": "null", 
      "place": "Gudiyattam", 
      "sentneg": "0.05", 
      "sentpos": "0.6", 
      "tweetid": 972601335714521088
    }, 
    {
      "coordinates": null, 
      "issue": "null", 
      "place": null, 
      "sentneg": "0.05", 
      "sentpos": "0.75", 
      "tweetid": 972562664080617472
    }, 
    {
      "coordinates": null, 
      "issue": "null", 
      "place": null, 
      "sentneg": "0.09090909090909091", 
      "sentpos": "0.7272727272727273", 
      "tweetid": 972561176105123840
    }
  ]
}
