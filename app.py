from flask import Flask,render_template,request
import requests
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def hello():
  city="chennai"
  if request.method=='POST':
      new_city=request.form.get('city')
      if new_city:
        city=new_city
      print(new_city)
  url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=3469353e1730342fbef91d916b38c6da'
  r=requests.get(url.format(city)).json()
  weather={
      'city':city,
      'temp': round(r['main']['temp']-273.15,2),
      'description':  r['weather'][0]['description'],
      'icon': r['weather'][0]['icon']
    }
  print(weather)
  return render_template("home.html",weather=weather)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)