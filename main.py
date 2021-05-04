# Import the required module
import json,requests

city_name = 'london'
units = 'metric'
api_key = '#'

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={api_key}"

def main_function():
    '''This function is used to convert json data to pyhton dictionary'''
    try:

        r = requests.get(url)
        r.raise_for_status
        
        # load the json data
        with open('Weatherdata.json','w') as f:
            source = r.json()
            f.write(json.dumps(source,indent=2))

        # make python dictionary
        with open('Weatherdata.json','r') as f:
            python_data = json.load(f)

        # desired results
        def weather_data(): 
            '''This function is responsible to print the weather info'''   
            print(f'Getting the weather info of --> {city_name} 🌇')

            print(f"1. {python_data['weather'][0]['description']} ")
            print(f"2. Minimum Temp --> {python_data['main']['temp_min']} degree celcius 🌡️")
            print(f"3. Maximum Temp --> {python_data['main']['temp_max']} degree celcius 🌡️")
            print(f"4. Feels Like --> {python_data['main']['temp']} degree celcius 🌡️")
            print(f"5. Wind Speed --> {python_data['wind']['speed']} kilometer per hour 🌬️")
            print(f"6. Humidity --> {python_data['main']['humidity']} ")

        weather_data()   


    except Exception as e:
        print("Something Went Wrong 💢 ",e)



if __name__ == "__main__":

    main_function()
    print("Code Completed 🔥")