import logging


def save_review_to_file(review, output_path):
    """
    Writes the review content to the specified output file.
    """
    logging.debug(f"Saving review to {output_path}")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(review)
        logging.info(f"Successfully wrote review to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save review: {e}")
