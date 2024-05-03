import os
from PIL import Image

if __name__ == '__main__':
    print('Running BatchThumbnailGenerator.py')
    # Paths for input and output directories
    input_dir = 'images'
    output_dir = 'new_images'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # get list of all images in the directory
    image_files = [file for file in os.listdir(input_dir) if file.endswith(('.jpg', '.png', '.jpeg'))] 

    print(f'Found {len(image_files)} images to process in the directory.')

    # loop through all images and process each 
    for i, image_file in enumerate(image_files):
        print(f'Processing image {i+1}: {image_file}')
        
        # open image
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path) 
        
        # convert from jpg to png
        image = image.convert('RGB')

        # crop edges to square
        width, height = image.size
        size = min(width, height)
        left = (width - size) / 2
        top = (height - size) / 2
        right = left + size
        bottom = top + size
        image = image.crop((left, top, right, bottom))

        #rotate image
        image = image.rotate(-90)

        #resize image to 75x75 pixels
        image = image.resize((75, 75))  

        #convert to grayscale
        image = image.convert('L')

        #save image with a new filename
        new_filename = f'pic{i:04d}.png'
        new_image_path = os.path.join(output_dir, new_filename)
        image.save(new_image_path)

        print(f'Process {image_file} and saved as {new_filename}')
            
    print(f'Processed {image_file}')
    
print('Image processing complete.')
