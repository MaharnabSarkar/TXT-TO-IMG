# Text-to-Image Generation with Stable Diffusion

## Description
This project uses Hugging Face's `diffusers` library and Stable Diffusion to generate images from text prompts.

## Setup Instructions

1. **Clone or Extract the Project**
2. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Project**
   ```bash
   python main.py
   ```

## Notes
- Make sure you have a GPU or sufficient system memory for CPU inference.
- You can customize `guidance_scale` and `num_inference_steps` in `main.py`.
