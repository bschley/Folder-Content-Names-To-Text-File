import glob;


def main():
    filetype = "jpg"
    filename = "result.txt"
    newfilepath = "../images/"

    content = (glob.glob("images/*." + filetype))

    file = open(filename, "w")

    for a in content:
        src = a[7:]    # removes filepath in string
        alt = src[:-4] # removes the filetype (.jpg) for the alt)
        file.write('<img src="' + newfilepath + src + '" alt="' + alt + '">\n')

    file.close()


if __name__ == "__main__":
    main()
