import base64
import io
import joblib
import torch
import torch.nn.functional as F

from PIL import Image


mnist_model = joblib.load('main/utils/MNIST_model.pkl')


def preprocess_image(base64_encoded_image: str):
    image_bytes = io.BytesIO(base64.b64decode(base64_encoded_image.replace("data:image/jpeg;base64,", "")))

    image = Image.open(image_bytes).convert("L")
    image = image.resize((28, 28))
    pixel_map = list(map(lambda x: x / 255, [x for x in image.getdata()]))
    return torch.tensor(pixel_map)


def predict_mnist_model(pixel_map: torch.Tensor) -> tuple[int, list[str]]:
    outputs = mnist_model(pixel_map)
    probabilities = F.softmax(outputs, dim=1)
    _, preds = torch.max(probabilities, dim=1)

    probabilities = ["{} - {}%".format(idx, round(100 * item, 2)) for idx, item in enumerate(probabilities.tolist()[0])]

    return int(preds.item()), probabilities
