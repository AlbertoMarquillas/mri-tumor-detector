import streamlit as st
import numpy as np
from PIL import Image

# Detectron2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2 import model_zoo

from util import visualize  # set_background is optional

st.set_page_config(page_title="MRI Tumor Detection", layout="centered")
st.title("Brain MRI Tumor Detection")
st.write("Upload an MRI image to run object detection with a RetinaNet model (Detectron2).")

# File upload
file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Threshold slider
score_threshold = st.slider("Detection threshold", min_value=0.10, max_value=0.95, value=0.50, step=0.05)

# Load config & model
@st.cache_resource
def load_predictor(thr: float):
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/retinanet_R_101_FPN_3x.yaml"))
    # NOTE: place your trained weights in models/model.pth (ignored by git by default)
    cfg.MODEL.WEIGHTS = "models/model.pth"
    cfg.MODEL.DEVICE = "cpu"
    cfg.MODEL.RETINANET.SCORE_THRESH_TEST = thr
    return DefaultPredictor(cfg)

predictor = load_predictor(score_threshold)

# Inference
if file is not None:
    image = Image.open(file).convert("RGB")
    image_array = np.asarray(image)

    outputs = predictor(image_array)
    instances = outputs["instances"].to("cpu")

    preds = instances.pred_classes.tolist() if instances.has("pred_classes") else []
    scores = instances.scores.tolist() if instances.has("scores") else []
    bboxes = instances.pred_boxes if instances.has("pred_boxes") else []

    # Filter by threshold (redundant if we set SCORE_THRESH_TEST, but kept for safety)
    bboxes_ = []
    for j, box in enumerate(bboxes):
        score = scores[j]
        if score >= score_threshold:
            x1, y1, x2, y2 = [int(v) for v in box.tolist()]
            bboxes_.append([x1, y1, x2, y2])

    visualize(image, bboxes_)
else:
    st.info("Choose an image file to start.")
