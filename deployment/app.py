from fastai.vision.all import *
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

model = load_learner('cap-recognizer-v2.pkl')

cap_labels = model.dls.vocab

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(cap_labels, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'unknown00.png',
    'unknown01.png',
    'unknown02.png',
    'unknown03.png'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)