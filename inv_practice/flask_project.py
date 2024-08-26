from flask import Flask,request,jsonify
import psycopg2

app=Flask(__name__)

db_params={
    'host': 'your_host',
    'port': 'your_port',
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password'
}

def get_db_connection():
    conn=psycopg2.connect(**db_params)

@app.route('/users',methods=['GET'])
def get_users():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("select * from users")
    users=curr.fetchall()
    cur.close()
    conn.close()
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    name = new_user.get('name')
    email = new_user.get('email')

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": "User created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)