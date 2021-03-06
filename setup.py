from setuptools import setup
import setuptools
setup(name='classification_pipeline',
      version='0.26',
      description='Declaraqtively configured pipeline for image segmentation',
      url='https://github.com/petrochenko-pavel-a/segmentation_training_pipeline',
      author='Petrochenko Pavel',
      author_email='petrochenko.pavel.a@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      include_package_data=True,
      dependency_links=['https://github.com/aleju/imgaug'],
      install_requires=["musket_core>=0.30"],
      zip_safe=False)