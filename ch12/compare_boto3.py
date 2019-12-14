import boto3

if __name__ == "__main__":
    sourceFile='img/source.jpg'
    targetFile='img/target.jpg'
    client=boto3.client('rekognition')
    
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    try:
        response=client.compare_faces(SimilarityThreshold=70, SourceImage={'Bytes': imageSource.read()}, TargetImage={'Bytes': imageTarget.read()})
        for faceMatch in response['FaceMatches']:
            result  = faceMatch['Similarity']
            
        imageSource.close()
        imageTarget.close()
        print(result)
    except:
        print(0)


      
