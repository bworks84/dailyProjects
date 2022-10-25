import urllib.request as urllib

# use urllib.request to get the data from the url
# write a function that takes a url and returns a response


def main(url):
    print("Checking connectivity ")

    response = urllib.urlopen(url)

    print("Connected to", url, " successfully")
    print("the response code was:", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the the site: ")

main(input_url)
