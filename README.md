# image-to-ascii
Simple Python program that transforms an image to an ASCII equivalent using OpenCV.<br/> <br/>
![python_logo](https://github.com/GustavoHenriqueMuller/image-to-ascii/blob/main/examples/logo.png)<br/>
![python_logo_ascii](https://github.com/GustavoHenriqueMuller/image-to-ascii/blob/main/examples/logoASCII.png)

To install requirements:
`pip install requirements.txt`

To run:
`python main.py <image path> <scale>`

Where:
> `image path`: Path to image you want to convert to ASCII. Must be PNG, JPG, JPEG or GIF.<br/>
> `scale`: Positive non-zero float value that represents the scale of the image (e.g: scale of 0.25 will set the width/height to 0.25 * their original size).

(Recommended) Save your images on /images directory relative to main.py, because of .gitignore.
