print("👋 Hello, I'm Cee Bot 🤖")

# Ask the user's name
name = input("What's your name?\n")

# Greet and ask how they're feeling
print(f"Nice to meet you, {name}! 😊")
feeling = input("How are you feeling today?\n")

# Clean and simplify the feeling input
feeling = feeling.lower().replace("i'm ", "").replace("i am ", "").strip()

# Respond based on the user's emotion
if "happy" in feeling:
    print(f"That's wonderful to hear, {name}! Keep smiling! 😄")
elif "sad" in feeling:
    print(f"Oh no, {name}. I'm here for you. Things will get better soon. 💖")
elif "angry" in feeling:
    print(f"I understand, {name}. Take a deep breath. I'm sure you'll feel better soon. 😌")
else:
    print(f"Thank you for sharing, {name}. I'm always here to chat! 💬")

# Thank-you message
print("🙏 Thank you for chatting with me! Have a peaceful day! 🌸")
