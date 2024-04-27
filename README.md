# whisper_hindi

This repository contains the implementation of Whisper-Large ASR model on the Gramvaani and Kathbath dataset for evaluation

- The scripts for running the evaluation for the datasets are present here :

> Kathbath [here](https://github.com/nerdlab53/whisper_hindi/tree/main/Kathbath%20Hindi%20Eval)

> Gramvaani [here](https://github.com/nerdlab53/whisper_hindi/tree/main/Graamvani%20Hindi%20Eval)


## The model used for the evaluation purposes is the Whisper-Large by OpenAI
> ![whisper-large](assets/whisper-large.png)


## Times taken to evaluate on the datasets : 

| Dataset        | Time Taken for evaluation           | Overall WER |
|:--------------:|:-----------------------------------:|:-----------:| 
| Kathbath       | ~4.5 hours                          |0.2971       |
| Gramvaani      | ~2 hours                            |0.5017       | 

## Specs used for evaluation (Kaggle basic): 

> RAM : 30GB

> GPUs : T4x2
