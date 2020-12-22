from imageai.Detection import ObjectDetection
import os
import sys


def get_bus(images):
    execution_path = os.getcwd()
    buses_images=[]
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel() 
    range_of_images = range(0, len(images))

    for i in range_of_images:
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , images[i]), output_image_path=os.path.join(execution_path , "imagenew1"+str(i)+".jpg"))
        for eachObject in detections:
            if eachObject['name']=='bus':
                buses_images.append(images[i])

    return buses_images

    

        
            
