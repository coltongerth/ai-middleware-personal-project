# ai-middleware-personal-project
A personal deep dive for getting a feel for developing api driven ai language models, I am pulling the distilbert-base-uncased-finetuned-sst-2-english model from huggingface to act as a AI blackbox model to interact with. This is not a study of fine-tuning the model, rather more of exploring and experimenting with developing an api structure to interact with the model to set up a system for a user to use it on a front end ui.


To run this project, first download the required libraries:

python -m pip install -r requirements.txt

Then run the following command in a commandline (bash, ubuntu, cmd, powershell, etc):

uvicorn src.main:app --reload

This will run the project locally, which you will be able to interact with on your web browser with the following url:

http://127.0.0.1:8000/

If you've made it this far, have fun playing with it, there's not much beef to it, but it's been a fun project to work on!