# Artificial Face Generator

A simple way to generate an artificial human face. This Daisi calls an api to get the image data from server and returns in image format.


## Requirements

Well You can directly run this Daisi on platform and even run it manually into pc in stream mode as well as directly.
This Daisi requires python3 installed on pc with added into path. Next you require to install these python libraries thispersondoesnotexist , pillow and streamlit(optional to use web interface)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python libraries
```bash
pip install pydaisi thispersondoesnotexist pillow streamlit
```

Clone the repository for manual usage
```bash
git clone https://github.com/localhost-server/Fake-Face-Generator.git
```

## Calling the Daisi using Pydaisi in python/ipython

Import the PyDaisi module
```bash
import pydaisi as pyd
```

Call the Daisi inside a variable
```bash
afg = pyd.Daisi("kali/Artificial Face Generator")
```

To generate an image
```bash
img = a.aFace().value
```

To save the image
```bash
img.save('name_of_image')
```

To see the saved image
```bash
img.show()
```

To see an image without saving
```
a.aFace().value.show()
```

## Calling the Daisi manually

Get into Fake-Face-Generator dir
```bash
cd Fake-Face-Generator
```

Run as web-stream mode
```bash
streamlit run FakeFaceGenerator.py
```

Run using command prompt 
```bash
python/ipython
```

Import the Daisi
```bash
import FakeFaceGenerator as f
```

To save the image
```bash
f.saveImage("name_of_image")
```

To open the saved image
```bash
f.showimage()
```

To display as new image
```bash
f.aFace().show()
```

## Running the Daisi App

You can also do this by [Running the Daisi App](https://app.daisi.io/daisies/kali/Artificial%20Face%20Generator/app)

You can check the GitHub repository [Here](https://github.com/localhost-server/Fake-Face-Generator)

## References

[Try out more cool stuff here](https://thisxdoesnotexist.com/)

