class CharCounter:

    def __init__(self, input_string):
        self.input_string = input_string
        self.appearances_dict = {}

    def count_appearances(self):
        for char in self.input_string:
            if char in self.appearances_dict:
                self.appearances_dict[char] += 1
            else:
                self.appearances_dict[char] = 1

    def get_result(self):
        return self.appearances_dict

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    counter = CharCounter(user_input)
    counter.count_appearances()
    result = counter.get_result()
    print("Appearance count of each character:")
    print(result)
