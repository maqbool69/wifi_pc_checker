
# time.sleep(3)
# # Use easyocr to extract text from the image
# reader = easyocr.Reader(['en'])  # You can specify the language(s) you want to use
# results = reader.readtext("screenshot.png")

# # Function to extract integers from a string
# def extract_integers(text):
#     integers = []
#     for word in text.split():
#         try:
#             integer = int(word)
#             integers.append(integer)
#         except ValueError:
#             pass
#     return integers

# # Extract and print the detected integers
# detected_text = ' '.join([result[1] for result in results])
# integers = extract_integers(detected_text)

# if integers:
#     print("Detected integers in the screenshot:")
#     for integer in integers:
#         print(integer)
# else:
#     print("No integers detected in the screenshot.")
