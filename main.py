import requests
import csv

urlOfSizeUrls = 'https://www.freelancer.com/ajax/directory/getFreelancer.php?countries%5B%5D=Brazil'
currentlocation = 'Brazil'
try:
    # Make a GET request to the URL
    response = requests.get(urlOfSizeUrls)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data
        json_data = response.json()
        sizeOfUrls = round(json_data['count']/10)
        urls = []

        header = ['Name', 'Email', 'Reviews', 'hourlyrate']
        with open(currentlocation + '.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for i in range(sizeOfUrls):
                urls.append('https://www.freelancer.com/ajax/directory/getFreelancer.php?countries%5B%5D=Brazil&offset=' + str(i * 10))

                freelancerdata = requests.get(urls[i])
                print('part'+ str(i+1))
                if freelancerdata.status_code == 200:
                    json_freelancer = freelancerdata.json()

                    for result in (json_freelancer['users']):
                        
                        name = result['username']
                        email = result['username']
                        if 'no_reviews' in result:
                            reviews = result['no_reviews']
                        else:
                            reviews = -1
                        hourlyrate = result['hourlyrate']
                        
                        if 0 < reviews < 10:
                            data = [name, email + "@gmail.com", reviews, hourlyrate]
                            writer.writerow(data)
                            print('ok')
                        else:
                            continue
                else:
                    # Print an error message if the request was not successful
                    print(f"Error: {response.status_code}")
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
except Exception as e:
    # Handle any exceptions that may occur during the request
    print(f"An error occurred: {e}")
