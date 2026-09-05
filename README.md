# Donut Terminal Animation

A simple Python project that renders a rotating 3D donut in the terminal using ASCII characters. This is a visual experiment inspired by the classic "donut.c" program, built with Pygame for display.

## What It Does

This program creates a 3D donut shape and rotates it on your screen. Each frame of the animation uses math to calculate where every character should go. The result is a spinning, colorful representation of a donut made of letters and symbols.

The characters change based on depth and lighting, creating a pseudo-3D effect. Darker parts of the donut use symbols like . , - ~, while brighter parts use ! * # $ @.

## How It Works

The code uses a mathematical model to map a 3D donut onto a 2D screen. For each frame, it goes through every point on the donut, calculates its position in 3D space, applies rotation, and projects it onto the screen. The depth of each point determines what character gets displayed.

The rotation is controlled by two angles, A and B, which change slightly each frame. This creates the spinning effect.

## Running the Program

You will need Python and Pygame installed on your system. If you dont have Pygame, you can install it using pip.
