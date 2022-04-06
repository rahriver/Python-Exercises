user = input("Hey how's it going? ")
# we want to say as long as the user is not saying the magic word, do this.
while user != "stop copying me":
    print(user)
    user = input()
# The line below, will get executed when the while loop has been finished.
print("UGH FINE YOU WIN")
