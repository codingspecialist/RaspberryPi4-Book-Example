import boto3
def detect_labels_local_file(photo):
    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
    return len(response['Labels'])
def main():
    photo='img/input.jpg' # filename
    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))
if __name__ == "__main__":
    main()