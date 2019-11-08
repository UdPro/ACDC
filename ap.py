from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/order', methods = ['GET'])
def order():
    k = [{"Order_id":"1","Product_name":"headphone","Product_Code":"123","Product_Type":"electronic","Status":"dispatch"},{"Order_id":"2","Product_name":"watch","Product_Code":"124","Product_Type":"electronic","Status":"cancel"},{"Order_id":"3","Product_name":"chair","Product_Code":"156","Product_Type":"stationary","Status":"in-process"},{"Order_id":"4","Product_name":"speaker","Product_Code":"1587","Product_Type":"electronic","Status":"dispatch"},{"Order_id":"5","Product_name":"chicken","Product_Code":"557","Product_Type":"Food","Status":"dispatch"},{"Order_id":"6","Product_name":"apple","Product_Code":"799","Product_Type":"food","Status":"cancel"},{"Order_id":"7","Product_name":"Book","Product_Code":"445","Product_Type":"stationary","Status":"in-process"},{"Order_id":"8","Product_name":"harddisk","Product_Code":"899","Product_Type":"electronic","Status":"dispatch"},{"Order_id":"9","Product_name":"shoes","Product_Code":"777","Product_Type":"cloth","Status":"cancel"},{"Order_id":"10","Product_name":"watch","Product_Code":"124","Product_Type":"electronic","Status":"cancel"},{"Order_id":"11","Product_name":"chair","Product_Code":"156","Product_Type":"stationary","Status":"in-process"},{"Order_id":"12","Product_name":"speaker","Product_Code":"1587","Product_Type":"electronic","Status":"dispatch"},{"Order_id":"13","Product_name":"chicken","Product_Code":"557","Product_Type":"Food","Status":"dispatch"},{"Order_id":"14","Product_name":"apple","Product_Code":"799","Product_Type":"food","Status":"cancel"},{"Order_id":"15","Product_name":"Book","Product_Code":"445","Product_Type":"stationary","Status":"in-process"},{"Order_id":"16","Product_name":"harddisk","Product_Code":"899","Product_Type":"electronic","Status":"dispatch"},{"Order_id":"17","Product_name":"shoes","Product_Code":"777","Product_Type":"cloth","Status":"cancel"}]
    return jsonify({'order': k})

if __name__ ==  '__main__':
    app.run(debug = True)

