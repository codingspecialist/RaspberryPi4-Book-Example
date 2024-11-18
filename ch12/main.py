from flask import Flask, render_template
import os
import boto3

app = Flask(__name__)

def compare_face():
    sourceFile='detect/source.jpg'
    targetFile='detect/target.jpg'
    client=boto3.client('rekognition')
    
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')
    try:
        response=client.compare_faces(SimilarityThreshold=70,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
        for faceMatch in response['FaceMatches']:
            result  = faceMatch['Similarity']
            
        imageSource.close()
        imageTarget.close()
        return result
    except:
        return 0
    
@app.route("/detect")
def detect():
    os.system("libcamera-still -o /home/pi/webapps/ch12/detect/source.jpg")
    result = compare_face()
    return str(result)

@app.route("/")
def indeX():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8889, debug=True)