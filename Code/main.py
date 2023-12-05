import data_analysis
import literature_review
import predictive_analytics
import image_video_analysis
import task_automation
import advanced_stats_ml
import ethics_and_sentiment

def main_menu():
    print("AI-Driven Research Assistant")
    print("1. Data Analysis and Processing")
    print("2. Literature Review and Management")
    print("3. Predictive Analytics and Forecasting")
    print("4. Image and Video Analysis")
    print("5. Automation of Repetitive Tasks")
    print("6. Advanced Statistical Analysis and Machine Learning")
    print("7. Ethical and Bias Consideration")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            data_analysis.run()
        elif choice == "2":
            literature_review.run()
        elif choice == "3":
            predictive_analytics.run()
        elif choice == "4":
            image_video_analysis.run()
        elif choice == "5":
            task_automation.run()
        elif choice == "6":
            advanced_stats_ml.run()
        elif choice == "7":
            ethics_and_sentiment.run()
        elif choice == "0":
            print("Have a great day! Come back if you need further analysis.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
