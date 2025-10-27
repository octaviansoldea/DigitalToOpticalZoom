import cv2

def super_resolve(input_path, output_path, model_path="EDSR_x3.pb", scale=3):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel("edsr", scale)

    img = cv2.imread(input_path)
    result = sr.upsample(img)
    cv2.imwrite(output_path, result)
    return output_path
