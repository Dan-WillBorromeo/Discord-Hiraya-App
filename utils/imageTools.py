from PIL import Image
import os

def mergeImagesHorizontal (imagePaths, outputPath="merged.png"):
    images = [Image.open(path) for path in imagePaths]

    maxHeight = max(img.height for img in images)
    resized = []

    for img in images:
        ratio = maxHeight / img.height
        newWidth = int(img.width * ratio)
        
        resized.append(img.resize((newWidth, maxHeight)))

    totalWidth = sum(img.width for img in resized)

    merged = Image.new("RGBA", (totalWidth, maxHeight))

    x=0
    for img in resized:
        merged.paste(img, (x, 0))
        x+=img.width
    
    merged.save(outputPath)
    return outputPath