import random # used to generate random questions for each player/ or shuffling
import datetime # used to store score date and time
import time # used for time count
import os
from quiz_data import questions # to import from separate file

TOP_SCORES_FILE = "top_scores.txt" # creates file to save score

# fun to load questions
def load_questions(category:str) ->list:
    #get dic for selected category
    selected_cata = questions[category]
    # to store the selected questions
    final_questions =[]
    #loop over difficulty levels
    for level in ["easy","medium","hard"]:

        question_list = selected_cata[level][:]# to loop over difficulty levels
        random.shuffle(question_list)# for random shuffles
        final_questions += question_list[:2]  # 2 per level
    random.shuffle(final_questions ) # to repeat shuffles

    return final_questions  # returns questions in the selected category shuffled with difficulty level


def check_answer(user_answer: str,correct_answer: str) -> bool:

# returns true if the answer is correct
            return user_answer.strip().lower() ==  correct_answer.strip().lower()


def calculate_score(correct: bool,time_taken_to_answer: float) -> int:

    base = 10 if correct else 0 # 10 points if correct or 0 if incorrect
    if correct:
        if time_taken_to_answer <=5:
            return base+5  # fast bonus
        elif time_taken_to_answer > 10:
            return base-5  # slow penalty
    return base# base is returned if no time adjustment applies



def save_scores(player_scores: dict,category: str,start: str,end: str):

    # try block for if file write fails
    try:
        with open(TOP_SCORES_FILE, "a") as f:
            f.write(f"\n=== Game Session: {start} to {end} ===\n")
            f.write(f"Category: {category.title()}\n")
            for name, score in player_scores.items():
                f.write(f"{name}: {score} points\n")
    except IOError as e:
        print(f"Error saving scores.")


  # to display results in the terminal
def display_reults(player_scores: dict):

    print("\n======== Final Rankings ========")
    ranked =sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(ranked, 1):# enumerates with rank number
        print(f"{i}. {name} - {score} pts")



def main():
    print('======== Ultimate Quiz Showdown =======')

    # validate category
    valid_categories =list(questions.keys())
    while True:
        # ask the user to choice a category
        category =input(f"Choose a category {valid_categories}: ").strip().lower()
        if category in valid_categories:
            break
        print("Invalid category. Try again.")

    # validate number of players
    while True:

        num_input =input("How many players? ").strip()
        if num_input.isdigit():
            number_players = int(num_input)
            if number_players >= 1:
                break
        print("Please enter a valid number.")

    player_scores = {}
    start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # loop through each player
    for i in range(number_players):
        while True:
            name =input(f"Enter name for Player {i + 1}:").strip()
            if name and not name.isdigit():
                break
            print("Name must not be empty or numeric.")

        score =0 # initialize score for each player

        # load the questions for each player
        questions_list =load_questions(category)

        # loops through each questions
        for q in questions_list:

            print(f"\n{name}, Question: {q['question']}")
            t1 =time.time()
            user_ans = input('Your answer: ')
            t2 =time.time()
            time_taken =t2 - t1

            is_correct = check_answer(user_ans, q["answer"])
            points = calculate_score(is_correct, time_taken)
            score += points

            print("✅ Nice!" if is_correct else f"❌ Oops... answer was {q['answer']}")
            print(f"Time: {int(time_taken)}s | Points: {points}")
        #to save players score
        player_scores[name] = score
    # score documenting for time, score and save results to file
    end_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_scores(player_scores,category,start_time,end_time)
    display_reults(player_scores)


# main to run the script
if __name__ == "__main__":
    main()