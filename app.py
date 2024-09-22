from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Helper function to filter numbers and alphabets
def filter_numbers_and_alphabets(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    return numbers, alphabets

# Helper function to get the highest lowercase alphabet
def highest_lowercase(alphabets):
    lowercases = [char for char in alphabets if char.islower()]
    if lowercases:
        return max(lowercases)
    return None

# Helper function to handle file validation
def validate_file(file_b64):
    if not file_b64:
        return False, None, None
    
    try:
        # Decode the base64 string to check validity
        file_data = base64.b64decode(file_b64)
        file_size_kb = len(file_data) / 1024  # Size in KB
        
        # Assuming the file is a PNG image if valid (simplification)
        mime_type = "image/png"
        return True, mime_type, round(file_size_kb, 2)
    except Exception:
        return False, None, None

# POST method: Route /bfhl
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Extract request data
        data = request.json.get("data", [])
        file_b64 = request.json.get("file_b64", None)

        # Hardcoded user information
        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"

        # Separate numbers and alphabets
        numbers, alphabets = filter_numbers_and_alphabets(data)

        # Get the highest lowercase alphabet
        highest_alpha = highest_lowercase(alphabets)

        # Validate file
        file_valid, file_mime_type, file_size_kb = validate_file(file_b64)

        # Response
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_alpha] if highest_alpha else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

# GET method: Route /bfhl
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == "__main__":
    app.run(debug=True)
