def reverse(string):
    print(len(string))
    if string is not None and len(string) != 0:

        list_of_words = string.split(" ")
        for i in range(len(list_of_words)-1 , -1, -1):
            print(list_of_words[i],end=" ")
    else:
        print("Given String is empty")


# reverse("I am an Engineer")
reverse("  ")






