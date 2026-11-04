from pathlib import Path
import sys

# Load the local client even when Python skips the editable install's .pth file.
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))

from gr_tradinggame.coding.client import Client
from solution import play

client = Client('YourTeamName', password='YourPassword')
client.test(play)
