import sys
import time

def show_developer_info():
    """Prints developer introduction and application overview."""
    print("=" * 60)
    print("DEVELOPER PROFILE & APPLICATION OVERVIEW")
    print("=" * 60)
    print("Developer       : Nguyễn Minh Tới")
    print("Role            : Lead Developer & Application Reviewer")
    print("Project Scope   : Central Hub for Android/Java Toolkits & Projects")
    print("Language        : English (Technical Standard)")
    print("-" * 60)
    print("OVERVIEW:")
    print("This application serves as an integrated project collection hub,")
    print("bringing together various Android and Java utilities, core systems,")
    print("and performance tools under a unified development workflow.")
    print("=" * 60)
    print("\n")

def calculate_typing_speed(sample_text: str):
    """Measures typing speed in Words Per Minute (WPM) and accuracy."""
    print("=== TYPING SPEED TEST (WPM) ===")
    print("\nSample Text:")
    print(f'"{sample_text}"\n')
    
    input("Press Enter when you are ready to start...")
    print("\nSTART TYPING!")
    
    start_time = time.time()
    user_input = input("> ")
    end_time = time.time()
    
    # Calculate elapsed time in seconds
    elapsed_time = end_time - start_time
    
    # Standard WPM calculation (1 word = 5 characters)
    words_typed = len(user_input) / 5
    wpm = (words_typed / elapsed_time) * 60 if elapsed_time > 0 else 0
    
    # Calculate accuracy percentage
    correct_chars = sum(1 for a, b in zip(user_input, sample_text) if a == b)
    total_chars = max(len(sample_text), len(user_input))
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

    print("\n" + "=" * 35)
    print("YOUR RESULTS:")
    print(f"- Time Taken : {elapsed_time:.2f} seconds")
    print(f"- Typing Speed: {wpm:.1f} WPM")
    print(f"- Accuracy    : {accuracy:.1f}%")
    print("=" * 35)

if __name__ == "__main__":
    show_developer_info()
    SAMPLE = "Python is a programming language that emphasizes code readability."
    calculate_typing_speed(SAMPLE)
    