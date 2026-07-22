from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    description='A package for detecting emotions from text using Watson NLP Library',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
    ],
    python_requires='>=3.6',
)