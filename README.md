# MRI Tumor Detector

![Language](https://img.shields.io/badge/language-Python-blue)
![Framework](https://img.shields.io/badge/framework-Streamlit-red)
![Model](https://img.shields.io/badge/model-Detectron2-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Release](https://img.shields.io/github/v/release/AlbertoMarquillas/mri-tumor-detector)
![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow)

---

## 📌 Overview

The **MRI Tumor Detector** is an interactive **web application** built with **Streamlit** that allows users to upload brain MRI images and automatically detect tumors using an object detection model from **Detectron2**. The system demonstrates the integration of deep learning (PyTorch + Detectron2) with a user-friendly interface for medical imaging workflows.

This project originated as part of a computer vision exploration but has been fully reorganized into a **professional portfolio repository**.

---

## 📂 Repository Structure

```
<repo>/
├─ src/                     # Source code (Streamlit app + utilities)
│  ├─ main.py               # Streamlit entrypoint
│  └─ util.py               # Visualization and background utilities
├─ models/                  # Model weights (ignored in .gitignore)
│  └─ model.pth (not included)
├─ data/                    # Dataset placeholder (not included)
│  └─ README.md             # Instructions on how to obtain dataset
├─ docs/                    # Documentation and assets
│  └─ assets/               # Figures, plots, screenshots
├─ test/                    # Placeholder for tests
├─ build/                   # Temporary outputs (ignored)
├─ requirements.txt         # Dependencies
└─ README.md                # Project documentation
```

---

## ⚙️ Installation

Ensure you have **Python 3.9+** and a working **PyTorch** environment (CPU or GPU). Clone the repository and install the dependencies:

```powershell
git clone https://github.com/AlbertoMarquillas/mri-tumor-detector.git
cd mri-tumor-detector
pip install -r requirements.txt
```

If you are running in a headless environment (no GUI), replace `opencv-python` with `opencv-python-headless` in `requirements.txt`.

---

## 🚀 Usage

1. Place your trained weights at `models/model.pth`. By default, the code expects a RetinaNet model from Detectron2.
2. Launch the Streamlit app:

```powershell
streamlit run src/main.py
```

3. Open the local URL (usually `http://localhost:8501/`).
4. Upload an MRI image (`.png`, `.jpg`, `.jpeg`).
5. Adjust the detection threshold with the slider and view the bounding boxes overlayed on the image.

---

## 📊 Dataset

The dataset is not included in this repository due to size constraints. The expected structure inside `data/` is:

```
data/
├─ train/
├─ test/
└─ data.yaml
```

This dataset was exported from **Roboflow**. You can re-download it from your Roboflow project dashboard or use your own dataset following the same YOLO-style structure.

More details are available in `data/README.md`.

---

## 🔍 Features

* **Streamlit WebApp** for interactive inference.
* **Detectron2 (RetinaNet)** backbone for object detection.
* Adjustable detection **score threshold**.
* Bounding box visualization with **Plotly**.
* Support for multiple image formats (`.png`, `.jpg`, `.jpeg`).
* Modular structure (`src/` for code, `models/` for weights, `data/` for datasets).

---

## 📚 What I Learned

Through this project I gained experience in:

* Integrating **deep learning models** with a web-based interface.
* Using **Streamlit** to rapidly prototype ML applications.
* Working with **Detectron2** (configuration, inference, thresholds).
* Organizing repositories for reproducibility and professional presentation.
* Managing datasets and model weights responsibly in public repos.

---

## 📜 License

This project is released under the [MIT License](LICENSE).
