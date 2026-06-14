import os
import re

base_dir = r"F:\Resilio\AIGC\Projects\0613Paper\website"
presentation_dir = os.path.join(base_dir, "presentations")

# Create presentations folder if not exists
os.makedirs(presentation_dir, exist_ok=True)

files_to_move = [
    "PP01_reveal.html",
    "PP02_reveal.html",
    "PP03_reveal.html",
    "PP02_Web3D_pptx_exact_reveal.html",
    "PP02_Web3D_original_animation.html"
]

# 1. Update paths and move presentation HTMLs
for filename in files_to_move:
    src_path = os.path.join(base_dir, filename)
    dest_path = os.path.join(presentation_dir, filename)
    
    if not os.path.exists(src_path):
        print(f"Skipping {filename}: file not found in root.")
        continue
        
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace references to make them go one level up
    # reveal.js
    content = content.replace('href="reveal.js/', 'href="../reveal.js/')
    content = content.replace('src="reveal.js/', 'src="../reveal.js/')
    content = content.replace("href='reveal.js/", "href='../reveal.js/")
    content = content.replace("src='reveal.js/", "src='../reveal.js/")
    
    # Analysis folders
    content = content.replace('src="PP02_Web3D_analysis/', 'src="../PP02_Web3D_analysis/')
    content = content.replace('src="PP03_analysis/', 'src="../PP03_analysis/')
    
    # Slide image folders
    content = content.replace('src="PP02_Web3D_exact_slides/', 'src="../PP02_Web3D_exact_slides/')
    
    # Video
    content = content.replace('src="PP02_Web3D_original_animation.mp4"', 'src="../PP02_Web3D_original_animation.mp4"')
    content = content.replace("src='PP02_Web3D_original_animation.mp4'", "src='../PP02_Web3D_original_animation.mp4'")
    
    # HTML folder subpages
    content = content.replace('src="HTML/', 'src="../HTML/')
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Remove the original file
    os.remove(src_path)
    print(f"Moved and updated: {filename} -> presentations/{filename}")

# 2. Update index.html to point to presentations/ folder
index_path = os.path.join(base_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    for filename in files_to_move:
        # Avoid double replacing
        index_content = index_content.replace(f'data-load="{filename}"', f'data-load="presentations/{filename}"')
        index_content = index_content.replace(f'href="{filename}"', f'href="presentations/{filename}"')
        
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Updated index.html references.")
else:
    print("index.html not found.")
