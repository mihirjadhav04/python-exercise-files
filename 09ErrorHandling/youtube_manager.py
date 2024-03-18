
import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file) # read the file data and load it into json format.
            print(test)
            return test
    except FileNotFoundError: 
        return [] 


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print("*" * 50)
    print("\n")

def add_youtube_video(videos):
    name = input("Enter your video name: ")
    time = input("Enter your video time: ")
    videos.append({'name' : name, 'time': time})
    save_data_helper(videos)

def update_youtube_video(videos):
    list_all_videos(videos)
    index = int(input("Please select the number of item you want to update: \t"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video name : ")
        videos[index-1] = {'name' : name, 'time' : time}
        save_data_helper(videos)
    else:
        print("Invalid Video Index Selected.")
        
def delete_youtube_video(videos):
    list_all_videos(videos)
    index = int(input("Please select the number of item you want to delete: \t"))
    
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else: 
        print("Invalid Video Index Selected.")


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: \t ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_youtube_video(videos)

            case '3':
                update_youtube_video(videos)

            case '4':
                delete_youtube_video(videos)
            
            case '5':
                break
                
            case _:
                print("Invalid Choice!")


# starting point of the file.
# dunder method - which tell that if we have main function present in the file then please run that - it's the starting point.

if __name__ == "__main__":
    main()