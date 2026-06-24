import sys
import time
from recommender import get_all_genres, recommend_movies

def print_separator():
    print("-" * 50)

def main():
    print_separator()
    print("Welcome to the AI Movie Recommender System!")
    print("This system uses pattern matching and Jaccard Similarity to recommend movies.")
    print_separator()
    
    available_genres = get_all_genres()
    print("\nAvailable Genres:")
    print(", ".join(available_genres))
    print()
    
    # Get user input
    print("Enter your favorite genres from the list above.")
    print("You can enter multiple genres separated by commas (e.g., Action, Sci-Fi).")
    print("Type 'quit' or 'exit' at any time to leave.")
    
    while True:
        user_input = input("\nYour genres: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("Thank you for using the AI Movie Recommender! Goodbye.")
            break
            
        if not user_input:
            print("Please enter at least one genre.")
            continue
            
        # Parse user input
        user_genres = [g.strip() for g in user_input.split(',')]
        
        print("\nAnalyzing your preferences and calculating matches...")
        time.sleep(1) # Add a slight delay to simulate processing
        
        # Get recommendations
        recommendations = recommend_movies(user_genres, top_n=5)
        
        if not recommendations:
            print(f"Sorry, we couldn't find any movies matching the genres: {', '.join(user_genres)}")
            print("Try different genres from the available list.")
            continue
            
        print("\nHere are your top recommended movies:")
        print_separator()
        for i, (movie, score) in enumerate(recommendations, 1):
            title = movie['title']
            genres_str = ", ".join(movie['genres'])
            match_percentage = round(score * 100)
            print(f"{i}. {title} ({match_percentage}% match)")
            print(f"   Genres: {genres_str}")
        print_separator()
        
        print("\nWould you like another recommendation?")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting program...")
        sys.exit(0)
