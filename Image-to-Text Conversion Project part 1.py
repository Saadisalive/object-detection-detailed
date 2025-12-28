import os
import warnings
import logging
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from colorama import init, Fore, Style


warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)
init(autoreset=True)

