from PIL import Image
import numpy as np
import argparse
import os

def img_resizer(img, new_width=80):
    """
    Resize the image based on the new width
    """
    
    w, h = img.size
    
    assert w > new_width, "New width can't be greater than old width"
    
    ratio = h / w
    
    new_height = int(ratio * new_width)
    
    resized_img = img.resize((new_width, new_height))
    
    return resized_img

def img_to_ascii(img, ASCII, output=None):
    """
    Convert image to ASCII characters
    """
    
    ascii_img = []
    img_arr = np.array(img)
    
    for ind, i in enumerate(img_arr):
        ascii_img.append('')
        for j in i:
            indx = (j * (len(ASCII)-1)) // 255
            ascii_char = ASCII[indx]
            ascii_img[ind] += ascii_char
        ascii_img[ind] += '\n'
    
    if output:
        if os.path.isdir(output):
            output_path = os.path.join(output, 'Logorain-ASCII-Art.html')
        else:
            print(f"The output path: ''{output}'' doesn't exist: the file will be saved on your current folder")
            current_path = os.path.abspath(os.curdir)
            output_path = os.path.join(current_path, "Logorain-ASCII-Art.html")
            
        with open(output_path, 'w') as f:
            f.write('<span style="display:block;line-height:8px; font-size: 10px; font-weight:bold;white-space:pre;font-family: monospace;color: black; background: white;">\n')
            f.writelines(ascii_img)
            f.write('</span>')
    else:
        with open('Logorain-ASCII-Art.html', 'w') as f:
            f.write('<span style="display:block;line-height:8px; font-size: 10px; font-weight:bold;white-space:pre;font-family: monospace;color: black; background: white;">\n')
            f.writelines(ascii_img)
            f.write('</span>')


def get_args():
    Parser = argparse.ArgumentParser(description='Logorain-ASCII-Art is a simple ASCII Art maker that convert images to ASCII Art.')
    Parser.add_argument('-i', '--input', help='Define the image path on your local machine.', type=str, required=True)
    Parser.add_argument('-w', '--width', help='Define a width for the ASCII Art image', type=int, required=False)
    Parser.add_argument('-o', '--output', help='Define the output path', type=str, required=False)
    
    return Parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    ASCII = "@%#*+=-:. "
    try:
        img = Image.open(args.input).convert('L')
        
        if args.width:
            resized_img = img_resizer(img, new_width=args.width)
        else:
            resized_img = img_resizer(img, new_width=80)
        
        if args.output:
            img_to_ascii(resized_img, ASCII, args.output)
        else:
            img_to_ascii(resized_img, ASCII)
            
    except Exception as err:
        print(f"Error: {err}")
