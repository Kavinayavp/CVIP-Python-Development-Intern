import time

def typing_speed_test(text):
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)
    
    print("\nYou typed at a speed of {:.2f} words per minute.".format(words_per_minute))

if __name__ == "__main__":
    sample_text = "This is a sample text for typing speed test. Try to type it as quickly and accurately as possible."
    typing_speed_test(sample_text)

