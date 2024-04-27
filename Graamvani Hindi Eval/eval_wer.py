import jiwer
import argparse

def calculate_wer(ground_truth_file, predictions_file):
    # Read the ground truth and predictions
    with open(ground_truth_file, 'r', encoding='utf-8') as f:
        ground_truth = f.readlines()

    with open(predictions_file, 'r', encoding='utf-8') as f:
        predictions = f.readlines()

    # Check if the number of lines in both files are equal
    if len(ground_truth) != len(predictions):
        raise ValueError("The number of lines in ground truth and predictions files are not equal.")

    # Extract the transcripts from the files
    ground_truth_transcripts = [line.strip() for line in ground_truth]
    predicted_transcripts = [line.strip() for line in predictions]

    # Calculate the WER
    wer = jiwer.wer(ground_truth_transcripts, predicted_transcripts)

    print(f'The WER is {wer} for the ground_truth_transcripts against predicted_transcripts')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Word Error Rate (WER)")
    parser.add_argument("--ground_truth_file", type=str, help="Path to the ground truth file")
    parser.add_argument("--predictions_file", type=str, help="Path to the predictions file")

    args = parser.parse_args()

    wer = calculate_wer(args.ground_truth_file, args.predictions_file)
