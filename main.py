from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configuration
DEBUG = True  # Enable debugging for development

# Route for the home page
@app.route('/')
def home():
    """
    Renders the home page with links to the three systems.
    """
    return render_template('index.html')

# Route for the Crop Monitoring System
@app.route('/crop_monitoring')
def crop_monitoring():
    """
    Renders the Crop Monitoring System page.
    Simulates fetching data from sensors and weather API.
    """
    # In a real application, you would fetch data from sensors and APIs
    sensor_data = {
        'temperature': 25,
        'humidity': 60,
        'soil_moisture': 70
    }
    weather_forecast = {
        'temperature': 28,
        'condition': 'Sunny',
        'wind_speed': 10
    }
    pest_alerts = [
        {'type': 'Aphids', 'severity': 'Low', 'location': 'Field 1'},
        {'type': 'Spider Mites', 'severity': 'Medium', 'location': 'Field 2'}
    ]
    crop_health = {
        'ndvi': 0.85,
        'growth_stage': 'Flowering'
    }

    return render_template(
        'crop_monitoring.html',
        sensor_data=sensor_data,
        weather_forecast=weather_forecast,
        pest_alerts=pest_alerts,
        crop_health=crop_health
    )

# Route for the Livestock Management System
@app.route('/livestock_management')
def livestock_management():
    """
    Renders the Livestock Management System page.
    Simulates fetching data about livestock.
    """
    # In a real application, you would fetch data from a database or API
    livestock_data = [
        {
            'id': '12345',
            'type': 'Cow',
            'breed': 'Holstein',
            'health_status': 'Healthy',
            'last_checkup': '2024-01-15',
            'breeding_status': 'Open',
            'productivity': {'milk_yield': 25, 'weight': 550}
        },
        {
            'id': '67890',
            'type': 'Cow',
            'breed': 'Jersey',
            'health_status': 'Healthy',
            'last_checkup': '2024-02-20',
            'breeding_status': 'Pregnant',
            'productivity': {'milk_yield': 20, 'weight': 500}
        },
        {
            'id': '24680',
            'type': 'Sheep',
            'breed': 'Dorper',
            'health_status': 'Healthy',
            'last_checkup': '2024-03-10',
            'breeding_status': 'Not Bred',
            'productivity': {'wool_yield': 5, 'weight': 70}
        }
    ]
    return render_template('livestock_management.html', livestock_data=livestock_data)

# Route for the Agri-Inputs Marketplace
@app.route('/agri_marketplace')
def agri_marketplace():
    """
    Renders the Agri-Inputs Marketplace page.
    Simulates fetching data about products.
    """
    # In a real application, you would fetch data from a database
    products = [
        {
            'id': 'S101',
            'name': 'Hybrid Corn Seeds',
            'category': 'Seeds',
            'price': 150,
            'unit': 'kg',
            'description': 'High-yield hybrid corn seeds',
            'supplier': 'ABC Seed Company',
            'reviews': [
                {'user': 'Farmer John', 'rating': 5, 'comment': 'Excellent seeds!'},
                {'user': 'Farmer Jane', 'rating': 4, 'comment': 'Good germination rate.'}
            ]
        },
        {
            'id': 'F202',
            'name': 'Nitrogen Fertilizer',
            'category': 'Fertilizers',
            'price': 50,
            'unit': 'bag',
            'description': 'High-quality nitrogen fertilizer',
            'supplier': 'XYZ Chemicals',
            'reviews': [
                {'user': 'Farmer Peter', 'rating': 4, 'comment': 'Good product, fast delivery.'},
                {'user': 'Farmer Paul', 'rating': 3, 'comment': 'Slightly expensive.'}
            ]
        },
        {
            'id': 'P303',
            'name': 'Pesticide X',
            'category': 'Pesticides',
            'price': 75,
            'unit': 'liter',
            'description': 'Effective pesticide for broad-spectrum control',
            'supplier': 'Green Agro Solutions',
            'reviews': [
                {'user': 'Farmer Mary', 'rating': 5, 'comment': 'Very effective against pests.'},
                {'user': 'Farmer Mike', 'rating': 4, 'comment': 'Easy to use.'}
            ]
        },
        {
            'id': 'E404',
            'name': 'Tractor Model T100',
            'category': 'Equipment',
            'price': 10000,
            'unit': 'unit',
            'description': 'Powerful tractor for all farming needs',
            'supplier': 'Best Tractors Ltd.',
            'reviews': [
                {'user': 'Farmer David', 'rating': 5, 'comment': 'Excellent tractor, very reliable'},
                {'user': 'Farmer Sarah', 'rating': 4, 'comment': 'Good value for money'}
            ]
        }
    ]
    return render_template('agri_marketplace.html', products=products)

if __name__ == '__main__':
    app.run(debug=DEBUG)
