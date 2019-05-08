# class4-homework

Instructions for building and running the Dockerfile:
A. Building the Dockerfile into an image:
- In the terminal, make sure to change your directory to the one containing the Dockerfile, as well as the other required files.
- In the command line type: docker build --tag="your_image_name"
- The "your_image_name" can be anything, but should ideally be named according to what the image does.

B. Running the image you built
- In the command line type: docker run your_image_name
substituting in the name to the image you gave when building in step A



Continuous Integration:
Continuous integregation is the process of automating the build and testing of code every time a change is committed to the original version of the code. First it should make sure that the code compiles, then ensures that it works as designed. This is a very useful took for GitHub, as every time a change is commited by a team member the continuous integration checks to make sure nothing is wrong. If you did not have continuous integration implemented, you may commit many changes, only to go through every line to debug later on. 
