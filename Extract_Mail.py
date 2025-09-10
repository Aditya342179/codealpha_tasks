import re

def extract_emails(input_file, output_file):
    # Regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        with open(input_file, 'r') as file:
            text = file.read()

        # Find all email addresses using regex
        emails = re.findall(email_pattern, text)

        if emails:
            # Remove duplicates by converting to a set
            unique_emails = sorted(set(emails))

            with open(output_file, 'w') as file:
                for email in unique_emails:
                    file.write(email + '\n')

            print(f"Extracted {len(unique_emails)} unique email(s) to '{output_file}'.")
        else:
            print("No email addresses found in the input file.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_path = input("Enter the path to the input .txt file: ")
    output_path = input("Enter the path for the output file to save emails: ")
    extract_emails(input_path, output_path)