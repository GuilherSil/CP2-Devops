from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
mydb = mysql.connector.connect(
    host="db_mysql",
    user="developer",
    password="devs",
    database="app_almoxarifado"
)

# Rota para retornar todos os materiais
@app.route('/lista-materiais')
def get_materiais():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM materiais")
    rows = cursor.fetchall()

    materiais = []
    for row in rows:
        material = {
            "id": row[0],
            "nome": row[1],
            "quantidade": row[2],
            "unidade": row[3]
        }
        materiais.append(material)

    return jsonify(materiais)



@app.route('/material', methods=['POST'])
def create_material():
    nome = request.json['nome']
    quantidade = request.json['quantidade']
    unidade = request.json['unidade']

    cursor = mydb.cursor()
    sql = "INSERT INTO materiais (nome, quantidade, unidade) VALUES (%s, %s, %s)"
    val = (nome, quantidade, unidade)
    cursor.execute(sql, val)
    mydb.commit()

    return jsonify({'message': 'Material cadastrado com sucesso'})

@app.route('/material/<int:id>', methods=['PUT'])
def update_material(id):
    nome = request.json['nome']
    quantidade = request.json['quantidade']
    unidade = request.json['unidade']

    cursor = mydb.cursor()
    sql = "UPDATE materiais SET nome = %s, quantidade = %s, unidade = %s WHERE id = %s"
    val = (nome, quantidade, unidade, id)
    cursor.execute(sql, val)
    mydb.commit()

    return jsonify({'message': 'Material atualizado com sucesso'})

@app.route('/material/<int:id>', methods=['DELETE'])
def delete_material(id):
    cursor = mydb.cursor()
    sql = "DELETE FROM materiais WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()

    return jsonify({'message': 'Material excluído com sucesso'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)