from . import panda
from .panda import WalkingPanda


import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--panda-scale", help="Resize Panda", type=float, default=0.005)
    parser.add_argument("--camera-distance", help="Set Camera Distance", type=float, default=20)
    parser.add_argument("--rotation-speed", help="Set Camera Rotation Speed", type=float, default=6)

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
