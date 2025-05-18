import torch
from diffusers import StableDiffusionPipeline
import os

def generate_image(prompt, output_path="output/generated_image.png", guidance_scale=3.0, num_inference_steps=10):
    model_id = "stabilityai/sd-turbo"

    # Detect device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    # Load pipeline (without safety checker for speed)
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=dtype,
        
    )
    pipe = pipe.to(device)

    # Enable memory-efficient attention (if available and using GPU)
    if device == "cuda":
        pipe.enable_xformers_memory_efficient_attention()

    # Generate image
    result = pipe(prompt=prompt, guidance_scale=guidance_scale, num_inference_steps=num_inference_steps)
    image = result.images[0]

    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    print(f"✅ Image saved at {output_path}")

if __name__ == "__main__":
    prompt = input("Enter a prompt for image generation: ")
    generate_image(prompt)

