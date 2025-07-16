import re
class WordToValue:
    def __init__(self):
        # Define the character set with their index values
        self.characters = "abcdefghijklmnopqrstuvwxyz.,?/-!"
        self.char_list = list(self.characters)

    def is_string(self, word):
        # Check if the input is a string
        return isinstance(word, str)

    def str_value(self, word):
        # Calculate the sum of character indices in the word
        total = 0
        word = word.lower()
        for ch in word:
            if ch in self.char_list:
                total += self.char_list.index(ch)
        return total
    
    def main(self, word):
        # Process the word if it's a string
        if self.is_string(word):
            return self.str_value(word)
        else:
            print("Input is not a string.")
WordClass = WordToValue()
class FileHandler:
    def __init__(self):
        pass

    def read_file(self, filename):
        # Read file contents
        try:
            with open(filename, "r", encoding='utf-8') as file:
                print(f"Successfully opened {filename}")
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return None
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            return None

    def append_to_file(self, filename, data):
        # Append data to a file
        try:
            with open(filename, "a", encoding='utf-8') as file:
                file.write(data + "\n")
            print(f"Successfully appended to {filename}")
        except Exception as e:
            print(f"Error appending to {filename}: {e}")

    def overwrite_file(self, filename, data):
        # Overwrite the entire file with data
        try:
            with open(filename, "w", encoding='utf-8') as file:
                file.write(data)
            print(f"Successfully overwritten {filename}")
        except Exception as e:
            print(f"Error overwriting {filename}: {e}")

    def extract_sentences(self, filename):
        # Extract sentences from file content using regex for better splitting
        content = self.read_file(filename)
        if content is None:
            return []

        try:
            # Split on period, question mark, or exclamation mark
            sentences = re.split(r'[.?!]', content)
            # Remove leading/trailing whitespace and filter out empty strings
            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
            print("Successfully extracted sentences")
            return sentences
        except Exception as e:
            print(f"Error extracting sentences: {e}")
            return []

    def transport_sentences(self, source_filename, target_filename): # from first to second
        # Transfer sentences from source file to target file
        sentences = self.extract_sentences(source_filename)
        if not sentences:
            print("No sentences to transport.")
            return

        # Clear target file before appending
        self.overwrite_file(target_filename, "")

        for sentence in sentences:
            self.append_to_file(target_filename, sentence)

FHC = FileHandler()
# new idea make a sentence counter to identify sentences and then analyse large data to try and find similar counts 
# lets add to a file word : value 

class DataPairing:
    def __init__(self):
        pass

    def percents(self, total, part):
        return (part / total) * 100 if total != 0 else 0

    def tuple(self, x, y):
        return (x, y)

    def tuple_pairing(self, data):
        paired_tuples = []
        try:
            for x in range(len(data) - 1):
                paired_tuples.append(self.tuple(data[x], data[x + 1]))
            return paired_tuples
        except TypeError:
            print("Error: data should be a list of numbers.")
            return []
        
ToupleClass = DataPairing()

class PredictNext():
    def __init__(self, data):
        self.data = data
        self.storage = []  # Will hold paired tuples
        self.inst = {}     # Dictionary to count occurrences of tuples

    def GetTouples(self):
        # Pair the data and store in self.storage
        self.storage = ToupleClass.tuple_pairing(self.data)
        return True

    def instance_count(self):
        # Ensure tuples are paired before counting
        if not self.storage:
            if not self.GetTouples():
                print("Failed to pair data.")
                return False

        # Count the occurrences of each tuple
        self.inst = {}  # Reset counts
        for touple in self.storage:
            if touple in self.inst:
                self.inst[touple] += 1
            else:
                self.inst[touple] = 1
        return True

    def predictionn(self, value):
        # Count tuples if not already counted
        if not self.inst:
            if not self.instance_count():
                return None  # Failed to count

        # Find the tuple with the highest count where the first element matches 'value'
        filtered = {k: v for k, v in self.inst.items() if k[0] == value}
        if not filtered:
            print(f"No tuples starting with {value}")
            return None

        # Find the tuple with the maximum count
        max_tuple = max(filtered.items(), key=lambda item: item[1])[0]
        # Return the second element of the tuple as the predicted next value
        return max_tuple[1]
