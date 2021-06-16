from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Webpage.html')

@app.route('/predict',methods=['POST'])
def predict():
       
    input_features = [x for x in request.form.values()]
    bath = input_features[0]
    balcony = input_features[1]
    total_sqft_int = input_features[2]
    bhk = input_features[3]
    price_per_sqft = input_features[4]
    area_type = input_features[5]
    availability = input_features[6]
    location = input_features[7]
    
    predicted_price = model.predict_house_price(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)       


    return render_template('Webpage.html', prediction_text='Predicted Price of Bangalore House is {}'.format(predicted_price))
    
if __name__ == "__main__":
    app.run()
    